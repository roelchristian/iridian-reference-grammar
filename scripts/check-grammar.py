#!/usr/bin/env python3
"""Check active-source links and narrowly specified linguistic regressions.

This is a source check, not a TeX compiler or an Iridian phonological analyser.
It checks the published stress table against independent nucleus/stress
expectations, checks selected palatalisation derivations and pronunciation
pairs against fixed fixtures, and rejects superseded example spellings.
Archives and working notes are deliberately outside its scope.
"""
from collections import Counter
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'util'))
sys.path.insert(0, str(ROOT / 'scripts'))
from source_domains import domain_sources  # noqa: E402
from collect_lexicon import extract, strip_comments  # noqa: E402
from boundary_transducer import BoundaryTransducer, check_boundary_fixtures  # noqa: E402
from quantity_grades import QuantityGrades, QuantityLicence  # noqa: E402
from phasal_diagnostics import check_phasal_diagram, check_phasal_sources  # noqa: E402
from clausal_diagnostics import check_clausal_sources  # noqa: E402
from stative_diagnostics import check_stative_sources  # noqa: E402
from stative_scope_guard import check_scope  # noqa: E402
from stative_lexicon import load_lexicon, check_lexical_extension_sources  # noqa: E402


def active_sources(path, seen=None):
    """Follow literal includes from the book, retaining source locations."""
    seen = set() if seen is None else seen
    path = path.resolve()
    if path in seen:
        return {}
    seen.add(path)
    text = strip_comments(path.read_text(encoding='utf-8'))
    sources = {path.relative_to(ROOT).as_posix(): text}
    for name in re.findall(r'\\(?:input|include)\{([^}]+)\}', text):
        child = ROOT / name
        if not child.suffix:
            child = child.with_suffix('.tex')
        sources.update(active_sources(child, seen))
    return sources


def gloss_tokens(text):
    """Split interlinear words, retaining spaces inside braced TeX groups."""
    tokens, word, depth = [], [], 0
    for character in text.strip():
        if character.isspace() and depth == 0:
            if word:
                tokens.append(''.join(word))
                word = []
        else:
            word.append(character)
            depth += (character == '{') - (character == '}')
    if word:
        tokens.append(''.join(word))
    return tokens


def lexical_velar_checks(sources):
    """Validate specified lexical examples, without deriving sounds from ě.

    These are stored pronunciations of existing words, not a rule assigning
    palatality to arbitrary written kě. Dots may clarify syllabification; the
    consonants, stress and quantity of each broad transcription are fixed.
    """
    expected = {'kěda': 'ˈkʲɛda', 'těda': 'ˈcɛda',
                'kánek': 'ˈkaːnɛk', 'kánnik': 'ˈkaːnnɪk', 'kanžek': 'ˈkanʒɛk'}
    lexical_specs = {'kěda': 'kʲ', 'kan-': 'k', 'těda': 'c'}
    found, entries, failures = set(), set(), []
    for path, text in sources.items():
        examples = []
        for record in extract(text, path):
            if record['macro'] == 'phon':
                examples.append((record['form'], record['pronunciation']))
            elif record['macro'] == 'lexentry':
                form, notes = record['form'], record['notes']
                if form in lexical_specs:
                    entries.add(form)
                    metadata = re.findall(r'lexical(?: initial)?\s+/([^/]+)/', notes)
                    if metadata != [lexical_specs[form]]:
                        failures.append(f'{path}: lexical metadata for {form} must specify /{lexical_specs[form]}/')
                if form in expected:
                    examples.extend((form, ipa) for ipa in re.findall(
                        r'\\ipagloss\{\[([^\]]+)\]\}', notes))
        # Also inspect existing tables and prose using separate form/IPA macros.
        examples.extend(re.findall(
            r'\\ird\{([^{}]+)\}\s*(?:&\s*)?(?:\\ipagloss\{)?\[([^\]]+)\]', text))
        for form, ipa in examples:
            if form not in expected:
                continue
            found.add(form)
            broad = re.sub(r'[.\s\[\]]', '', ipa)
            if broad != expected[form]:
                failures.append(f'{path}: lexical pronunciation of {form}: [{ipa}] '
                                f'conflicts with [{expected[form]}]')
    failures.extend(f'missing lexical pronunciation fixture: {form}' for form in sorted(expected.keys() - found))
    failures.extend(f'missing lexical metadata entry: {form}' for form in sorted(lexical_specs.keys() - entries))

    # Keep the two productive velar outputs distinct from the lexical /kʲ/.
    phonology = sources.get('chapters/02-phonology.tex', '')
    table = re.search(r'\\label\{tab:velar-fronting\}(.*?)\\end\{table\}', phonology, re.S)
    if table is None:
        failures.append('missing productive velar-grade table')
    else:
        for grade, output in (('Front', 'ts'), ('Restricted velar-front', 'ts'), ('Mixed', 'tʃ')):
            row = re.search(re.escape(grade) + r'\s*&\s*/k/\s*\$\\rightarrow\$\s*/([^/]+)/', table[1])
            if row is None or row[1] != output:
                failures.append(f'productive {grade} grade must retain /k/ → /{output}/')
    return failures


def check_palatalisation(phonology, fixtures):
    """Check independently specified examples together, without deriving forms.

    A form occurring elsewhere cannot satisfy a derivation fixture, and an IPA
    string paired with a different spelling cannot satisfy a pronunciation.
    These fixtures preserve the stated synchronic correspondences; they do not
    establish lexical attestation or prove the completeness of the analysis.
    """
    failures = []
    for fixture in fixtures['derivations']:
        marker = r'\label{' + fixture['label'] + '}'
        start = phonology.find(marker)
        section = '' if start < 0 else re.split(
            r'\\(?:subsection|section|chapter)\b', phonology[start:], maxsplit=1)[0]
        rows = re.findall(r'\\a\s+(.*?)(?=\\a\s|\\xe\b)', section, re.S)
        derivations = [re.findall(r'\\ird\{([^{}]+)\}', row)
                       for row in rows if r'\rightarrow' in row]
        found = fixture['forms'] in derivations
        # A surviving correct row must not conceal a contradictory duplicate
        # with the same inputs in the section being checked.
        for forms in derivations:
            if forms[:-1] == fixture['forms'][:-1] and forms[-1:] != fixture['forms'][-1:]:
                failures.append('palatalisation derivation: ' + fixture['process']
                                + ': conflicting output ' + forms[-1]
                                + ', expected ' + fixture['forms'][-1])
        if not found:
            failures.append('palatalisation derivation: ' + fixture['process']
                            + ': expected ' + ' + '.join(fixture['forms'][:-1])
                            + ' → ' + fixture['forms'][-1]
                            + ' in ' + fixture['label'])
    marker = r'\label{tab:morph-trigger}'
    start = phonology.find(marker)
    table = '' if start < 0 else phonology[start:].split(r'\end{table}', 1)[0]
    for fixture in fixtures['classes']:
        rows = [row.strip() for row in table.split(r'\\')]
        if not any(re.search(r'(?:^|\n)' + re.escape(fixture['grade']) + r'\s', row)
                   and r'\ird{' + fixture['suffix'] + '}' in row.split('&')[1]
                   for row in rows if '&' in row):
            failures.append(f"palatalisation class: {fixture['suffix']}: "
                            f"expected {fixture['grade']}")
    pairs = {(record['form'], record['pronunciation'])
             for record in extract(phonology, 'chapters/02-phonology.tex')
             if record['macro'] == 'phon'}
    pairs.update(re.findall(
        r'\\ird\{([^{}]+)\}\s*(?:&\s*)?\\ipagloss\{\[([^{}]+)\]\}', phonology))
    pairs.update(re.findall(
        r'\\ird\{([^{}]+)\}\s*(?:&\s*)?\[([^\[\]{}\n]+)\]', phonology))
    broad_marks = str.maketrans('', '', 'ˈˌ.')
    for fixture in fixtures['pronunciations']:
        if (fixture['form'], fixture['ipa']) not in pairs:
            failures.append(f"palatalisation pronunciation: {fixture['form']}: "
                            f"expected [{fixture['ipa']}] ({fixture['process']})")
        # Repeated examples must agree even when one correct occurrence survives.
        # Stress and syllable dots may be omitted in broad transcriptions.
        for form, ipa in sorted(pairs):
            if (form == fixture['form']
                    and ipa.translate(broad_marks) != fixture['ipa'].translate(broad_marks)):
                failures.append(f"palatalisation pronunciation: {form}: "
                                f"conflicting [{ipa}], expected [{fixture['ipa']}]")
    return failures


def spelling_nuclei(form):
    """Count native written nuclei: i is vocalic and j never adds a nucleus.

    The diphthong ou has one nucleus; lexical softness does not alter counting.
    """
    return len(re.findall(r'[aeiouyáéíóúýě]', form.lower().replace('ou', 'o')))


def sibilant_spelling_checks(sources):
    """Reject superseded outputs in active examples, preserving other lexical ě.

    Explicitly starred forms may illustrate rejected spellings. Prose discussing
    an older transcription is not an active example; phon macros, paired IPA,
    lexicon headwords and interlinear surface lines are checked as data.
    """
    failures = []
    old_spellings = re.compile(r'[szc]ě', re.IGNORECASE)
    explicit_soft_e = re.compile(r'[ťďňľ]e', re.IGNORECASE)
    silent_labial_i = re.compile(r'pi[aá](?:št|šč|sn)', re.IGNORECASE)
    redundant = re.compile(r'[ťďňľčšž]ě', re.IGNORECASE)
    old_words = re.compile(r'(?<!\w)(?:siarc|zia|ziou|ciu)(?!\w)', re.IGNORECASE)
    for path, raw in sources.items():
        text = strip_comments(raw)
        examples = [(m[1], text.count('\n', 0, m.start()) + 1)
                    for m in re.finditer(r'\\(?:irdp?|phon|lexentry)\{([^{}]+)\}', text)]
        examples.extend((m[1], text.count('\n', 0, m.start()) + 1)
                        for m in re.finditer(r'\\gla\s+(.+?)//', text, re.S))
        for form, line in examples:
            if form.lstrip().startswith('*'):
                continue
            if explicit_soft_e.search(form):
                failures.append(f'{path}:{line}: soft coronals before ɛ require tě/dě/ně/lě: {form}')
            if silent_labial_i.search(form):
                failures.append(f'{path}:{line}: labial softness before back vowels requires j: {form}')
            if old_spellings.search(form):
                failures.append(f'{path}:{line}: superseded sibilant spelling {form}')
            if redundant.search(form):
                failures.append(f'{path}:{line}: redundant palatal spelling {form}')
            if old_words.search(form):
                failures.append(f'{path}:{line}: superseded silent-i sibilant spelling {form}')
        # Retired alveolopalatals must not survive in published pronunciation
        # data even when a correct duplicate occurs elsewhere in the chapter.
        ipa_examples = [(record['pronunciation'], record['line'])
                        for record in extract(text, path) if record['macro'] == 'phon']
        ipa_examples.extend((m[1], text.count('\n', 0, m.start()) + 1)
                            for m in re.finditer(r'\\ipagloss\{\[([^{}]+)\]\}', text))
        ipa_examples.extend((m[1], text.count('\n', 0, m.start()) + 1)
                            for m in re.finditer(r'\\ird\{[^{}]+\}\s*(?:&\s*)?\[([^\[\]{}\n]+)\]', text))
        for ipa, line in ipa_examples:
            if re.search('[ɕʑ]', ipa):
                failures.append(f'{path}:{line}: superseded alveolopalatal pronunciation [{ipa}]')
    return failures


def check_valency(verbal, fixtures):
    """Preserve reviewed forms, glosses and translations in finite paradigms.

    These checks detect transcription regressions; they neither infer case
    from spelling nor decide whether an unreviewed construction is grammatical.
    Negative examples and schematic suffix strings are outside this inventory.
    """
    failures = []
    for fixture in fixtures:
        marker = r'\label{' + fixture['label'] + '}'
        start = verbal.find(marker)
        group = '' if start < 0 else verbal[start:].split(r'\xe', 1)[0]
        examples = []
        translations = []
        for example in re.findall(r'\\begingl\b(.*?)\\endgl\b', group, re.S):
            surface = re.search(r'\\gla\s+(.*?)//', example, re.S)
            gloss = re.search(r'\\glb\s+(.*?)//', example, re.S)
            translation = re.search(r'\\glft\s+(.*?)//', example, re.S)
            if surface and gloss:
                examples.append((' '.join(surface[1].split()),
                                 ' '.join(gloss[1].split())))
                translations.append(' '.join(translation[1].split()) if translation else None)
        expected = [(row['surface'], row['gloss']) for row in fixture['examples']]
        if examples != expected:
            failures.append('valency paradigm: ' + fixture['label']
                            + ': reviewed surface/gloss pairs changed')
        for row, translation in zip(fixture['examples'], translations):
            if 'translation' in row and row['translation'] != translation:
                failures.append('valency paradigm: ' + fixture['label']
                                + ': reviewed translation changed')
        for surface, gloss in examples:
            if gloss.count(r'\Dir{}') != 1:
                failures.append('valency paradigm: ' + fixture['label']
                                + ': expected one direct-case participant in ' + surface)
            verbal_gloss = gloss_tokens(gloss)[-1].replace(r'\textsc{trs}', r'\Trs{}')
            if r'\Antip{}' in verbal_gloss and r'\Appl{}' in verbal_gloss:
                failures.append('valency paradigm: ' + fixture['label']
                                + ': antipassive/applicative combination')
            if verbal_gloss.count(r'\Appl{}') > 1:
                failures.append('valency paradigm: ' + fixture['label']
                                + ': repeated applicative')
            for inner in (r'\Antip{}', r'\Appl{}'):
                if (inner in verbal_gloss and r'\Caus{}' in verbal_gloss
                        and verbal_gloss.index(inner) > verbal_gloss.index(r'\Caus{}')):
                    failures.append('valency paradigm: ' + fixture['label']
                                    + ': inner valency follows causative')
            if (r'\Caus{}' in verbal_gloss and r'\Trs{}' in verbal_gloss
                    and verbal_gloss.index(r'\Trs{}') < verbal_gloss.index(r'\Caus{}')):
                failures.append('valency paradigm: ' + fixture['label']
                                + ': patient-selecting Voice precedes causative')
    return failures


def check_prescribed_pronunciations(sources, fixtures, context):
    """Require each reviewed IPA pair and reject contradictory duplicates."""
    expected = {case['form'].casefold(): case['ipa'].replace('.', '') for case in fixtures}
    seen, failures = set(), []
    for path, text in sources.items():
        for record in extract(strip_comments(text), path):
            form = record['form'].casefold()
            if record['macro'] != 'phon' or form not in expected:
                continue
            seen.add(form)
            if record['pronunciation'].replace('.', '') != expected[form]:
                failures.append(f"{path}: {context} pronunciation: {record['form']}: "
                                f"unexpected [{record['pronunciation']}]")
    failures.extend(f'missing {context} pronunciation fixture: ' + form
                    for form in sorted(expected.keys() - seen))
    return failures


def check_quantity_sources(sources, fixtures):
    """Keep independent grade/declension/aspect cells paired in source tables."""
    failures = []
    for table in fixtures['source_tables']:
        text = strip_comments(sources.get(table['path'], ''))
        marker = r'\label{' + table['label'] + '}'
        bodies = re.findall(re.escape(marker) + r'(.*?)\\end\{table\}', text, re.S)
        width = table['width']
        rows = [forms[-width:] for body in bodies for row in body.split(r'\\')
                for forms in [re.findall(r'\\ird\{([^{}]+)\}', row)] if len(forms) >= width]
        if rows != table['rows']:
            failures.append('quantity paradigm: ' + table['label'] + ': reviewed cells changed')
    for passage in fixtures.get('source_paragraphs', []):
        text = strip_comments(sources.get(passage['path'], ''))
        start = text.find(passage['marker'])
        body = '' if start < 0 else re.split(
            r'\\(?:subsection|section)\b', text[start + len(passage['marker']):], maxsplit=1)[0]
        paragraphs = [re.findall(r'\\ird\{([^{}]+)\}', paragraph)
                      for paragraph in re.split(r'\n\s*\n', body)]
        matching = [forms[forms.index(passage['forms'][0]):] for forms in paragraphs
                    if passage['forms'][0] in forms]
        if not matching or any(forms != passage['forms'] for forms in matching):
            failures.append('quantity passage: ' + passage['marker'] + ': reviewed forms changed')
        surfaces = [' '.join(surface.split())
                    for surface in re.findall(r'\\gla\s+(.*?)//', body, re.S)]
        if passage['surface'] not in surfaces:
            failures.append('quantity passage: ' + passage['marker'] + ': reviewed example changed')
    return failures


def check_contemplative_sources(sources, fixtures):
    """Preserve long /aːʒ/, its contextual phonetics and reviewed suppletion.

    The quantifier nách and name Bách are distinct lexemes, explicitly protected
    rather than swept into a spelling replacement. Starred rejected examples
    and comments do not count as prescribed contemplative forms.
    """
    failures = check_prescribed_pronunciations(sources, fixtures['pronunciations'], 'contemplative')
    for table in fixtures['table_rows']:
        text = strip_comments(sources.get(table['path'], ''))
        marker = r'\label{' + table['label'] + '}'
        bodies = re.findall(re.escape(marker) + r'(.*?)\\end\{table\}', text, re.S)
        rows = [re.findall(r'\\ird\{([^{}]+)\}', row)
                for body in bodies for row in body.split(r'\\')
                if re.search(r'(?:^|\n)\s*' + re.escape(table['row']) + r'\s*&', row)]
        if not rows or any(row != table['forms'] for row in rows):
            failures.append('contemplative paradigm: ' + table['label'] + ': reviewed row changed')
    for fixture in fixtures['protected_lexemes']:
        records = extract(strip_comments(sources.get(fixture['path'], '')), fixture['path'])
        if not any(record['macro'] == 'lexentry' and record['form'] == fixture['form']
                   and record['gloss'] == fixture['gloss'] for record in records):
            failures.append('missing protected lexical pair: ' + fixture['form'] + ' / ' + fixture['gloss'])
    for fixture in fixtures['protected_surfaces']:
        surfaces = re.findall(r'\\gla\s+(.*?)//', strip_comments(sources.get(fixture['path'], '')), re.S)
        if fixture['surface'] not in [' '.join(surface.split()) for surface in surfaces]:
            failures.append('missing protected surface: ' + fixture['surface'])
    for path, raw in sources.items():
        text = strip_comments(raw)
        examples = [record['form'] for record in extract(text, path)]
        examples.extend(re.findall(r'\\gla\s+(.*?)//', text, re.S))
        for form in examples:
            if form.lstrip().startswith('*'):
                continue
            words = re.findall(r'[-\w]+', form)
            obsolete = [word for word in words if
                        ('ách' in word.casefold() and word.casefold() not in {'nách', 'bách'})
                        or word.casefold() in {'jecach', 'zadach'}]
            if obsolete:
                failures.append(f'{path}: obsolete contemplative output: ' + ', '.join(obsolete))
    return failures


def check_evidential_sources(sources, fixtures):
    """Check reviewed host/Evid/linker rows and independent broad IPA pairs.

    These are source prescriptions, not a parser deriving morphology from
    written words. Each triple must occur together in its named table; a
    contradictory duplicate cannot be concealed by a surviving correct row.
    """
    failures = []
    cases = {case['id']: case for case in fixtures['cases']}
    for table in fixtures['tables']:
        text = strip_comments(sources.get(table['path'], ''))
        marker = r'\label{' + table['label'] + '}'
        bodies = re.findall(re.escape(marker) + r'(.*?)\\end\{table\}', text, re.S)
        rows = [re.findall(r'\\ird\{([^{}]+)\}', row)
                for body in bodies for row in body.split(r'\\')]
        for case_id in table['case_ids']:
            expected = cases[case_id]['forms']
            matching = [row[row.index(expected[0]):row.index(expected[0]) + 3]
                        for row in rows if expected[0] in row]
            if not matching or any(row != expected for row in matching):
                failures.append(f"evidential paradigm: {table['label']}: "
                                f"expected paired forms {' / '.join(expected)}")
    for section in fixtures.get('prose_derivations', []):
        text = strip_comments(sources.get(section['path'], ''))
        marker = r'\label{' + section['label'] + '}'
        start = text.find(marker)
        body = '' if start < 0 else re.split(
            r'\\(?:section|subsection|subsubsection)\b', text[start:], maxsplit=1)[0]
        paragraphs = [re.findall(r'\\ird\{([^{}]+)\}', paragraph)
                      for paragraph in re.split(r'\n\s*\n', body)]
        for case_id in section['case_ids']:
            expected = cases[case_id]['forms']
            matching = [forms[forms.index(expected[0]):forms.index(expected[0]) + 3]
                        for forms in paragraphs if expected[0] in forms]
            if not matching or any(forms != expected for forms in matching):
                failures.append(f"evidential derivation: {section['label']}: "
                                f"expected paired forms {' / '.join(expected)}")
    failures.extend(check_prescribed_pronunciations(sources, fixtures['pronunciations'], 'evidential'))
    for path, raw in sources.items():
        text = strip_comments(raw)
        for record in extract(text, path):
            if (not record['form'].lstrip().startswith('*')
                    and re.search(r'ej(?:[ťt]e|tě)', record['form'], re.IGNORECASE)):
                failures.append(f"{path}: obsolete evidential exponent: {record['form']}")
        for match in re.finditer(r'\\gla\s+(.*?)//', text, re.S):
            if re.search(r'ej(?:[ťt]e|tě)', match[1], re.IGNORECASE):
                failures.append(f'{path}: obsolete evidential in interlinear example')
    return failures


def verbs_heading_checks(sources):
    """Enforce chapter → section → subsection throughout the grammar."""
    failures = []
    for path, raw in sources.items():
        if not path.startswith('chapters/'):
            continue
        text = strip_comments(raw)
        failures.extend(
            f'{path}:{text.count(chr(10), 0, match.start()) + 1}: '
            'Chapter headings must stop at subsection'
            for match in re.finditer(
                r'\\(?:subsubsection|paragraph|subparagraph)\*?\s*(?=\{|\[)', text))
    return failures


def renamed_particle_checks(sources):
    """Keep the renamed particles and their independent lexical readings paired."""
    failures = []
    for path, text in sources.items():
        if re.search(r'\b(?:ktady|kday|hlavdy|moc)\b', text, re.IGNORECASE):
            failures.append(f'{path}: obsolete renamed particle')
    lexicon = sources.get('util/lexicon.tex', '')
    for form, ipa, gloss in [('hladě', 'ˈxla.ɟɛ', 'inferential particle, must'),
                             ('kady', 'ˈka.dɨ̞', 'speculative particle, perhaps'),
                             ('mó', 'ˈmoː', 'affirmative, confirmatory particle')]:
        entries = [record for record in extract(lexicon, 'util/lexicon.tex')
                   if record['macro'] == 'lexentry' and record['form'] == form]
        if (len(entries) != 1 or entries[0]['gloss'] != gloss
                or r'\ipagloss{[' + ipa + ']}' not in entries[0]['notes']):
            failures.append(f'lexicon: missing or changed particle entry for {form}')
    particles = sources.get('chapters/05-function-words.tex', '')
    section = re.search(r'\\subsection\{(?:\\ird\{)?Kady(?:\})?\}(.*?)(?=\\(?:subsection|section)|\Z)', particles, re.S)
    pronunciations = [] if section is None else re.findall(
        r'\\ipagloss\{\[([^\]]+)\]\}', section[1])
    if pronunciations != ['ˈka.dɨ̞']:
        failures.append('particles: missing or conflicting canonical kady pronunciation')
    return failures


def check():
    publication_sources = active_sources(ROOT / 'grammar.tex')
    sources = domain_sources(publication_sources)
    failures = lexical_velar_checks(sources)
    failures.extend(verbs_heading_checks(publication_sources))
    failures.extend(renamed_particle_checks(sources))
    phasal_fixtures = json.loads((ROOT / 'scripts/phasal-fixtures.json').read_text(encoding='utf-8'))
    failures.extend(check_phasal_diagram(
        sources.get('util/phasal-polarity-diagram.tex', ''), phasal_fixtures))
    failures.extend(check_phasal_sources(sources, phasal_fixtures))
    failures.extend(check_clausal_sources(sources))
    quantity_fixtures = json.loads((ROOT / 'scripts/quantity-fixtures.json').read_text(encoding='utf-8'))
    quantity_grades = QuantityGrades.from_file()
    for case in quantity_fixtures['cases']:
        licence = QuantityLicence(case['id'], case['grade'], True, tuple(case['domain']),
                                  tuple(case['eligible']), case['target'], case['raising_licensed'])
        if quantity_grades.apply(tuple(case['input']), licence) != tuple(case['expected']):
            failures.append('quantity grade fixture: ' + case['id'] + ': independent output changed')
    failures.extend(check_quantity_sources(sources, quantity_fixtures))
    stative_fixtures = json.loads((ROOT / 'scripts/stative-fixtures.json').read_text(encoding='utf-8'))
    failures.extend(check_stative_sources(sources, stative_fixtures))
    failures.extend(check_scope())
    lexical_statives = load_lexicon()
    failures.extend(check_lexical_extension_sources(sources, lexical_statives))
    failures.extend(check_prescribed_pronunciations(
        sources, quantity_fixtures['pronunciations'], 'quantity'))
    boundary_mapper = BoundaryTransducer.from_file()
    boundary_fixtures = json.loads((ROOT / 'scripts/boundary-fixtures.json').read_text(encoding='utf-8'))
    failures.extend(check_boundary_fixtures(boundary_mapper, boundary_fixtures))
    evidential_fixtures = json.loads((ROOT / 'scripts/evidential-fixtures.json').read_text(encoding='utf-8'))
    failures.extend(check_evidential_sources(sources, evidential_fixtures))
    contemplative_fixtures = json.loads((ROOT / 'scripts/contemplative-fixtures.json').read_text(encoding='utf-8'))
    failures.extend(check_contemplative_sources(sources, contemplative_fixtures))
    # The independently written prose table must describe the implemented bundles.
    phonology = sources['chapters/02-phonology.tex']
    registry = re.search(r'\\label\{tab:licensed-grades\}(.*?)\\end\{table\}', phonology, re.S)
    if registry is None:
        failures.append('missing licensed-grade specification table')
    else:
        for name, display in (('plain', 'Plain'), ('front', 'Front'), ('mixed', 'Mixed'),
                              ('restricted', 'Restricted velar-front')):
            spec = boundary_mapper.rules['grades'][name]
            pal = 'yes' if spec['coronal_labial_pal'] else 'no'
            velar = 'unchanged /k/' if spec['velar_output'] == 'identity' else '/' + spec['velar_output'] + '/'
            pattern = re.escape(display) + r'\s*&\s*' + pal + r'\s*&\s*' + re.escape(velar) + r'\s*&'
            if not re.search(pattern, registry[1]):
                failures.append('boundary grade specification differs between prose and mapping: ' + name)
    failures.extend(sibilant_spelling_checks(sources))
    labels, bibliography = Counter(), Counter()
    references, citations = [], []
    aligned = 0
    for path, text in publication_sources.items():
        labels.update(re.findall(r'\\label\{([^}]+)\}', text))
        bibliography.update(re.findall(r'\\bibitem(?:\[[^\]]*\])?\{([^}]+)\}', text))
        references.extend((path, key) for key in re.findall(r'\\(?:ref|pageref|eqref)\{([^}]+)\}', text))
        citations.extend((path, key.strip()) for keys in re.findall(r'\\cite(?:\[[^\]]*\])*\{([^}]+)\}', text)
                         for key in keys.split(','))
        stack = []
        for match in re.finditer(r'\\(begin|end)\{([^}]+)\}', text):
            action, environment = match.groups()
            if action == 'begin':
                stack.append(environment)
            elif not stack or stack.pop() != environment:
                failures.append(f'{path}: mismatched environment {environment}')
        if stack:
            failures.append(f'{path}: unclosed environments {stack}')
        for example in re.finditer(r'\\begingl\b(.*?)\\endgl\b', text, re.S):
            surface = re.search(r'\\gla\s+(.*?)//', example[1], re.S)
            gloss = re.search(r'\\glb\s+(.*?)//', example[1], re.S)
            if surface is None or gloss is None:
                continue
            aligned += 1
            if len(gloss_tokens(surface[1])) != len(gloss_tokens(gloss[1])):
                line = text.count('\n', 0, example.start()) + 1
                failures.append(f'{path}:{line}: interlinear word/gloss count mismatch')
    failures.extend(f'{path}: undefined reference {key}' for path, key in references if key not in labels)
    failures.extend(f'{path}: undefined citation {key}' for path, key in citations if key not in bibliography)
    failures.extend(f'duplicate label {key}' for key, count in labels.items() if count > 1)
    failures.extend(f'duplicate bibliography key {key}' for key, count in bibliography.items() if count > 1)

    # These are concrete obsolete outputs, not a general ban on lexical ě.
    obsolete = ('zdičev', 'zdíčev', 'prku', 'prce', 'pjaštiře', 'pjaštoviře',
                'pjaščace', 'pjaštnace', 'pjaščave', 'pjaštnave', 'pjaštimně',
                'pjastime', 'pjastnime')
    pattern = re.compile(r'(?<!\w)(?:' + '|'.join(map(re.escape, obsolete)) + r')(?!\w)', re.IGNORECASE)
    for path, text in sources.items():
        for match in pattern.finditer(text):
            line = text.count('\n', 0, match.start()) + 1
            failures.append(f'{path}:{line}: obsolete output {match[0]}')
    combined = '\n'.join(sources.values())
    for form in ('ratě', 'radě', 'raně', 'ralě', 'ruce', 'lúbcí', 'Marcí',
                 'zděcir', 'zďíčev', 'pjáščev', 'pjáščice', 'pjáščikou',
                 'pjáščavě', 'pjaštnávě', 'pjaštire', 'pjaštovire'):
        if not re.search(r'(?<!\w)' + re.escape(form) + r'(?!\w)', combined):
            failures.append(f'missing grade regression example: {form}')

    # Independently fixed expectations: (nuclei, nuclei before primary stress).
    # Count actual IPA vowels, excluding the nonsyllabic second part of /ou̯/.
    expected = {'pjaštník': (2, 0, 1), 'zapjaštník': (3, 1, 1),
                'premužna': (3, 0, 0), 'šarc': (1, 0, 0),
                'pjaštou': (2, 0, 0), 'perek': (2, 0, 0),
                'pérku': (2, 0, 1), 'pérce': (2, 0, 1)}
    valency_fixtures = json.loads(
        (ROOT / 'scripts/valency-fixtures.json').read_text(encoding='utf-8'))
    failures.extend(check_valency(sources['chapters/03-verbs.tex'], valency_fixtures))
    phonology = sources['chapters/02-phonology.tex']
    palatalisation_fixtures = json.loads(
        (ROOT / 'scripts/palatalisation-fixtures.json').read_text(encoding='utf-8'))
    failures.extend(check_palatalisation(phonology, palatalisation_fixtures))
    table = re.search(r'\\caption\{Initial stress and vocalic nuclei.*?\\end\{table\}', phonology, re.S)
    rows = {} if table is None else {
        form: (ipa, int(count)) for form, ipa, count in re.findall(
            r'\\phon\{([^{}]+)\}\{([^{}]+)\}\{[^{}]+\}\s*&\s*(\d+)', table[0])}
    for form, (nuclei, before_stress, long_nuclei) in expected.items():
        if form not in rows:
            failures.append(f'stress table: missing {form}')
            continue
        ipa, stated = rows[form]
        syllabic = re.sub(r'.[\u032f\u0311]', '', ipa)
        vowels = r'[aeiouyɑɐɒæɛɜɞəɘɤɨɪɔœøɵʊʌʉɯɶ]'
        actual = len(re.findall(vowels, syllabic))
        preceding = len(re.findall(vowels, syllabic.split('ˈ')[0]))
        if stated != nuclei or actual != nuclei or preceding != before_stress or ipa.count('ˈ') != 1:
            failures.append(f'stress table: {form}: unexpected nuclei or stress in [{ipa}], stated {stated}')
        if re.search(r'[rl]\u0329', ipa) or ipa.count('ː') != long_nuclei:
            failures.append(f'stress table: {form}: unexpected syllabic liquid or quantity change')
    pronunciations = 0
    for path, text in sources.items():
        for record in extract(text, path):
            if record['macro'] != 'phon':
                continue
            form, ipa = record['form'], record['pronunciation']
            pronunciations += 1
            # Only explicit examples are checked, not inferred dictionary IPA.
            # The glide letter j and diphthong ou do not add a nucleus.
            # Sibilants and lexical kě retain their stated segmental values.
            count = spelling_nuclei(form)
            ipa_nuclei = len(re.findall(vowels, re.sub(r'.[\u032f\u0311]', '', ipa)))
            if count != ipa_nuclei:
                failures.append(f"{path}:{record['line']}: {form}: spelling/IPA nucleus mismatch ({count}/{ipa_nuclei})")
            if len(re.findall('[áéíóúý]', form)) != ipa.count('ː'):
                failures.append(f"{path}:{record['line']}: {form}: orthographic/IPA quantity mismatch")
            if re.search(r'[rl]\u0329', ipa):
                failures.append(f"{path}:{record['line']}: {form}: syllabic liquid in pronunciation")
    if failures:
        print('\n'.join(failures), file=sys.stderr)
        return 1
    print(f'Grammar source checks passed: {len(publication_sources)} files, {len(labels)} labels, '
          f'{len(references)} references, {len(citations)} citations; '
          f'{aligned} interlinear alignments, {len(valency_fixtures)} valency paradigms, '
          f'{len(expected)} stress fixtures, '
          f"{len(boundary_fixtures['cases'])} independent boundary fixtures, "
          f"{len(evidential_fixtures['cases'])} evidential fixtures, "
          f"{len(quantity_fixtures['cases'])} independent quantity fixtures, "
          f"{sum(len(row['forms']) for row in stative_fixtures['paradigms'])} stative aspect cells, "
          f"{len(stative_fixtures['causatives'])} conditional stative causative paradigms, "
          f"{len(lexical_statives['entries'])} lexical stative records, "
          f"{len(lexical_statives['manifest']['forms'])} Manifest aspect cells, "
          "frozen relative-scope guard, "
          f"{len(quantity_fixtures['pronunciations'])} quantity pronunciation fixtures, "
          f"{len(contemplative_fixtures['pronunciations'])} contemplative pronunciation fixtures, "
          f"{sum(len(palatalisation_fixtures[key]) for key in ('derivations', 'pronunciations', 'classes'))} palatalisation fixtures, "
          f"{len(phasal_fixtures['diagram_rows'])} phasal diagram transitions, "
          f'{pronunciations} explicit pronunciation/quantity examples '
          'and lexical-velar/obsolete-spelling checks.')
    return 0


if __name__ == '__main__':
    sys.exit(check())

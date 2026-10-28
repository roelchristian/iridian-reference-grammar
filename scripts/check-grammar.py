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
from collect_lexicon import extract, strip_comments  # noqa: E402


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
    expected = {'kěda': 'ˈkʲɛda', 'ťeda': 'ˈcɛda',
                'kělek': 'ˈkʲɛlɛk', 'kělnik': 'ˈkʲɛwnɪk', 'kělšek': 'ˈkʲɛwʃɛk'}
    lexical_specs = {'kěda': 'kʲ', 'kěl-': 'kʲ', 'ťeda': 'c'}
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
        for grade, output in (('Palatal/front', 'ts'), ('Restricted velar-front', 'ts'), ('Yod', 'tʃ')):
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
        found = any(re.findall(r'\\ird\{([^{}]+)\}', row) == fixture['forms']
                    and r'\rightarrow' in row for row in rows)
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


def check():
    sources = active_sources(ROOT / 'grammar.tex')
    failures = lexical_velar_checks(sources)
    labels, bibliography = Counter(), Counter()
    references, citations = [], []
    aligned = 0
    for path, text in sources.items():
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
    obsolete = ('zdíčev', 'prku', 'prce', 'piaštiře', 'piaštoviře',
                'piaščace', 'piaštnace', 'piaščave', 'piaštnave', 'piaštimně', 'piaště',
                'hradě', 'mostě', 'stolě', 'sobotě', 'skorně', 'mrocně',
                'piastime', 'piastnime', 'tvírzně', 'ščehezně', 'mněrazně',
                'kaměnzně', 'sylozně', 'barocezně', 'zmocezně', 'svícezně', 'kmětezně')
    pattern = re.compile(r'(?<!\w)(?:' + '|'.join(map(re.escape, obsolete)) + r')(?!\w)', re.IGNORECASE)
    for path, text in sources.items():
        for match in pattern.finditer(text):
            line = text.count('\n', 0, match.start()) + 1
            failures.append(f'{path}:{line}: obsolete output {match[0]}')
    combined = '\n'.join(sources.values())
    for form in ('raťe', 'raďe', 'raňe', 'raľe', 'ruce', 'lubcí', 'Marcí',
                 'zděcir', 'zdičev', 'piaščev', 'piaščice', 'piaščikou',
                 'piaščavě', 'piaštnavě', 'piaštire', 'piaštovire'):
        if not re.search(r'(?<!\w)' + re.escape(form) + r'(?!\w)', combined):
            failures.append(f'missing grade regression example: {form}')

    # Independently fixed expectations: (nuclei, nuclei before primary stress).
    # Count actual IPA vowels, excluding the nonsyllabic second part of /ou̯/.
    expected = {'piaštnik': (2, 0), 'zapiaštnik': (3, 1),
                'premrocna': (3, 0), 'siarc': (1, 0),
                'piaštou': (2, 0), 'perek': (2, 0), 'perku': (2, 0), 'perce': (2, 0)}
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
    for form, (nuclei, before_stress) in expected.items():
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
        if re.search(r'[rl]\u0329', ipa) or 'ː' in ipa:
            failures.append(f'stress table: {form}: unexpected syllabic liquid or quantity change')
    pronunciations = 0
    for path, text in sources.items():
        for word in re.findall(r'\\ird\{([^{}]+)\}', text):
            if re.search(r'[ťďňľčšž]ě', word) and not word.startswith('*'):
                failures.append(f'{path}: redundant palatal spelling {word}')
        for match in re.finditer(r'\\gla\s+(.+?)//', text, re.S):
            if re.search(r'[ťďňľčšž]ě', match[1]):
                line = text.count('\n', 0, match.start()) + 1
                failures.append(f'{path}:{line}: redundant palatal spelling in example')
        for record in extract(text, path):
            if record['macro'] != 'phon':
                continue
            form, ipa = record['form'], record['pronunciation']
            pronunciations += 1
            # Only explicit examples are checked, not inferred dictionary IPA.
            # Nonvocalic i is permitted before the six specified back vowels;
            # ou is one nucleus. No syllabic-liquid repair is licensed.
            spelling = re.sub(r'(?<=[^aeiouyáéíóúýě])i(?=[aáoóuú])', '', form.lower())
            spelling = spelling.replace('ou', 'o')
            count = len(re.findall(r'[aeiouyáéíóúýě]', spelling))
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
    print(f'Grammar source checks passed: {len(sources)} files, {len(labels)} labels, '
          f'{len(references)} references, {len(citations)} citations; '
          f'{aligned} interlinear alignments, {len(valency_fixtures)} valency paradigms, '
          f'{len(expected)} stress fixtures, '
          f"{sum(len(palatalisation_fixtures[key]) for key in ('derivations', 'pronunciations', 'classes'))} palatalisation fixtures, "
          f'{pronunciations} explicit pronunciation/quantity examples '
          'and lexical-velar/obsolete-spelling checks.')
    return 0


if __name__ == '__main__':
    sys.exit(check())

#!/usr/bin/env python3
"""Check active-source links and narrowly specified linguistic regressions.

This is a source check, not a TeX compiler or an Iridian phonological analyser.
It checks the published stress table against independent nucleus/stress
expectations and rejects superseded example spellings in active sources.
Archives and working notes are deliberately outside its scope.
"""
from collections import Counter
from pathlib import Path
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


def check():
    sources = active_sources(ROOT / 'grammar.tex')
    failures = []
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
                'piaščace', 'piaštnace', 'piaštimně', 'piaště',
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
                 'piaščacě', 'piaštnacě', 'piaštire', 'piaštovire'):
        if not re.search(r'(?<!\w)' + re.escape(form) + r'(?!\w)', combined):
            failures.append(f'missing grade regression example: {form}')

    # Independently fixed expectations: (nuclei, nuclei before primary stress).
    # Count actual IPA vowels, excluding the nonsyllabic second part of /ou̯/.
    expected = {'piaštnik': (2, 0), 'zapiaštnik': (3, 1),
                'premrocna': (3, 0), 'siarc': (1, 0),
                'piaštou': (2, 0), 'perek': (2, 0), 'perku': (2, 0), 'perce': (2, 0)}
    phonology = sources['chapters/02-phonology.tex']
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
          f'{aligned} interlinear alignments, {len(expected)} stress fixtures, '
          f'{pronunciations} explicit pronunciation/quantity examples '
          'and obsolete-spelling checks.')
    return 0


if __name__ == '__main__':
    sys.exit(check())

"""Articleless-reference regression boundaries, independent of source prose.

The fixture records pre-reform ordinary paradigms at master 2ea86f3, rather
than deriving expected forms from the edited tables. Retired anchored strings
are compared as whole words only: ordinary homophones (notably ráne) remain
licensed. The active include graph is inspected, including literal utility
inputs. Historical research bodies are checked separately, not rewritten.
These checks are guardrails, not a grammatical acceptability analyser.
"""
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def read_active_sources(root=ROOT):
    """Follow the publication graph; reject missing inputs instead of skipping."""
    found = {}
    def visit(path):
        path = path.resolve()
        relative = path.relative_to(root.resolve()).as_posix()
        if relative in found:
            return
        # Match TeX escaping: an escaped percent is data, a doubled slash
        # before percent is not. Blank comments without changing line order.
        raw = path.read_text(encoding='utf-8')
        characters = list(raw)
        cursor = 0
        while cursor < len(raw):
            if raw[cursor] == '\\':
                cursor += 2
            elif raw[cursor] == '%':
                end = raw.find('\n', cursor)
                end = len(raw) if end < 0 else end
                characters[cursor:end] = ' ' * (end - cursor)
                cursor = end
            else:
                cursor += 1
        text = ''.join(characters)
        found[relative] = text
        for name in re.findall(r'\\(?:input|include)\{([^}]+)\}', text):
            child = root / name
            visit(child if child.suffix else child.with_suffix('.tex'))
    visit(root / 'grammar.tex')
    return found


def split_tex(text, separator):
    """Split only at ungrouped delimiters, retaining shortstack line breaks."""
    cells, start, depth, i = [], 0, 0, 0
    while i < len(text):
        character = text[i]
        if character == '\\':
            if depth == 0 and text.startswith(separator, i):
                cells.append(text[start:i].strip())
                i += len(separator)
                start = i
                continue
            i += 2
            continue
        if character == '{':
            depth += 1
        elif character == '}':
            depth -= 1
        if depth == 0 and text.startswith(separator, i):
            cells.append(text[start:i].strip())
            i += len(separator)
            start = i
            continue
        i += 1
    cells.append(text[start:].strip())
    return cells


def ordinary_cells(text, path):
    """Read exactly ordinary sg/pl columns, never manufacture cells by suffix."""
    found, errors = [], []
    table = re.search(r'\\begin\{tabularx\}\{\\textwidth\}\{[^}]*\}(.*?)'
                      r'\\end\{tabularx\}', text, re.S)
    if not table:
        return [], [f'{path}: ordinary paradigm table is missing']
    noun = None
    for row in split_tex(table[1], '\\\\'):
        cells = split_tex(row, '&')
        if len(cells) < 2 or not re.fullmatch(r'\\textsc\{(?:dir|trs|ind)\}', cells[1]):
            continue
        if len(cells) != 4:
            errors.append(f'{path}: case row must contain noun, case, sg and pl only')
            continue
        first = re.sub(r'\\(?:toprule|midrule|bottomrule|addlinespace)\s*', '', cells[0]).strip()
        if first:
            noun = first
        if noun is None:
            errors.append(f'{path}: case row has no independently identified noun')
            continue
        for number, value in zip(('sg', 'pl'), cells[2:]):
            found.append({'file': path, 'noun': noun, 'case': cells[1],
                          'number': number, 'ordinary': value})
    return found, errors


def canonical_cell(cell):
    return tuple(cell[key].strip() for key in
                 ('file', 'noun', 'case', 'number', 'ordinary'))


def check_ordinary_paradigms(sources, fixtures):
    failures = []
    expected = fixtures['cells']
    if (fixtures['base_sha'] != '2ea86f3046beff0d55ee9f7f7e0f06bb31932e26'
            or len(expected) != 102 or fixtures['ordinary_cell_count'] != 102):
        failures.append('articleless: ordinary-cell baseline lost its recorded provenance')
    for path in sorted({cell['file'] for cell in expected}):
        found, errors = ordinary_cells(sources.get(path, ''), path)
        failures.extend(errors)
        retained = [cell for cell in expected if cell['file'] == path]
        if list(map(canonical_cell, found)) != list(map(canonical_cell, retained)):
            failures.append(f'{path}: ordinary case--number cells differ from pristine master')

    return failures


def check_articleless_sources(sources, fixtures):
    failures = check_ordinary_paradigms(sources, fixtures)
    expected = fixtures['cells']
    # Whole retired forms only. Ordinary homophones remain legal in every
    # active source; their precise paradigmatic cells are independently frozen.
    forms = lambda key: {form.casefold() for cell in expected
                         for form in re.findall(r'\\ird\{([^{}]+)\}', cell[key])}
    retired = forms('anchored') - forms('ordinary')
    retired.update(fixtures['retired_nonparadigm_surfaces'])
    # Label names are retained when their incoming cross-reference remains
    # semantically sound; they are not grammatical exponents or examples.
    no_analysis = (
        (r'\bAnch(?:P\b|[0⁰]\b|\s*(?:\^\s*(?:0|\{0\})|\\textsuperscript\{0\}))'
         r'|\\(?:synhead|synfeat)\{Anch(?:\^?\{?0\}?)?\}'
         r'|\\textsc\{Anch(?:\\textsuperscript\{0\})?\}', 'dedicated Anch projection'),
        (r'\\(?:synfeat|textsc)\{(?:anch|shr|spkr\.anch)\}'
         r'|Topicality[–—-]+Anchoring Harmony', 'retired nominal anchoring analysis'),
        (r'\\(?:Def|Sanch)\b|\b(?:sg|pl)\.def\b'
         r'|\\textsc\{(?:def|DEF|sanch|SANCH)\}|(?<=\.)(?:DEF|SANCH)\b',
         'retired definiteness/anchoring gloss'),
        (r'(?:[+−±-]|\\(?:pm|mp))\s*'
         r'(?:\\(?:textsc|mathrm|mathit|operatorname|text)\{\s*)?(?:anch|shr)\b',
         'retired anchoring feature'),
    )
    exception = fixtures['phonological_si_exception']
    for path, original in sources.items():
        text = re.sub(r'\\(?:label|ref|pageref|autoref|hyperref)\{[^}]*\}', '', original)
        if path == exception['path']:
            text = text.replace(exception['text'], '')
        for pattern, description in no_analysis:
            if re.search(pattern, text):
                failures.append(f'{path}: {description} re-entered the active book')
        if re.search(r'(?<![\w])si(?![\w])', text, re.I):
            failures.append(f'{path}: unreviewed si outside the exact schematic phonological contrast')
        words = {word.casefold() for word in re.findall(r'[^\W\d_]+', text)}
        old = sorted(words & retired)
        if old:
            failures.append(f'{path}: retired anchored surfaces: {", ".join(old)}')

    path = 'chapters/08-derivation-nominalisation.tex'
    text = sources.get(path, '')
    table = re.search(r'\\label\{tab:ou-inflection\}(.*?)\\end\{tabularx\}', text, re.S)
    rows = []
    if table:
        for row in split_tex(table[1], '\\\\'):
            cells = split_tex(row, '&')
            if len(cells) > 1 and re.search(r'(?:Direct|Transitive|Indirect) singular', cells[0]):
                rows.append(re.findall(r'\\ird\{([^{}]+)\}', '&'.join(cells[1:])))
    if rows != fixtures['derived_singular_cells']:
        failures.append(f'{path}: independent event/participant singular cells changed')
    if not re.search(r'only direct singular\s+\\ird\{pjaštova\}', text, re.I):
        failures.append(f'{path}: continuous participant direct-only gap is no longer explicit')
    return failures


def check_historical_bodies(root, fixtures, overrides=None):
    """Permit one supersession preamble; protect the exact archived body."""
    failures = []
    overrides = {} if overrides is None else overrides
    for path, expected in fixtures['historical_bodies'].items():
        text = overrides.get(path)
        if text is None:
            text = (root / path).read_text(encoding='utf-8')
        parts = text.split('\n\n', 1)
        if len(parts) != 2 or not any(status in parts[0].lower() for status in ('supersed', 'historical', 'unadopted')):
            failures.append(f'{path}: historical record needs an explicit supersession preamble')
        elif hashlib.sha256(parts[1].encode('utf-8')).hexdigest() != expected:
            failures.append(f'{path}: original historical body was rewritten')
    return failures


def check_articleless(root=ROOT, sources=None, fixtures=None, archive_overrides=None):
    if fixtures is None:
        fixtures = json.loads((root / 'scripts/articleless-fixtures.json').read_text(encoding='utf-8'))
    sources = read_active_sources(root) if sources is None else sources
    return (check_articleless_sources(sources, fixtures)
            + check_historical_bodies(root, fixtures, archive_overrides))

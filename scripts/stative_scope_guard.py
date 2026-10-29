"""Compare the explicitly frozen relative scope with reviewed PR19 content.

Hashes record the reviewed baseline, rather than regenerated current text.
Whole source spans cover rules whose paragraphs do not repeat the exponent.
All exponent-bearing paragraphs are also compared in order, rejecting additions
as well as edits. This scope guard supplements independent linguistic review.
"""
import hashlib
import json
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]


def digest(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


# Reviewed finite-clause cross-references inside the frozen relative treatment.
# Normalise only these exact replacements; reduced selection, examples and
# morphology remain compared with the original reviewed hashes.
FINITE_REFERENCE_REVISIONS = (
    (" content questions permit in-situ and fronted interrogative expressions",
     " content questions permit interrogative expressions with ordinary placement\n"
     " or marked wh-fronting"),
    ("Finite content question & Interrogative expression in situ or overtly fronted &\n"
     r"Interrogative licensing independent of displacement; pre-\ird{by} landing site" "\n"
     "not established by the surface paradigm",
     "Finite content question & Ordinary placement or marked wh-fronting &\n"
     "Lower occurrence interpreted under Pol; marked focus lands above the ordinary\n"
     "placement field"),
)


def frozen_reference_text(path, text):
    if path == 'chapters/08-complex-sentences.tex':
        for original, revised in FINITE_REFERENCE_REVISIONS:
            text = text.replace(revised, original)
    return text


def check_scope(root=ROOT, fixtures=None, overrides=None):
    """Return discrepancies without requiring the baseline commit at runtime."""
    if fixtures is None:
        fixtures = json.loads((root / 'scripts/stative-scope-freeze.json').read_text())
    overrides = {} if overrides is None else overrides

    def read(path):
        text = overrides[path] if path in overrides else (root / path).read_text()
        return frozen_reference_text(path, text)

    failures = []
    current_paths = {p.relative_to(root).as_posix() for p in (root / 'chapters').glob('*.tex')}
    current_paths.add('util/lexicon.tex')
    for path in current_paths | set(fixtures['paragraphs']):
        expected = fixtures['paragraphs'].get(path, [])
        blocks = read(path).splitlines() if path == 'util/lexicon.tex' else re.split(r'\n\s*\n', read(path))
        observed = [digest(block) for block in blocks if 'ový' in block]
        if observed != expected:
            failures.append(f'{path}: frozen exponent-bearing paragraphs changed or added')
    for span in fixtures['spans']:
        source = read(span['source'])
        start, end = span['start'], span['end']
        if source.count(start) != 1 or source.count(end) != 1:
            failures.append(f"{span['source']}: frozen source span markers changed")
            continue
        block = source[source.index(start):source.index(end)]
        if digest(block) != span['sha256']:
            failures.append(f"{span['source']}: protected relative source span changed")
    for path, expected in fixtures['files'].items():
        if digest(read(path)) != expected:
            failures.append(f'{path}: earlier protected fixture or selection file changed')
    return failures

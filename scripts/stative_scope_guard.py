"""Compare the explicitly frozen relative scope with reviewed PR19 content.

Hashes record the reviewed baseline, rather than regenerated current text.
Whole source spans cover rules whose paragraphs do not repeat the exponent.
All exponent-bearing paragraphs are compared as a multiset after migration,
rejecting additions, losses and edits while allowing chapter relocation.
This scope guard supplements independent linguistic review.
"""
from collections import Counter
import hashlib
import json
from pathlib import Path
import re

from source_domains import DOMAIN_CHAPTERS


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


# The source postposition and open conditional were explicitly renamed.
# Normalise only their exact phrases in the protected example and overview;
# the surrounding case rules and relative constructions remain significant.
LEXICAL_FORM_REVISIONS = (
    (r"\ird{Marcí travěte pjaštově z} \trsl{since/after Marek's eating of the" "\n"
     r"bread}, the event head bears the case required by \ird{z}, while",
     r"\ird{Marcí travěte pjaštově cy} \trsl{since/after Marek's eating of the" "\n"
     r"bread}, the event head bears the case required by \ird{cy}, while"),
    (r"Non-finite converb suffixes (\ird{-u}, \ird{-ení}, \ird{-ěc}," "\n"
     "\t\t" r"\ird{-ic}, \ird{-ezmy}, \ird{-it}, \ird{-ouc}, \ird{-esny})",
     r"Non-finite converb suffixes (\ird{-u}, \ird{-ení}, \ird{-ěc}," "\n"
     "\t\t" r"\ird{-ej}, \ird{-ezmy}, \ird{-it}, \ird{-ouc}, \ird{-esny})"),
    (r"Event nominal in indirect case + \ird{z}, \ird{do}, \ird{na}, or \ird{u}",
     r"Event nominal in indirect case + \ird{cy}, \ird{do}, \ird{na}, or \ird{u}"),
)


def frozen_reference_text(path, text):
    if path == 'chapters/08-complex-sentences.tex':
        for original, revised in FINITE_REFERENCE_REVISIONS:
            text = text.replace(revised, original)
    for original, revised in LEXICAL_FORM_REVISIONS:
        text = text.replace(revised, original)
    return text


def structural_text(text):
    """Ignore headings/labels/spacing, plus two exact migrated cross-references.

    Every linguistic form, gloss, example, rule and citation remains significant.
    The cross-reference replacements are deliberately phrase-specific.
    """
    text = re.sub(r'\\(?:section|subsection|subsubsection|paragraph)\*?\{((?:[^{}]|\{[^{}]*\})*)\}', '', text)
    text = re.sub(r'\\label\{[^}]+\}(?:%[^\n]*)?', '', text)
    text = text.replace(r'\noindent', '')
    text = text.replace(
        r'in \ird{-(h)ár} and \ird{-ist} (§\,\ref{sec:lexical-agent-nouns}) classify a',
        r'in \ird{-(h)ár} and \ird{-ist} (Chapter~\ref{ch:derivational}) classify a')
    text = text.replace(
        r'is the ordinary property modifier (§\,\ref{sec:stative-attr}).',
        r'is the ordinary property modifier (Chapter~\ref{ch:verbs}).')
    return re.sub(r'\s+', ' ', text).strip()


def publication_sources(root, overrides):
    """Read actual included chapters, supporting legacy logical-domain mutations."""
    paths = re.findall(r'^\\include\{(chapters/[^}]+)\}',
                       (root / 'grammar.tex').read_text(), re.MULTILINE)
    sources = {path + '.tex': (root / (path + '.tex')).read_text()
               for path in paths}
    for path, text in overrides.items():
        key = Path(path).stem
        if path.startswith('chapters/') and key in DOMAIN_CHAPTERS:
            for chapter in DOMAIN_CHAPTERS[key]:
                sources.pop(f'chapters/{chapter}.tex', None)
            sources[path] = text
        elif path.startswith('chapters/'):
            sources[path] = text
    return sources


def check_scope(root=ROOT, fixtures=None, overrides=None):
    """Check migrated content against units verified from the reviewed baseline.

    The original raw span/paragraph digests remain in the fixture as provenance.
    Migration hashes derive from those verified originals, with one explicitly
    documented consolidation into the canonical equative treatment.
    """
    if fixtures is None:
        fixtures = json.loads((root / 'scripts/stative-scope-freeze.json').read_text())
    overrides = {} if overrides is None else overrides
    migration = fixtures['migration']
    failures = []
    paragraphs = []
    units = []
    sources = publication_sources(root, overrides)
    for path, text in sources.items():
        # Exact reviewed revisions retain the original migration hashes.
        text = frozen_reference_text('chapters/08-complex-sentences.tex', text)
        for block in re.split(r'\n\s*\n', text):
            normal = structural_text(block)
            if normal:
                units.append(digest(normal))
                if 'ový' in block:
                    paragraphs.append(digest(normal))
    lexicon = overrides.get('util/lexicon.tex')
    if lexicon is None:
        lexicon = (root / 'util/lexicon.tex').read_text()
    paragraphs.extend(digest(structural_text(line)) for line in lexicon.splitlines()
                      if 'ový' in line and structural_text(line))
    if Counter(paragraphs) != Counter(migration['paragraphs']):
        failures.append('publication: frozen exponent-bearing paragraphs changed, lost or added')
    observed = Counter(units)
    replacements = {item['original_span']: item
                    for item in migration['editorial_consolidations']}
    for span in migration['spans']:
        expected = Counter(span['units'])
        replacement = replacements.get(span['original_sha256'])
        if replacement:
            expected.subtract(replacement['original_units'])
            expected.update(replacement['replacement_units'])
        if expected - observed:
            failures.append('publication: protected relative source units changed or lost '
                            + span['original_sha256'][:12])
    # These current bounded regions retain the old whole-span protection
    # against adding an unreviewed rule even when it does not repeat -ový.
    # Region units were verified against the original chapters individually.
    for region in migration['regions']:
        candidates = [text for text in sources.values()
                      if region['start'] in text and region['end'] in text]
        if len(candidates) != 1:
            failures.append(region['source'] + ': protected region markers changed')
            continue
        text = frozen_reference_text('chapters/08-complex-sentences.tex', candidates[0])
        start, end = region['start'], region['end']
        if text.count(start) != 1 or text.count(end) != 1:
            failures.append(region['source'] + ': protected region markers are not unique')
            continue
        block = text[text.index(start):text.index(end)]
        current = Counter(digest(structural_text(unit))
                          for unit in re.split(r'\n\s*\n', block)
                          if structural_text(unit))
        if current != Counter(region['units']):
            failures.append(region['source'] + ': protected relative region changed or added')
    for path, expected in fixtures['files'].items():
        text = overrides[path] if path in overrides else (root / path).read_text()
        if digest(text) != expected:
            failures.append(f'{path}: earlier protected fixture or selection file changed')
    return failures

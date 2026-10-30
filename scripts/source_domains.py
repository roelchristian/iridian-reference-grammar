"""Compatibility views for reviewed fixtures after the chapter migration.

The historical fixture keys describe grammatical domains rather than published
files. Only diagnostic consumers use these views: publication links, label
uniqueness and heading checks always inspect the actual included files.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
DOMAIN_CHAPTERS = {
    '01-overview': ['01-overview', '09-clause-structure'],
    '02-phonology': ['02-phonology', '03-morphophonology'],
    '03-verbs': ['06-verbal-morphology', '07-argument-structure',
                 '08-derivation-nominalisation', '09-clause-structure',
                 '10-predicate-constructions', '11-negation', '13-clause-types',
                 '15-embedding', '16-clause-linking'],
    '04-nouns': ['04-nominal-morphology', '05-nominal-syntax',
                 '08-derivation-nominalisation', '14-information-structure'],
    '05-function-words': ['12-particles-scope', '13-clause-types',
                          '16-clause-linking', '17-discourse'],
    '06-simple-sentence': ['09-clause-structure', '10-predicate-constructions',
                           '11-negation', '12-particles-scope', '13-clause-types',
                           '14-information-structure'],
    '07-information-structure': ['14-information-structure'],
    '08-complex-sentences': ['15-embedding', '16-clause-linking'],
    '09-discourse': ['17-discourse'],
    '10-derivational': ['08-derivation-nominalisation', '02-phonology'],
}


def expand_tables(text, sources=None, root=ROOT):
    """Resolve the shared paradigm excerpts within their grammatical domain."""
    def replace(match):
        path = match[1] + ".tex"
        return sources.get(path, "") if sources is not None else (root / path).read_text()
    return re.sub(r"\\input\{(util/paradigm-tables/[^}]+)\}", replace, text)


def domain_sources(sources):
    """Build fixture views from active sources, leaving auxiliary inputs intact."""
    result = {path: text for path, text in sources.items()
              if not path.startswith('chapters/')}
    for domain, chapters in DOMAIN_CHAPTERS.items():
        result[f'chapters/{domain}.tex'] = '\n\n'.join(
            expand_tables(sources[f'chapters/{chapter}.tex'], sources) for chapter in chapters
            if f'chapters/{chapter}.tex' in sources)
    return result


def read_domain(path, root=ROOT):
    """Read a reviewed fixture domain without retaining obsolete chapter files."""
    path = Path(path)
    key = path.stem
    if path.parent.name == 'chapters' and key in DOMAIN_CHAPTERS:
        return '\n\n'.join(expand_tables((root / 'chapters' / f'{chapter}.tex').read_text(), root=root)
                            for chapter in DOMAIN_CHAPTERS[key])
    return (path if path.is_absolute() else root / path).read_text()

#!/usr/bin/env python3
"""Check Appendix A coverage of projection names and explicitly marked heads.

Follow the maintained book's includes, not archives, fixtures or research notes.
This lexical completeness check also counts labels discussed as provisional or
rejected: mentioning a label never establishes its theoretical status. Semantic
accuracy, bare head names, features and notation still require editorial review.
"""
from pathlib import Path
import re
import runpy
import sys

ROOT = Path(__file__).resolve().parents[1]
# Reuse the publication include walker and comment stripping of the full check.
active_sources = runpy.run_path(str(ROOT / 'scripts/check-grammar.py'))['active_sources']

# These P-final strings are glosses/indices/semantic predicates, not projections.
NON_PROJECTIONS = {'ANTIP', 'AP', 'OVERLAP'}
PROJECTION = re.compile(r'(?<![A-Za-z])(?:[A-Z][A-Za-z.]*P|[nv]P)(?![A-Za-z])')
HEAD = re.compile(r'(?<![A-Za-z])([A-Za-z][A-Za-z.]*)'
                  r'(?:\\textsuperscript\{0\}|\$\^\{?0\}?\$)')


def inventory(sources):
    projections, heads = set(), set()
    for path, text in sources.items():
        if not path.startswith(('chapters/', 'util/')) or path == 'util/abbreviations.tex':
            continue
        projections.update(set(PROJECTION.findall(text)) - NON_PROJECTIONS)
        heads.update(HEAD.findall(text))
        if re.search(r'\\surd\$?P', text):
            projections.add('√P')
    return projections, heads


def missing_entries(projections, heads, appendix):
    # Only the dedicated section can satisfy coverage, not an earlier example.
    if r'\label{sec:syntax-symbols}' not in appendix:
        return ['section sec:syntax-symbols']
    section = appendix.split(r'\label{sec:syntax-symbols}', 1)[1]
    missing = sorted(symbol for symbol in projections | heads
                     if (not re.search(r'\\surd\$?P', section) if symbol == '√P'
                         else not re.search(r'(?<![A-Za-z])' + re.escape(symbol)
                                            + r'(?![A-Za-z])', section)))
    return missing


def main():
    sources = active_sources(ROOT / 'grammar.tex')
    projections, heads = inventory(sources)
    missing = missing_entries(projections, heads, sources['util/abbreviations.tex'])
    if missing:
        print('Appendix A syntax inventory missing: ' + ', '.join(missing), file=sys.stderr)
        return 1
    print(f'Syntax inventory coverage OK: {len(projections)} projection/position spellings '
          f'(including √P), {len(heads)} explicitly zero-marked head spellings; '
          'features, bare heads and analytical status reviewed separately.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

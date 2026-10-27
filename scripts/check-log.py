#!/usr/bin/env python3
"""Fail on publication-blocking diagnostics in a completed LuaLaTeX log."""
from pathlib import Path
import re
import sys

path = Path(sys.argv[1])
if not path.is_file():
    sys.exit(f'No build log: {path}. Run make first.')
text = path.read_text(encoding='utf-8', errors='replace')
patterns = (
    r'Missing character:.*',
    r'LaTeX Warning: (?:Reference|Citation).*undefined.*',
    r'LaTeX Warning: There were undefined (?:references|citations).*',
    r'LaTeX Warning: Label\(s\) may have changed.*',
    r'LaTeX Warning: There were multiply-defined labels.*',
    r'^! .*',
    r'^.*: (?:LaTeX|Package \S+) Error:.*',
    r'.*Fatal error.*',
)
failures = []
for pattern in patterns:
    failures.extend(re.findall(pattern, text, re.MULTILINE))
if 'Output written on ' not in text:
    failures.append('No successful PDF output recorded.')
if failures:
    print('\n'.join(dict.fromkeys(failures)), file=sys.stderr)
    sys.exit(1)
overfull = len(re.findall(r'Overfull \\[hv]box', text))
print(f'PDF log passed: no missing glyphs, undefined references, or fatal errors. '
      f'Overfull boxes requiring visual review: {overfull}.')

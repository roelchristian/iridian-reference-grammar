#!/usr/bin/env python3
"""Read-only prerequisites check for the reference grammar's PDF pipeline."""
import argparse
from pathlib import Path
import re
import shutil
import subprocess
import sys

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--latexmk', default='latexmk')
args = parser.parse_args()
missing = []
for command in (args.latexmk, 'lualatex', 'kpsewhich'):
    executable = shutil.which(command)
    print(f'{command}: {executable or "MISSING"}')
    if executable is None:
        missing.append(command)

if shutil.which('kpsewhich'):
    sources = [Path('grammar.tex'), Path('cover.tex'), *Path('styles').glob('*.tex')]
    source = '\n'.join(path.read_text(encoding='utf-8') for path in sources if path.is_file())
    source = re.sub(r'(?m)(?<!\\)%.*$', '', source)
    packages = {'amsbook.cls'}
    for names in re.findall(r'\\usepackage(?:\[[^\]]*\])?\{([^}]+)\}', source):
        packages.update(name.strip() + '.sty' for name in names.split(','))
    for package in sorted(packages):
        result = subprocess.run(['kpsewhich', package], capture_output=True, text=True)
        if result.returncode:
            missing.append(package)
    print(f'TeX packages: {len(packages)} checked')
    fonts = sorted(set(re.findall(r'[A-Za-z][A-Za-z0-9-]*\.(?:otf|ttf)', source)))
    for font in fonts:
        if subprocess.run(['kpsewhich', font], capture_output=True).returncode:
            missing.append(font)
    print(f'TeX font files: {len(fonts)} checked')

if missing:
    print('\nMissing prerequisites: ' + ', '.join(missing), file=sys.stderr)
    print('Install a full TeX Live distribution (MacTeX on macOS), including LuaLaTeX, '
          'latexmk, and the listed packages; then rerun make doctor.', file=sys.stderr)
    sys.exit(1)
print('\nReady. Run make; the first build populates build/cache with LuaTeX font data.')

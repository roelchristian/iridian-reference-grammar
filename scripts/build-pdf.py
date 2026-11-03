#!/usr/bin/env python3
"""Compile away from the published PDF and replace it only after success."""

import argparse
import filecmp
import os
from pathlib import Path
import shlex
import shutil
import subprocess
import sys
import tempfile


def atomic_copy(source, destination):
    """Readers see the complete old file or the complete new file."""
    if destination.is_file() and filecmp.cmp(source, destination, shallow=False):
        return False
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(
            dir=destination.parent, prefix=f'.{destination.name}.', suffix='.tmp',
            delete=False,
        ) as stream:
            temporary = Path(stream.name)
            with source.open('rb') as incoming:
                shutil.copyfileobj(incoming, stream)
            stream.flush()
            os.fsync(stream.fileno())
        shutil.copymode(source, temporary)
        os.replace(temporary, destination)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)
    return True


def publish(output):
    staging = output.parent / '.staging'
    candidate = staging / output.name
    # Reject a missing or interrupted PDF even if the compiler returned zero.
    with candidate.open('rb') as stream:
        header = stream.read(5)
        stream.seek(max(0, candidate.stat().st_size - 1024))
        trailer = stream.read()
    if header != b'%PDF-' or b'%%EOF' not in trailer:
        raise ValueError(f'Incomplete PDF: {candidate}; keeping {output}')
    # Retain the existing public log path used by make check and check-log.py.
    atomic_copy(candidate.with_suffix('.log'), output.with_suffix('.log'))
    if atomic_copy(candidate, output):
        print(f'Published {output}', flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True, type=Path)
    parser.add_argument('--watch', action='store_true')
    parser.add_argument('--publish-only', action='store_true', help=argparse.SUPPRESS)
    parser.add_argument('command', nargs=argparse.REMAINDER)
    args = parser.parse_args()
    command = args.command
    if command[:1] == ['--']:
        command = command[1:]
    if not args.publish_only and not command:
        parser.error('supply a latexmk command after --')

    try:
        if args.publish_only:
            publish(args.output)
            return 0

        staging = args.output.parent / '.staging'
        for directory in (staging, staging / 'chapters', staging / 'util'):
            directory.mkdir(parents=True, exist_ok=True)
        # out2dir directs latexmk's previewer to the published PDF. Disable its
        # ordinary file copies: they overwrite in place, including after errors.
        command += [f'-outdir={staging}', f'-out2dir={args.output.parent}',
                    '-e', '@out2_exts = ();']
        environment = os.environ.copy()
        if args.watch:
            # latexmk invokes success_cmd after each completed successful cycle.
            # Its placeholder expansion requires literal percent signs doubled.
            environment['IRIDIAN_PUBLISH_COMMAND'] = shlex.join([
                sys.executable, str(Path(__file__).resolve()), '--publish-only',
                '--output', str(args.output),
            ]).replace('%', '%%')
            command += ['-pvc', '-e',
                        '$success_cmd = $ENV{"IRIDIAN_PUBLISH_COMMAND"}; '
                        '$pvc_view_file_via_temporary = 0;']
        result = subprocess.run(command, env=environment)
        if result.returncode:
            return result.returncode
        # Also publish up-to-date builds, e.g. if only the public PDF was removed.
        publish(args.output)
        return 0
    except (OSError, ValueError) as error:
        print(f'PDF build: {error}', file=sys.stderr)
        return 1
    except KeyboardInterrupt:
        return 130


if __name__ == '__main__':
    sys.exit(main())

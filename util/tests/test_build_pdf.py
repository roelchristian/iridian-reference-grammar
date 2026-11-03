"""Check publication while compiling, after failure, and across watch cycles."""

import importlib.util
import os
from pathlib import Path
import signal
import subprocess
import sys
import tempfile
import time
import unittest
from unittest.mock import patch


SCRIPT = Path(__file__).resolve().parents[2] / 'scripts' / 'build-pdf.py'
SPEC = importlib.util.spec_from_file_location('build_pdf', SCRIPT)
builder = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(builder)
OLD_PDF = b'%PDF-1.7\nprevious complete PDF\n%%EOF\n'
NEW_PDF = b'%PDF-1.7\nnew complete PDF\n%%EOF\n'

FAKE_COMPILER = r'''
import os
from pathlib import Path
import subprocess
import sys
import time

mode = sys.argv[1]
staging = Path(next(arg.split('=', 1)[1] for arg in sys.argv if arg.startswith('-outdir=')))
pdf = staging / 'sample.pdf'
pdf.write_bytes(b'%PDF-1.7\nunfinished')
Path('started').touch()
if mode == 'blocked':
    while not Path('release').exists():
        time.sleep(0.01)
if mode == 'failure':
    sys.exit(7)
if mode == 'truncated':
    sys.exit(0)
pdf.write_bytes(b'%PDF-1.7\nnew complete PDF\n%%EOF\n')
pdf.with_suffix('.log').write_text('successful compilation\n')
if mode == 'watch':
    subprocess.run(os.environ['IRIDIAN_PUBLISH_COMMAND'], shell=True, check=True)
    pdf.write_bytes(b'%PDF-1.7\nfailed next watch cycle')
    sys.exit(7)
'''


class BuildPdfTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.output = self.root / 'published' / 'sample.pdf'
        self.output.parent.mkdir()
        self.output.write_bytes(OLD_PDF)
        self.output.with_suffix('.log').write_text('previous successful compilation\n')
        self.compiler = self.root / 'compiler.py'
        self.compiler.write_text(FAKE_COMPILER)

    def command(self, mode, watch=False):
        return [sys.executable, str(SCRIPT), '--output', str(self.output),
                *(['--watch'] if watch else []), '--',
                sys.executable, str(self.compiler), mode]

    def run_build(self, mode, watch=False):
        return subprocess.run(self.command(mode, watch), cwd=self.root,
                              capture_output=True, text=True, timeout=10)

    def start_blocked_build(self):
        process = subprocess.Popen(self.command('blocked'), cwd=self.root,
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                   text=True, start_new_session=True)
        self.addCleanup(self.stop_build, process)
        deadline = time.monotonic() + 5
        while not (self.root / 'started').exists():
            if process.poll() is not None or time.monotonic() >= deadline:
                self.fail('Compiler did not reach its in-progress state')
            time.sleep(0.01)
        return process

    @staticmethod
    def stop_build(process):
        if process.poll() is None:
            os.killpg(process.pid, signal.SIGTERM)
        process.communicate(timeout=5)

    def test_old_pdf_remains_readable_until_successful_atomic_replacement(self):
        with self.output.open('rb') as open_reader:
            process = self.start_blocked_build()
            self.assertEqual(self.output.read_bytes(), OLD_PDF)
            (self.root / 'release').touch()
            stdout, stderr = process.communicate(timeout=10)
            self.assertEqual(process.returncode, 0, stdout + stderr)
            self.assertEqual(self.output.read_bytes(), NEW_PDF)
            self.assertEqual(open_reader.read(), OLD_PDF)
        self.assertEqual(self.output.with_suffix('.log').read_text(),
                         'successful compilation\n')

    def test_failed_compilation_preserves_previous_pdf_and_log(self):
        result = self.run_build('failure')
        self.assertEqual(result.returncode, 7, result.stdout + result.stderr)
        self.assertEqual(self.output.read_bytes(), OLD_PDF)
        self.assertEqual(self.output.with_suffix('.log').read_text(),
                         'previous successful compilation\n')
        self.assertIn(b'unfinished',
                      (self.output.parent / '.staging' / 'sample.pdf').read_bytes())

    def test_incomplete_output_is_rejected_even_after_zero_exit_status(self):
        result = self.run_build('truncated')
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('Incomplete PDF', result.stderr)
        self.assertEqual(self.output.read_bytes(), OLD_PDF)

    def test_interrupted_compilation_preserves_previous_pdf(self):
        process = self.start_blocked_build()
        os.killpg(process.pid, signal.SIGINT)
        process.communicate(timeout=10)
        self.assertNotEqual(process.returncode, 0)
        self.assertEqual(self.output.read_bytes(), OLD_PDF)

    def test_watch_keeps_last_success_when_next_cycle_fails(self):
        result = self.run_build('watch', watch=True)
        self.assertEqual(result.returncode, 7, result.stdout + result.stderr)
        self.assertEqual(self.output.read_bytes(), NEW_PDF)
        self.assertIn(b'failed next watch cycle',
                      (self.output.parent / '.staging' / 'sample.pdf').read_bytes())

    def test_copy_failure_preserves_previous_file_and_cleans_temporary(self):
        source = self.root / 'candidate.pdf'
        source.write_bytes(NEW_PDF)

        def fail_mid_copy(incoming, outgoing):
            outgoing.write(incoming.read(10))
            raise OSError('simulated disk full')

        with patch.object(builder.shutil, 'copyfileobj', side_effect=fail_mid_copy):
            with self.assertRaisesRegex(OSError, 'disk full'):
                builder.atomic_copy(source, self.output)
        self.assertEqual(self.output.read_bytes(), OLD_PDF)
        self.assertEqual(list(self.output.parent.glob('*.tmp')), [])

    def test_unchanged_pdf_keeps_inode_and_timestamp(self):
        result = self.run_build('success')
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        previous = self.output.stat()
        result = self.run_build('success')
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        current = self.output.stat()
        self.assertEqual(current.st_ino, previous.st_ino)
        self.assertEqual(current.st_mtime_ns, previous.st_mtime_ns)


if __name__ == '__main__':
    unittest.main()

"""The chapter hierarchy includes starred and run-in headings."""
import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location('heading_checker', ROOT / 'scripts/check-grammar.py')
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


class VerbsHeadingTests(unittest.TestCase):
    def test_rejects_each_deeper_heading_including_starred_and_optional_titles(self):
        for command in ('subsubsection', 'paragraph', 'subparagraph'):
            for suffix in ('{Title}', '*{Title}', '[Short]{Title}', '* {Title}'):
                with self.subTest(command=command, suffix=suffix):
                    failures = checker.verbs_heading_checks({
                        'chapters/03-verbs.tex': '\\' + command + suffix})
                    self.assertEqual(len(failures), 1)

    def test_rejects_deep_headings_in_every_substantive_chapter(self):
        for path in ('chapters/02-phonology.tex', 'chapters/12-particles-scope.tex',
                     'chapters/17-discourse.tex'):
            with self.subTest(path=path):
                self.assertEqual(len(checker.verbs_heading_checks({
                    path: r'\paragraph{Too deep}'})), 1)

    def test_accepts_ordinary_hierarchy_and_ignores_comments(self):
        self.assertEqual(checker.verbs_heading_checks({
            'chapters/03-verbs.tex': r'\chapter{Verbs}\section{Aspect}\subsection{Continuous}'
            '\n% \\paragraph{Editorial note}\n',
            'chapters/02-phonology.tex': r'\subsection{Phonology}',
        }), [])


if __name__ == '__main__':
    unittest.main()

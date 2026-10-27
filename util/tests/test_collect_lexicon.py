"""Regression tests for lexical source extraction (no external dependencies)."""

import importlib.util
from pathlib import Path
import tempfile
import unittest

SPEC = importlib.util.spec_from_file_location("collect_lexicon", Path(__file__).resolve().parents[1] / "collect_lexicon.py")
collector = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(collector)


class CollectorTests(unittest.TestCase):
    def test_comments_escaped_percent_and_nested_arguments(self):
        text = "% \\ird{ignored}\n\\irdp{žár-}{be {very} hot} % \\ird{ignored}\n\\ird{x\\%y}\n"
        entries = list(collector.extract(text, "chapter.tex"))
        self.assertEqual([entry["form"] for entry in entries], ["žár-", r"x\%y"])
        self.assertEqual(entries[0]["gloss"], "be {very} hot")
        self.assertEqual([entry["line"] for entry in entries], [2, 3])

    def test_real_comment_after_escaped_percent(self):
        text = r"\ird{x\%y} % \ird{ignored}"
        self.assertEqual([entry["form"] for entry in collector.extract(text, "x")], [r"x\%y"])

    def test_comment_between_arguments(self):
        entries = list(collector.extract("\\irdp{byl}% note\n{child}", "chapter.tex"))
        self.assertEqual(entries[0]["gloss"], "child")

    def test_macro_boundaries_and_definitions(self):
        text = r"\irdsomething{x} \newcommand{\ird}[1]{\textit{#1}} \ird{x}"
        self.assertEqual([entry["form"] for entry in collector.extract(text, "x")], ["x"])

    def test_phon_and_curated_entry(self):
        records = list(collector.extract(r"\phon{sam}{sam}{stake} \lexentry{byl}{\Ind{} \ird{bylam}}{child}", "x"))
        self.assertEqual(len(records), 2)
        self.assertEqual(records[0]["pronunciation"], "sam")
        self.assertEqual(records[1]["notes"], r"\Ind{} \ird{bylam}")

    def test_malformed_explicit_macro_fails_with_location(self):
        with self.assertRaisesRegex(ValueError, r"chapter.tex:2.*unclosed argument"):
            list(collector.extract("\n\\irdp{x}{broken", "chapter.tex"))
        with self.assertRaisesRegex(ValueError, "expects 2"):
            list(collector.extract(r"\irdp{x}", "chapter.tex"))

    def test_dedup_preserves_conflicting_glosses_and_provenance(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sample.tex"
            path.write_text("\\irdp{byl}{child}\n\\phon{byl}{bɘl}{ash}\n\\ird{byl}", encoding="utf-8")
            entries = collector.collect([path, path], Path(directory))
        self.assertEqual(len(entries), 1)
        self.assertEqual(entries[0]["glosses"], ["child", "ash"])
        self.assertEqual(len(entries[0]["occurrences"]), 3)
        self.assertEqual(entries[0]["occurrences"][0]["path"], "sample.tex")
        self.assertIn("sample.tex:2", collector.render(entries, "tsv"))


if __name__ == "__main__":
    unittest.main()

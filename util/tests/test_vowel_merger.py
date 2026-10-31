"""Vowel-grade convergence without loss of traditional morphological classes."""
import sys
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'scripts'))
from quantity_grades import QuantityGrades, QuantityLicence
from vowel_realisation import realise_vowel_classes


class VowelMergerTests(unittest.TestCase):
    def test_three_varieties_preserve_inherited_high_targets(self):
        source = ('eː', 'iː', 'oː', 'uː')
        for variety, expected in [
                ('principal', ('iː', 'iː', 'uː', 'uː')),
                ('back-merged', ('eː', 'iː', 'uː', 'uː')),
                ('conservative', source)]:
            with self.subTest(variety=variety):
                self.assertEqual(realise_vowel_classes(source, variety), expected)

    def test_six_short_and_four_long_principal_categories(self):
        short = ('a', 'ɛ', 'ɪ', 'ɨ', 'ɔ', 'ʊ')
        long = ('aː', 'eː', 'iː', 'ɨː', 'oː', 'uː')
        self.assertEqual(realise_vowel_classes(short), short)
        self.assertEqual(set(realise_vowel_classes(long)), {'aː', 'iː', 'ɨː', 'uː'})
        self.assertEqual(realise_vowel_classes(('ou̯',)), ('ou̯',))

    def test_short_mid_grades_converge_only_after_variety_selection(self):
        grades = QuantityGrades.from_file()
        for root, conservative, principal in [
                ('ɛ', ('ɛ', 'eː', 'ɪ', 'iː'), ('ɛ', 'iː', 'ɪ', 'iː')),
                ('ɔ', ('ɔ', 'oː', 'ʊ', 'uː'), ('ɔ', 'uː', 'ʊ', 'uː'))]:
            with self.subTest(root=root):
                outputs = tuple(grades.apply((root,), QuantityLicence(
                    'mid-root', grade, True, (0, 1), (0,), 0, True))[0]
                    for grade in ('G0', 'G1', 'G2', 'G3'))
                self.assertEqual(outputs, conservative)
                self.assertEqual(realise_vowel_classes(outputs), principal)

    def test_inherited_long_mid_grade_height_is_no_longer_audible(self):
        grades = QuantityGrades.from_file()
        for root, target in [('eː', 'iː'), ('oː', 'uː')]:
            for grade in ('G0', 'G1', 'G2', 'G3'):
                with self.subTest(root=root, grade=grade):
                    selected = grades.apply((root,), QuantityLicence(
                        'long-mid-root', grade, True, (0, 1), (0,), 0, True))
                    self.assertEqual(realise_vowel_classes(selected), (target,))

    def test_realisation_preserves_consonantal_grades_stress_and_quantity(self):
        source = ('ˈ', 't', 'eː', '.', 'd', 'oː', 'ˌ', 'ts', 'ɨː')
        expected = ('ˈ', 't', 'iː', '.', 'd', 'uː', 'ˌ', 'ts', 'ɨː')
        self.assertEqual(realise_vowel_classes(source), expected)
        self.assertEqual(sum('ː' in token for token in source),
                         sum('ː' in token for token in expected))
        # Contextual phonetics is later: this mapping never applies PAL.
        self.assertEqual(realise_vowel_classes(('p', 'eː', 'x', 'eː')),
                         ('p', 'iː', 'x', 'iː'))

    def test_unsupported_varieties_and_non_token_inputs_are_rejected(self):
        for variety in ('casual', '', None, []):
            with self.subTest(variety=variety), self.assertRaises(ValueError):
                realise_vowel_classes(('eː',), variety)
        for source in ('eː', ['eː'], (None,), ('',)):
            with self.subTest(source=source), self.assertRaises(ValueError):
                realise_vowel_classes(source)


if __name__ == '__main__':
    unittest.main()

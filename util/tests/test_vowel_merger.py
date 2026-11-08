"""Standard long-mid contrasts and explicitly regional vowel mergers."""
import sys
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'scripts'))
from quantity_grades import QuantityGrades, QuantityLicence
from vowel_realisation import lexical_stresses, realise_central_y, realise_vowel_classes


class VowelMergerTests(unittest.TestCase):
    def test_varieties_preserve_inherited_high_targets_and_uo(self):
        source = ('eː', 'iː', 'oː', 'uː', 'uɔ')
        for variety, expected in [
                ('principal', source),
                ('conservative', source),
                ('front-merged', ('iː', 'iː', 'oː', 'uː', 'uɔ')),
                ('back-merged', ('eː', 'iː', 'uː', 'uː', 'uɔ')),
                ('fully-merged', ('iː', 'iː', 'uː', 'uː', 'uɔ'))]:
            with self.subTest(variety=variety):
                self.assertEqual(realise_vowel_classes(source, variety), expected)

    def test_seven_short_and_five_long_principal_categories(self):
        short = ('a', 'ɛ', 'ɪ', 'ɨ', 'ə', 'ɔ', 'ʊ')
        long = ('aː', 'eː', 'iː', 'oː', 'uː')
        self.assertEqual(realise_vowel_classes(short), short)
        self.assertEqual(realise_vowel_classes(long), long)
        self.assertEqual(realise_vowel_classes(('ou̯', 'uɔ')), ('ou̯', 'uɔ'))

    def test_short_mid_grades_remain_distinct_in_principal(self):
        grades = QuantityGrades.from_file()
        for root, expected in [
                ('ɛ', ('ɛ', 'eː', 'ɪ', 'iː')),
                ('ɔ', ('ɔ', 'oː', 'ʊ', 'uː'))]:
            with self.subTest(root=root):
                outputs = tuple(grades.apply((root,), QuantityLicence(
                    'mid-root', grade, True, (0, 1), (0,), 0, True))[0]
                    for grade in ('G0', 'G1', 'G2', 'G3'))
                self.assertEqual(outputs, expected)
                self.assertEqual(realise_vowel_classes(outputs), expected)

    def test_uo_and_restored_mid_vowels_preserve_central_y_stress_domains(self):
        # Four nuclei: uo occupies the initial syllable, y the secondary foot.
        source = ('uɔ', 'r', 'eː', 'n', 'ɨ', 'k', 'oː')
        stress = lexical_stresses(4)
        self.assertEqual(stress, ('primary', 'unstressed', 'secondary', 'unstressed'))
        self.assertEqual(realise_central_y(realise_vowel_classes(source), stress),
                         ('uɔ', 'r', 'eː', 'n', 'ɯ̯ɨ', 'k', 'oː'))

    def test_inherited_long_mid_grade_height_is_audible(self):
        grades = QuantityGrades.from_file()
        for root, raised in [('eː', 'iː'), ('oː', 'uː')]:
            for grade in ('G0', 'G1', 'G2', 'G3'):
                with self.subTest(root=root, grade=grade):
                    selected = grades.apply((root,), QuantityLicence(
                        'long-mid-root', grade, True, (0, 1), (0,), 0, True))
                    target = root if grade in ('G0', 'G1') else raised
                    self.assertEqual(realise_vowel_classes(selected), (target,))

    def test_realisation_preserves_grades_stress_boundaries_and_quantity(self):
        source = ('ˈ', 't', 'eː', '.', 'd', 'oː', 'ˌ', 'ts', 'ɨ', 'ou̯', 'uɔ')
        self.assertEqual(realise_vowel_classes(source), source)
        for variety, front, back in [('front-merged', 'iː', 'oː'),
                                     ('back-merged', 'eː', 'uː'),
                                     ('fully-merged', 'iː', 'uː')]:
            expected = ('ˈ', 't', front, '.', 'd', back, 'ˌ', 'ts', 'ɨ', 'ou̯', 'uɔ')
            self.assertEqual(realise_vowel_classes(source, variety), expected)
            self.assertEqual(sum('ː' in token for token in source),
                             sum('ː' in token for token in expected))
        # Contextual phonetics is later: this mapping never applies PAL.
        self.assertEqual(realise_vowel_classes(('p', 'eː', 'x', 'eː')),
                         ('p', 'eː', 'x', 'eː'))

    def test_unsupported_varieties_and_non_token_inputs_are_rejected(self):
        for variety in ('casual', '', None, []):
            with self.subTest(variety=variety), self.assertRaises(ValueError):
                realise_vowel_classes(('eː',), variety)
        for source in ('eː', ['eː'], (None,), ('',)):
            with self.subTest(source=source), self.assertRaises(ValueError):
                realise_vowel_classes(source)


if __name__ == '__main__':
    unittest.main()

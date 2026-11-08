"""Independent nucleus and quantity examples for the opening gliding vowel."""
import importlib.util
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location('check_grammar', ROOT / 'scripts/check-grammar.py')
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


class ComplexNucleusTests(unittest.TestCase):
    def test_schematic_forms_and_ipa_have_matching_nuclei(self):
        for spelling, ipa, expected in (
                ('suot', 'ˈsuɔt', 1), ('sout', 'ˈsou̯t', 1),
                ('sót', 'ˈsoːt', 1), ('sút', 'ˈsuːt', 1),
                ('šuora', 'ˈʃuɔ.ra', 2), ('šuorime', 'ˈʃuɔ.rɪ.mɛ', 3),
                ('uo', 'ˈʔuɔ', 1), ('pasuora', 'ˈpa.suɔ.ra', 3)):
            with self.subTest(spelling=spelling):
                self.assertEqual(checker.spelling_nuclei(spelling), expected)
                self.assertEqual(checker.ipa_nuclei(ipa), expected)

    def test_explicit_boundaries_preserve_hiatus(self):
        for spelling, ipa in (('u-o', 'ʊ.ɔ'), ('u+o', 'u+ɔ'), ('u.o', 'u.ɔ')):
            with self.subTest(spelling=spelling):
                self.assertEqual(checker.spelling_nuclei(spelling), 2)
                self.assertEqual(checker.ipa_nuclei(ipa), 2)

    def test_quantity_is_independent_of_acutes_and_stress(self):
        for ipa in ('ˈsuɔt', 'paˈsuɔt', 'ˈsoːt', 'ˈsuːt', 'ˈsou̯t'):
            with self.subTest(ipa=ipa):
                self.assertEqual(checker.ipa_long_nuclei(ipa), 1)
        self.assertEqual(checker.ipa_long_nuclei('ˈʊ.ɔ'), 0)

    def test_nonsyllabic_coda_does_not_create_opening_nucleus(self):
        self.assertEqual(checker.ipa_nuclei('ˈpaw'), 1)
        self.assertEqual(checker.ipa_long_nuclei('ˈpaw'), 0)
        self.assertEqual(checker.spelling_nuclei('SUOT'), 1)


if __name__ == '__main__':
    unittest.main()

"""Lexical po- inventory, homophones and inherited quantity/stress fixtures."""
import importlib.util
import json
from pathlib import Path
import re
import sys
import unittest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'scripts'))
from quantity_grades import QuantityGrades, QuantityLicence

SPEC = importlib.util.spec_from_file_location('check_grammar', ROOT / 'scripts/check-grammar.py')
checker = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(checker)


class ReversativePoTests(unittest.TestCase):
    def test_lexical_preverb_is_added_without_removing_its_homophones(self):
        entries = [record for record in checker.extract(
            (ROOT / 'util/lexicon.tex').read_text(), 'util/lexicon.tex')
            if record['macro'] == 'lexentry']
        prefixes = [entry for entry in entries if entry['form'] == 'po-']
        self.assertEqual(len(prefixes), 2)
        self.assertEqual({entry['gloss'] for entry in prefixes},
                         {'reverse a resultant condition; remove; dismantle', 'slightly; somewhat'})
        self.assertIn('declarative complementizer',
                      next(entry['gloss'] for entry in entries if entry['form'] == 'po'))
        verbs = (ROOT / 'chapters/03-verbs.tex').read_text()
        self.assertIn(r'\ird{pomužna}  & \ird{pomúžna}', verbs)
        source = (ROOT / 'chapters/10-derivational.tex').read_text()
        table = source.split(r'\label{tab:lexical-preverbs}', 1)[1].split(r'\end{table}', 1)[0]
        inventory = re.findall(r'^\s*\\ird\{([^}]+)\} &', table, re.M)
        self.assertEqual(len(inventory), 11)
        self.assertIn('po-', inventory)
        self.assertIn('ne-', inventory)

    def test_prefix_and_suffix_nuclei_are_outside_the_root_grade_target(self):
        selected = QuantityGrades.from_file().apply(
            ('p', 'ɔ', 's', 'x', 'ɔ', 'd', 'ɪ', 'm', 'ɛ'),
            QuantityLicence('po-progressive-root', 'G1', True, (2, 6), (4,), 4))
        self.assertEqual(selected, ('p', 'ɔ', 's', 'x', 'oː', 'd', 'ɪ', 'm', 'ɛ'))

    def test_external_negation_preserves_initial_lexical_prefix_stress(self):
        source = (ROOT / 'chapters/10-derivational.tex').read_text()
        fixtures = json.loads((ROOT / 'scripts/quantity-fixtures.json').read_text())
        selected = [case for case in fixtures['pronunciations']
                    if case['form'] in {'poshódime', 'zaposhódime'}]
        self.assertEqual(len(selected), 2)
        self.assertEqual(checker.check_prescribed_pronunciations(
            {'derivation': source}, selected, 'reversative'), [])
        for before, after in [('ˈpɔ.sxoː', 'pɔ.ˈsxoː'), ('zaˈpɔ', 'ˈza.pɔ'),
                              ('ˈpɔ.sxoː', 'ˈpoː.sxɔ')]:
            with self.subTest(change=after):
                self.assertTrue(checker.check_prescribed_pronunciations(
                    {'derivation': source.replace(before, after)}, selected, 'reversative'))


if __name__ == '__main__':
    unittest.main()

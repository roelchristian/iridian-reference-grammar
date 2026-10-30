"""Selected abundance base grade, suffix boundary and limited principal parts."""
import importlib.util
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'scripts'))
from quantity_grades import QuantityGrades, QuantityLicence
from boundary_transducer import BoundaryLicence, BoundaryState, BoundaryTransducer

SPEC = importlib.util.spec_from_file_location('check_grammar', ROOT / 'scripts/check-grammar.py')
checker = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(checker)


class AbundanceAtTests(unittest.TestCase):
    def test_selected_reduced_g0_base_retains_quantity_and_its_nasal(self):
        # Lexical reduction is selected first, independently of quantity.
        base = ('k', 'ɔ', 'l', 'n')
        selected = QuantityGrades.from_file().apply(base, QuantityLicence(
            'abundance-reduced-base', 'G0', True, (0, 4), (1,), 1))
        derived = BoundaryTransducer.from_file().apply(BoundaryState(selected),
            BoundaryLicence('abundance-at', 'plain', True), ('a', 't'))
        self.assertEqual(derived.segments, ('k', 'ɔ', 'l', 'n', 'a', 't'))

    def test_lexical_principal_parts_do_not_assign_unknown_classes(self):
        records = {record['form']: record for record in checker.extract(
            (ROOT / 'util/lexicon.tex').read_text(), 'util/lexicon.tex')
            if record['macro'] == 'lexentry'}
        self.assertEqual(records['kolen']['gloss'], 'grass')
        self.assertIn(r'reduced G0 \ird{koln-}', records['kolen']['notes'])
        self.assertIn('declension and quantity class unassigned', records['kolen']['notes'])
        self.assertIn('finite quantity and ordinary ATTR classes unassigned',
                      records['kolnat-']['notes'])
        source = (ROOT / 'chapters/10-derivational.tex').read_text()
        self.assertIn(r'\ird{koln-} + \ird{-at-} $\rightarrow$ \ird{kolnat-}', source)
        self.assertIn(r'\label{sec:abundance-at}', source)

    def test_stem_pronunciation_preserves_short_root_and_coda_vocalisation(self):
        source = (ROOT / 'chapters/10-derivational.tex').read_text()
        fixtures = json.loads((ROOT / 'scripts/quantity-fixtures.json').read_text())
        selected = [item for item in fixtures['pronunciations'] if item['form'] == 'kolnat-']
        self.assertEqual(len(selected), 1)
        self.assertEqual(checker.check_prescribed_pronunciations(
            {'derivation': source}, selected, 'abundance'), [])
        for wrong in ('ˈkoːw.nat', 'ˈkɔl.nat', 'kɔw.ˈnat'):
            with self.subTest(ipa=wrong):
                self.assertTrue(checker.check_prescribed_pronunciations(
                    {'derivation': source.replace('ˈkɔw.nat', wrong)}, selected, 'abundance'))


if __name__ == '__main__':
    unittest.main()

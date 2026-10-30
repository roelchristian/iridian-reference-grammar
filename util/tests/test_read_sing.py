"""Quantity, Voice and linkage regressions for kař- and kan-."""
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]
import sys
sys.path.insert(0, str(ROOT / 'scripts'))
from source_domains import read_domain, domain_sources

SPEC = importlib.util.spec_from_file_location('check_grammar', ROOT / 'scripts/check-grammar.py')
checker = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(checker)


class ReadSingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.path = 'chapters/03-verbs.tex'
        cls.source = read_domain(cls.path)
        fixtures = json.loads((ROOT / 'scripts/quantity-fixtures.json').read_text())
        cls.table = {'source_tables': [table for table in fixtures['source_tables']
                     if table['label'] == 'tab:read-sing-principal-parts']}
        cls.pronunciations = [case for case in fixtures['pronunciations']
                              if case['form'] in {'kánek', 'kánnik', 'kanžek', 'kářnik', 'kážek',
                                                 'kánice', 'kánnice', 'kanžice', 'kářnice', 'kážice'}]

    def test_principal_parts_preserve_quantity_and_orientation(self):
        self.assertEqual(checker.check_quantity_sources({self.path: self.source}, self.table), [])
        for before, after in [('kářime', 'kařime'), ('kařáž', 'kářaž'),
                              ('kánnik', 'kánik'), ('kannáv', 'kanáv')]:
            with self.subTest(form=before):
                changed = self.source.replace(before, after)
                self.assertTrue(checker.check_quantity_sources({self.path: changed}, self.table))

    def test_ipa_preserves_voice_stems_quantity_nasals_and_linker(self):
        self.assertEqual(checker.check_prescribed_pronunciations(
            {self.path: self.source}, self.pronunciations, 'read/sing'), [])
        for before, after in [('ˈkaːn.nɪk', 'ˈkaː.nɪk'), ('ˈkan.ʒɛk', 'ˈkaːn.ʒɛk'),
                              ('ˈkaːʒ.nɪk', 'ˈkaːʃ.nɪk'), ('ˈkan.ʒɪ.tsɛ', 'ˈkan.ʒɪ.tʃɛ')]:
            with self.subTest(ipa=before):
                changed = self.source.replace(before, after)
                self.assertTrue(checker.check_prescribed_pronunciations(
                    {self.path: changed}, self.pronunciations, 'read/sing'))

    def test_lexicon_records_both_antipassive_principal_parts(self):
        entries = {record['form']: record for record in
                   checker.extract((ROOT / 'util/lexicon.tex').read_text(), 'util/lexicon.tex')
                   if record['macro'] == 'lexentry'}
        self.assertIn(r'\ird{kanžek}', entries['kan-']['notes'])
        self.assertIn(r'\ird{káž-}', entries['kař-']['notes'])
        self.assertIn(r'\ird{kářnikový}', entries['kař-']['notes'])
        self.assertEqual(entries['kař-']['gloss'], 'read')


if __name__ == '__main__':
    unittest.main()

"""Class I quantity, anchoring and lexical meanings for nuž and vruh."""
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location('check_grammar', ROOT / 'scripts/check-grammar.py')
checker = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(checker)


class CityTownTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.path = 'chapters/04-nouns.tex'
        cls.source = (ROOT / cls.path).read_text()
        fixtures = json.loads((ROOT / 'scripts/quantity-fixtures.json').read_text())
        cls.table = {'source_tables': [table for table in fixtures['source_tables']
                     if table['label'] == 'tab:city-town-paradigms']}
        cls.pronunciations = [case for case in fixtures['pronunciations']
                              if case['form'] in {'nuž', 'nužo', 'vruh', 'vrúhe'}]

    def test_case_number_and_anchoring_keep_their_licensed_quantities(self):
        self.assertEqual(checker.check_quantity_sources({self.path: self.source}, self.table), [])
        for before, after in [('núže', 'nuže'), ('nužam', 'núžam'), ('vrúhe', 'vrúže'),
                              ('vruham', 'vruhe'), ('vrúhove', 'vruhove'),
                              ('núžete', 'núžé'), ('vruhato', 'vruhá')]:
            with self.subTest(form=before):
                changed = self.source.replace(before, after)
                self.assertTrue(checker.check_quantity_sources({self.path: changed}, self.table))

    def test_pronunciations_keep_devoicing_quantity_and_velar(self):
        self.assertEqual(checker.check_prescribed_pronunciations(
            {self.path: self.source}, self.pronunciations, 'city/town'), [])
        for before, after in [('nʊʃ', 'nʊʒ'), ('ˈnʊ.ʒɔ', 'ˈnʊ.ʃɔ'),
                              ('vrʊx', 'vrʊʒ'), ('ˈvruː.xɛ', 'ˈvrʊ.xɛ')]:
            with self.subTest(ipa=before):
                changed = self.source.replace(before, after)
                self.assertTrue(checker.check_prescribed_pronunciations(
                    {self.path: changed}, self.pronunciations, 'city/town'))

    def test_unique_city_and_town_entries_preserve_other_meanings(self):
        entries = [record for record in checker.extract(
            (ROOT / 'util/lexicon.tex').read_text(), 'util/lexicon.tex')
            if record['macro'] == 'lexentry']
        for meaning, form in [('city', 'nuž'), ('town', 'vruh')]:
            selected = [entry for entry in entries if entry['gloss'] == meaning]
            self.assertEqual([entry['form'] for entry in selected], [form])
            self.assertIn('Class I', selected[0]['notes'])
        self.assertEqual([entry['gloss'] for entry in entries if entry['form'] == 'hrad'],
                         ['goodness; be good'])
        self.assertIn(r'\ird{barocezná dvorba}', (ROOT / 'chapters/10-derivational.tex').read_text())


if __name__ == '__main__':
    unittest.main()

"""Nominal possessor omission preserves overt cases and clausal argument count."""
import importlib.util
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location('check_grammar', ROOT / 'scripts/check-grammar.py')
checker = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(checker)


class ImplicitPossessionTests(unittest.TestCase):
    def test_overt_and_implicit_possessors_keep_the_same_head_and_predicate(self):
        source = (ROOT / 'chapters/04-nouns.tex').read_text()
        block = source.split(r'\pex\label{ex:nm-implicit-poss}', 1)[1].split(r'\xe', 1)[0]
        pairs = [(surface.strip(), gloss.strip()) for surface, gloss in re.findall(
            r'\\gla\s+(.*?)//\s*\\glb\s+(.*?)//', block, re.S)]
        self.assertEqual(pairs, [
            ('Čás konca.', r'head.\Dir{} hurt-\Cont{}'),
            ('Že čás konca.', r'1\textsc{sg}.\Ind{} head.\Dir{} hurt-\Cont{}'),
            ('Marcí čás konca.', r'Marek.\Ind{} head.\Dir{} hurt-\Cont{}')])
        for surface, gloss in pairs:
            self.assertEqual(len(checker.gloss_tokens(surface)), len(checker.gloss_tokens(gloss)))
            self.assertEqual(gloss.count(r'\Dir{}'), 1)
            self.assertEqual(checker.gloss_tokens(gloss)[-1], r'hurt-\Cont{}')

    def test_lexical_entries_and_pronoun_paradigm_do_not_supply_extra_person_or_class(self):
        records = {entry['form']: entry for entry in checker.extract(
            (ROOT / 'util/lexicon.tex').read_text(), 'util/lexicon.tex')
            if entry['macro'] == 'lexentry'}
        self.assertIn('relational body-part noun', records['čás']['notes'])
        self.assertIn(r'lexical long \ird{á}', records['čás']['notes'])
        self.assertIn('quantity class unspecified', records['konc-']['notes'])
        self.assertIn(r'listed continuous \ird{konca}', records['konc-']['notes'])
        self.assertIn('Class IX', records['mamka']['notes'])
        nouns = (ROOT / 'chapters/04-nouns.tex').read_text()
        row = re.search(r'1\\textsc\{sg\}\s*&\s*\\ird\{dá\}.*?\\\\', nouns, re.S)
        self.assertIsNotNone(row)
        self.assertIn(r'\ird{že}', row[0])
        self.assertEqual(records['dá']['notes'], r'\Trs{} \ird{dam}; \Ind{} \ird{že}')


if __name__ == '__main__':
    unittest.main()

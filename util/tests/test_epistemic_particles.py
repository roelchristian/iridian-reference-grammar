"""Literal particle spellings, pronunciations and preserved example readings."""
import importlib.util
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location('epistemic_checker', ROOT / 'scripts/check-grammar.py')
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


class EpistemicParticleTests(unittest.TestCase):
    def setUp(self):
        self.sources = checker.active_sources(ROOT / 'grammar.tex')

    def test_current_sources_and_literal_lexical_pronunciations(self):
        self.assertEqual(checker.renamed_particle_checks(self.sources), [])
        path = 'util/lexicon.tex'
        for old, new in [('ˈgda.ɨ', 'ˈkda.ɨ'), ('ˈgda.ɨ', 'ˈgdaj'),
                         ('ˈxla.ɟɛ', 'ˈxla.dɛ'), ('ˈxla.ɟɛ', 'ˈhla.ɟɛ'),
                         ('ˈxla.ɟɛ', 'ˈxla.ɟeː'), ('ˈmoː', 'ˈmɔ'),
                         ('ˈmoː', 'ˈmoːts')]:
            with self.subTest(ipa=new):
                changed = dict(self.sources)
                changed[path] = changed[path].replace(old, new)
                self.assertTrue(checker.renamed_particle_checks(changed))

    def test_obsolete_forms_rejected_case_insensitively_without_matching_substrings(self):
        for form in ('ktady', 'Ktady', 'HLAVDY', 'hlavdy', 'moc', 'Moc', 'MOC'):
            with self.subTest(form=form):
                changed = dict(self.sources, **{'chapters/03-verbs.tex': form})
                self.assertTrue(checker.renamed_particle_checks(changed))
        changed = dict(self.sources, **{'chapters/03-verbs.tex': 'xktady hlavdyx mrocna mocx'})
        self.assertEqual(checker.renamed_particle_checks(changed), [])

    def test_existing_particle_combinations_and_glosses_remain_paired(self):
        source = self.sources['chapters/05-function-words.tex']
        for phrase, gloss in [('Hladě Janek vy ščének.', 'infer'),
                              (r'\ljudge{\#}Hladě Janek vy ščének.', 'infer'),
                              ('Kday Marek doktor?', 'speculative'),
                              ('Janek mó vy ščének.', None),
                              ('Mó vy piaštím!', 'affirm')]:
            match = re.search(r'\\gla\s+' + re.escape(phrase) + r'//\s*\\glb\s+(.*?)//', source, re.S)
            self.assertIsNotNone(match)
            self.assertEqual(match[1].split()[1] if gloss is None else match[1].split()[0],
                             'affirm' if gloss is None else gloss)
        self.assertIn(r'\ird{Kday Marek so doktor?}', source)


if __name__ == '__main__':
    unittest.main()

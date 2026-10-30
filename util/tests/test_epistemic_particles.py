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
        for old, new in [('ˈka.dɨ̞', 'ˈgda.ɨ'), ('ˈka.dɨ̞', 'ˈga.dɨ'),
                         ('ˈka.dɨ̞', 'ˈka.dj'), ('ˈka.dɨ̞', 'ka.ˈdɨ'),
                         ('ˈxla.ɟɛ', 'ˈxla.dɛ'), ('ˈxla.ɟɛ', 'ˈhla.ɟɛ'),
                         ('ˈxla.ɟɛ', 'ˈxla.ɟeː'), ('ˈmoː', 'ˈmɔ'),
                         ('ˈmoː', 'ˈmoːts')]:
            with self.subTest(ipa=new):
                changed = dict(self.sources)
                changed[path] = changed[path].replace(old, new)
                self.assertTrue(checker.renamed_particle_checks(changed))

    def test_obsolete_forms_rejected_case_insensitively_without_matching_substrings(self):
        for form in ('ktady', 'Ktady', 'kday', 'Kday', 'KDAY',
                     'HLAVDY', 'hlavdy', 'moc', 'Moc', 'MOC'):
            with self.subTest(form=form):
                changed = dict(self.sources, **{'chapters/03-verbs.tex': form})
                self.assertTrue(checker.renamed_particle_checks(changed))
        changed = dict(self.sources, **{'chapters/03-verbs.tex':
                       'xktady xkday kdayx -eškady hlavdyx mužna mocx'})
        self.assertEqual(checker.renamed_particle_checks(changed), [])

    def test_kady_pronunciation_is_paired_in_current_description(self):
        path = 'chapters/05-function-words.tex'
        for pronunciation in ('ˈgda.ɨ', 'ˈga.dɨ̞', 'ˈka.dɨ', 'ka.ˈdɨ̞', 'ˈka.ɟɨ̞'):
            with self.subTest(ipa=pronunciation):
                changed = dict(self.sources)
                changed[path] = changed[path].replace('ˈka.dɨ̞', pronunciation)
                self.assertTrue(checker.renamed_particle_checks(changed))
        # The unrelated temporal suffix retains its original spelling.
        for path in ('chapters/03-verbs.tex', 'chapters/08-complex-sentences.tex'):
            self.assertIn(r'\ird{-eškady}', self.sources[path])

    def test_existing_particle_combinations_and_glosses_remain_paired(self):
        source = self.sources['chapters/05-function-words.tex']
        for phrase, gloss in [('Janek hladě vy ščének.', 'infer'),
                              (r'\ljudge{\#}Janek hladě vy ščének.', 'infer'),
                              ('Janek mó vy ščének.', None),
                              ('Mó vy piaštím!', 'affirm')]:
            match = re.search(r'\\gla\s+' + re.escape(phrase) + r'//\s*\\glb\s+(.*?)//', source, re.S)
            self.assertIsNotNone(match)
            self.assertEqual(match[1].split()[1] if phrase != 'Mó vy piaštím!' else match[1].split()[0],
                             'affirm' if gloss is None else gloss)
        # The speculative example is now an English schema pending lexemes.
        speculative = source.split(r'\paragraph{Kady}', 1)[1].split(r'\paragraph{Mlada}', 1)[0]
        self.assertIn(r'\trsl{Might the oldest candle still be burning?}', speculative)
        self.assertIn('a tentative assessment', speculative)
        self.assertIn('English schema', speculative)


if __name__ == '__main__':
    unittest.main()

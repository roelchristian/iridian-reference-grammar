"""Literal phasal expectations and falsifying scope/diagram counterexamples."""
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'scripts'))
from phasal_diagnostics import ordinary_phase, exclusive_phase, check_phasal_diagram, check_phasal_sources


class PhasalDiagnosticsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fixtures = json.loads((ROOT / 'scripts/phasal-fixtures.json').read_text())

    def test_four_phases_and_wrong_backgrounds(self):
        for case in self.fixtures['phases']:
            with self.subTest(case=case):
                before, now = case['before_p'], case['now_p']
                if case['negative']:
                    before, now = not before, not now
                self.assertEqual(ordinary_phase(case['particle'], before, now), case['licensed'])

    def test_exclusive_readings_have_independent_counterexamples(self):
        for case in self.fixtures['exclusive_diagnostics']:
            for scope, expected in [('high-exclusive', case['high_exclusive']),
                                    ('low-exclusive', case['low_exclusive'])]:
                with self.subTest(case=case, scope=scope):
                    self.assertEqual(exclusive_phase(case['particle'], case['before'], case['now'], scope), expected)

    def test_rejects_unlicensed_operators_and_underspecified_context(self):
        for args in [('och', True, True), ('vy', None, True), ('so', True, 1)]:
            with self.assertRaises(ValueError):
                ordinary_phase(*args)
        for before, now, scope in [([True], [True], 'high-exclusive'),
                                   ([True, False], [True], 'high-exclusive'),
                                   ([True, False], [True, False], 'free-reconstruction')]:
            with self.assertRaises(ValueError):
                exclusive_phase('so', before, now, scope)

    def test_source_readings_require_their_own_context_and_local_qualifications(self):
        path = 'chapters/05-function-words.tex'
        source = (ROOT / path).read_text()
        syntax_path = 'chapters/06-simple-sentence.tex'
        sources = {path: source, syntax_path: (ROOT / syntax_path).read_text()}
        self.assertEqual(check_phasal_sources(sources, self.fixtures), [])
        for old, new in [('Ježe Marku so piaštník?', 'Mám Marku so piaštník?'),
                         ('Janek visited on Friday', 'Janek had never visited'),
                         ('another arrival', 'the only arrival'),
                         ('least likely', 'equally likely'),
                         ('does not assert', 'asserts'),
                         ('not a presupposed actual occurrence', 'a presupposed actual occurrence'),
                         ('relevant discontinuity', 'uninterrupted persistence')]:
            with self.subTest(replacement=new):
                self.assertIn(old, source)
                self.assertTrue(check_phasal_sources(dict(sources, **{path: source.replace(old, new)}), self.fixtures))

    def test_exclusive_source_pair_cannot_swap_scope_or_current_exclusion(self):
        sources = {path: (ROOT / path).read_text() for path in
                   ('chapters/05-function-words.tex', 'chapters/06-simple-sentence.tex')}
        path = 'chapters/06-simple-sentence.tex'
        self.assertEqual(check_phasal_sources(sources, self.fixtures), [])
        cases = self.fixtures['exclusive_source_examples']
        for old, new in [(cases[0]['scope'], cases[1]['scope']),
                         ('remains the sole open gate today', 'another gate is open today'),
                         ('a third gate\n has just opened', 'a third gate\n has remained open')]:
            with self.subTest(change=new):
                self.assertIn(old, sources[path])
                changed = dict(sources, **{path: sources[path].replace(old, new)})
                self.assertTrue(check_phasal_sources(changed, self.fixtures))

    def test_diagram_literal_rows_and_scope_are_not_generated_from_rules(self):
        source = (ROOT / 'util/phasal-polarity-diagram.tex').read_text()
        self.assertEqual(check_phasal_diagram(source, self.fixtures), [])
        for old, new in [('{vy}{(\\neg P)}{P}{\\neg P}', '{vy}{(\\neg P)}{\\neg P}{P}'),
                         ('{so}{(\\neg P)}', '{so}{P}'),
                         ('{still}', '{not yet}'), ('{vy}{P}', '{so}{P}'),
                         ('{$#4$}', '{$#5$}'), ('{$#5$}', '{$#4$}')]:
            with self.subTest(new=new):
                self.assertIn(old, source)
                self.assertTrue(check_phasal_diagram(source.replace(old, new), self.fixtures))
        self.assertTrue(check_phasal_diagram(source + '\n' + source, self.fixtures))


if __name__ == '__main__':
    unittest.main()

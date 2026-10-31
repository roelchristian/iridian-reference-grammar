"""Falsifying semantic contexts and selection counterexamples, not prose matches."""
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[2]
import sys
sys.path.insert(0, str(ROOT / 'scripts'))
from source_domains import read_domain, domain_sources

sys.path.insert(0, str(ROOT / 'scripts'))
from clausal_diagnostics import (comment_phase, negative_mood_prejacent,
                                 reduced_description, check_clausal_sources)
from phasal_diagnostics import ordinary_phase


class ClausalDiagnosticsTests(unittest.TestCase):
    def test_published_rows_cannot_reverse_scope_or_change_surface(self):
        path = 'chapters/06-simple-sentence.tex'
        source = read_domain(path)
        self.assertEqual(check_clausal_sources({path: source}), [])
        for old, new in ((r'$D(A(S(\neg P)))$', r'$D(A(\neg S(P)))$'),
                         ('Marek oh so zazdrávime.', 'Marek so oh zazdrávime.'),
                         ('Kamo so pjaštir.', 'Kamo so zapjaštir.'),
                         ('$R(E(V(\\neg P)))$ & L', '$R(E(V(\\neg P)))$ & M')):
            with self.subTest(change=new):
                self.assertIn(old, source)
                self.assertTrue(check_clausal_sources({path: source.replace(old, new)}))

    def test_each_negative_mood_interprets_negation_below_phase(self):
        # For so, ¬SO(P) is true in BOTH rows: it cannot distinguish them.
        # SO(¬P) licenses only continued restraint in the first row.
        for mood in ('imperative', 'hortative', 'irrealis'):
            for particle, old, new, expected in (
                    ('so', False, False, True), ('so', True, False, False),
                    ('vy', True, False, True), ('vy', False, False, False)):
                with self.subTest(mood=mood, particle=particle, old=old):
                    self.assertEqual(negative_mood_prejacent(
                        mood, particle, [old], [new]), expected)
            self.assertNotEqual(negative_mood_prejacent(mood, 'so', [True], [False]),
                                not ordinary_phase('so', True, False))
            self.assertNotEqual(negative_mood_prejacent(mood, 'vy', [False], [False]),
                                not ordinary_phase('vy', False, False))

    def test_mood_licensing_cannot_cross_boundaries_or_add_indicative_neg(self):
        for changes in ({'local': False}, {'indicative_neg': True}):
            with self.assertRaises(ValueError):
                negative_mood_prejacent('imperative', 'so', [False], [False], **changes)
        with self.assertRaises(ValueError):
            negative_mood_prejacent('indicative', 'so', [False], [False])

    def test_affirmative_negative_additive_and_exclusive_cross(self):
        # All eight basic combinations have literal positive and negative cases.
        for negative in (False, True):
            for particle in ('vy', 'so'):
                old = particle == 'so'
                encode = lambda xs: [not x for x in xs] if negative else xs
                for comment, other in (('oh', True), ('kamo', False)):
                    before = encode([old, old if other else False])
                    now = encode([True, other])
                    with self.subTest(negative=negative, particle=particle, comment=comment):
                        self.assertTrue(comment_phase(particle, before, now,
                                        negative=negative, comment=comment))
                        bad = encode([False, other])
                        self.assertFalse(comment_phase(particle, before, bad,
                                         negative=negative, comment=comment))
                        if negative:
                            for mood in ('imperative', 'hortative', 'irrealis'):
                                self.assertTrue(negative_mood_prejacent(
                                    mood, particle, before, now, comment=comment))

    def test_negative_exclusive_readings_diverge_with_same_associate(self):
        # Negated alternatives: previously both refrain, now only associate does.
        before, now = [False, False], [False, True]
        for particle, high, low in (('so', True, False), ('vy', False, True)):
            for scope, expected in (('high', high), ('low', low)):
                self.assertEqual(comment_phase(particle, before, now, negative=True,
                                               comment='kamo', scope=scope), expected)
        for comment in (None, 'oh'):
            with self.assertRaises(ValueError):
                comment_phase('so', before, now, comment=comment, scope='low')

    def test_reduced_selector_keeps_inner_structure_excludes_internal_operators(self):
        asp = ('AspP', ('VoiceOrient', ('CausP', ('VoiceP', ('vP', ('VP',))))))
        self.assertTrue(reduced_description(asp))
        self.assertTrue(reduced_description(
            ('AspP', ('VoiceOrient', ('CausP', ('ApplP', ('vP', ('VP',))))))))
        for operator in ('NegP', 'OpNeg', 'PhasP', 'Comm-field', 'MoodP',
                         'EvidPinner', 'EvidPouter'):
            with self.subTest(operator=operator):
                self.assertFalse(reduced_description((operator, asp)))
                self.assertFalse(reduced_description(('AspP', (operator, ('VP',)))))
                # External scope does not change the selected subtree's licence.
                matrix = (operator, asp)
                self.assertTrue(reduced_description(matrix[1]))
        self.assertFalse(reduced_description(('VP',)))


if __name__ == '__main__':
    unittest.main()

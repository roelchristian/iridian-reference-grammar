"""Countermodels for exclusivity, scalar upper bounds and low progress."""
from itertools import product
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'scripts'))
from exclusive_diagnostics import exclusive_content, low_progress, projection_probe
from phasal_diagnostics import exclusive, exclusive_phase


class ExclusiveDiagnosticsTests(unittest.TestCase):
    def test_individual_exclusivity_agrees_with_old_satisfaction_only_model(self):
        # Unordered individual alternatives: each proposition compares to itself.
        for values in product((False, True), repeat=3):
            content = exclusive_content(dict(enumerate(values)), 0,
                                        {(i, i) for i in range(3)})
            self.assertEqual(content.satisfied, exclusive(values))
        absent = exclusive_content({'north': False, 'south': False}, 'north',
                                   {('north', 'north'), ('south', 'south')})
        self.assertFalse(absent.minimum)
        self.assertTrue(absent.maximum)
        additional = exclusive_content({'north': True, 'south': True}, 'north',
                                       {('north', 'north'), ('south', 'south')})
        self.assertTrue(additional.minimum)
        self.assertFalse(additional.maximum)

    def test_scalar_bounds_allow_lower_true_alternatives(self):
        order = {(a, b) for a in range(1, 4) for b in range(1, 4) if a >= b}
        content = exclusive_content({1: True, 2: True, 3: False}, 2, order)
        self.assertTrue(content.satisfied)
        self.assertFalse(exclusive([True, True, False]))
        exceeded = exclusive_content({1: True, 2: True, 3: True}, 2, order)
        self.assertTrue(exceeded.minimum)
        self.assertFalse(exceeded.maximum)
        unachieved = exclusive_content({1: True, 2: False, 3: False}, 2, order)
        self.assertFalse(unachieved.minimum)
        self.assertTrue(unachieved.maximum)

    def test_partial_order_max_also_excludes_incomparables(self):
        order = {('low', 'low'), ('high', 'high'), ('other', 'other'),
                 ('high', 'low')}
        content = exclusive_content({'low': True, 'high': False, 'other': True},
                                    'low', order)
        self.assertTrue(content.minimum)
        self.assertFalse(content.maximum)
        # No true proposition is strictly above low, yet MAX fails.
        self.assertFalse(any(truth and (q, 'low') in order and q != 'low'
                             for q, truth in {'high': False, 'other': True}.items()))

    def test_min_is_not_unconditionally_the_prejacent(self):
        order = {(a, b) for a in (1, 2) for b in (1, 2)}  # tied strengths
        content = exclusive_content({1: False, 2: True}, 1, order)
        self.assertFalse(content.prejacent)
        self.assertTrue(content.satisfied)

    def test_gate_scope_contrast_and_low_entails_high_for_still(self):
        before, now = [True, True, False], [True, False, True]
        self.assertTrue(exclusive_phase('so', before, now, 'high-exclusive'))
        self.assertFalse(exclusive_phase('so', before, now, 'low-exclusive'))
        for values in product((False, True), repeat=6):
            before, now = values[:3], values[3:]
            if exclusive_phase('so', before, now, 'low-exclusive'):
                self.assertTrue(exclusive_phase('so', before, now, 'high-exclusive'))

    def test_progress_anchors_min_at_reference_stage(self):
        scribe = low_progress(1, 3, 3, 4, 20)
        self.assertTrue(scribe.satisfied)
        # SO of a full exclusive proposition would wrongly demand earlier MIN.
        self.assertFalse(1 >= 3)
        self.assertTrue(scribe.prior_maximum)
        self.assertTrue(low_progress(1, 2, 2, 3, 5).satisfied)  # milestones
        self.assertTrue(low_progress(0, 3, 3, 4, 20).satisfied)

    def test_progress_distinguishes_assertion_presupposition_and_context(self):
        cases = [
            ((1, 2, 3, 4, 20), (False, True, True)),  # unachieved MIN
            ((1, 4, 3, 4, 20), (True, False, True)),  # exceeded MAX
            ((4, 3, 3, 4, 20), (False, True, False)), # earlier MAX fails
            ((3, 3, 3, 4, 20), (True, True, False)), # no progress
            ((1, 3, 3, 4, 3), (True, True, False)),  # no higher expectation
        ]
        for degrees, expected in cases:
            with self.subTest(degrees=degrees):
                content = low_progress(*degrees)
                self.assertEqual((content.presupposed, content.asserted,
                                  content.context_licensed), expected)
                self.assertFalse(content.satisfied)
        # Evaluative regret is absent from the input: reassuring floodwater too.
        self.assertTrue(low_progress(1, 2, 2, 3, 8).satisfied)

    def test_projection_hypotheses_are_explicit_and_separate_from_assertion(self):
        content = exclusive_content({'p': False}, 'p', {('p', 'p')})
        for environment in (lambda a: not a,                     # negation
                            lambda a: ('by', (a, not a)),         # question
                            lambda a: ('negative-Mood', a),       # opaque force
                            lambda a: ('epistemic', a)):          # opaque modality
            projected = projection_probe(content, environment, project_minimum=True)
            self.assertIs(projected['projected_minimum'], False)
            self.assertEqual(projected['at_issue'], environment(True))
            local = projection_probe(content, environment, project_minimum=False)
            self.assertIsNone(local['projected_minimum'])
        self.assertFalse(content.prejacent)

    def test_rejects_unprovided_ordering_and_malformed_progress(self):
        for order in (set(), {('p', 'p'), ('q', 'q'), ('p', 'q'), ('q', 'r'), ('r', 'r')}):
            with self.assertRaises(ValueError):
                exclusive_content({'p': True, 'q': False, 'r': False}, 'p', order)
        for degrees in ((1, 3, 3, 3, 20), (1, float('inf'), 3, 4, 20),
                        (True, 3, 3, 4, 20)):
            with self.assertRaises(ValueError):
                low_progress(*degrees)


if __name__ == '__main__':
    unittest.main()

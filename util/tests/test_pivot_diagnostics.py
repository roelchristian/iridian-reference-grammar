"""Independent literal frames and countermodels; no grammatical judgment inferred."""
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'scripts'))
from pivot_diagnostics import (configurational_case, successive_agree_case,
                               outer_selection, naive_all_dp_case, accessible,
                               matching_goal, quantifier_scopes, negative_scopes)


class PivotDiagnosticsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads((ROOT / 'scripts/pivot-fixtures.json').read_text())
        cls.frames = {frame['name']: frame for frame in cls.data['frames']}

    def test_independent_frames_under_both_candidates(self):
        self.assertEqual(len(self.frames), 23)
        for frame in self.frames.values():
            for model in (configurational_case, successive_agree_case):
                with self.subTest(frame=frame['name'], model=model.__name__):
                    self.assertEqual(model(frame), frame['expected'])

    def test_directive_external_case_requires_separate_mood_licence(self):
        for name, expected in [('directive overt simple actor', {'A': 'TRS', 'T': 'DIR'}),
                               ('directive overt causative causer', {'C': 'TRS', 'X': 'IND', 'T': 'DIR'}),
                               ('directive sole participant', {'A': 'DIR'})]:
            frame = self.frames[name]
            for model in (configurational_case, successive_agree_case):
                self.assertEqual(model(frame), expected)
                missing = {key: value for key, value in frame.items() if key != 'external_licence'}
                with self.assertRaises(ValueError):
                    model(missing)
                with self.assertRaises(ValueError):
                    model(dict(frame, external_licence='IND'))

    def test_all_dp_competition_wrongly_marks_causee_and_applied_argument(self):
        self.assertEqual(naive_all_dp_case(['C', 'X', 'B', 'T']),
                         {'C': 'TRS', 'X': 'TRS', 'B': 'TRS', 'T': 'DIR'})
        canonical = self.frames['ERG causative applied transitive']
        self.assertNotEqual(naive_all_dp_case(canonical['order']), canonical['expected'])
        unrestricted = dict(canonical, excluded=[])
        self.assertEqual(configurational_case(unrestricted)['X'], 'TRS')
        with self.assertRaises(ValueError):
            successive_agree_case(unrestricted)

    def test_nearest_nominal_is_not_outer_selected_theme(self):
        self.assertEqual(matching_goal([('C', []), ('X', []), ('T', [])], {'T'}), 'T')
        self.assertEqual(matching_goal([('C', []), ('X', []), ('T', [])], {'C', 'X', 'T'}), 'C')

    def test_inner_appl_priority_cannot_replace_outer_causative_priority(self):
        self.assertEqual(outer_selection('T', 'B', 'X'), 'T')
        self.assertEqual(outer_selection(None, 'B', 'X'), 'B')
        self.assertEqual(outer_selection(None, None, 'X'), 'X')

    def test_pronounced_order_is_wrong_case_configuration(self):
        self.assertEqual(naive_all_dp_case(['T', 'A']), {'T': 'TRS', 'A': 'DIR'})
        self.assertNotEqual(naive_all_dp_case(['T', 'A']),
                            self.frames['active ERG transitive']['expected'])

    def test_reversed_ergative_geometry_is_not_a_licensed_case_input(self):
        frame = self.frames['active ERG transitive']
        for model in (configurational_case, successive_agree_case):
            with self.assertRaisesRegex(ValueError, 'licensing order'):
                model(dict(frame, order=['T', 'A']))
            with self.assertRaisesRegex(ValueError, 'eligible external'):
                model(dict(frame, excluded=['A']))
            with self.assertRaisesRegex(ValueError, 'eligible external'):
                model(dict(frame, external=None))

    def test_chain_copy_does_not_create_a_new_case_competitor(self):
        frame = self.frames['ERG causative transitive']
        copies = dict(frame, order=['C', 'X', 'T', 'T'])
        for model in (configurational_case, successive_agree_case):
            self.assertEqual(model(copies), {'C': 'TRS', 'X': 'IND', 'T': 'DIR'})
        self.assertEqual(naive_all_dp_case(['C', 'T', 'C'])['C'], 'DIR')
        # A new occurrence must not overwrite the already valued chain's TRS.
        self.assertEqual(configurational_case(dict(frame, order=['C','X','T','C']))['C'], 'TRS')

    def test_passive_is_not_active_ergative(self):
        frame = self.frames['NOM passive']
        self.assertEqual(configurational_case(frame), {'A': 'IND', 'T': 'DIR'})
        self.assertEqual(naive_all_dp_case(frame['order'])['A'], 'TRS')

    def test_antipassive_does_not_restore_a_conceptual_patient(self):
        frame = self.frames['ERG causative antipassive']
        self.assertEqual(outer_selection(causee='X'), 'X')
        self.assertNotIn('T', configurational_case(frame))
        with self.assertRaises(ValueError):
            configurational_case(dict(frame, selected='T'))

    def test_nonmatching_dp_does_not_export_a_phase_internal_goal(self):
        for case in self.data['locality']:
            self.assertEqual(accessible(case['boundaries']), case['expected'])
        self.assertIsNone(matching_goal([('X', []), ('T', [(True, False)])], {'T'}))
        self.assertEqual(matching_goal([('X', []), ('T', [(True, True)])], {'T'}), 'T')

    def test_scope_truth_models_distinguish_readings(self):
        for case in self.data['scope']:
            self.assertEqual(quantifier_scopes(case['relation']), case['expected'])
        for case in self.data['negation']:
            self.assertEqual(negative_scopes(case['values']), case['expected'])
        for invalid in ([], [[]], [[True], [False, True]], [[1]]):
            with self.assertRaises(ValueError):
                quantifier_scopes(invalid)
        with self.assertRaises(ValueError):
            negative_scopes([None])


if __name__ == '__main__':
    unittest.main()

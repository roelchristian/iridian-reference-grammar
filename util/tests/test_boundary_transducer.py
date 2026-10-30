"""Independent boundary outputs, locality, invalid licences and mapping regressions."""
import copy
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'scripts'))
from boundary_transducer import (BoundaryError, BoundaryLicence, BoundaryState,
                                 BoundaryTransducer, check_boundary_fixtures)


class BoundaryTransducerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rules = json.loads((ROOT / 'scripts/boundary-mapping.json').read_text(encoding='utf-8'))
        cls.fixtures = json.loads((ROOT / 'scripts/boundary-fixtures.json').read_text(encoding='utf-8'))

    def test_independently_authored_expected_outputs_and_rejections(self):
        self.assertEqual(check_boundary_fixtures(BoundaryTransducer(self.rules), self.fixtures), [])

    def test_independent_expectations_detect_rule_table_regressions(self):
        for section, key, replacement in (
                ('pal_correspondences', 'ts', 'ts'),
                ('pal_correspondences', 't', 'tʃ'),
                ('pal_correspondences', 'r', 'ʒ')):
            with self.subTest(key=key):
                rules = copy.deepcopy(self.rules)
                rules[section][key] = replacement
                self.assertTrue(check_boundary_fixtures(BoundaryTransducer(rules), self.fixtures))
        for grade, field, replacement in (('front', 'velar_output', 'tʃ'),
                                           ('restricted', 'coronal_labial_pal', True),
                                           ('mixed', 'coronal_labial_pal', False)):
            with self.subTest(grade=grade, field=field):
                rules = copy.deepcopy(self.rules)
                rules['grades'][grade][field] = replacement
                self.assertTrue(check_boundary_fixtures(BoundaryTransducer(rules), self.fixtures))

    def test_rejects_extra_grade_instead_of_free_feature_product(self):
        rules = copy.deepcopy(self.rules)
        rules['grades']['no-pal-mixed'] = {'coronal_labial_pal': False, 'velar_output': 'tʃ'}
        with self.assertRaises(BoundaryError):
            BoundaryTransducer(rules)

    def test_rejects_velar_rule_inside_coronal_labial_mapping(self):
        rules = copy.deepcopy(self.rules)
        rules['pal_correspondences']['k'] = 'ts'
        with self.assertRaises(BoundaryError):
            BoundaryTransducer(rules)

    def test_requires_segment_tokens_and_explicit_boolean_licensing(self):
        mapper = BoundaryTransducer(self.rules)
        with self.assertRaises(BoundaryError):
            mapper.apply(BoundaryState('rat'), BoundaryLicence('case', 'front', True))
        for value in ('yes', 1, None):
            with self.subTest(value=value), self.assertRaises(BoundaryError):
                mapper.apply(BoundaryState(('r', 'a', 't')), BoundaryLicence('case', 'front', value))

    def test_requires_boundary_identity_and_grade_name(self):
        mapper = BoundaryTransducer(self.rules)
        for licence in (BoundaryLicence('', 'front', True),
                        BoundaryLicence('case', {'pal': True, 'velar': 'ts'}, True)):
            with self.subTest(licence=licence), self.assertRaises(BoundaryError):
                mapper.apply(BoundaryState(('r', 'a', 't')), licence)

    def test_suffix_does_not_choose_grade_or_retroactively_mutate_its_own_edge(self):
        mapper = BoundaryTransducer(self.rules)
        state = BoundaryState(('r', 'a', 't'))
        output = mapper.apply(state, BoundaryLicence('inner', 'front', True), ('a', 's'))
        self.assertEqual(output.segments, ('r', 'a', 'c', 'a', 's'))
        self.assertEqual(state.segments, ('r', 'a', 't'))
        self.assertEqual(state.history, ())
        outer = mapper.apply(output, BoundaryLicence('outer', 'front', True), ('ɛ',))
        self.assertEqual(outer.segments, ('r', 'a', 'c', 'a', 'ʃ', 'ɛ'))
        self.assertEqual(outer.history, ('inner', 'outer'))


if __name__ == '__main__':
    unittest.main()

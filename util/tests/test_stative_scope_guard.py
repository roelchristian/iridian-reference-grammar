"""The second pass must preserve every reviewed relative construction span."""
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'scripts'))
from stative_scope_guard import check_scope


class StativeScopeGuardTests(unittest.TestCase):
    def test_reviewed_relative_scope_is_unchanged(self):
        self.assertEqual(check_scope(), [])

    def test_rejects_rule_change_without_repeated_exponent(self):
        path = 'chapters/08-complex-sentences.tex'
        source = (ROOT / path).read_text()
        original = 'The silent operator binds the position privileged by embedded Voice and aspect;'
        self.assertIn(original, source)
        changed = source.replace(original, 'The silent operator can bind any participant;', 1)
        self.assertTrue(check_scope(overrides={path: changed}))

    def test_rejects_changed_example_and_added_relative(self):
        path = 'chapters/03-verbs.tex'
        source = (ROOT / path).read_text()
        for changed in (source.replace('mužnový nuž', 'mužnový dum', 1),
                        source + '\n\n' + r'\ird{new-ový}' + '\n'):
            with self.subTest(added=changed.endswith('new-ový}\n')):
                self.assertTrue(check_scope(overrides={path: changed}))

    def test_ordinary_new_metadata_outside_protected_scope_is_allowed(self):
        path = 'chapters/03-verbs.tex'
        source = (ROOT / path).read_text()
        changed = source + '\n\nA lexical metadata record specifies ordinary ATTR class.\n'
        self.assertEqual(check_scope(overrides={path: changed}), [])

    def test_earlier_paradigm_examples_cannot_be_rewritten(self):
        path = 'scripts/stative-fixtures.json'
        source = (ROOT / path).read_text()
        changed = source.replace('mužnový', 'revised-relative', 1)
        self.assertTrue(check_scope(overrides={path: changed}))

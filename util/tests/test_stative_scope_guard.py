"""The second pass must preserve every reviewed relative construction span."""
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[2]
import sys
sys.path.insert(0, str(ROOT / 'scripts'))
from source_domains import read_domain, domain_sources

sys.path.insert(0, str(ROOT / 'scripts'))
from stative_scope_guard import check_scope


class StativeScopeGuardTests(unittest.TestCase):
    def test_reviewed_relative_scope_is_unchanged(self):
        self.assertEqual(check_scope(), [])

    def test_rejects_rule_change_without_repeated_exponent(self):
        path = 'chapters/08-complex-sentences.tex'
        source = read_domain(path)
        original = 'The silent operator binds the position privileged by embedded Voice and aspect;'
        self.assertIn(original, source)
        changed = source.replace(original, 'The silent operator can bind any participant;', 1)
        self.assertTrue(check_scope(overrides={path: changed}))

    def test_rejects_changed_example_and_added_relative(self):
        path = 'chapters/03-verbs.tex'
        source = read_domain(path)
        for changed in (source.replace('mužnový nuž', 'mužnový dum', 1),
                        source + '\n\n' + r'\ird{new-ový}' + '\n'):
            with self.subTest(added=changed.endswith('new-ový}\n')):
                self.assertTrue(check_scope(overrides={path: changed}))

    def test_reviewed_finite_reference_update_preserves_reduced_rule_guard(self):
        path = 'chapters/08-complex-sentences.tex'
        source = read_domain(path)
        self.assertIn('Finite content question & Ordinary placement or marked wh-fronting', source)
        # This finite cross-reference was reviewed; selection remains frozen.
        self.assertEqual(check_scope(overrides={path: source}), [])
        changed = source.replace('no finite I-position required', 'full finite PolP required', 1)
        self.assertTrue(check_scope(overrides={path: changed}))
        # Only the exact reviewed wording is accepted, not arbitrary row edits.
        changed = source.replace('Lower occurrence interpreted under Pol;',
                                 'Every fronted occurrence interpreted above Pol;', 1)
        self.assertTrue(check_scope(overrides={path: changed}))

    def test_ordinary_new_metadata_outside_protected_scope_is_allowed(self):
        path = 'chapters/03-verbs.tex'
        source = read_domain(path)
        changed = source + '\n\nA lexical metadata record specifies ordinary ATTR class.\n'
        self.assertEqual(check_scope(overrides={path: changed}), [])

    def test_source_lexeme_revision_preserves_nominal_case_rule_guard(self):
        path = 'chapters/08-derivation-nominalisation.tex'
        source = (ROOT / path).read_text()
        revised = (r'\ird{Marcí travěte pjaštově cy} '
                   r"\trsl{since/after Marek's eating of the" + '\n'
                   r'bread}, the event head bears the case required by \ird{cy}, while')
        self.assertIn(revised, source)
        self.assertIn('retain their nominal indirect forms', source)
        self.assertEqual(check_scope(overrides={path: source}), [])
        # Renaming the postposition does not authorise a new case frame or
        # another lexical substitution inside the same protected treatment.
        changes = {
            'case rule': source.replace('retain their nominal indirect forms',
                                        'retain their nominal direct forms', 1),
            'postposition': source.replace(revised, revised.replace(r'\ird{cy}', r'\ird{do}'), 1),
        }
        for name, changed in changes.items():
            with self.subTest(change=name):
                self.assertTrue(check_scope(overrides={path: changed}))

    def test_overview_lexeme_revisions_preserve_relative_row_guard(self):
        path = 'chapters/16-clause-linking.tex'
        source = (ROOT / path).read_text()
        self.assertEqual(check_scope(overrides={path: source}), [])
        original = r'Prenominal participant-oriented relative in \ird{-ový}'
        self.assertIn(original, source)
        changed = source.replace(original, r'Unrestricted relative in \ird{-ový}', 1)
        self.assertTrue(check_scope(overrides={path: changed}))

    def test_consolidated_equative_case_rule_remains_protected(self):
        path = 'chapters/10-predicate-constructions.tex'
        source = (ROOT / path).read_text()
        original = 'it is not an overt patient argument inside'
        self.assertIn(original, source)
        changed = source.replace(original, 'it is an overt patient argument inside', 1)
        self.assertTrue(check_scope(overrides={path: changed}))

    def test_rejects_new_rule_without_exponent_inside_migrated_span(self):
        path = 'chapters/15-embedding.tex'
        source = (ROOT / path).read_text()
        marker = r'\subsection{The participant gap and accessibility}'
        self.assertIn(marker, source)
        changed = source.replace(marker, marker + '\n\nAny participant can be selected.\n', 1)
        self.assertTrue(check_scope(overrides={path: changed}))

    def test_earlier_paradigm_examples_cannot_be_rewritten(self):
        path = 'scripts/stative-fixtures.json'
        source = read_domain(path)
        changed = source.replace('mužnový', 'revised-relative', 1)
        self.assertTrue(check_scope(overrides={path: changed}))

"""The second pass must preserve every reviewed relative construction span."""
from pathlib import Path
import sys
import unittest
import json
import hashlib

ROOT = Path(__file__).resolve().parents[2]
import sys
sys.path.insert(0, str(ROOT / 'scripts'))
from source_domains import read_domain, domain_sources

sys.path.insert(0, str(ROOT / 'scripts'))
from stative_scope_guard import (RETROSPECTIVE_REVISIONS, check_scope,
                                frozen_reference_text, articleless_reference_text)


class StativeScopeGuardTests(unittest.TestCase):
    def test_reviewed_relative_scope_is_unchanged(self):
        self.assertEqual(check_scope(), [])

    def test_retrospective_replacement_preserves_relative_selection_guard(self):
        path = 'chapters/08-derivation-nominalisation.tex'
        source = (ROOT / path).read_text()
        self.assertIn(r'\ird{mužnaisovy nuž}', source)
        self.assertEqual(check_scope(overrides={path: source}), [])
        changed = source.replace('mužnaisovy nuž', 'mužnaisovy dum', 1)
        self.assertTrue(check_scope(overrides={path: changed}))

    def test_relative_spelling_migration_preserves_independent_short_ovy(self):
        # Old characters in this expectation are historical comparison input.
        row = (r'Transitive singular & \ird{pjáščikovy / pjáščikovyte} '
               r'& \ird{pjaštovy / pjaštovyte}')
        source = r'\ird{-ovy} \ird{mužnovy} \ird{novy}' + '\n' + row
        expected = r'\ird{-ový} \ird{mužnový} \ird{novy}' + '\n' + row
        self.assertEqual(frozen_reference_text('probe.tex', source), expected)

    def test_articleless_literal_migrations_preserve_original_freeze_provenance(self):
        fixture = json.loads((ROOT / 'scripts/articleless-scope-migrations.json').read_text())
        self.assertEqual(fixture['base_sha'], '2ea86f3046beff0d55ee9f7f7e0f06bb31932e26')
        self.assertEqual(hashlib.sha256((ROOT / 'scripts/stative-scope-freeze.json').read_bytes()).hexdigest(),
                         fixture['freeze_sha256'])
        for passage in fixture['passages']:
            with self.subTest(source=passage['source'], original=passage['original_sha256'][:10]):
                self.assertEqual(hashlib.sha256(passage['original'].encode()).hexdigest(),
                                 passage['original_sha256'])
                self.assertEqual(articleless_reference_text(passage['source'], passage['revised']),
                                 passage['original'])
                self.assertEqual(articleless_reference_text('unrelated.tex', passage['revised']),
                                 passage['revised'])

    def test_articleless_migrations_reject_further_form_rule_and_case_changes(self):
        fixture = json.loads((ROOT / 'scripts/articleless-scope-migrations.json').read_text())
        for passage in fixture['passages']:
            path = passage['source']
            source = (ROOT / path).read_text()
            revised = passage['revised']
            for original, current in RETROSPECTIVE_REVISIONS:
                revised = revised.replace(original, current)
            self.assertIn(revised, source)
            # A changed relative slot, participant form, or example no longer
            # matches the complete approved source-specific passage. Existing
            # original hashes must detect it, even inside migrated material.
            changed = revised.replace(r'\ird{', r'\ird{INVALID-', 1)
            if changed == revised:
                changed = revised.replace('ovy', 'INVALID', 1)
            self.assertNotEqual(changed, revised)
            with self.subTest(source=path, original=passage['original_sha256'][:10]):
                self.assertTrue(check_scope(overrides={path: source.replace(revised, changed, 1)}))

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
        for changed in (source.replace('mužnovy nuž', 'mužnovy dum', 1),
                        source + '\n\n' + r'\ird{new-ovy}' + '\n'):
            with self.subTest(added=changed.endswith('new-ovy}\n')):
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
        revised = (r'\ird{Marcí travě pjaštově cy} '
                   r"\trsl{since/after Marėk's eating of the" + '\n'
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
        original = r'Prenominal participant-oriented relative in \ird{-ovy}'
        self.assertIn(original, source)
        changed = source.replace(original, r'Unrestricted relative in \ird{-ovy}', 1)
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
        changed = source.replace('mužnovy', 'revised-relative', 1)
        self.assertTrue(check_scope(overrides={path: changed}))

    def test_authorised_state_selection_does_not_open_relative_scope(self):
        path = 'chapters/15-embedding.tex'
        source = (ROOT / path).read_text()
        original = 'a stative output admits continuous, retrospective or\ncontemplative aspect'
        self.assertIn(original, source)
        changed = source.replace(original,
                                 'a stative output admits progressive and perfective aspect', 1)
        self.assertTrue(check_scope(overrides={path: changed}))

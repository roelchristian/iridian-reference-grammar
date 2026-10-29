"""Independent allomorph, locality and quantity expectations for inner Evid."""
import copy
import importlib.util
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'scripts'))
from boundary_transducer import BoundaryError, BoundaryLicence, BoundaryState, BoundaryTransducer
from evidential_realisation import attach_indirect_evidential

spec = importlib.util.spec_from_file_location('evidential_source_checker', ROOT / 'scripts/check-grammar.py')
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


class EvidentialRealisationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fixtures = json.loads((ROOT / 'scripts/evidential-fixtures.json').read_text(encoding='utf-8'))

    def test_literal_isolated_and_joined_forms(self):
        mapper = BoundaryTransducer.from_file()
        for case in self.fixtures['cases']:
            with self.subTest(case=case['id']):
                original = BoundaryState(tuple(case['host_segments']), ('selected-host',))
                evidential = attach_indirect_evidential(original, 'evidential', True, mapper)
                self.assertEqual(evidential.segments, tuple(case['evidential_segments']))
                self.assertEqual(evidential.history, ('selected-host', 'evidential'))
                joined = mapper.apply(evidential, BoundaryLicence('linker', 'front', True), ('ɛ',))
                self.assertEqual(joined.segments, tuple(case['linked_segments']))
                self.assertEqual(joined.history, ('selected-host', 'evidential', 'linker'))
                self.assertEqual(original.segments, tuple(case['host_segments']))

    def test_linker_does_not_reach_inner_perfective_or_progressive(self):
        mapper = BoundaryTransducer.from_file()
        for host, expected in [
                (('pʲ', 'aː', 'ʃ', 'tʃ', 'ɛ', 'k'), ('pʲ', 'aː', 'ʃ', 'tʃ', 'ɛ', 'k', 'a', 'ʎ', 'ɛ')),
                (('pʲ', 'a', 'ʃ', 't', 'iː', 'm', 'ɛ'), ('pʲ', 'a', 'ʃ', 't', 'iː', 'm', 'ɛ', 'ʎ', 'ɛ'))]:
            with self.subTest(host=host):
                evidential = attach_indirect_evidential(BoundaryState(host), 'evid', True, mapper)
                joined = mapper.apply(evidential, BoundaryLicence('linker', 'front', True), ('ɛ',))
                self.assertEqual(joined.segments, expected)
                self.assertEqual(joined.segments[:len(host)], host)

    def test_all_vowel_tokens_select_l_without_losing_quantity(self):
        # Test this helper's edge selection, without asserting lexical words.
        mapper = BoundaryTransducer.from_file()
        for vowel in ('a', 'aː', 'ɛ', 'eː', 'ɪ', 'iː', 'ɨ', 'ɨː', 'ɔ', 'oː', 'ʊ', 'uː', 'ou̯'):
            with self.subTest(vowel=vowel):
                result = attach_indirect_evidential(BoundaryState(('t', vowel)), 'evid', True, mapper)
                self.assertEqual(result.segments, ('t', vowel, 'l'))

    def test_lexical_palatal_or_glide_edge_is_consonantal(self):
        mapper = BoundaryTransducer.from_file()
        for edge in ('kʲ', 'pʲ', 'j', 'l', 'ʎ', 'v'):
            with self.subTest(edge=edge):
                result = attach_indirect_evidential(BoundaryState(('a', edge)), 'evid', True, mapper)
                self.assertEqual(result.segments, ('a', edge, 'a', 'l'))

    def test_coda_phonetics_is_not_evidential_exponence(self):
        state = BoundaryState(('pʲ', 'a', 'ʃ', 't', 'a'))
        evidential = attach_indirect_evidential(state, 'evid', True)
        self.assertEqual(evidential.segments, ('pʲ', 'a', 'ʃ', 't', 'a', 'l'))
        self.assertNotIn('w', evidential.segments)
        with self.assertRaises(BoundaryError):
            attach_indirect_evidential(BoundaryState(('a', 'w')), 'evid', True)

    def test_requires_explicit_licensing_and_fresh_boundary(self):
        host = BoundaryState(('t', 'a'))
        for value in (False, None, 1, 'yes'):
            with self.subTest(value=value), self.assertRaises(BoundaryError):
                attach_indirect_evidential(host, 'evid', value)
        for host in (BoundaryState(()), BoundaryState('piašta'), BoundaryState(('t', 'ě'))):
            with self.subTest(host=host), self.assertRaises(BoundaryError):
                attach_indirect_evidential(host, 'evid', True)
        result = attach_indirect_evidential(BoundaryState(('t', 'a')), 'evid', True)
        with self.assertRaises(BoundaryError):
            attach_indirect_evidential(result, 'evid', True)

    def test_consonantal_mapper_keeps_vowel_final_pal_rejection(self):
        mapper = BoundaryTransducer.from_file()
        with self.assertRaises(BoundaryError):
            mapper.apply(BoundaryState(('t', 'a')), BoundaryLicence('linker', 'front', True), ('ɛ',))

    def test_joined_expectations_detect_lateral_mapping_regression(self):
        mapper = BoundaryTransducer.from_file()
        rules = copy.deepcopy(mapper.rules)
        rules['pal_correspondences']['l'] = 'l'
        broken = BoundaryTransducer(rules)
        evidential = attach_indirect_evidential(BoundaryState(('t', 'a')), 'evid', True, broken)
        joined = broken.apply(evidential, BoundaryLicence('linker', 'front', True), ('ɛ',))
        self.assertNotEqual(joined.segments, ('t', 'a', 'ʎ', 'ɛ'))

    def test_source_checks_require_same_row_not_scattered_forms(self):
        fixtures = {'cases': [{'id': 'one', 'forms': ['piaštíme', 'piaštímel', 'piaštímeľe']}],
                    'tables': [{'path': 'example.tex', 'label': 'tab:evid', 'case_ids': ['one']}],
                    'pronunciations': []}
        correct = (r'\label{tab:evid}\ird{piaštíme} & \ird{piaštímel} & '
                   r'\ird{piaštímeľe} \\ \end{table}')
        self.assertEqual(checker.check_evidential_sources({'example.tex': correct}, fixtures), [])
        for changed in (correct.replace('piaštímel', 'piaštímeal'),
                        correct.replace('&', r'\\', 1),
                        correct + r'\label{tab:evid}\ird{piaštíme} & \ird{piaštímeal} & \ird{piaštímeľe} \\ \end{table}'):
            with self.subTest(changed=changed):
                self.assertTrue(checker.check_evidential_sources({'example.tex': changed}, fixtures))

    def test_source_pronunciations_distinguish_coda_w_and_onset_lateral(self):
        fixtures = {'cases': [], 'tables': [], 'pronunciations': [
            {'form': 'piaštal', 'ipa': 'ˈpʲaʃ.taw'},
            {'form': 'piaštaľe', 'ipa': 'ˈpʲaʃ.ta.ʎɛ'}]}
        correct = r'\phon{piaštal}{ˈpʲaʃ.taw}{report} \phon{piaštaľe}{ˈpʲaʃ.ta.ʎɛ}{joined report}'
        self.assertEqual(checker.check_evidential_sources({'example.tex': correct}, fixtures), [])
        for changed in (correct.replace('taw', 'tal'), correct.replace('ʎɛ', 'lɛ'),
                        correct.replace('ˈpʲaʃ.taw', 'pʲaˈʃ.taw'),
                        correct + r'\phon{piaštal}{ˈpʲaʃ.taːw}{wrong length}'):
            with self.subTest(changed=changed):
                self.assertTrue(checker.check_evidential_sources({'example.tex': changed}, fixtures))

    def test_commented_rows_cannot_supply_evidential_paradigm_coverage(self):
        fixtures = {'cases': [{'id': 'one', 'forms': ['piaštíme', 'piaštímel', 'piaštímeľe']}],
                    'tables': [{'path': 'example.tex', 'label': 'tab:evid', 'case_ids': ['one']}],
                    'pronunciations': []}
        row = r'\ird{piaštíme} & \ird{piaštímel} & \ird{piaštímeľe} \\'
        source = '\\label{tab:evid}\n' + row + '\n\\end{table}'
        self.assertEqual(checker.check_evidential_sources({'example.tex': source}, fixtures), [])
        self.assertTrue(checker.check_evidential_sources(
            {'example.tex': source.replace(row, '%' + row)}, fixtures))

    def test_capitalised_evidential_ipa_cannot_hide_a_contradiction(self):
        fixtures = {'cases': [], 'tables': [], 'pronunciations': [
            {'form': 'piaštal', 'ipa': 'ˈpʲaʃ.taw'}]}
        correct = r'\phon{Piaštal}{ˈpʲaʃ.taw}{report}'
        self.assertEqual(checker.check_evidential_sources({'example.tex': correct}, fixtures), [])
        for source in (correct.replace('taw', 'tal'),
                       correct + r'\phon{piaštal}{ˈpʲaʃ.tal}{contradiction}'):
            self.assertTrue(checker.check_evidential_sources({'example.tex': source}, fixtures))

    def test_source_checks_reject_old_evidential_but_allow_explicit_rejection(self):
        fixtures = {'cases': [], 'tables': [], 'pronunciations': []}
        for source in (r'\ird{-ejte}', r'\ird{piaštnikejťe}',
                       r'\begingl\gla Piaštnikejte.//\endgl'):
            with self.subTest(source=source):
                self.assertTrue(checker.check_evidential_sources({'example.tex': source}, fixtures))
        self.assertEqual(checker.check_evidential_sources(
            {'example.tex': r'\ird{*piaštnikejte} % \ird{-ejte}'}, fixtures), [])

    def test_reviewed_table_and_negative_prose_mutations_are_detected(self):
        sources = checker.active_sources(ROOT / 'grammar.tex')
        self.assertEqual(checker.check_evidential_sources(sources, self.fixtures), [])
        for before, after in (
                (r'\ird{piaštímal}', r'\ird{piaštimal}'),
                (r'\ird{piaštél}', r'\ird{piaštéwal}'),
                (r'\ird{piaštiral}', r'\ird{piašticeal}'),
                (r'\ird{piáščeval}', r'\ird{piaščival}'),
                (r'\ird{zapiaštníkal}', r'\ird{piaštníkal}'),
                (r'\ird{piaštéľe}', r'\ird{piašteľe}')):
            with self.subTest(before=before, after=after):
                original = sources['chapters/03-verbs.tex']
                self.assertIn(before, original)
                changed = dict(sources)
                changed['chapters/03-verbs.tex'] = original.replace(before, after, 1)
                self.assertTrue(checker.check_evidential_sources(changed, self.fixtures))


if __name__ == '__main__':
    unittest.main()

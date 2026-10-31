"""Independent long-contemplative, boundary and contextual-phonetics checks."""
import copy
import importlib.util
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[2]
import sys
sys.path.insert(0, str(ROOT / 'scripts'))
from source_domains import read_domain, domain_sources

sys.path.insert(0, str(ROOT / 'scripts'))
from boundary_transducer import BoundaryLicence, BoundaryState, BoundaryTransducer
from evidential_realisation import attach_indirect_evidential

spec = importlib.util.spec_from_file_location('contemplative_checker', ROOT / 'scripts/check-grammar.py')
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


class ContemplativeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fixtures = json.loads((ROOT / 'scripts/contemplative-fixtures.json').read_text(encoding='utf-8'))

    def test_underlying_postalveolar_survives_direct_and_evidential_linking(self):
        mapper = BoundaryTransducer.from_file()
        host = BoundaryState(('pʲ', 'a', 'ʃ', 't', 'aː', 'ʒ'))
        linked = mapper.apply(host, BoundaryLicence('linker', 'front', True), ('ɛ',))
        self.assertEqual(linked.segments, ('pʲ', 'a', 'ʃ', 't', 'aː', 'ʒ', 'ɛ'))
        evid = attach_indirect_evidential(host, 'evid', True, mapper)
        self.assertEqual(evid.segments, ('pʲ', 'a', 'ʃ', 't', 'aː', 'ʒ', 'a', 'l'))
        joined = mapper.apply(evid, BoundaryLicence('linker', 'front', True), ('ɛ',))
        self.assertEqual(joined.segments, ('pʲ', 'a', 'ʃ', 't', 'aː', 'ʒ', 'a', 'ʎ', 'ɛ'))
        self.assertEqual(host.segments[-1], 'ʒ')

    def test_front_grade_does_not_supply_x_to_zh_rule(self):
        mapper = BoundaryTransducer.from_file()
        # Constructed phonological strings test identity, not lexical paradigms.
        for edge in ('x', 'ʃ', 'ʒ'):
            with self.subTest(edge=edge):
                result = mapper.apply(BoundaryState(('aː', edge)),
                                      BoundaryLicence('linker', 'front', True), ('ɛ',))
                self.assertEqual(result.segments, ('aː', edge, 'ɛ'))

    def test_voiced_identity_expectation_detects_a_mapping_regression(self):
        rules = copy.deepcopy(BoundaryTransducer.from_file().rules)
        rules['pal_correspondences']['ʒ'] = 'ʃ'
        output = BoundaryTransducer(rules).apply(
            BoundaryState(('aː', 'ʒ')), BoundaryLicence('linker', 'front', True), ('ɛ',))
        self.assertNotEqual(output.segments, ('aː', 'ʒ', 'ɛ'))

    def test_explicit_ipa_fixes_stress_quantity_and_contextual_voicing(self):
        fixtures = dict(self.fixtures, table_rows=[], protected_lexemes=[], protected_surfaces=[])
        source = '\n'.join(r'\phon{' + f['form'] + '}{' + f['ipa'] + '}{example}'
                           for f in fixtures['pronunciations'])
        self.assertEqual(checker.check_contemplative_sources({'test.tex': source}, fixtures), [])
        for before, after in [('taːʃ', 'taʃ'), ('taːʃ', 'taːʒ'),
                              ('taː.ʒɛ', 'taː.ʃɛ'), ('taː.ʒaw', 'taː.xaw'),
                              ('taː.ʒa.ʎɛ', 'taː.ʒa.lɛ'), ('ˈpʲaʃ.taːʃ', 'pʲaʃ.ˈtaːʃ')]:
            with self.subTest(after=after):
                self.assertTrue(checker.check_contemplative_sources(
                    {'test.tex': source.replace(before, after)}, fixtures))
        # A correct occurrence cannot conceal a contradictory duplicate.
        self.assertTrue(checker.check_contemplative_sources(
            {'test.tex': source + r'\phon{pjaštáž}{ˈpʲaʃ.taʃ}{wrong quantity}'}, fixtures))

    def test_old_outputs_are_rejected_but_each_and_name_are_preserved(self):
        fixtures = {'pronunciations': [], 'table_rows': [],
                    'protected_lexemes': [], 'protected_surfaces': []}
        for form in ('-ách', 'pjaštách', 'pjaštáchal', 'pjaštáchalě', 'zanách',
                     '-áh', 'pjaštáh', 'pjaštáhal', 'pjaštáhalě', 'zanáh',
                     'jecach', 'Jecach', 'zadach', 'Zadach', 'jecah', 'zadah'):
            with self.subTest(form=form):
                self.assertTrue(checker.check_contemplative_sources(
                    {'test.tex': r'\ird{' + form + '}'}, fixtures))
        accepted = r'\ird{náh študent} \ird{Náh študent} \ird{Báh} \ird{záhár} \ird{záhárí} \ird{*pjaštách} \ird{knářaž} \ird{-až} % \ird{-ách}'
        self.assertEqual(checker.check_contemplative_sources({'test.tex': accepted}, fixtures), [])

    def test_capitalised_contemplative_ipa_cannot_hide_pronunciation_changes(self):
        fixtures = dict(self.fixtures, pronunciations=[self.fixtures['pronunciations'][0]],
                        table_rows=[], protected_lexemes=[], protected_surfaces=[])
        correct = r'\phon{Pjaštáž}{ˈpʲaʃ.taːʃ}{projected eating}'
        self.assertEqual(checker.check_contemplative_sources({'test.tex': correct}, fixtures), [])
        for source in (correct.replace('taːʃ', 'taʃ'),
                       correct.replace('ˈpʲaʃ.taːʃ', 'pʲaʃ.ˈtaːʒ'),
                       correct + r'\phon{pjaštáž}{ˈpʲaʃ.taʃ}{contradiction}'):
            self.assertTrue(checker.check_contemplative_sources({'test.tex': source}, fixtures))

    def test_reviewed_copular_and_existential_rows_preserve_suppletion(self):
        sources = domain_sources(checker.active_sources(ROOT / 'grammar.tex'))
        self.assertEqual(checker.check_contemplative_sources(sources, self.fixtures), [])
        for path, before, after in [
                ('chapters/06-simple-sentence.tex', r'\ird{náž}', r'\ird{neháž}'),
                ('chapters/06-simple-sentence.tex', r'\ird{zanáž}', r'\ird{zanách}'),
                ('chapters/06-simple-sentence.tex', r'\ird{jecáž}', r'\ird{jecach}'),
                ('chapters/06-simple-sentence.tex', r'\ird{zadáž}', r'\ird{zadážal}'),
                ('util/lexicon.tex', r'\lexentry{náh}', r'\lexentry{náž}'),
                ('chapters/06-simple-sentence.tex', 'Báh němscvení kompozitor.', 'Báž němscvení kompozitor.')]:
            with self.subTest(before=before, after=after):
                self.assertIn(before, sources[path])
                changed = dict(sources)
                # Change all occurrences so that a prose occurrence cannot
                # conceal the table row or protected lexical item under test.
                changed[path] = sources[path].replace(before, after)
                self.assertTrue(checker.check_contemplative_sources(changed, self.fixtures))


if __name__ == '__main__':
    unittest.main()

"""Independent local quantity, grade-domain and paradigm regressions."""
import copy
import importlib.util
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'scripts'))
from quantity_grades import QuantityError, QuantityGrades, QuantityLicence
from boundary_transducer import BoundaryLicence, BoundaryState, BoundaryTransducer

spec = importlib.util.spec_from_file_location('quantity_checker', ROOT / 'scripts/check-grammar.py')
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


class QuantityGradesTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fixtures = json.loads((ROOT / 'scripts/quantity-fixtures.json').read_text(encoding='utf-8'))

    def test_independent_literal_outputs(self):
        grades = QuantityGrades.from_file()
        for case in self.fixtures['cases']:
            with self.subTest(case=case['id']):
                licence = QuantityLicence(case['id'], case['grade'], True,
                                          tuple(case['domain']), tuple(case['eligible']),
                                          case['target'], case['raising_licensed'])
                self.assertEqual(grades.apply(tuple(case['input']), licence), tuple(case['expected']))

    def test_stored_run_target_is_second_nucleus_and_c_is_preserved(self):
        grades = QuantityGrades.from_file()
        selected = grades.apply(('z', 'ɛ', 'm', 'a', 'ts'),
            QuantityLicence('run-root', 'G1', True, (0, 5), (1, 3), 3))
        self.assertEqual(selected, ('z', 'ɛ', 'm', 'aː', 'ts'))
        finite = BoundaryTransducer.from_file().apply(
            BoundaryState(selected), BoundaryLicence('perfective', 'plain', True), ('ɛ', 'k'))
        self.assertEqual(finite.segments, ('z', 'ɛ', 'm', 'aː', 'ts', 'ɛ', 'k'))

    def test_bound_quantity_and_consonant_grade_remain_independent(self):
        grades, consonants = QuantityGrades.from_file(), BoundaryTransducer.from_file()
        for stem, grade, raising, expected in [
                (('p', 'ɛ', 'r', 'k'), 'G1', False, ('p', 'eː', 'r', 'ts', 'ɛ')),
                (('l', 'ɔ', 'b', 'k'), 'G3', True, ('l', 'uː', 'b', 'ts', 'iː'))]:
            with self.subTest(stem=stem):
                selected = grades.apply(stem, QuantityLicence('bound-root', grade, True,
                                                             (0, 4), (1,), 1, raising))
                suffix = ('ɛ',) if grade == 'G1' else ('iː',)
                result = consonants.apply(BoundaryState(selected),
                                          BoundaryLicence('case', 'front', True, True), suffix)
                self.assertEqual(result.segments, expected)

    def test_prefix_and_suffix_nuclei_are_outside_root_domain(self):
        grades = QuantityGrades.from_file()
        source = ('p', 'r', 'ɛ', 'z', 'ɛ', 'm', 'a', 'ts', 'ɪ', 'm', 'ɛ')
        result = grades.apply(source, QuantityLicence('prefixed-run-root', 'G1', True,
                                                     (3, 8), (4, 6), 6))
        self.assertEqual(result, ('p', 'r', 'ɛ', 'z', 'ɛ', 'm', 'aː', 'ts', 'ɪ', 'm', 'ɛ'))
        for target in (2, 8, 10):
            with self.subTest(target=target), self.assertRaises(QuantityError):
                grades.apply(source, QuantityLicence('root-only', 'G1', True, (3, 8), (4, 6), target))

    def test_fleeting_or_unlicensed_nucleus_cannot_be_targeted(self):
        grades = QuantityGrades.from_file()
        for target in (0, 3):
            with self.subTest(target=target), self.assertRaises(QuantityError):
                grades.apply(('p', 'ɛ', 'r', 'ɛ', 'k'),
                             QuantityLicence('perek-retained-root', 'G1', True, (0, 5), (1,), target))

    def test_raising_requires_membership_and_a_defined_mid_nucleus(self):
        grades = QuantityGrades.from_file()
        for grade in ('G2', 'G3'):
            with self.subTest(grade=grade), self.assertRaises(QuantityError):
                grades.apply(('ɛ',), QuantityLicence('plain-class', grade, True, (0, 1), (0,), 0))
            with self.subTest(grade=grade), self.assertRaises(QuantityError):
                grades.apply(('a',), QuantityLicence('no-raised-a', grade, True, (0, 1), (0,), 0, True))

    def test_plain_does_not_shorten_and_strong_has_no_third_length(self):
        grades = QuantityGrades.from_file()
        source = ('p', 'eː', 'r', 'ts', 'eː')
        for grade in ('G0', 'G1'):
            with self.subTest(grade=grade):
                self.assertEqual(grades.apply(source, QuantityLicence('protected-anchor', grade, True,
                                                                     (0, 5), (1, 4), 4)), source)
        bad = copy.deepcopy(grades.rules)
        bad['long_pairs']['eː'] = 'eːː'
        with self.assertRaises(QuantityError):
            QuantityGrades(bad, grades.inventory)
        bad = copy.deepcopy(grades.rules)
        bad['long_pairs']['a'] = 'aːː'
        with self.assertRaises(QuantityError):
            QuantityGrades(bad, grades.inventory)
        bad = copy.deepcopy(grades.rules)
        bad['raised_pairs']['ɛ'] = 'iː'
        with self.assertRaises(QuantityError):
            QuantityGrades(bad, grades.inventory)

    def test_requires_valid_licensing_targets_and_phonological_tokens(self):
        grades = QuantityGrades.from_file()
        for value in (False, 1, 'yes'):
            with self.subTest(value=value), self.assertRaises(QuantityError):
                grades.apply(('ɛ',), QuantityLicence('root', 'G1', value, (0, 1), (0,), 0))
        for source in ('perek', (), ('ě',), ('á',), ('p', 'i', 'a')):
            with self.subTest(source=source), self.assertRaises(QuantityError):
                grades.apply(source, QuantityLicence('root', 'G1', True, (0, 1), (0,), 0))

    def test_independent_expectations_detect_length_and_raising_regressions(self):
        grades = QuantityGrades.from_file()
        for section, key, wrong in [('long_pairs', 'ɛ', 'iː'), ('raised_pairs', 'ɔ', 'ɪ')]:
            with self.subTest(section=section):
                rules = copy.deepcopy(grades.rules)
                rules[section][key] = wrong
                if section == 'long_pairs':
                    rules[section]['ɪ'] = 'eː'
                broken = QuantityGrades(rules, grades.inventory)
                cases = [case for case in self.fixtures['cases'] if key in case['input']]
                self.assertTrue(any(broken.apply(tuple(c['input']), QuantityLicence(
                    c['id'], c['grade'], True, tuple(c['domain']), tuple(c['eligible']),
                    c['target'], c['raising_licensed'])) != tuple(c['expected']) for c in cases))

    def test_source_rows_keep_independent_quantity_cells_paired(self):
        table = {'path': 'test.tex', 'label': 'tab:quantity', 'width': 4,
                 'rows': [['pérce', 'pércem', 'pércé', 'pérceme']]}
        fixture = {'source_tables': [table]}
        correct = (r'\label{tab:quantity}\ird{pérce} & \ird{pércem} & '
                   r'\ird{pércé} & \ird{pérceme} \\ \end{table}')
        self.assertEqual(checker.check_quantity_sources({'test.tex': correct}, fixture), [])
        for before, after in [('pércem', 'percem'), ('pércé', 'pérce'),
                              ('pérceme', 'pércéme')]:
            with self.subTest(after=after):
                self.assertTrue(checker.check_quantity_sources(
                    {'test.tex': correct.replace(before, after)}, fixture))

    def test_run_pronunciations_preserve_initial_stress_second_nucleus_length_and_ts(self):
        fixtures = self.fixtures['pronunciations']
        correct = (r'\phon{zemácime}{ˈzɛ.maː.tsɪ.mɛ}{progressive run} '
                   r'\phon{zemácek}{ˈzɛ.maː.tsɛk}{perfective run}')
        self.assertEqual(checker.check_prescribed_pronunciations(
            {'test.tex': correct}, fixtures, 'quantity'), [])
        for old, new in [('ˈzɛ.maː', 'zɛ.ˈmaː'), ('tsɪ', 'tʃɪ'),
                         ('tsɛk', 'tʃɛk'), ('zɛ.maː', 'zmaː'),
                         ('maː', 'ma'), ('zemácek', 'zemáček'),
                         ('zemácime', 'zmácime')]:
            with self.subTest(replacement=new):
                self.assertTrue(checker.check_prescribed_pronunciations(
                    {'test.tex': correct.replace(old, new)}, fixtures, 'quantity'))

    def test_conditioned_short_contemplative_is_class_specific(self):
        fixture = {'source_tables': [{'path': 'test.tex', 'label': 'tab:classes', 'width': 2,
                                     'rows': [['piašta', 'piaštáž'], ['knářa', 'knářaž']]}]}
        correct = (r'\label{tab:classes}\ird{piašta} & \ird{piaštáž} \\ '
                   r'\ird{knářa} & \ird{knářaž} \\ \end{table}')
        self.assertEqual(checker.check_quantity_sources({'test.tex': correct}, fixture), [])
        for changed in (correct.replace('piaštáž', 'piaštaž'), correct.replace('knářaž', 'knářáž')):
            self.assertTrue(checker.check_quantity_sources({'test.tex': changed}, fixture))

    def test_noncanonical_class_iii_plural_is_distinct_from_singular_transitive(self):
        sources = checker.active_sources(ROOT / 'grammar.tex')
        self.assertEqual(checker.check_quantity_sources(sources, self.fixtures), [])
        path = 'chapters/09-discourse.tex'
        for before, after in [(r'\ird{žémy}', r'\ird{žemy}'),
                              (r'\ird{žém}', r'\ird{žem}'),
                              (r'\ird{žémam}', r'\ird{žemám}'),
                              ('Žémy Marku koupnik.', 'Žemy Marku koupnik.')]:
            with self.subTest(after=after):
                self.assertIn(before, sources[path])
                changed = dict(sources)
                changed[path] = sources[path].replace(before, after)
                self.assertTrue(checker.check_quantity_sources(changed, self.fixtures))
        # The reviewed paragraph cannot conceal a contradictory second paradigm.
        changed = dict(sources)
        marker = r'\subsubsection{Clause-peripheral hedge use}'
        contradiction = (r'\ird{žema} \ird{žemy} \ird{žemy} '
                         r'\ird{žem} \ird{žemám} \ird{žema}')
        self.assertIn(marker, sources[path])
        changed[path] = sources[path].replace(marker, contradiction + '\n\n' + marker)
        self.assertTrue(checker.check_quantity_sources(changed, self.fixtures))


if __name__ == '__main__':
    unittest.main()

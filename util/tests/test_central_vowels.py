"""Independent acceptance probes for central vowels, stress and fixed targets.

Unlexicalised inputs test bounded operations. Explicitly selected reduced stems
are supplied by the caller; these tests do not infer deletion from dotted e.
"""
import importlib.util
import json
import sys
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'scripts'))
from boundary_transducer import BoundaryLicence, BoundaryState, BoundaryTransducer
from quantity_grades import QuantityError, QuantityGrades, QuantityLicence
from vowel_realisation import lexical_stresses, realise_central_y, realise_vowel_classes

SPEC = importlib.util.spec_from_file_location('central_vowel_checker', ROOT / 'scripts/check-grammar.py')
checker = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(checker)


class CentralVowelTests(unittest.TestCase):
    def test_independent_primary_secondary_and_unstressed_probes(self):
        # Literal phonological inputs and outputs, not a spelling decoder.
        cases = (
            ('pyrėk', ('p', 'ɨ', 'r', 'ə', 'k'), ('primary', 'unstressed'),
             ('p', 'ɯ̯ɨ', 'r', 'ə', 'k')),
            ('naryk', ('n', 'a', 'r', 'ɨ', 'k'), ('primary', 'unstressed'),
             ('n', 'a', 'r', 'ɨ', 'k')),
            ('narėk', ('n', 'a', 'r', 'ə', 'k'), ('primary', 'unstressed'),
             ('n', 'a', 'r', 'ə', 'k')),
            ('narek', ('n', 'a', 'r', 'ɛ', 'k'), ('primary', 'unstressed'),
             ('n', 'a', 'r', 'ɛ', 'k')),
            ('paranyk', ('p', 'a', 'r', 'a', 'n', 'ɨ', 'k'),
             ('primary', 'unstressed', 'unstressed'),
             ('p', 'a', 'r', 'a', 'n', 'ɨ', 'k')),
            ('paranyka', ('p', 'a', 'r', 'a', 'n', 'ɨ', 'k', 'a'),
             ('primary', 'unstressed', 'secondary', 'unstressed'),
             ('p', 'a', 'r', 'a', 'n', 'ɯ̯ɨ', 'k', 'a')),
            ('paranėka', ('p', 'a', 'r', 'a', 'n', 'ə', 'k', 'a'),
             ('primary', 'unstressed', 'secondary', 'unstressed'),
             ('p', 'a', 'r', 'a', 'n', 'ə', 'k', 'a')),
        )
        for name, source, stress, expected in cases:
            with self.subTest(probe=name):
                self.assertEqual(lexical_stresses(len(stress)), stress)
                self.assertEqual(realise_central_y(source, stress), expected)

    def test_alternating_secondary_stress_requires_a_nonfinal_foot(self):
        self.assertEqual(lexical_stresses(1), ('primary',))
        self.assertEqual(lexical_stresses(5),
                         ('primary', 'unstressed', 'secondary', 'unstressed', 'unstressed'))
        self.assertEqual(lexical_stresses(6),
                         ('primary', 'unstressed', 'secondary', 'unstressed', 'secondary', 'unstressed'))

    def test_both_trajectories_are_one_short_nucleus_and_leave_coda_separate(self):
        for choice, expected in [('back-central', 'ɯ̯ɨ'), ('central-front', 'ɨi̯')]:
            with self.subTest(trajectory=choice):
                output = realise_central_y(('p', 'ɨ', 'l'), ('primary',), choice)
                self.assertEqual(output, ('p', expected, 'l'))
                self.assertEqual(checker.ipa_nuclei(''.join(output)), 1)
                self.assertNotIn('ː', ''.join(output))
                self.assertNotIn('j', output)

    def test_lexical_j_and_consonantal_grade_survive_beside_unstressed_y(self):
        source = ('n', 'a', 'j', 'ɨ', 'k')
        self.assertEqual(realise_central_y(source, ('primary', 'unstressed')), source)
        self.assertEqual(realise_central_y(('n', 'ɨ'), ('primary',), 'central-front'),
                         ('n', 'ɨi̯'))
        self.assertEqual(realise_central_y(('ɲ', 'ɨ'), ('primary',)), ('ɲ', 'ɯ̯ɨ'))

    def test_broad_realiser_preserves_central_categories_without_guessing_stress(self):
        source = ('ɨ', 'ə', 'ɛ', 'j')
        for variety in ('principal', 'back-merged', 'conservative'):
            self.assertEqual(realise_vowel_classes(source, variety), source)
        self.assertEqual(realise_central_y(('ə', 'k'), ('primary',)), ('ə', 'k'))

    def test_precise_stress_and_token_inputs_are_required(self):
        for value in (0, -1, True, 2.5, '3'):
            with self.subTest(value=value), self.assertRaises(ValueError):
                lexical_stresses(value)
        for source, stress, trajectory in (
                ('ɨ', ('primary',), 'back-central'),
                (('ɨ',), (), 'back-central'),
                (('ɨ',), ('emphasis',), 'back-central'),
                (('ɨ',), ('primary',), 'long'),
                (('ɨː',), ('primary',), 'back-central')):
            with self.subTest(source=source, stress=stress), self.assertRaises(ValueError):
                realise_central_y(source, stress, trajectory)

    def test_selected_rightmost_y_is_identity_without_leftward_retargeting(self):
        source = ('p', 'a', 'r', 'ɨ', 'k')
        licence = QuantityLicence('constructed-rightmost-y', 'G1', True, (0, 5), (1, 3), 3)
        self.assertEqual(QuantityGrades.from_file().apply(source, licence), source)
        self.assertEqual((licence.grade, licence.target), ('G1', 3))

    def test_schwa_membership_and_fleeting_eligibility_are_independent(self):
        grades = QuantityGrades.from_file()
        retained = ('p', 'ɛ', 'r', 'ə', 'k')
        # A fleeting slot remains present as a vowel but excluded as a target.
        selected = grades.apply(retained, QuantityLicence(
            'retained-perek', 'G1', True, (0, 5), (1,), 1))
        self.assertEqual(selected, ('p', 'eː', 'r', 'ə', 'k'))
        with self.assertRaises(QuantityError):
            grades.apply(retained, QuantityLicence(
                'excluded-fleeting-slot', 'G1', True, (0, 5), (1,), 3))
        # Stable schwa is an explicit hypothetical eligible input, never deleted.
        stable = ('n', 'ə', 'k')
        self.assertEqual(grades.apply(stable, QuantityLicence(
            'stable-schwa-probe', 'G1', True, (0, 3), (1,), 1)), stable)
        for vowel in ('ɨ', 'ə'):
            for grade in ('G2', 'G3'):
                with self.subTest(vowel=vowel, grade=grade), self.assertRaises(QuantityError):
                    grades.apply((vowel,), QuantityLicence(
                        'no-new-raised-class', grade, True, (0, 1), (0,), 0, True))

    def test_selected_bound_stems_keep_independent_grade_and_case(self):
        grades = QuantityGrades.from_file()
        mapper = BoundaryTransducer.from_file()
        records = {item['new']: item for item in json.loads(
            (ROOT / 'docs/central-vowel-migrations.json').read_text())['migrations']}
        source = (ROOT / 'chapters/03-morphophonology.tex').read_text()
        full = {'Janėk': ('j', 'a', 'n', 'ə', 'k'),
                'perėk': ('p', 'ɛ', 'r', 'ə', 'k'),
                'lobėk': ('l', 'ɔ', 'b', 'ə', 'k')}
        for name, selected, grade, raising, expected in (
                ('Janėk', ('j', 'a', 'n', 'k'), 'G0', False, ('j', 'a', 'n', 'k', 'ʊ')),
                ('perėk', ('p', 'ɛ', 'r', 'k'), 'G1', False, ('p', 'eː', 'r', 'k', 'ʊ')),
                ('lobėk', ('l', 'ɔ', 'b', 'k'), 'G3', True, ('l', 'uː', 'b', 'k', 'ʊ'))):
            with self.subTest(lexeme=name):
                self.assertEqual(tuple(records[name]['full_segments']), full[name])
                self.assertEqual(tuple(records[name]['reduced_base_segments']), selected)
                graded = grades.apply(selected, QuantityLicence(
                    name, grade, True, (0, 4), (1,), 1, raising))
                self.assertEqual(tuple(records[name]['selected_bound_segments']), graded)
                result = mapper.apply(BoundaryState(graded),
                                      BoundaryLicence('transitive', 'plain', True), ('ʊ',))
                self.assertEqual(result.segments, expected)
        for before, after in [('Janėk', 'Janku'), ('perėk', 'pérku'), ('lobėk', 'lúbku')]:
            self.assertIn(r'\ird{' + before + r'} + \ird{-u} $\rightarrow$ \ird{' + after + '}', source)

    def test_retained_and_stable_schwa_and_perfective_are_source_constraints(self):
        source = ' '.join((ROOT / 'chapters/03-morphophonology.tex').read_text().split())
        self.assertIn(r'Fleeting \ird{ė} is retained when deletion would prevent this '
                      r'syllabification without unlicensed consonant loss', source)
        self.assertIn('Liquids are always non-syllabic', source)
        self.assertIn('a stable schwa would remain present in the same environment', source)
        self.assertIn(r'distinct from verbal perfective \ird{-ek} and its bound '
                      r'\ird{-ik-} grade', source)
        # Unlexicalised retention probe: removing this sole nucleus would leave
        # /br/, which cannot be syllabified under the cited no-syllabic-liquid rule.
        # The bounded realiser retains the selected full stem; it does not decide
        # morphological reduction or infer it from the spelling of schwa.
        self.assertEqual(checker.ipa_nuclei('bər'), 1)
        self.assertEqual(checker.ipa_nuclei('br'), 0)
        self.assertEqual(realise_central_y(('b', 'ə', 'r'), ('primary',)), ('b', 'ə', 'r'))

    def test_schwa_does_not_supply_a_palatalisation_instruction(self):
        mapper = BoundaryTransducer.from_file()
        for edge in ('n', 'ɲ', 'p', 'pʲ', 'bʲ', 'mʲ', 'vʲ'):
            with self.subTest(edge=edge):
                result = mapper.apply(BoundaryState((edge,)),
                                      BoundaryLicence('schwa-probe', 'plain', True), ('ə',))
                self.assertEqual(result.segments, (edge, 'ə'))
        spellings = r'\ird{nė} \ird{ňė} \ird{ťė} \ird{ďė} \ird{ľė} '
        spellings += r'\ird{pjė} \ird{bjė} \ird{mjė} \ird{vjė}'
        self.assertEqual(checker.sibilant_spelling_checks({'probe.tex': spellings}), [])

    def test_unicode_and_moving_ipa_nucleus_counts(self):
        for spelling in ('ė', 'Ė', 'e\u0307', 'E\u0307', 'pjė', 'ňė', 'nė'):
            with self.subTest(spelling=spelling):
                self.assertEqual(checker.spelling_nuclei(spelling), 1)
        for spelling, ipa, count in (
                ('pyrėk', 'ˈpɯ̯ɨ.rək', 2), ('pyrėk', 'ˈpɨi̯.rək', 2),
                ('paranyka', 'ˈpa.raˌnɨi̯.ka', 4), ('obėl', 'ˈʔɔ.bəw', 2),
                ('oblu', 'ˈʔɔ.blʊ', 2), ('pjaštou', 'ˈpʲaʃ.tou̯', 2)):
            with self.subTest(spelling=spelling):
                self.assertEqual(checker.spelling_nuclei(spelling), count)
                self.assertEqual(checker.ipa_nuclei(ipa), count)


if __name__ == '__main__':
    unittest.main()

"""Selection counterexamples which morphology alone cannot distinguish."""
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'scripts'))
from valency_profiles import ValencyLicenceError, load_profiles, select


class ValencyProfilesTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.entries = {e['stem']: e for e in load_profiles()['entries']}

    def test_same_lexeme_distinguishes_activity_and_antipassive(self):
        eat = self.entries['pjašt']
        self.assertTrue(select(eat, 'activity', domain='NOM'))
        self.assertTrue(select(eat, 'antipassive', domain='ERG'))
        for construction, domain in [('activity', 'ERG'), ('antipassive', 'NOM')]:
            with self.subTest(construction=construction, domain=domain):
                with self.assertRaises(ValencyLicenceError):
                    select(eat, construction, domain=domain)
        with self.assertRaises(ValencyLicenceError):
            select(eat, 'antipassive', domain='ERG', indicative=False)
        with self.assertRaises(ValencyLicenceError):
            select(eat, 'activity', domain='NOM', indicative=False)
        with self.assertRaises(ValencyLicenceError):
            select(eat, 'antipassive', domain='ERG', overt_patient=True)

    def test_lexical_ambitransitive_preserves_erg_activity(self):
        self.assertTrue(select(self.entries['kan'], 'activity', domain='ERG'))

    def test_instrument_reading_does_not_follow_from_appl_spelling(self):
        self.assertTrue(select(self.entries['pjašt'], 'applicative', domain='NOM',
                               role='instrument', instrument_context=True))
        for stem, contextual in [('pjašt', False), ('zemac', True)]:
            with self.assertRaises(ValencyLicenceError):
                select(self.entries[stem], 'applicative', domain='NOM',
                       role='instrument', instrument_context=contextual)
        with self.assertRaises(ValencyLicenceError):
            select(self.entries['pjašt'], 'applicative', domain='NOM', role='recipient')

    def test_service_performer_is_not_anaphoric_omission(self):
        self.assertTrue(select(self.entries['mar'], 'causative', domain='NOM',
                               omitted_causee=True, service=True))
        with self.assertRaises(ValencyLicenceError):
            select(self.entries['pjašt'], 'causative', domain='NOM',
                   omitted_causee=True, service=True)
        with self.assertRaises(ValencyLicenceError):
            select(self.entries['mar'], 'causative', domain='NOM', omitted_causee=True)
        self.assertTrue(select(self.entries['pjašt'], 'causative', domain='NOM',
                               omitted_causee=True, recoverable_causee=True))

    def test_service_cannot_silently_compose_with_other_frames(self):
        cook = self.entries['mar']
        for change in ({'indicative': False}, {'overt_causee': True},
                       {'recoverable_causee': True}, {'applied': True},
                       {'omitted_causee': False}):
            request = dict(domain='NOM', service=True, omitted_causee=True)
            request.update(change)
            with self.subTest(change=change):
                with self.assertRaises(ValencyLicenceError):
                    select(cook, 'causative', **request)
        with self.assertRaises(ValencyLicenceError):
            select(cook, 'applicative', domain='NOM', role='benefactive', service=True)

    def test_psychological_causation_needs_its_individual_licence(self):
        happy = self.entries['všihn']
        with self.assertRaises(ValencyLicenceError):
            select(happy, 'causative', domain='NOM', causable=True)
        self.assertTrue(select(happy, 'causative', domain='NOM', lexical_causative=True))

    def test_directive_requires_overt_derived_participants(self):
        eat = self.entries['pjašt']
        self.assertTrue(select(eat, 'causative', domain='NOM', directive=True,
                               overt_causee=True))
        with self.assertRaises(ValencyLicenceError):
            select(eat, 'causative', domain='NOM', directive=True,
                   omitted_causee=True, recoverable_causee=True)
        with self.assertRaises(ValencyLicenceError):
            select(eat, 'causative', domain='NOM', directive=True,
                   overt_causee=True, applied=True)
        self.assertTrue(select(eat, 'causative', domain='NOM', directive=True,
                               overt_causee=True, applied=True, overt_applied=True))
        with self.assertRaises(ValencyLicenceError):
            select(eat, 'applicative', domain='NOM', directive=True, role='benefactive')
        self.assertTrue(select(eat, 'applicative', domain='NOM', directive=True,
                               role='benefactive', overt_applied=True))
        # A nonindicative request alone does not assert directive Mood.
        self.assertTrue(select(eat, 'causative', domain='NOM', indicative=False,
                               omitted_causee=True, recoverable_causee=True))

    def test_allomorph_assignment_does_not_supply_semantic_licence(self):
        with self.assertRaises(ValencyLicenceError):
            select(self.entries['svorn'], 'causative', domain='ERG')
        self.assertTrue(select(self.entries['svorn'], 'causative', domain='ERG', causable=True))
        with self.assertRaises(ValencyLicenceError):
            select(self.entries['lov'], 'causative', domain='ERG', lexical_causative=True)
        with self.assertRaises(ValencyLicenceError):
            select(self.entries['kař'], 'causative', domain='ERG')

    def test_applied_causatives_are_lexically_bounded(self):
        self.assertTrue(select(self.entries['pjašt'], 'causative', domain='ERG', applied=True))
        with self.assertRaises(ValencyLicenceError):
            select(self.entries['stoj'], 'causative', domain='ERG', applied=True)


if __name__ == '__main__':
    unittest.main()

"""Mutation checks for the bounded valency-regression checker."""
import importlib.util
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location(
    'check_grammar', Path(__file__).resolve().parents[2] / 'scripts/check-grammar.py')
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


class ValencyChecks(unittest.TestCase):
    def source(self, surface, gloss):
        return (r'\pex\label{ex:test}\begingl\gla ' + surface + '//'
                + r'\glb ' + gloss + r'//\glft Translation//\endgl\xe')

    def fixture(self, surface, gloss):
        return [{'label': 'ex:test', 'examples': [{'surface': surface, 'gloss': gloss}]}]

    def test_reviewed_pair_passes(self):
        surface = 'Byl Marcí travě pjaštébime.'
        gloss = r'child.\Dir{} Marek.\Ind{} bread.\Ind{} eat-\Appl{}-\Prog{}'
        self.assertEqual([], checker.check_valency(self.source(surface, gloss),
                                                  self.fixture(surface, gloss)))

    def test_form_and_gloss_must_remain_paired(self):
        expected = self.fixture('Byl pjaštébime.', r'child.\Dir{} eat-\Appl{}-\Prog{}')
        failures = checker.check_valency(self.source('Byl pjaštime.',
                               r'child.\Dir{} eat-\Appl{}-\Prog{}'), expected)
        self.assertTrue(any('pairs changed' in failure for failure in failures))

    def test_two_direct_arguments_are_rejected(self):
        surface = 'Marek byl pjaštébime.'
        gloss = r'Marek.\Dir{} child.\Dir{} eat-\Appl{}-\Prog{}'
        failures = checker.check_valency(self.source(surface, gloss), self.fixture(surface, gloss))
        self.assertTrue(any('one direct-case' in failure for failure in failures))

    def test_translation_change_is_rejected(self):
        surface = 'Byl Marcí travě pjaštébime.'
        gloss = r'child.\Dir{} Marek.\Ind{} bread.\Ind{} eat-\Appl{}-\Prog{}'
        fixture = self.fixture(surface, gloss)
        fixture[0]['examples'][0]['translation'] = 'Translation'
        source = self.source(surface, gloss)
        self.assertEqual([], checker.check_valency(source, fixture))
        failures = checker.check_valency(source.replace('Translation', 'Feed the child'), fixture)
        self.assertTrue(any('translation changed' in failure for failure in failures))

    def test_illegal_productive_combination_and_order_are_rejected(self):
        for gloss, diagnostic in [
            (r'agent.\Dir{} eat-\Antip{}-\Appl{}-\Pf{}', 'antipassive/applicative'),
            (r'theme.\Dir{} eat-\Trs{}-\Caus{}-\Pf{}', 'precedes causative'),
            (r'beneficiary.\Dir{} run-\Caus{}-\Appl{}-\Pf{}', 'inner valency follows'),
            (r'causee.\Dir{} eat-\Caus{}-\Antip{}-\Pf{}', 'inner valency follows'),
            (r'beneficiary.\Dir{} eat-\Appl{}-\Appl{}-\Pf{}', 'repeated applicative'),
        ]:
            with self.subTest(gloss=gloss):
                failures = checker.check_valency(self.source('Example.', gloss),
                                                 self.fixture('Example.', gloss))
                self.assertTrue(any(diagnostic in failure for failure in failures))

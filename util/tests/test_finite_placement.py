"""Source regressions for finite placement and its preserved lower dependencies.

These check the published contrasts, rather than claiming to implement an
independent parser or to prove the movement analysis.
"""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[2]
import sys
sys.path.insert(0, str(ROOT / 'scripts'))
from source_domains import read_domain, domain_sources



def example_occurrences(source):
    """Preserve duplicate surfaces so every published gloss can be checked."""
    return [(surface.strip(), gloss.strip(), translation.strip())
            for surface, gloss, translation in re.findall(
                r'\\gla\s+(.*?)//\s*\\glb\s+(.*?)//\s*\\glft\s+(.*?)//',
                source, re.S)]


def examples(source):
    return {surface: (gloss, translation)
            for surface, gloss, translation in example_occurrences(source)}


class FinitePlacementTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.simple = read_domain('chapters/06-simple-sentence.tex')
        cls.particles = read_domain('chapters/05-function-words.tex')
        cls.complex = read_domain('chapters/08-complex-sentences.tex')
        cls.nominals = read_domain('chapters/04-nouns.tex') + '\n' + (ROOT / 'chapters/11-negation.tex').read_text()
        cls.publication = '\n'.join(p.read_text() for p in sorted((ROOT / 'chapters').glob('*.tex')))

    def test_question_order_and_gloss_connectivity(self):
        inventory = examples(self.simple + '\n' + self.particles)
        for surface, gloss in [
                ('Marek jena mulša?', r'Marek.\Dir{} where live-\Cont{}'),
                ('Marek jena by mulša?', r'Marek.\Dir{} where \textsc{q} live-\Cont{}'),
                ('Jena Marek mulša?', r'where Marek.\Dir{} live-\Cont{}'),
                ('Jena Marek by mulša?', r'where Marek.\Dir{} \textsc{q} live-\Cont{}')]:
            with self.subTest(surface=surface):
                self.assertEqual(inventory[surface][0], gloss)
                self.assertIn('Where does Marek live?', inventory[surface][1])
        for obsolete in ('Jena by Marek mulša?', 'Oče tak tóm by Janku vy koupnik?',
                         'Jas Janek by vy ščének?'):
            self.assertNotIn(obsolete, inventory)
        self.assertIn('Janek by jas vy ščének?', inventory)
        self.assertIn('Tak tóm Janku oče by vy koupnik?', inventory)

    def test_every_repeated_purchase_question_preserves_case_gloss(self):
        surface = 'Tak tóm Janku oče by vy koupnik?'
        occurrences = [gloss for form, gloss, _ in example_occurrences(
            self.publication) if form == surface]
        self.assertGreaterEqual(len(occurrences), 1)
        for gloss in occurrences:
            with self.subTest(gloss=gloss):
                # Lexical labels (mirative/question versus MIR/Q) may differ;
                # the direct patient and transitive actor may not lose case.
                self.assertTrue(gloss.startswith(r'this book.\Dir{} Janek.\Trs{} '))
                self.assertTrue(gloss.endswith(r'already buy-\Trs{}-\Pf{}'))

    def test_wh_and_quantified_placement_are_not_necessarily_topics(self):
        self.assertIn('At most one marked wh-fronting dependency', self.simple)
        self.assertIn('without dedicated wh-fronting', self.simple)
        connectivity = self.simple.split(r'\label{sec:pivot-scope-connectivity}', 1)[1]
        connectivity = connectivity.split(r'\section', 1)[0]
        self.assertRegex(connectivity, r'ordinary placement does not turn it into\s+a referential topic')
        self.assertRegex(connectivity, r'Wh-variables are interpreted at their lower occurrences under Pol')
        self.assertRegex(connectivity, r'case is not recalculated from surface order')
        self.assertIn('no scope reversal or new binding relation', connectivity)
        self.assertIn('svem', connectivity)

    def test_local_domains_and_whole_selected_complement(self):
        inventory = examples(self.complex)
        self.assertEqual(inventory['Že pomadit by prítek?'][0],
                         r'\textsc{1sg}.\Ind{} talk.to-\Purp{} \textsc{q} come-\Pf{}')
        self.assertRegex(self.complex, r'matrix placement does not extract arbitrary embedded\s+arguments across the finite boundary')
        self.assertRegex(self.complex, r'without acquiring\s+the full finite placement field or additional Mood, Pol or stance projections')
        self.assertRegex(self.nominals, r'matrix clause does not license a negative indefinite inside a finite\s+complement')

    def test_recurrence_keeps_three_stages_and_persistence_contrast(self):
        # The declared profile must retain present truth, intervening falsity
        # and earlier truth, rather than reducing recurrence to ordinary vy.
        for condition in (r"\text{asserted content:}\quad & Q(r)",
                          r"\neg Q(r^{-})\ \wedge",
                          r"\exists r_0<r^{-}\,[Q(r_0)]"):
            self.assertIn(condition, self.particles)
        inventory = examples(self.particles)
        self.assertIn('again', inventory['Janek jas vy zdrávime.'][1])
        self.assertIn('still sleeping', inventory['Janek jas so zdrávime.'][1])
        self.assertIn('without interruption', self.particles)
        self.assertIn('waiting for a first arrival', self.particles)

    def test_predicate_types_keep_their_distinct_orders(self):
        inventory = examples(self.particles)
        self.assertIn('Pivo vy zada.', inventory)
        # Equative order remains explicit; replacement state examples are
        # English schemata until their Iridian lexemes are supplied.
        self.assertIn(r'\ird{Marek doktor vy staly}', self.particles)
        self.assertIn(r'\ird{Marek doktor so staly}', self.particles)
        self.assertIn(r'\trsl{The western gate is already open.}', self.particles)
        placement = self.simple.split(r'\label{sec:pivot-placement}', 1)[1]
        self.assertRegex(placement, r'Operator particles, predicate heads and material internal to\s+a nominal or selected clause are ineligible goals')


if __name__ == '__main__':
    unittest.main()

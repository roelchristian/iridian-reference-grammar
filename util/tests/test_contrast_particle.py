"""Independent source regressions for the discourse-reorienting particle."""
import importlib.util
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[2]
import sys
sys.path.insert(0, str(ROOT / 'scripts'))
from source_domains import read_domain, domain_sources

spec = importlib.util.spec_from_file_location('particle_checker', ROOT / 'scripts/check-grammar.py')
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


class ContrastParticleTests(unittest.TestCase):
    def test_active_sources_use_current_particle(self):
        # Archives are deliberately not input to the published grammar.
        for name, source in domain_sources(checker.active_sources(ROOT / 'grammar.tex')).items():
            with self.subTest(path=name):
                self.assertIsNone(re.search(r'\bjse\b', source, re.IGNORECASE))

    def test_isolated_and_combined_examples_keep_gloss_and_order(self):
        source = read_domain('chapters/05-function-words.tex')
        for phrase in ('Janek zdrava. Marek jas znóhtime.',
                       'Dá graže jas pjašta.',
                       'Marek zdrávime. Janek oh jas zdrávime.',
                       'Janek jas vy váržek.', 'Janek jas vy zaščének.',
                       'Čas jas so jeca.', 'Tak jas so staly.', 'Jas okouzé!'):
            with self.subTest(phrase=phrase):
                match = re.search(r'\\gla\s+' + re.escape(phrase) + r'//\s*\\glb\s+(.*?)//', source, re.S)
                self.assertIsNotNone(match)
                self.assertIn('contrast', match[1].split())
        for cluster in ('jas vy', 'jas so', 'by jas', 'By jas vy', 'By jas so'):
            self.assertIn(r'\ird{' + cluster + '}', source)

    def test_lexical_pronunciation_has_short_plain_vowel_and_sibilant(self):
        lexicon = (ROOT / 'util/lexicon.tex').read_text()
        self.assertIn(r'\lexentry{jas}{}{contrast particle, as for, meanwhile}', lexicon)
        source = read_domain('chapters/05-function-words.tex')
        self.assertIn(r'\ird{Jas} /jas/', source)


if __name__ == '__main__':
    unittest.main()

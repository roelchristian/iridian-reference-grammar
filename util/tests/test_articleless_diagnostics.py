"""Ordinary paradigms and historical evidence survive anchoring removal."""
import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'scripts'))
from articleless_diagnostics import (check_articleless, check_articleless_sources,
                                    check_historical_bodies, check_ordinary_paradigms, read_active_sources)


class ArticlelessDiagnosticsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fixtures = json.loads((ROOT / 'scripts/articleless-fixtures.json').read_text())
        cls.sources = read_active_sources()

    def test_active_publication_and_exact_historical_bodies(self):
        self.assertEqual(check_articleless(), [])
        self.assertEqual(len(self.fixtures['cells']), 102)
        self.assertEqual(len(self.fixtures['baseline_sources']), 5)

    def test_every_ordinary_cell_rejects_an_independent_quantity_mutation(self):
        # Exercise all 102 cells, including ordinary ráne and multi-variant
        # študent plurals, against pre-reform values rather than new snapshots.
        for cell in self.fixtures['cells']:
            path = cell['file']
            changed = self.sources.copy()
            changed[path] = changed[path].replace(cell['ordinary'], r'\ird{INVALID}')
            with self.subTest(file=path, noun=cell['noun'], case=cell['case'], number=cell['number']):
                self.assertNotEqual(changed[path], self.sources[path])
                self.assertTrue(check_ordinary_paradigms(changed, self.fixtures))

        # Internal lexical spaces are content, not table-layout whitespace.
        changed = self.sources.copy()
        path = 'util/paradigm-tables/nm-plural-paradigm.tex'
        changed[path] = changed[path].replace(r'\ird{byl}', r'\ird{by l}')
        self.assertTrue(check_ordinary_paradigms(changed, self.fixtures))

    def test_unglossed_retired_surfaces_and_projections_are_rejected(self):
        path = 'util/event-existential-comparison.tex'
        for added in (r'\ird{Nužo}', r'\ird{Bylo}', 'Markuto', r'\ird{Veňo}', r'\ird{pjáščikovat}',
                      r'\synhead{AnchP}', r'\synhead{Anch}', '[+anch,-shr]',
                      r'child.\Dir{}.\Def{}', 'sg.def', r'\ird{si}',
                      r'Anch\textsuperscript{0}', r'\(Anch^0\)', r'\(Anch^{0}\)',
                      r'[\pm\mathrm{anch}]', r'[\pm\mathrm{shr}]',
                      r'\glb child.DIR.DEF', r'\textsc{def}'):
            changed = self.sources.copy()
            changed[path] += '\n' + added + '\n'
            with self.subTest(added=added):
                self.assertTrue(check_articleless_sources(changed, self.fixtures))

    def test_ordinary_homophones_and_exact_phonological_si_are_allowed(self):
        changed = self.sources.copy()
        changed['util/event-existential-comparison.tex'] += r'\ird{ráne} \ird{pivo} \ird{stólek}'
        self.assertEqual(check_articleless_sources(changed, self.fixtures), [])
        # The rest of the chapter is still checked; exception is one exact
        # schematic contrast with no lexical assignment, not a file exclusion.
        changed['chapters/02-phonology.tex'] += r'\ird{si} \ird{byl}'
        self.assertTrue(check_articleless_sources(changed, self.fixtures))

    def test_maintained_diagnostics_are_checked_outside_the_tex_graph(self):
        path = 'clause-linking-diagnostics.md'
        self.assertIn(path, self.fixtures['maintained_diagnostics'])
        self.assertNotIn(path, self.sources)
        current = (ROOT / path).read_text(encoding='utf-8')
        self.assertIn('Marcí travě pjaštou', current)
        self.assertEqual(check_articleless(sources=self.sources), [])
        for added in ('Marcí travěte pjaštou', 'bread.IND.DEF', 'AnchP'):
            changed = self.sources.copy()
            changed[path] = current + '\n' + added + '\n'
            with self.subTest(added=added):
                failures = check_articleless(sources=changed)
                self.assertTrue(any(failure.startswith(path + ':') for failure in failures))

        allowed = self.sources.copy()
        allowed[path] = current + '\n`ráne` `pivo`\n'
        self.assertEqual(check_articleless(sources=allowed), [])
        self.assertNotIn(path, self.sources)
        historical = {name: (ROOT / name).read_text(encoding='utf-8')
                      for name in self.fixtures['historical_bodies']}
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            diagnostic = root / path
            diagnostic.write_text(current.replace('Marcí travě pjaštou',
                                                   'Marcí travěte pjaštou'),
                                  encoding='utf-8')
            failures = check_articleless(root=root, sources=self.sources,
                                         fixtures=self.fixtures,
                                         archive_overrides=historical)
            self.assertTrue(any(failure.startswith(path + ': retired anchored surfaces:')
                                for failure in failures))
            diagnostic.unlink()
            with self.assertRaises(FileNotFoundError) as missing:
                check_articleless(root=Path(directory), sources=self.sources,
                                  fixtures=self.fixtures, archive_overrides=historical)
            self.assertEqual(missing.exception.filename, str(diagnostic))

    def test_include_graph_follows_new_literal_utility_inputs(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'util').mkdir()
            (root / 'grammar.tex').write_text(r'\input{util/outer}')
            (root / 'util/outer.tex').write_text(r'\% visible \input{util/inner.tex}' + '\n'
                                                    + r'\\% \input{missing-ignored-comment}')
            (root / 'util/inner.tex').write_text(r'\ird{Bylo}')
            sources = read_active_sources(root)
            self.assertIn('util/inner.tex', sources)
            self.assertTrue(any('util/inner.tex: retired anchored surfaces' in failure
                                for failure in check_articleless_sources(sources, self.fixtures)))

    def test_historical_body_changes_and_missing_status_are_rejected(self):
        for path in self.fixtures['historical_bodies']:
            original = (ROOT / path).read_text()
            with self.subTest(path=path):
                self.assertTrue(check_historical_bodies(ROOT, self.fixtures,
                                {path: original + '\nChanged historical evidence.\n'}))
                self.assertTrue(check_historical_bodies(ROOT, self.fixtures,
                                {path: original.split('\n\n', 1)[1]}))

    def test_derived_cells_and_unattested_gaps_cannot_be_completed_by_inference(self):
        path = 'chapters/08-derivation-nominalisation.tex'
        for before, after in [(r'\ird{pjáščikovy}', r'\ird{pjáščikový}'),
                              ('only direct singular', 'all singular and plural forms'),
                              (r'\ird{pjaštova}', r'\ird{pjaštovat}')]:
            changed = self.sources.copy()
            changed[path] = changed[path].replace(before, after)
            with self.subTest(before=before):
                self.assertNotEqual(changed[path], self.sources[path])
                self.assertTrue(check_articleless_sources(changed, self.fixtures))


if __name__ == '__main__':
    unittest.main()

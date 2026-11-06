"""Orthographic h preserves /x/ without rewriting other-language evidence."""
import importlib.util
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location('dorsal_checker', ROOT / 'scripts/check-grammar.py')
checker = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(checker)


class DorsalOrthographyTests(unittest.TestCase):
    def check_spelling(self, text):
        return checker.dorsal_spelling_checks({'example.tex': text})

    def test_final_internal_capitalised_and_letter_forms_are_rejected(self):
        for text in (r'\ird{bych}', r'\ird{chrás}', r'\ird{Chrás}',
                     r'\ird{CH}', r'\orth{ch}', r'\gla Nách domach.//',
                     r'\lexentry{och}{also}{particle}',
                     r'\phon{nách}{naːx}{each}'):
            with self.subTest(text=text):
                self.assertTrue(self.check_spelling(text))

    def test_h_forms_retain_x_and_fronted_ipa(self):
        self.assertEqual(self.check_spelling(
            r'\phon{náh}{naːx}{each} \phon{hěř}{çɛʃ}{brow} '
            r'\ird{Hrás} \ird{byh} \ird{domah} \orth{h}'), [])

    def test_english_tex_references_ipa_and_foreign_data_are_outside_scope(self):
        self.assertEqual(self.check_spelling(
            r'\chapter{A chapter on Czech} \label{ch:phon} '
            r'\cite{schachterotanes1972} \href{https://example.com/check}{Schachter} '
            r'\textit{Czech ch} /x/ [x] % \ird{ch}' + '\n'
            r'\ird{náh} \gla Veň \textnormal{[[watch]]}\textsubscript{\Cont{}}.//'), [])

    def test_nested_form_macros_are_checked_without_counting_tex_commands(self):
        self.assertTrue(self.check_spelling(r'\lexentry{náh}{each}{cf.\ \ird{nách}}'))
        self.assertEqual(self.check_spelling(r'\ird{\textsc{h}}'), [])

    def test_foreign_interlinear_labels_do_not_exempt_iridian_forms(self):
        foreign = (r'\begingl\glpreamble \textit{Korean}//'
                   r'\gla chayk-ul ilk-ess-ta.//\endgl')
        self.assertEqual(self.check_spelling(foreign), [])
        self.assertTrue(self.check_spelling(foreign + r'\gla och.//'))
        self.assertTrue(self.check_spelling(foreign + r'\ird{och}'))
        self.assertTrue(self.check_spelling(
            r'\begingl\glpreamble \textit{Iridian}//\gla och.//\endgl'))

    def test_schematic_feature_annotations_are_not_surface_spelling(self):
        annotation = r'\textsubscript{\textsc{state.inch}.\Prog{}}'
        self.assertEqual(self.check_spelling(r'\gla [[wide]]' + annotation + r'.//'), [])
        self.assertTrue(self.check_spelling(r'\gla nách' + annotation + r'.//'))


if __name__ == '__main__':
    unittest.main()

"""Regressions for canonical sibilants and boundary-sensitive grade outputs."""
import importlib.util
import json
from pathlib import Path
import unittest

SPEC = importlib.util.spec_from_file_location(
    'check_grammar', Path(__file__).resolve().parents[2] / 'scripts/check-grammar.py')
checker = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(checker)


class SibilantMergerChecks(unittest.TestCase):
    def check_spelling(self, text):
        return checker.sibilant_spelling_checks({'chapter.tex': text})

    def test_rejects_retired_sibilants_in_each_active_data_format(self):
        for text in (r'\ird{lesě}', r'\irdp{strazě}{indirect}',
                     r'\phon{sěbec}{ʃɛbɛts}{soil}',
                     r'\lexentry{cěna}{}{example}',
                     r'\gla Byl lesě.//'):
            with self.subTest(text=text):
                self.assertTrue(any('superseded sibilant spelling' in error
                                    for error in self.check_spelling(text)))

    def test_checks_nested_lexicon_notes_and_multiple_occurrences(self):
        text = r'\lexentry{les}{\Ind{} \ird{lesě}}{forest} \ird{leše}'
        self.assertTrue(self.check_spelling(text))

    def test_preserves_other_e_hook_and_explicit_rejected_spellings(self):
        text = (r'\ird{pě} \ird{bě} \ird{mě} \ird{vě} \ird{kěda} '
                r'\ird{hě} \ird{tězeň} \ird{travě} '
                r'\ird{*sěbec} \ird{*čě} % \ird{sěbec}')
        self.assertEqual(self.check_spelling(text), [])

    def test_rejects_old_silent_i_sibilant_examples_but_keeps_high_i(self):
        for form in ('siarc', 'zia', 'ziou', 'ciu'):
            with self.subTest(form=form):
                self.assertTrue(self.check_spelling(r'\ird{' + form + '}'))
        self.assertEqual(self.check_spelling(
            r'\ird{si} \ird{zi} \ird{ci} \ird{Marcí} \ird{lubcí} '
            r'\ird{šarc} \ird{ža} \ird{žou} \ird{ču}'), [])

    def test_rejects_old_ipa_even_if_spelling_has_been_updated(self):
        for text in (r'\phon{šarc}{ˈɕarts}{door}',
                     r'\ird{či} \ipagloss{[tɕɪ]}',
                     r'\ird{ža} [ʑa]',
                     r'\ird{ža} & [ʑa] & bell',
                     r'\phon{ci}{tsɪ}{sequence} \phon{ci}{tɕɪ}{sequence}'):
            with self.subTest(text=text):
                self.assertTrue(any('alveolopalatal' in error
                                    for error in self.check_spelling(text)))

    def test_silent_i_is_limited_to_documented_labials(self):
        for form, expected in (('piaštnik', 2), ('piaštou', 2), ('bia', 1),
                               ('mia', 1), ('via', 1), ('šarc', 1),
                               ('siarc', 2), ('zia', 2), ('ciu', 2),
                               ('kia', 2), ('gia', 2), ('hia', 2), ('fia', 2),
                               ('kěda', 2), ('Marcí', 2), ('lúbcí', 2)):
            with self.subTest(form=form):
                self.assertEqual(checker.spelling_nuclei(form), expected)

    def test_independent_fixtures_preserve_ce_che_and_high_front_contrast(self):
        fixtures = json.loads((checker.ROOT / 'scripts/palatalisation-fixtures.json')
                              .read_text(encoding='utf-8'))
        selected = [item for item in fixtures['pronunciations']
                    if item['form'] in {'ce', 'če', 'si', 'ši', 'ci', 'či', 'Marcí', 'lúbcí'}]
        self.assertEqual(len(selected), 8)
        focused = {'derivations': [], 'classes': [], 'pronunciations': selected}
        source = '\n'.join(r'\phon{' + item['form'] + '}{' + item['ipa'] + '}{sequence}'
                           for item in selected)
        self.assertEqual(checker.check_palatalisation(source, focused), [])
        for original, revised in (('tsɛ', 'tʃɛ'), ('sɪ', 'ʃɪ'),
                                  ('mar.tsiː', 'mar.tʃiː'), ('luːp.tsiː', 'luːp.tʃiː')):
            with self.subTest(revised=revised):
                self.assertTrue(checker.check_palatalisation(source.replace(original, revised), focused))

    def test_fricative_derivations_preserve_mutation_and_quantity_together(self):
        fixtures = json.loads((checker.ROOT / 'scripts/palatalisation-fixtures.json')
                              .read_text(encoding='utf-8'))
        derivations = [item for item in fixtures['derivations']
                       if item['forms'][0] in {'les', 'stráz'}]
        self.assertEqual(len(derivations), 2)
        focused = {'derivations': derivations, 'classes': [], 'pronunciations': []}
        source = (r'\subsection{PAL}\label{sec:front-softening}\pex '
                  r'\a \ird{les} + \ird{-ě} $\rightarrow$ \ird{leše} '
                  r'\a \ird{stráz} + \ird{-ě} $\rightarrow$ \ird{straže}\xe')
        self.assertEqual(checker.check_palatalisation(source, focused), [])
        for original, revised in (('leše', 'lese'), ('straže', 'straze'),
                                  ('straže', 'stráže')):
            with self.subTest(revised=revised):
                self.assertTrue(checker.check_palatalisation(
                    source.replace(original, revised), focused))

    def test_derivation_fixtures_reject_feeding_and_wrong_underlying_c_output(self):
        fixtures = json.loads((checker.ROOT / 'scripts/palatalisation-fixtures.json')
                              .read_text(encoding='utf-8'))
        derivations = [item for item in fixtures['derivations']
                       if item['forms'] in (['ruk', '-ě', 'ruce'], ['rac', '-e', 'rače'])]
        self.assertEqual(len(derivations), 2)
        focused = {'derivations': derivations, 'classes': [], 'pronunciations': []}
        source = (r'\subsection{PAL}\label{sec:front-softening}\pex '
                  r'\a \ird{rac} + \ird{-e} $\rightarrow$ \ird{rače}\xe '
                  r'\subsection{Interactions}\label{sec:morphophon-interactions}\pex '
                  r'\a \ird{ruk} + \ird{-ě} $\rightarrow$ \ird{ruce}\xe')
        self.assertEqual(checker.check_palatalisation(source, focused), [])
        for original, revised in (('ruce', 'ruče'), ('rače', 'race')):
            with self.subTest(revised=revised):
                self.assertTrue(checker.check_palatalisation(source.replace(original, revised), focused))
        # A correct output elsewhere cannot rescue the wrong derivation row.
        mutated = source.replace('ruce', 'ruče') + r'\ird{ruce}'
        self.assertTrue(checker.check_palatalisation(mutated, focused))
        duplicate = source.replace(r'\xe',
                                   r'\a \ird{ruk} + \ird{-ě} $\rightarrow$ \ird{ruče}\xe')
        self.assertTrue(checker.check_palatalisation(duplicate, focused))


if __name__ == '__main__':
    unittest.main()

"""Regressions for lexical /kʲ/ versus /c/ and productive velar grades."""
import importlib.util
import json
from pathlib import Path
import unittest

SPEC = importlib.util.spec_from_file_location(
    'check_grammar', Path(__file__).resolve().parents[2] / 'scripts/check-grammar.py')
checker = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(checker)


def sources():
    return {'chapters/02-phonology.tex': r'''
\phon{kěda}{ˈkʲɛ.da}{jail}
\ird{kěda} & \ipagloss{[ˈkʲɛ.da]} & jail
\phon{ťeda}{ˈcɛ.da}{cork}
\label{tab:velar-fronting}
Front & /k/ $\rightarrow$ /ts/ & front grade \\
Restricted velar-front & /k/ $\rightarrow$ /ts/ & restricted grade \\
Yod & /k/ $\rightarrow$ /tʃ/ & yod grade \\
\end{table}
''', 'chapters/03-verbs.tex': r'''
\phon{kánek}{ˈkaː.nɛk}{sang}
\phon{kánnik}{ˈkaːn.nɪk}{sang it}
\phon{kanžek}{ˈkan.ʒɛk}{was singing}
''', 'util/lexicon.tex': r'''
\lexentry{kěda}{lexical /kʲ/; \ipagloss{[ˈkʲɛ.da]}}{jail}
\lexentry{kan-}{lexical initial /k/}{sing, perform}
\lexentry{ťeda}{lexical /c/; \ipagloss{[ˈcɛ.da]}}{cork}
'''}


class LexicalVelarTests(unittest.TestCase):
    def test_shared_pronunciation_fixtures_align_with_option_a(self):
        fixtures = json.loads((checker.ROOT / 'scripts/palatalisation-fixtures.json').read_text(encoding='utf-8'))
        selected = [item for item in fixtures['pronunciations'] if item['form'] in {'kěda', 'ťeda'}]
        self.assertEqual({item['form'] for item in selected}, {'kěda', 'ťeda'})
        focused = {'derivations': [], 'classes': [], 'pronunciations': selected}
        phonology = sources()['chapters/02-phonology.tex']
        self.assertEqual(checker.check_palatalisation(phonology, focused), [])
        for item in selected:
            if item['form'] == 'kěda':
                item['ipa'] = 'ˈcɛ.da'
        self.assertTrue(any('kěda' in error for error in checker.check_palatalisation(phonology, focused)))

    def test_distinct_lexical_and_productive_outputs(self):
        self.assertEqual(checker.lexical_velar_checks(sources()), [])

    def test_rejects_lexical_merger_in_each_example_not_only_first(self):
        data = sources()
        data['chapters/02-phonology.tex'] = data['chapters/02-phonology.tex'].replace(
            r'\ipagloss{[ˈkʲɛ.da]}', r'\ipagloss{[ˈcɛ.da]}')
        self.assertTrue(any('kěda' in error for error in checker.lexical_velar_checks(data)))

    def test_keeps_lexical_palatal_stop(self):
        data = sources()
        data['chapters/02-phonology.tex'] = data['chapters/02-phonology.tex'].replace('ˈcɛ.da', 'ˈkʲɛ.da')
        self.assertTrue(any('ťeda' in error for error in checker.lexical_velar_checks(data)))

    def test_rejects_merger_in_lexicon_metadata(self):
        data = sources()
        data['util/lexicon.tex'] = data['util/lexicon.tex'].replace('[ˈkʲɛ.da]', '[ˈcɛ.da]')
        self.assertTrue(any('util/lexicon.tex' in error for error in checker.lexical_velar_checks(data)))

    def test_rejects_incorrect_phonemic_metadata_even_with_correct_ipa(self):
        for before, after in ((r'\lexentry{kěda}{lexical /kʲ/', r'\lexentry{kěda}{lexical /c/'),
                              (r'\lexentry{kan-}{lexical initial /k/', r'\lexentry{kan-}{lexical initial /c/'),
                              (r'\lexentry{ťeda}{lexical /c/', r'\lexentry{ťeda}{lexical /kʲ/')):
            with self.subTest(entry=before):
                data = sources()
                data['util/lexicon.tex'] = data['util/lexicon.tex'].replace(before, after)
                self.assertTrue(any('lexical metadata' in error for error in checker.lexical_velar_checks(data)))

    def test_rejects_wrong_stem_pronunciation_stress_quantity_or_coda(self):
        for replacement in ('ˈcaː.nɛk', 'kaːˈnɛk', 'ˈka.nɛk'):
            with self.subTest(replacement=replacement):
                data = sources()
                data['chapters/03-verbs.tex'] = data['chapters/03-verbs.tex'].replace('ˈkaː.nɛk', replacement)
                self.assertTrue(checker.lexical_velar_checks(data))
        data = sources()
        data['chapters/03-verbs.tex'] = data['chapters/03-verbs.tex'].replace('ˈkaːn.nɪk', 'ˈkaː.nɪk')
        self.assertTrue(checker.lexical_velar_checks(data))

    def test_missing_fixture_is_not_a_pass(self):
        data = sources()
        del data['chapters/03-verbs.tex']
        self.assertTrue(any('missing lexical pronunciation fixture' in error
                            for error in checker.lexical_velar_checks(data)))

    def test_rejects_productive_output_changes(self):
        for grade, before, after in (('Front', 'ts', 'kʲ'),
                                     ('Restricted velar-front', 'ts', 'c'), ('Yod', 'tʃ', 'c')):
            with self.subTest(grade=grade):
                data = sources()
                old = grade + r' & /k/ $\rightarrow$ /' + before + '/'
                new = grade + r' & /k/ $\rightarrow$ /' + after + '/'
                data['chapters/02-phonology.tex'] = data['chapters/02-phonology.tex'].replace(old, new)
                self.assertTrue(any('productive' in error for error in checker.lexical_velar_checks(data)))


if __name__ == '__main__':
    unittest.main()

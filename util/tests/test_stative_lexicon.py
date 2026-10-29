"""Independent ordinary-ATTR, lexical selection and manifestation checks."""
import copy
import json
from pathlib import Path
import sys
import unittest

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'scripts'))
from stative_lexicon import (LexicalLicenceError,load_lexicon,derive,finite,
    ordinary_attributive,manner,participant,evidential,causative,
    stimulus_applicative,perspective_licensed,manifestation_holds,check_lexical_extension_sources)
from boundary_transducer import BoundaryLicence,BoundaryState,BoundaryTransducer
from quantity_grades import QuantityGrades,QuantityLicence

# Explicit spelling-to-token aid for expected selections only. The helper is
# not a phonetic renderer and makes no claim about stress or syllabification.
SPELL=dict(zip('abdehiklmnoprstuvyz',
 ('a','b','d','ɛ','x','ɪ','k','l','m','n','ɔ','p','r','s','t','ʊ','v','ɨ','z')))
SPELL.update({'á':'aː','é':'eː','í':'iː','ó':'oː','ú':'uː','ý':'ɨː',
 'š':'ʃ','ž':'ʒ','č':'tʃ','c':'ts','ň':'ɲ','ľ':'ʎ'})
def tokens(form):
    return tuple(SPELL[c] for c in form)


class StativeLexiconTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=load_lexicon()
        cls.entries={entry['stem']:entry for entry in cls.data['entries']}
        cls.aspects=('continuous','progressive','perfective','retrospective','contemplative')

    def test_eleven_records_separate_meaning_from_morphological_class(self):
        self.assertEqual(set(self.entries),{'mužn','hradn','svorn','četn','ptakn',
            'smrn','všihn','žbirn','hvodn','trpan','tvírzn'})
        self.assertEqual(self.entries['tvírzn']['finite_class'],'C')
        self.assertEqual(self.entries['všihn']['manifest_class'],'ESH-A')
        self.assertIsNone(self.entries['ptakn']['manifest_class'])
        self.assertEqual(self.entries['žbirn']['attributive_class'],'III')
        self.assertIsNone(self.entries['hvodn']['attributive_class'])

    def test_ninety_independent_validated_state_and_become_cells(self):
        count=0
        for entry in self.entries.values():
            if entry['principal_part_status']!='listed':
                continue
            for kind in ('state','become'):
                for aspect,expected in zip(self.aspects,entry['expected'][kind]):
                    with self.subTest(stem=entry['stem'],kind=kind,aspect=aspect):
                        self.assertEqual(finite(entry,kind,aspect,stage_level=True,bounded=True),
                                         tokens(expected))
                        count+=1
        self.assertEqual(count,90)

    def test_el_strength_requires_a_lexical_class_not_short_root(self):
        entry=copy.deepcopy(self.entries['mužn'])
        entry['become_class']=None
        with self.assertRaises(LexicalLicenceError):
            derive(entry,'become')
        # This conditional input checks the selector's dependence on its class,
        # not the existence of a new short-base EL-P lexeme in the grammar.
        entry['become_class']='EL-P'
        self.assertEqual(derive(entry,'become')[0],tokens('mužnel'))
        self.assertNotEqual(derive(entry,'become')[0],tokens('mužnél'))
        self.assertEqual(derive(self.entries['tvírzn'],'become')[0],tokens('tvírznel'))

    def test_all_listed_records_preserve_ordinary_derived_operations(self):
        for entry in self.entries.values():
            if entry['principal_part_status']!='listed':
                continue
            expected=entry['expected']['operations']
            for offset,kind in ((0,'state'),(3,'become')):
                with self.subTest(stem=entry['stem'],kind=kind):
                    self.assertEqual(evidential(entry,kind,'continuous'),tokens(expected[offset]))
                    self.assertEqual(participant(entry,kind,'continuous'),tokens(expected[offset+1]))
                    self.assertEqual(causative(entry,kind,'progressive',causable=True),tokens(expected[offset+2]))
            self.assertEqual(manner(entry),tokens(entry['expected']['manner']))

    def test_state_aspect_still_requires_the_explicit_contexts(self):
        entry=self.entries['mužn']
        for aspect in ('progressive','perfective'):
            with self.assertRaises(ValueError):
                finite(entry,'state',aspect)
        self.assertEqual(entry['aspect_licences']['retrospective'],
                         'anterior-no-cessation-entailment')
        self.assertEqual(entry['aspect_licences']['contemplative'],
                         'projection-not-noninitiation')

    def test_soft_attribute_uses_only_its_own_front_boundary(self):
        for stem,attribute,adverb in [('všihn','všihňa','všihňe'),
                                      ('žbirn','žbirňa','žbirňe')]:
            with self.subTest(stem=stem):
                entry=self.entries[stem]
                self.assertEqual(ordinary_attributive(entry),tokens(attribute))
                self.assertEqual(manner(entry),tokens(adverb))
                self.assertNotEqual(ordinary_attributive(entry),tokens(adverb))
                self.assertEqual(ordinary_attributive(entry)[:-2],tuple(entry['segments'])[:-1])
        self.assertEqual(ordinary_attributive(self.entries['mužn']),tokens('múžna'))
        self.assertEqual(ordinary_attributive(self.entries['hradn']),tokens('hradná'))
        self.assertEqual(ordinary_attributive(self.entries['tvírzn']),tokens('tvírzná'))

    def test_attribute_class_does_not_follow_condition_semantics(self):
        for stem in ('ptakn','hvodn'):
            with self.subTest(stem=stem),self.assertRaises(LexicalLicenceError):
                ordinary_attributive(self.entries[stem])
        for entry in self.entries.values():
            self.assertNotIn('definiteness',entry)
            self.assertNotIn('agreement',entry)
            self.assertNotIn('temporal_anchoring',entry)

    def test_manifest_five_literal_cells_preserve_own_local_nucleus(self):
        entry=self.entries['všihn']
        for aspect,expected in zip(self.aspects,self.data['manifest']['forms']):
            self.assertEqual(finite(entry,'manifest',aspect),tokens(expected))
        self.assertEqual(finite(entry,'manifest','progressive'),tokens('všihnéšime'))
        self.assertNotEqual(finite(entry,'manifest','progressive'),tokens('všíhnešime'))
        self.assertNotEqual(finite(entry,'manifest','perfective'),tokens('všihnéšik'))
        self.assertEqual(derive(entry,'manifest')[0],tokens('všihneš'))

    def test_manifest_is_enumerated_not_automatic_experiential_derivation(self):
        for stem,entry in self.entries.items():
            if stem=='všihn':
                continue
            with self.subTest(stem=stem),self.assertRaises(LexicalLicenceError):
                derive(entry,'manifest')
        with self.assertRaises(LexicalLicenceError):
            derive(self.entries['všihn'],'become-manifest')
        with self.assertRaises(LexicalLicenceError):
            stimulus_applicative(self.entries['všihn'],'continuous',
                                  stimulus_present=True,kind='manifest')

    def test_manifest_display_does_not_entail_genuine_feeling(self):
        self.assertTrue(manifestation_holds(True,False))
        self.assertTrue(manifestation_holds(True,True))
        self.assertFalse(manifestation_holds(False,True))
        with self.assertRaises(LexicalLicenceError):
            manifestation_holds('yes',False)

    def test_manifest_nominal_and_evidential_are_distinct_from_manifest_head(self):
        entry=self.entries['všihn']
        for aspect,nominal,evid in zip(self.aspects,self.data['manifest']['participant'],
                                       self.data['manifest']['evidential']):
            # ou has one diphthongal nucleus in segment tokens.
            out=participant(entry,'manifest',aspect)
            self.assertEqual(out, self._nominal_tokens(nominal))
            self.assertEqual(evidential(entry,'manifest',aspect),tokens(evid))
        linked=BoundaryTransducer.from_file().apply(
            BoundaryState(tokens('všihnéšik')),
            BoundaryLicence('direct-PF-linker','front',True,True),('ɛ',))
        self.assertEqual(linked.segments,tokens('všihnéšice'))
        self.assertNotEqual(tokens('všihnešal'),tokens('všihnal'))

    @staticmethod
    def _nominal_tokens(form):
        if form.endswith('ou'):
            return tokens(form[:-2])+('ou̯',)
        return tokens(form)

    def test_causative_preserves_lexical_and_derivational_locality(self):
        for aspect,expected in zip(self.aspects,self.data['manifest']['causative']):
            self.assertEqual(causative(self.entries['všihn'],'manifest',aspect,causable=True),
                             tokens(expected))
        self.assertEqual(causative(self.entries['tvírzn'],'become','progressive',causable=True),
                         tokens('tvírznelrime'))
        with self.assertRaises(LexicalLicenceError):
            causative(self.entries['všihn'],'manifest','progressive')

    def test_stimulus_requires_its_frame_and_never_establishes_actual_cause(self):
        self.assertEqual(stimulus_applicative(self.entries['všihn'],'perfective',
                         stimulus_present=True),tokens('všihnébik'))
        with self.assertRaises(LexicalLicenceError):
            stimulus_applicative(self.entries['všihn'],'perfective')
        for stem in ('mužn','ptakn','žbirn'):
            with self.subTest(stem=stem),self.assertRaises(LexicalLicenceError):
                stimulus_applicative(self.entries[stem],'continuous',stimulus_present=True)
        self.assertEqual(self.entries['všihn']['argument_frame'],'experiencer-only')
        self.assertEqual(self.entries['všihn']['stimulus'],'applicative-eb')

    def test_anchoring_is_not_person_or_an_automatic_evidential_suffix(self):
        entry=self.entries['všihn']
        self.assertTrue(perspective_licensed(entry,experiencer='speaker'))
        self.assertFalse(perspective_licensed(entry,experiencer='Marek'))
        self.assertFalse(perspective_licensed(entry,experiencer='Marek',anchor='Marek'))
        self.assertTrue(perspective_licensed(entry,experiencer='Marek',anchor='Marek',
                                             shifted=True,clause_type='report'))
        self.assertTrue(perspective_licensed(entry,experiencer='Marek',evidence=True))
        for clause in ('question','report','narrative','embedded'):
            self.assertFalse(perspective_licensed(entry,experiencer='Marek',clause_type=clause))
            self.assertFalse(perspective_licensed(entry,experiencer='Marek',clause_type=clause,
                                                   shifted=True))
            self.assertTrue(perspective_licensed(entry,experiencer='Marek',anchor='Marek',
                                                  clause_type=clause,shifted=True))
            self.assertFalse(perspective_licensed(entry,experiencer='Marek',anchor='Janek',
                                                   clause_type=clause,shifted=True))
        self.assertFalse(perspective_licensed(entry,experiencer='Marek',shifted=True))
        self.assertTrue(perspective_licensed(self.entries['žbirn'],experiencer='Marek'))
        self.assertTrue(perspective_licensed(entry,experiencer='Marek',kind='manifest'))
        self.assertFalse(perspective_licensed(entry,experiencer='Marek',internal_reading=False))
        self.assertFalse(perspective_licensed(self.entries['ptakn'],experiencer='Marek'))
        self.assertTrue(perspective_licensed(self.entries['ptakn'],experiencer='Marek',internal_reading=False))
        with self.assertRaises(LexicalLicenceError):
            perspective_licensed(self.entries['ptakn'],experiencer='Marek',kind='manifest')

    def test_missing_vocalism_and_cluster_licence_do_not_generate_repairs(self):
        self.assertIsNone(self.entries['smrn']['quantity_target'])
        for stem in ('smrn','trpan'):
            entry=self.entries[stem]
            for kind in ('state','become','manifest'):
                with self.subTest(stem=stem,kind=kind),self.assertRaises(LexicalLicenceError):
                    finite(entry,kind,'continuous')
            with self.assertRaises(LexicalLicenceError):
                manner(entry)
        self.assertEqual(self.entries['trpan']['quantity_target'],3)
        self.assertEqual(self.data['excluded_candidates'],['trpá','smerňa'])
        # The recorded a target permits a conditional grade calculation only;
        # it does not establish a legal /trp/ onset or a new finite principal part.
        selected=QuantityGrades.from_file().apply(tokens('trpan'),
            QuantityLicence('conditional-trpan','G1',True,(0,5),(3,),3))
        self.assertEqual(selected,tokens('trpán'))

    def test_new_source_prescriptions_are_bound_and_mutations_rejected(self):
        source=(ROOT/'chapters/03-verbs.tex').read_text()
        sources={'chapters/03-verbs.tex':source}
        self.assertEqual(check_lexical_extension_sources(sources,self.data),[])
        marker=r'\label{tab:stative-manifest}'
        prefix,tail=source.split(marker,1)
        broken={'chapters/03-verbs.tex':prefix+marker+tail.replace('všihnéšek','všíhnešek',1)}
        self.assertTrue(check_lexical_extension_sources(broken,self.data))
        broken={'chapters/03-verbs.tex':source.replace(r'\phon{všihňa}',r'\phon{všihná}')}
        self.assertTrue(check_lexical_extension_sources(broken,self.data))

if __name__=='__main__':
    unittest.main()

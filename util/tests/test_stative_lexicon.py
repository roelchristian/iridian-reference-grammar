"""Independent ordinary-ATTR, lexical selection and manifestation checks."""
import copy
import json
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

ROOT=Path(__file__).resolve().parents[2]
import sys
sys.path.insert(0, str(ROOT / 'scripts'))
from source_domains import read_domain, domain_sources
from stative_diagnostics import ASPECTS, STATE_ASPECTS

sys.path.insert(0,str(ROOT/'scripts'))
from stative_lexicon import (LexicalLicenceError,load_lexicon,derive,finite,
    ordinary_attributive,manner,participant,evidential,causative,
    stimulus_applicative,manifestation_holds,check_lexical_extension_sources)
from boundary_transducer import BoundaryLicence,BoundaryState,BoundaryTransducer
from quantity_grades import QuantityGrades,QuantityLicence

# Explicit spelling-to-token aid for expected selections only. The helper is
# not a phonetic renderer and makes no claim about stress or syllabification.
SPELL=dict(zip('abdehiklmnoprstuvyz',
 ('a','b','d','ɛ','x','ɪ','k','l','m','n','ɔ','p','r','s','t','ʊ','v','ɨ','z')))
SPELL.update({'á':'aː','é':'eː','í':'iː','ó':'oː','ú':'uː','ė':'ə',
 'š':'ʃ','ž':'ʒ','č':'tʃ','c':'ts','ň':'ɲ','ľ':'ʎ','ř':'ʒ','j':'j'})
def tokens(form):
    # A narrow expected-form decoder; morphology is asserted independently.
    segments = []
    soft = {'t': 'c', 'd': 'ɟ', 'n': 'ɲ', 'l': 'ʎ'}
    for index, char in enumerate(form):
        if char == 'ě':
            segments.append('ɛ')
        elif char in soft and form[index + 1:index + 2] == 'ě':
            segments.append(soft[char])
        else:
            segments.append(SPELL[char])
    return tuple(segments)


class StativeLexiconTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=load_lexicon()
        cls.entries={entry['stem']:entry for entry in cls.data['entries']}
        cls.aspects=ASPECTS

    def test_eleven_records_separate_meaning_from_morphological_class(self):
        self.assertEqual(set(self.entries),{'mužn','hradn','svorn','četn','řejn',
            'sledn','všihn','žbirn','hvodn','torban','tvírzn'})
        self.assertEqual(self.entries['tvírzn']['finite_class'],'C')
        self.assertEqual(self.entries['všihn']['manifest_class'],'ESH-A')
        self.assertIsNone(self.entries['řejn']['manifest_class'])
        self.assertEqual(self.entries['žbirn']['attributive_class'],'III')
        self.assertIsNone(self.entries['hvodn']['attributive_class'])

    def test_independent_restricted_state_and_full_become_cells(self):
        count=0
        for entry in self.entries.values():
            if entry['principal_part_status']!='listed':
                continue
            for kind,aspects in (('state',STATE_ASPECTS),('become',ASPECTS)):
                for aspect,expected in zip(aspects,entry['expected'][kind]):
                    with self.subTest(stem=entry['stem'],kind=kind,aspect=aspect):
                        self.assertEqual(finite(entry,kind,aspect),
                                         tokens(expected))
                        count+=1
        listed=sum(entry['principal_part_status']=='listed' for entry in self.entries.values())
        self.assertEqual(count,listed*(len(STATE_ASPECTS)+len(ASPECTS)))

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

    def test_state_aspect_restriction_survives_context_and_embedding_operations(self):
        for entry in self.entries.values():
            if entry['principal_part_status']!='listed':
                continue
            for aspect in ('progressive','perfective'):
                for operation in (finite,participant,evidential):
                    for flags in ({}, {'stage_level':True}, {'bounded':True},
                                  {'stage_level':True,'bounded':True}):
                        with self.subTest(stem=entry['stem'],aspect=aspect,
                                          operation=operation.__name__,flags=flags), self.assertRaises(LexicalLicenceError):
                            operation(entry,'state',aspect,**flags)

    def test_state_anteriority_and_projection_are_distinct_from_becoming(self):
        entry=self.entries['mužn']
        self.assertEqual(finite(entry,'state','retrospective'),tokens('mužnáv'))
        self.assertEqual(finite(entry,'state','contemplative'),tokens('mužnáž'))
        self.assertEqual(finite(entry,'become','retrospective'),tokens('mužnélav'))
        self.assertEqual(finite(entry,'become','contemplative'),tokens('mužnélaž'))
        self.assertEqual(entry['aspect_licences']['retrospective'],
                         'anterior-no-cessation-entailment')
        self.assertEqual(entry['aspect_licences']['contemplative'],
                         'projection-not-noninitiation')

    def test_lexical_inventory_omits_unavailable_state_principal_parts(self):
        for entry in self.entries.values():
            self.assertEqual(set(entry['aspect_licences']),set(STATE_ASPECTS))
            self.assertEqual(len(entry['expected']['state']),len(STATE_ASPECTS))
            self.assertEqual(len(entry['expected']['become']),len(ASPECTS))

    def test_loader_rejects_reintroduced_state_aspect_and_mismatched_inventory(self):
        for change in ('aspect','principal-parts'):
            data=copy.deepcopy(self.data)
            entry=data['entries'][0]
            if change=='aspect':
                entry['aspect_licences']['perfective']='bounded-state'
            else:
                entry['expected']['state'].append('múžnik')
            with self.subTest(change=change), patch('stative_lexicon.Path.read_text',
                    return_value=json.dumps(data)), self.assertRaises(LexicalLicenceError):
                load_lexicon()

    def test_dynamic_derivatives_keep_eventive_aspects(self):
        entry=self.entries['mužn']
        self.assertEqual(finite(entry,'become','progressive'),tokens('mužnélime'))
        self.assertEqual(finite(entry,'become','perfective'),tokens('mužnélek'))
        self.assertEqual(causative(entry,'state','progressive',causable=True),
                         tokens('mužnérime'))
        self.assertEqual(causative(entry,'state','perfective',causable=True),
                         tokens('mužnéranik'))

    def test_soft_attribute_uses_only_its_own_front_boundary(self):
        for stem,attribute,adverb in [('všihn','všihňa','všihně'),
                                      ('žbirn','žbirňa','žbirně')]:
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
        for stem in ('řejn','hvodn'):
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
        for aspect,form in (('continuous','všihnéba'),
                            ('retrospective','všihnébav'),
                            ('contemplative','všihnébaž')):
            self.assertEqual(stimulus_applicative(self.entries['všihn'],aspect,
                             stimulus_present=True),tokens(form))
        for aspect in ('progressive','perfective'):
            with self.subTest(aspect=aspect),self.assertRaises(LexicalLicenceError):
                stimulus_applicative(self.entries['všihn'],aspect,stimulus_present=True)
        with self.assertRaises(LexicalLicenceError):
            stimulus_applicative(self.entries['všihn'],'retrospective')
        for stem in ('mužn','řejn','žbirn'):
            with self.subTest(stem=stem),self.assertRaises(LexicalLicenceError):
                stimulus_applicative(self.entries[stem],'continuous',stimulus_present=True)
        self.assertEqual(self.entries['všihn']['argument_frame'],'experiencer-only')
        self.assertEqual(self.entries['všihn']['stimulus'],'applicative-eb')

    def test_unassigned_lexical_classes_do_not_generate_forms(self):
        self.assertEqual(self.entries['sledn']['segments'],list(tokens('sledn')))
        self.assertEqual(self.entries['sledn']['quantity_target'],2)
        self.assertEqual(self.entries['sledn']['principal_part_status'],'class-unresolved')
        for stem in ('sledn','torban'):
            entry=self.entries[stem]
            for kind in ('state','become','manifest'):
                with self.subTest(stem=stem,kind=kind),self.assertRaises(LexicalLicenceError):
                    finite(entry,kind,'continuous')
            with self.assertRaises(LexicalLicenceError):
                manner(entry)
        self.assertEqual(self.entries['torban']['quantity_target'],4)
        self.assertEqual(self.data['excluded_candidates'],['smerňa'])
        self.assertEqual(self.entries['torban']['principal_part_status'],'class-unresolved')
        # A known target supports a conditional grade calculation without
        # supplying finite, Become, attributive or manner class membership.
        selected=QuantityGrades.from_file().apply(tokens('torban'),
            QuantityLicence('conditional-torban','G1',True,(0,6),(4,),4))
        self.assertEqual(selected,tokens('torbán'))
        with self.assertRaises(LexicalLicenceError):
            ordinary_attributive(self.entries['torban'])

    def test_torban_predictions_require_explicit_hypothetical_classes(self):
        entry=copy.deepcopy(self.entries['torban'])
        predictions=self.data['conditional_predictions']['torban']
        self.assertIsNone(entry['finite_class'])
        self.assertIsNone(entry['become_class'])
        self.assertIsNone(entry['attributive_class'])
        self.assertEqual(entry['expected']['state'],[None]*len(STATE_ASPECTS))
        self.assertEqual(entry['expected']['become'],[None]*len(ASPECTS))
        entry['principal_part_status']='listed'
        entry['finite_class']=predictions['hypothetical_finite_class']
        entry['become_class']=predictions['hypothetical_become_class']
        for kind,aspects in (('state',STATE_ASPECTS),('become',ASPECTS)):
            for aspect,expected in zip(aspects,predictions[kind]):
                with self.subTest(kind=kind,aspect=aspect):
                    self.assertEqual(finite(entry,kind,aspect),
                                     tokens(expected))
        with self.assertRaises(LexicalLicenceError):
            manner(entry)
        entry['manner']='licensed'
        self.assertEqual(manner(entry),tokens(predictions['manner']))
        with self.assertRaises(LexicalLicenceError):
            ordinary_attributive(entry)

    def test_new_source_prescriptions_are_bound_and_mutations_rejected(self):
        source=read_domain('chapters/03-verbs.tex')
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

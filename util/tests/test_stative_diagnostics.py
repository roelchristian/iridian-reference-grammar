"""Independent finite paradigms, semantic counterexamples and local PF checks."""
import copy
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'scripts'))
from stative_diagnostics import (ASPECTS, StativeStem, check_stative_sources,
    event_derived_state, experiential_source, inflect, phased_state, relative_context, scalar_reading)
from quantity_grades import QuantityGrades, QuantityLicence
from boundary_transducer import BoundaryLicence, BoundaryState, BoundaryTransducer
from evidential_realisation import attach_indirect_evidential
from clausal_diagnostics import reduced_description, negative_mood_prejacent
from pivot_diagnostics import configurational_case

# This restricted transcription represents selected segments BEFORE contextual
# voicing, coda vocalisation, syllabification, stress and standard spelling.
SPELLING = dict(zip('abdehiklmnoprstuvyz',
                    ('a','b','d','ɛ','x','ɪ','k','l','m','n','ɔ','p','r','s','t','ʊ','v','ɨ','z')))
SPELLING.update({'á':'aː','é':'eː','í':'iː','ó':'oː','ú':'uː','ý':'ɨː',
                 'š':'ʃ','ž':'ʒ','č':'tʃ','c':'ts','ň':'ɲ','ľ':'ʎ'})

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
            segments.append(SPELLING[char])
    return tuple(segments)


class StativeDiagnosticsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fixtures = json.loads((ROOT / 'scripts/stative-fixtures.json').read_text())
        cls.targets = {'mužn':1,'hradn':2,'svorn':2,'četn':1,
                       'ptakn':2,'všihn':2,'hvodn':2,'tvírzn':2}

    def test_eighty_independent_finite_cells(self):
        count = 0
        for row in self.fixtures['paradigms']:
            stem = StativeStem(tokens(row['stem']), row['quantity_class'],
                               self.targets[row['stem']], row['quantity_class'] == 'C')
            for cell in row['forms']:
                with self.subTest(stem=row['stem'],kind=cell['kind'],aspect=cell['aspect']):
                    result = inflect(stem, cell['aspect'], inchoative=cell['kind']=='inchoative',
                                     stage_level=True, bounded=True)
                    self.assertEqual(result, tokens(cell['finite']))
                    count += 1
        self.assertEqual(count, 80)

    def test_fixture_operation_matrix_is_complete_and_conditional(self):
        self.assertEqual({r['stem'] for r in self.fixtures['paradigms']}, set(self.targets))
        for row in self.fixtures['paradigms']:
            self.assertEqual({(c['kind'],c['aspect']) for c in row['forms']},
                {(kind, aspect) for kind in ('state','inchoative') for aspect in ASPECTS})
            for cell in row['forms']:
                for field in ('finite','negative','vy','so','linked','participant','relative',
                              'evidential','evidential_linked','licence'):
                    self.assertTrue(cell[field], (row['stem'], field))
                self.assertEqual(cell['negative'], 'za'+cell['finite'])
                self.assertEqual(cell['vy'], 'vy '+cell['finite'])
                self.assertEqual(cell['so'], 'so '+cell['finite'])
        row = self.fixtures['paradigms'][0]
        self.assertEqual(row['simple_attributive'], 'múžna')
        self.assertEqual(row['forms'][0]['relative'], 'mužnový')
        self.assertEqual(row['forms'][0]['licence'], 'marked-stage-relative')

    def test_state_aspect_does_not_supply_covert_become(self):
        stem = StativeStem(tokens('mužn'),'A',1)
        for aspect in ('progressive','perfective'):
            with self.subTest(aspect=aspect), self.assertRaises(ValueError):
                inflect(stem,aspect)
        self.assertEqual(inflect(stem,'progressive',stage_level=True),tokens('múžnime'))
        self.assertEqual(inflect(stem,'perfective',bounded=True),tokens('múžnik'))
        self.assertEqual(inflect(stem,'retrospective'),tokens('mužnáv'))
        self.assertEqual(inflect(stem,'contemplative'),tokens('mužnáž'))

    def test_become_quantity_blocks_outer_root_regrading(self):
        stem = StativeStem(tokens('mužn'),'A',1)
        self.assertEqual(inflect(stem,'progressive',inchoative=True),tokens('mužnélime'))
        self.assertNotEqual(inflect(stem,'progressive',inchoative=True),tokens('múžnélime'))
        protected = StativeStem(tokens('tvírzn'),'C',2,True)
        self.assertEqual(inflect(protected,'perfective',inchoative=True),tokens('tvírznelek'))
        self.assertNotEqual(inflect(protected,'perfective',inchoative=True),tokens('tvírznélek'))
        with self.assertRaises(ValueError):
            inflect(StativeStem(tokens('tvírzn'),'A',2,True),'continuous')

    def test_beauty_boundary_and_strong_u_grade_need_no_repair(self):
        transducer = BoundaryTransducer.from_file()
        plain = transducer.apply(BoundaryState(tokens('muž')),
                                 BoundaryLicence('State','plain',True),('n',))
        self.assertEqual(plain.segments,tokens('mužn'))
        strong = QuantityGrades.from_file().apply(plain.segments,
            QuantityLicence('root-strong','G1',True,(0,3),(1,),1))
        self.assertEqual(strong,tokens('múžn'))
        manner = transducer.apply(plain,BoundaryLicence('manner','front',True),('ɛ',))
        self.assertEqual(manner.segments,('m','ʊ','ʒ','ɲ','ɛ'))

    def test_bound_perfective_then_single_front_boundary(self):
        result = BoundaryTransducer.from_file().apply(BoundaryState(tokens('mužnélik')),
            BoundaryLicence('linker','front',True,True),('ɛ',))
        self.assertEqual(result.segments,tokens('mužnélice'))
        self.assertNotEqual(result.segments,tokens('mužnéliče'))
        pf = self.fixtures['paradigms'][0]['forms'][7]
        self.assertEqual((pf['finite'],pf['participant'],pf['relative']),
                         ('mužnélek','mužnélikou','mužnélikový'))

    def test_evidential_protects_finite_host_from_linker_allomorphy(self):
        for host, expected in [('mužnélek','mužnélekalě'),('mužnélime','mužnélimelě'),
                               ('všihna','všihnalě'),('tvírznaž','tvírznažalě')]:
            with self.subTest(host=host):
                evid = attach_indirect_evidential(BoundaryState(tokens(host)),'Evid',True)
                linked = BoundaryTransducer.from_file().apply(evid,
                    BoundaryLicence('outer-linker','front',True),('ɛ',))
                self.assertEqual(linked.segments,tokens(expected))
        self.assertNotEqual(tokens('mužnélekalě'),tokens('mužnélicalě'))

    def test_scale_change_threshold_and_cause_are_separate(self):
        self.assertFalse(scalar_reading('state',2,4,threshold=5))
        self.assertTrue(scalar_reading('increase',2,4))
        self.assertFalse(scalar_reading('become-threshold',2,4,threshold=5))
        self.assertTrue(scalar_reading('become-threshold',2,6,threshold=5))
        self.assertFalse(scalar_reading('become-threshold',6,8,threshold=5))
        self.assertFalse(scalar_reading('cause-increase',2,4))
        self.assertTrue(scalar_reading('cause-increase',2,4,caused=True))
        self.assertFalse(scalar_reading('cause-threshold',2,4,threshold=5,caused=True))
        self.assertTrue(scalar_reading('cause-threshold',2,6,threshold=5,caused=True))
        with self.assertRaises(ValueError):
            scalar_reading('become-threshold',2,6)

    def test_phase_of_state_is_not_an_inchoative_stem(self):
        self.assertTrue(phased_state('vy',False,True))
        self.assertTrue(phased_state('so',True,True))
        self.assertFalse(phased_state('vy',True,True))
        self.assertTrue(phased_state('vy',True,False,negative=True))
        self.assertFalse(phased_state('vy',True,False))
        self.assertTrue(negative_mood_prejacent('imperative','vy',[True],[False]))
        with self.assertRaises(ValueError):
            negative_mood_prejacent('imperative','vy',[True],[False],indicative_neg=True)

    def test_psych_perspective_is_selective_and_not_person_ban(self):
        self.assertEqual(experiential_source(psychological=True,other_person=True,
                                             access='inferred'),'indirect-preferred')
        for access in ('reported','narrative','direct'):
            self.assertEqual(experiential_source(psychological=True,other_person=True,
                                                 access=access),'licensed')
        self.assertEqual(experiential_source(psychological=False,other_person=True,
                                             access='observable'),'licensed')
        self.assertEqual(experiential_source(psychological=False,other_person=True,
                                             access='inferred'),'licensed')

    def test_result_state_requires_event_but_lexical_state_does_not(self):
        self.assertTrue(event_derived_state(True,False))
        self.assertFalse(event_derived_state(True,False,result=True))
        self.assertTrue(event_derived_state(True,True,result=True))
        self.assertFalse(event_derived_state(False,True,result=True))

    def test_lower_projections_do_not_admit_internal_higher_operators(self):
        self.assertTrue(reduced_description(('AspP',('BecomeP',('StateP',('VP',))))))
        self.assertTrue(reduced_description(('AspP',('ResP',('VP',)))))
        for high in ('NegP','MoodP','EvidP','PhasP','Op¬','comment'):
            self.assertFalse(reduced_description(('AspP',('StateP',(high,)))))

    def test_inchoative_holder_case_and_causative_case_remain_distinct(self):
        for domain in ('NOM','ERG'):
            frame = dict(domain=domain,order=['holder'],selected='holder',
                         external='holder',excluded=[])
            self.assertEqual(configurational_case(frame),{'holder':'DIR'})
        nom = dict(domain='NOM',order=['causer','holder'],selected='causer',
                   external='causer',excluded=[])
        erg = dict(domain='ERG',order=['causer','holder'],selected='holder',
                   external='causer',excluded=[])
        self.assertEqual(configurational_case(nom),{'causer':'DIR','holder':'IND'})
        self.assertEqual(configurational_case(erg),{'causer':'TRS','holder':'DIR'})

    def test_marked_continuous_relative_is_not_free_lexical_attribute(self):
        self.assertFalse(relative_context('state','continuous'))
        for condition in ('episodic','temporal','contrastive'):
            self.assertTrue(relative_context('state','continuous',**{condition:True}))
        self.assertTrue(relative_context('inchoative','continuous'))
        self.assertTrue(relative_context('state','retrospective'))
        with self.assertRaises(ValueError):
            relative_context('state','continuous',episodic='yes')

    def test_causative_domains_preserve_lower_become_and_outer_orientation(self):
        cells={(r['stem'],r['kind']):r for r in self.fixtures['causatives']}
        self.assertEqual(len(cells),16)
        self.assertEqual(cells['svorn','state-causative']['perfective'],'svornéranik')
        self.assertEqual(cells['mužn','inchoative-causative']['progressive'],'mužnélrime')
        self.assertEqual(cells['tvírzn','inchoative-causative']['perfective'],'tvírznelranik')
        self.assertEqual(cells['tvírzn','state-causative']['continuous'],'tvírznera')
        selected=BoundaryTransducer.from_file().apply(BoundaryState(tokens('mužnél')),
            BoundaryLicence('compact-Caus','plain',True),('r',))
        self.assertEqual(selected.segments,tokens('mužnélr'))
        self.assertNotEqual(selected.segments,tokens('mužnéler'))

    def test_reduced_mood_stem_and_directive_case_do_not_reuse_indicative(self):
        selected=BoundaryState(tokens('svornér'))
        ipfv=BoundaryTransducer.from_file().apply(selected,
            BoundaryLicence('imperative','plain',True),('iː','m'))
        self.assertEqual(ipfv.segments,tokens('svornérím'))
        pfv=BoundaryTransducer.from_file().apply(selected,
            BoundaryLicence('directive-PFV','plain',True),('ɔ','v'))
        imperative=BoundaryTransducer.from_file().apply(pfv,
            BoundaryLicence('imperative','plain',True),('iː','m'))
        self.assertEqual(imperative.segments,tokens('svornérovím'))
        self.assertNotEqual(imperative.segments,tokens('svornérimeím'))
        frame=dict(domain='DIRECTIVE',order=['causer','holder'],selected='holder',
                   external='causer',excluded=[],external_licence='TRS')
        self.assertEqual(configurational_case(frame),{'causer':'TRS','holder':'DIR'})

    def test_source_bindings_and_detected_paradigm_mutation(self):
        source=(ROOT/'chapters/03-verbs.tex').read_text()
        sources={'chapters/03-verbs.tex':source, 'chapters/06-simple-sentence.tex':(ROOT/'chapters/06-simple-sentence.tex').read_text()}
        self.assertEqual(check_stative_sources(sources,self.fixtures),[])
        broken=copy.deepcopy(sources)
        # Alter one cell ONLY within the independently bounded canonical table.
        anchor=r'\label{tab:stative-become}'
        prefix,tail=broken['chapters/03-verbs.tex'].split(anchor,1)
        broken['chapters/03-verbs.tex']=prefix+anchor+tail.replace('mužnélek','mužnélik',1)
        self.assertTrue(check_stative_sources(broken,self.fixtures))
        comparative=copy.deepcopy(sources)
        comparative['chapters/06-simple-sentence.tex']=comparative['chapters/06-simple-sentence.tex'].replace('četnélime','čétnime')
        self.assertTrue(check_stative_sources(comparative,self.fixtures))

    def test_source_binding_detects_lost_locality_constraint(self):
        source=(ROOT/'chapters/03-verbs.tex').read_text().replace('Asp cannot reach through Become',
                                                               'Asp may regrade roots through Become')
        self.assertTrue(any('locality' in error or 'Asp cannot' in error for error in check_stative_sources({'chapters/03-verbs.tex':source,'chapters/06-simple-sentence.tex':(ROOT/'chapters/06-simple-sentence.tex').read_text()},self.fixtures)))

if __name__ == '__main__':
    unittest.main()

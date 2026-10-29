"""Explicit lexical licences for the ordinary stative extension.

This bounded model consumes listed principal parts and supplied interpretations.
It neither infers classes from short spelling nor supplies missing vocalism,
phonetic output, perspective shifts or causable meanings. Relative formation is
outside its interface and is intentionally unchanged.
"""
import json
from pathlib import Path

from boundary_transducer import BoundaryLicence, BoundaryState, BoundaryTransducer
from quantity_grades import QuantityGrades, QuantityLicence
from evidential_realisation import attach_indirect_evidential
from stative_diagnostics import ASPECTS, SHORT, StativeStem, inflect


class LexicalLicenceError(ValueError):
    """A requested operation lacks a listed lexical or contextual licence."""


def load_lexicon(path=None):
    path = Path(path) if path else Path(__file__).with_name('stative-lexicon.json')
    data = json.loads(path.read_text(encoding='utf-8'))
    for entry in data['entries']:
        required = {'stem','subclass','morphological_class','finite_class','segments',
                    'quantity_target','argument_frame','gradability','aspect_licences',
                    'become_class','manifest_class','attributive_class','stimulus',
                    'perspective','causative','manner','principal_part_status','expected',
                    'protected_quantity','nominalisation'}
        if set(entry) != required:
            raise LexicalLicenceError('lexical record has missing or unknown fields')
        if entry['principal_part_status'] not in ('listed','unresolved','cluster-unresolved'):
            raise LexicalLicenceError('unknown principal-part status')
        if type(entry['protected_quantity']) is not bool:
            raise LexicalLicenceError('protected quantity must be explicit')
        if entry['principal_part_status']=='listed' and (entry['finite_class'] is None
                or entry['protected_quantity'] != (entry['finite_class']=='C')):
            raise LexicalLicenceError('listed finite class and protected quantity disagree')
        if entry['finite_class'] not in ('A','C',None):
            raise LexicalLicenceError('unlisted finite class')
        if entry['become_class'] not in ('EL-S','EL-P',None):
            raise LexicalLicenceError('unlisted Become class')
        if entry['manifest_class'] not in ('ESH-A',None):
            raise LexicalLicenceError('unlisted Manifest class')
        if entry['attributive_class'] not in ('I','II','III',None):
            raise LexicalLicenceError('unlisted attributive class')
        if entry['principal_part_status'] == 'unresolved':
            if entry['quantity_target'] is not None or entry['finite_class'] is not None:
                raise LexicalLicenceError('unresolved principal part cannot acquire a quantity target')
        elif (type(entry['quantity_target']) is not int
              or not 0 <= entry['quantity_target'] < len(entry['segments'])):
            raise LexicalLicenceError('explicit principal-part nucleus required')
    if len({entry['stem'] for entry in data['entries']}) != len(data['entries']):
        raise LexicalLicenceError('duplicate lexical record')
    return data


def _available(entry):
    if entry['principal_part_status'] != 'listed':
        raise LexicalLicenceError('principal parts unresolved; no vowel repair is licensed')
    return tuple(entry['segments'])


def _strength(segments, target, identifier):
    return QuantityGrades.from_file().apply(segments,
        QuantityLicence(identifier,'G1',True,(0,len(segments)),(target,),target))


def derive(entry, kind):
    """Return the explicitly licensed stem and its local quantity target."""
    segments = _available(entry)
    if kind == 'state':
        return segments, entry['quantity_target']
    if kind == 'become':
        # An EL-S assignment is indispensable: shortness alone supplies none.
        if entry['become_class'] not in ('EL-S','EL-P'):
            raise LexicalLicenceError('Become class not listed')
        extension = ('eː','l') if entry['become_class']=='EL-S' else ('ɛ','l')
        result = BoundaryTransducer.from_file().apply(BoundaryState(segments),
            BoundaryLicence('listed-Become','plain',True),extension)
        return result.segments, len(segments)
    if kind == 'manifest':
        if entry['manifest_class'] != 'ESH-A':
            raise LexicalLicenceError('Manifest is not listed for this lexeme')
        result = BoundaryTransducer.from_file().apply(BoundaryState(segments),
            BoundaryLicence('listed-Manifest','plain',True),('ɛ','ʃ'))
        return result.segments, len(segments)
    raise LexicalLicenceError('unknown derivational head; stacking is not licensed')


def finite(entry, kind, aspect, *, stage_level=False, bounded=False):
    if aspect not in ASPECTS:
        raise LexicalLicenceError('unknown aspect')
    segments,target = derive(entry,kind)
    if kind == 'state':
        return inflect(StativeStem(segments,entry['finite_class'],target,
                                   entry['finite_class']=='C'),aspect,
                       stage_level=stage_level,bounded=bounded)
    if kind == 'become':
        return segments+SHORT[aspect]
    # ESH-A is the explicitly listed derived class; G1 targets its own e.
    if aspect in ('progressive','perfective'):
        segments = _strength(segments,target,'Manifest-local-Asp')
    ending = SHORT[aspect]
    if aspect in ('retrospective','contemplative'):
        ending = ('aː','v' if aspect=='retrospective' else 'ʒ')
    return segments+ending


def ordinary_attributive(entry):
    segments = _available(entry)
    klass = entry['attributive_class']
    if klass is None:
        raise LexicalLicenceError('ordinary attributive principal part unlisted')
    if klass == 'I':
        return _strength(segments,entry['quantity_target'],'ATTR-I')+('a',)
    if klass == 'II':
        return segments+('aː',)
    return BoundaryTransducer.from_file().apply(BoundaryState(segments),
        BoundaryLicence('ATTR-III-local-front','front',True),('a',)).segments


def manner(entry):
    if entry['manner'] != 'licensed':
        raise LexicalLicenceError('manner principal part unresolved')
    return BoundaryTransducer.from_file().apply(BoundaryState(_available(entry)),
        BoundaryLicence('manner-front','front',True),('ɛ',)).segments


def participant(entry, kind, aspect, **licences):
    selected = finite(entry,kind,aspect,**licences)
    if aspect == 'continuous':
        return selected[:-1]+('ɔ','v','a')
    if aspect == 'progressive':
        return selected[:-1]+('ou̯',)
    if aspect == 'perfective' and kind in ('become','manifest'):
        selected = selected[:-2]+('ɪ','k')
    return selected+('ou̯',)


def evidential(entry, kind, aspect, **licences):
    return attach_indirect_evidential(BoundaryState(finite(entry,kind,aspect,**licences)),
                                     'indirect-Evid',True).segments


def causative(entry, kind, aspect, *, causable=False):
    if causable is not True or entry['causative'] != 'conditional':
        raise LexicalLicenceError('a licensed causable interpretation must be supplied')
    segments,target = derive(entry,kind)
    if kind == 'state':
        extension = ('ɛ','r') if entry['finite_class']=='C' else ('eː','r')
        selected = segments+extension
    elif kind == 'become':
        # Become already supplies protected local strength, including EL-P.
        selected = segments+('r',)
    else:
        # Caus selects Manifest's exposed e, not the hidden property root.
        selected = _strength(segments,target,'derived-local-Caus')+('r',)
    if aspect not in ASPECTS:
        raise LexicalLicenceError('unknown aspect')
    if aspect == 'perfective':
        return selected+('a','n','ɪ','k')
    if aspect == 'retrospective':
        return selected+('a','n','a','v')
    return selected+SHORT[aspect]


def stimulus_applicative(entry, aspect, *, stimulus_present=False, kind='state'):
    if kind!='state' or entry['stimulus']!='applicative-eb' or stimulus_present is not True:
        raise LexicalLicenceError('this frame has no licensed overt stimulus applicative')
    segments = _available(entry)+('eː','b')
    if aspect not in ASPECTS:
        raise LexicalLicenceError('unknown aspect')
    return segments+(('ɪ','k') if aspect=='perfective' else SHORT[aspect])


def perspective_licensed(entry, *, experiencer, anchor='speaker',
                         clause_type='declarative', shifted=False, evidence=False,
                         kind='state', internal_reading=True):
    """Check a supplied anchoring dependency, not infer one from person.

    This is an internal-state assertion check, not an emotion detector.
    Clause type alone cannot establish the independent report/attitude relation.
    Indirect evidence may support a proposition without shifting the anchor.
    A licensed Manifest display or an observable bodily reading does not assert
    genuine internal experience and therefore does not inherit this dependency.
    """
    if (clause_type not in ('declarative','question','report','narrative','embedded')
            or type(shifted) is not bool or type(evidence) is not bool
            or type(internal_reading) is not bool or kind not in ('state','manifest')
            or not isinstance(anchor,str) or not anchor
            or not isinstance(experiencer,str) or not experiencer):
        raise LexicalLicenceError('explicit clause and anchoring conditions required')
    if kind=='manifest':
        derive(entry,'manifest')  # The observation reading still needs its head.
        return True
    if not internal_reading:
        return entry['perspective'] != 'psych-anchored'
    if entry['perspective']=='none':
        return True
    if evidence:
        return True
    if anchor=='speaker':
        return experiencer=='speaker'
    return (shifted and clause_type in ('question','report','narrative','embedded')
            and experiencer==anchor)


def manifestation_holds(display, genuine_feeling):
    if type(display) is not bool or type(genuine_feeling) is not bool:
        raise LexicalLicenceError('supply explicit display and feeling truth values')
    return display


def check_lexical_extension_sources(sources, data):
    """Bind new ordinary ATTR/Manifest prescriptions to their own sections."""
    source=sources.get('chapters/03-verbs.tex','')
    failures=[]
    marker=r'\label{tab:stative-manifest}'
    table=source.split(marker,1)[1].split(r'\end{table}',1)[0] if marker in source else ''
    for form in data['manifest']['forms']:
        if r'\ird{'+form+'}' not in table:
            failures.append('lexical extension: missing Manifest table form '+form)
    for form in ('všihňa','všihňe','žbirňa','žbirňe'):
        if r'\phon{'+form+'}' not in source:
            failures.append('lexical extension: missing local ATTR/manner contrast '+form)
    return failures

"""Bounded stative-form and semantic diagnostics for the reviewed design.

The caller supplies lexical quantitative class, eligible nucleus, protected
quantity and semantic context. This is not a lexical analyser, phonetic renderer
or source of attestation. In particular, it does not infer a repair from a
written cluster, establish causative selection, or compute arbitrary Mood forms.
"""
from dataclasses import dataclass
import re

from quantity_grades import QuantityGrades, QuantityLicence
from boundary_transducer import BoundaryLicence, BoundaryState, BoundaryTransducer
from phasal_diagnostics import ordinary_phase

ASPECTS = ('continuous', 'progressive', 'perfective', 'retrospective', 'contemplative')
SHORT = {'continuous': ('a',), 'progressive': ('ɪ', 'm', 'ɛ'),
         'perfective': ('ɛ', 'k'), 'retrospective': ('a', 'v'),
         'contemplative': ('a', 'ʒ')}


@dataclass(frozen=True)
class StativeStem:
    segments: tuple
    quantity_class: str
    target: int
    protected: bool = False


def inflect(stem, aspect, *, inchoative=False, stage_level=False, bounded=False):
    """Select a supplied State or Become stem before higher operations.

    State progressive/PF require explicit contextual licences. Become creates
    a local stem; Aspect cannot select an inner root grade through that head.
    Only indicative, single-participant forms are implemented here.
    """
    if (not isinstance(stem, StativeStem) or stem.quantity_class not in ('A', 'C')
            or aspect not in ASPECTS or type(inchoative) is not bool
            or type(stage_level) is not bool or type(bounded) is not bool):
        raise ValueError('explicit stative stem, class and aspect required')
    if (stem.quantity_class == 'C') != stem.protected:
        raise ValueError('these fixtures require independently protected Class C')
    if not inchoative and aspect == 'progressive' and not stage_level:
        raise ValueError('simple-state progressive needs a licensed marked context')
    if not inchoative and aspect == 'perfective' and not bounded:
        raise ValueError('simple-state perfective needs a bounded-state context')
    if inchoative:
        # Plain attachment selects no PAL or root quantity mutation.
        extension = ('ɛ', 'l') if stem.protected else ('eː', 'l')
        state = BoundaryTransducer.from_file().apply(BoundaryState(stem.segments),
            BoundaryLicence('Become', 'plain', True), extension)
        return state.segments + SHORT[aspect]
    selected = stem.segments
    if stem.quantity_class == 'A' and aspect in ('progressive', 'perfective'):
        selected = QuantityGrades.from_file().apply(selected,
            QuantityLicence('State-Asp', 'G1', True, (0, len(selected)),
                            (stem.target,), stem.target))
    ending = SHORT[aspect]
    if aspect == 'perfective':
        ending = ('ɪ', 'k')  # STATE's independently selected high-vowel PF
    elif stem.quantity_class == 'A' and aspect in ('retrospective', 'contemplative'):
        ending = ('aː', 'v' if aspect == 'retrospective' else 'ʒ')
    return selected + ending


def scalar_reading(kind, before, after, *, threshold=None, caused=False):
    """Evaluate supplied scale points, with causation separately stipulated.

    No aspect or spelling is used to infer a threshold, endpoint or causer.
    """
    if kind not in ('state', 'increase', 'become-threshold', 'cause-increase', 'cause-threshold'):
        raise ValueError('unknown bounded scalar diagnostic')
    if (type(before) not in (int, float) or type(after) not in (int, float)
            or type(caused) is not bool):
        raise ValueError('explicit numeric scale points and causal relation required')
    if kind in ('state', 'become-threshold', 'cause-threshold') and type(threshold) not in (int, float):
        raise ValueError('threshold is a separate contextual input')
    if kind == 'state':
        return after >= threshold
    transition = (before < threshold <= after if 'threshold' in kind else after > before)
    return transition and (caused if kind.startswith('cause-') else True)


def phased_state(particle, before, now, *, negative=False):
    """Phas scopes over supplied positive/negative state propositions."""
    if type(negative) is not bool:
        raise ValueError('explicit polarity required')
    return ordinary_phase(particle, not before if negative else before,
                          not now if negative else now)


def experiential_source(*, psychological, other_person, access):
    """Return the specified evidential preference, never an inflectional ban.

    Reports and narrative perspective license another person's direct state
    description; observable bodily conditions do not inherit a psych rule.
    """
    if (type(psychological) is not bool or type(other_person) is not bool
            or access not in ('direct', 'inferred', 'reported', 'narrative', 'observable')):
        raise ValueError('supply predicate subclass, perspective and evidence')
    return 'indirect-preferred' if psychological and other_person and access == 'inferred' else 'licensed'


def event_derived_state(state_holds, event_occurred, *, result=False):
    """Lexical openness need not entail an opening; Res requires that event."""
    if any(type(x) is not bool for x in (state_holds, event_occurred, result)):
        raise ValueError('explicit event/state conditions required')
    return state_holds and (event_occurred if result else True)


def check_stative_sources(sources, fixtures):
    """Bind independent paradigm cells and locality to bounded source sections.

    Matching a prescription does not establish grammaticality. Semantic
    counterexamples and independent token-level quantity tests run separately.
    """
    normalise = lambda value: ' '.join(value.split())
    failures = []
    for binding in fixtures['source_bindings']:
        source = sources.get(binding.get('source', 'chapters/03-verbs.tex'), '')
        found = source.split(binding['anchor'], 1)
        if len(found) != 2:
            failures.append('stative source: missing anchor ' + binding['anchor'])
            continue
        section = normalise(found[1].split(binding['end'], 1)[0])
        for required in binding['required']:
            if normalise(required) not in section:
                failures.append('stative source: missing prescribed form/constraint ' + required)
    for example in fixtures.get('source_examples', []):
        blocks = re.findall(r'\\begingl(.*?)\\endgl',
                            sources.get(example['source'], ''), re.S)
        matched = [block for block in blocks if
                   r'\gla ' + example['form'] + '//' in block]
        if not matched:
            failures.append('stative source: missing example ' + example['form'])
        for block in matched:
            for required in example['required']:
                if normalise(required) not in normalise(block):
                    failures.append('stative source: changed gloss/reading for ' + example['form'])
    return failures


def relative_context(kind, aspect, *, episodic=False, temporal=False, contrastive=False):
    """Context gate for the marked continuous State relative only.

    Structural selection and holder abstraction are checked separately. This
    function does not let a contextual flag admit higher operators internally.
    """
    if kind not in ('state', 'inchoative') or aspect not in ASPECTS:
        raise ValueError('supply state/inchoative and a licensed aspect')
    if any(type(value) is not bool for value in (episodic, temporal, contrastive)):
        raise ValueError('contextual licences must be explicit Booleans')
    return kind != 'state' or aspect != 'continuous' or episodic or temporal or contrastive

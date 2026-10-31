"""Bounded lexical selection, separate from phonological form generation.

A successful check supplies a listed constructional licence, not an attestation,
frequency estimate or finite form. Unresolved records withhold approval without
making an ungrammaticality judgment. Case selection remains a separate model.
"""
import json
from pathlib import Path


class ValencyLicenceError(ValueError):
    """The supplied lexical or constructional licence is unavailable."""


def load_profiles(path=None):
    path = Path(path) if path else Path(__file__).with_name('valency-profiles.json')
    data = json.loads(path.read_text(encoding='utf-8'))
    stems = [entry['stem'] for entry in data['entries']]
    if len(stems) != len(set(stems)):
        raise ValencyLicenceError('duplicate lexical profile')
    for entry in data['entries']:
        if not entry['basic_frame'] or not entry['source']:
            raise ValencyLicenceError('basic frame and source required')
        if entry['causative']['licence'] not in (
                'listed', 'lexically-conditional', 'causability-conditional', 'unresolved'):
            raise ValencyLicenceError('unknown causative licence')
        if not set(entry['activity_domains']) <= {'NOM', 'ERG'}:
            raise ValencyLicenceError('unknown activity domain')
    return data


def select(entry, construction, *, domain, indicative=True, directive=False, role=None,
           overt_patient=False, causable=False, lexical_causative=False,
           omitted_causee=False, overt_causee=False, recoverable_causee=False, service=False,
           applied=False, overt_applied=False, instrument_context=False):
    """Check an explicitly requested reading; never infer licensing from a form.

    ``lexical_causative`` records a separately supplied lexical decision for a
    conditional predicate; ``causable`` supplies the interpretation required
    for a property causative. Neither flag repairs an unresolved profile.
    A service request explicitly closes the performer role (``omitted_causee``),
    excluding an overt or anaphorically recovered causee. Ordinary omissions
    retain that separate role. ``instrument_context`` supplies both implement
    compatibility and the contextual prominence specified for the applied use.
    ``directive=True`` selects directive Mood and therefore overrides the
    default ``indicative=True``. It requires separately overt causee/applied
    participants where those roles are retained, as prescribed for directives.
    """
    if directive:
        indicative = False
    if domain not in ('NOM', 'ERG'):
        raise ValencyLicenceError('unknown alignment domain')
    if omitted_causee and overt_causee:
        raise ValencyLicenceError('causee cannot be both overt and omitted')
    if service and construction != 'causative':
        raise ValencyLicenceError('service interpretation requires a causative')
    if construction == 'activity':
        if overt_patient or domain not in entry['activity_domains']:
            raise ValencyLicenceError('patientless activity frame unavailable')
        if domain == 'NOM' and entry['stem'] in ('pjašt', 'kař') and not indicative:
            raise ValencyLicenceError('new NOM activity licence is indicative')
    elif construction == 'antipassive':
        if not entry['antipassive'] or domain != 'ERG' or not indicative or overt_patient:
            raise ValencyLicenceError('antipassive requires indicative ERG and excludes a patient')
    elif construction == 'applicative':
        if directive and not overt_applied:
            raise ValencyLicenceError('directive requires an overt applied participant')
        if role not in entry['applicative_roles']:
            raise ValencyLicenceError('applied role not listed for this predicate')
        if role == 'instrument' and not instrument_context:
            raise ValencyLicenceError('instrument use requires an implement-compatible context')
    elif construction == 'causative':
        if directive and (not overt_causee or omitted_causee):
            raise ValencyLicenceError('directive requires an overt causee')
        if directive and applied and not overt_applied:
            raise ValencyLicenceError('directive requires an overt applied participant')
        licence = entry['causative']['licence']
        if licence == 'unresolved':
            raise ValencyLicenceError('causative lexical licence unresolved')
        if licence == 'lexically-conditional' and not lexical_causative:
            raise ValencyLicenceError('separate lexical causative licence required')
        if licence == 'causability-conditional' and not causable:
            raise ValencyLicenceError('causable property reading required')
        if applied and not entry['causative']['applied']:
            raise ValencyLicenceError('causative of applied frame not listed')
        if service:
            if not entry['causative']['service']:
                raise ValencyLicenceError('service causative not listed')
            if not indicative:
                raise ValencyLicenceError('service causative requires indicative Mood')
            if not omitted_causee or overt_causee or recoverable_causee:
                raise ValencyLicenceError('service performer is existential, not a separate causee')
            if applied:
                raise ValencyLicenceError('applied service causative has no separate licence')
        if omitted_causee and not (recoverable_causee or service):
            raise ValencyLicenceError('ordinary omitted causee requires contextual licensing')
    else:
        raise ValencyLicenceError('unknown construction')
    return True

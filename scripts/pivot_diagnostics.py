"""Bounded comparisons, not an analyser or a proof of Iridian syntax.

Callers supply argument-chain identities, the selected participant, residual
case exclusions and accessible occurrences. Neither model derives eligibility
from a pivot diacritic, morphology, or the desired case output. Case is evaluated
on licensing order, before the hypothesised finite displacement. Directive
external case is a separate supplied Mood licence, not ERG dependent case.
A directive inventory without an external chain models only the listed roles;
it does not establish that an unpronounced actor is absent from syntax.
"""


def _inputs(frame):
    order = list(dict.fromkeys(frame['order']))  # copies are one competitor
    selected, external = frame['selected'], frame.get('external')
    if selected not in order or (external is not None and external not in order):
        raise ValueError('selected/external chain must belong to the inventory')
    excluded = set(frame['excluded'])
    if not excluded <= set(order) or selected in excluded:
        raise ValueError('invalid residual licensing exclusions')
    if frame['domain'] not in ('NOM', 'ERG', 'DIRECTIVE'):
        raise ValueError('explicit domain required')
    if frame['domain'] == 'ERG':
        if external is None or external in excluded:
            raise ValueError('ERG candidate requires an eligible external chain')
        if external != selected and order.index(external) > order.index(selected):
            raise ValueError('ERG licensing order must place external above selected')
    if frame['domain'] == 'DIRECTIVE':
        required = None if external is None else ('DIR' if external == selected else 'TRS')
        if 'external_licence' not in frame or frame['external_licence'] != required:
            raise ValueError('directive requires the explicit constructional external licence')
    return order, selected, external, excluded


def configurational_case(frame):
    order, selected, external, excluded = _inputs(frame)
    case = dict.fromkeys(order, 'IND')
    case[selected] = 'DIR'
    if frame['domain'] == 'DIRECTIVE' and external is not None:
        case[external] = frame['external_licence']
    if frame['domain'] == 'ERG':
        competitors = [chain for chain in order if chain not in excluded]
        for position, chain in enumerate(competitors):
            if chain != selected and competitors[position + 1:]:
                case[chain] = 'TRS'
    return case


def successive_agree_case(frame):
    order, selected, external, excluded = _inputs(frame)
    case = dict.fromkeys(order, 'IND')
    case[selected] = 'DIR'
    if frame['domain'] == 'DIRECTIVE' and external is not None:
        case[external] = frame['external_licence']
    if frame['domain'] == 'ERG':
        goals = [chain for chain in order if chain not in excluded]
        # This candidate needs the stipulated two-goal geometry. It does not
        # silently solve the still-open feature mechanism for residual DPs.
        if set(goals) != {external, selected} or len(goals) > 2:
            raise ValueError('candidate needs an explicit external/selected domain')
        contacted = set()
        for goal in reversed(goals):  # explicitly expanding lower search
            contacted.add(goal)
        if len(contacted) == 2:
            case[external] = 'TRS'
    return case


def outer_selection(retained=None, applied=None, causee=None):
    """Supplied role inventory of an ERG causative, not syntactic probing."""
    for participant in (retained, applied, causee):
        if participant is not None:
            return participant
    raise ValueError('no licensed embedded participant')


def naive_all_dp_case(order):
    """Falsifying control: every higher pronounced occurrence gets TRS."""
    if not order:
        raise ValueError('empty inventory')
    return {chain: ('DIR' if i == len(order) - 1 else 'TRS')
            for i, chain in enumerate(order)}


def accessible(boundaries):
    """Each (opaque, exported_to_edge) pair describes one crossed domain."""
    for opaque, exported in boundaries:
        if type(opaque) is not bool or type(exported) is not bool:
            raise ValueError('explicit boundary and edge conditions required')
        if opaque and not exported:
            return False
    return True


def matching_goal(goals, eligible):
    """DP nonmatching is distinct from access through a transferred phase."""
    for chain, boundaries in goals:
        if chain in eligible and accessible(boundaries):
            return chain
    return None


def quantifier_scopes(relation):
    """Rows are existential witnesses; columns are universal participants."""
    if not relation or not relation[0] or any(len(row) != len(relation[0]) for row in relation):
        raise ValueError('a nonempty rectangular truth model is required')
    if any(type(value) is not bool for row in relation for value in row):
        raise ValueError('truth values must be explicit')
    return {'exists_every': any(all(row) for row in relation),
            'every_exists': all(any(row[i] for row in relation)
                                for i in range(len(relation[0])))}


def negative_scopes(values):
    if not values or any(type(value) is not bool for value in values):
        raise ValueError('explicit nonempty interpretation domain required')
    return {'not_exists': not any(values), 'exists_not': any(not v for v in values)}

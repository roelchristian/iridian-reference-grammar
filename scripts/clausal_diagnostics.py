"""Bounded semantic/selection diagnostics for the specified Iridian design.

Inputs are supplied stage values and labelled domains, never inferred from
spelling. Modal force is opaque: only its phasal prejacent is evaluated. These
checks do not turn toy truth values into attestation or speaker judgments.
Boolean satisfaction does not distinguish false assertions from failed
presuppositions; locality is supplied, not inferred from clause structure.
"""
import re

from phasal_diagnostics import ordinary_phase, exclusive


NEGATIVE_MOODS = frozenset(('imperative', 'hortative', 'irrealis'))
INNER_DOMAINS = frozenset(('AspP', 'VoiceOrient', 'CausP', 'VoiceP', 'ApplP',
                           'vP', 'VP', 'StateP', 'BecomeP', 'ResP'))


def comment_phase(particle, before, now, *, negative=False, comment=None,
                  scope='high'):
    """Evaluate a fixed associate (index 0) and its explicit alternatives.

    Only exclusive focus has the specified low interpretation. Negation acts
    on each proposition before phase, including in the low-exclusive reading.
    Additive's existence requirement is checked, without scalar ordering.
    """
    if (len(before) != len(now) or not before
            or any(type(x) is not bool for x in (*before, *now))
            or type(negative) is not bool):
        raise ValueError('supply matching explicit Boolean stage alternatives')
    if comment not in (None, 'och', 'kamo'):
        raise ValueError('diagnostic covers only och and kamo')
    if scope not in ('high', 'low') or (scope == 'low' and comment != 'kamo'):
        raise ValueError('only kamo licenses the bounded low interpretation')
    if comment and len(before) < 2:
        raise ValueError('focus operators require a nontrivial alternative set')
    previous = [not x if negative else x for x in before]
    current = [not x if negative else x for x in now]
    if scope == 'low':
        return ordinary_phase(particle, exclusive(previous), exclusive(current))
    phased = [ordinary_phase(particle, x, y) for x, y in zip(previous, current)]
    if comment == 'kamo':
        return exclusive(phased)
    if comment == 'och':
        return phased[0] and any(phased[1:])
    return phased[0]


def negative_mood_prejacent(mood, particle, before, now, *, local=True,
                            indicative_neg=False, comment=None, scope='high'):
    """High negative Mood licenses one lower Op¬ in its own domain.

    `local=False` represents an intervening finite/nominal selection boundary.
    A second indicative Neg is excluded rather than silently double-negated.
    """
    if mood not in NEGATIVE_MOODS or not local or indicative_neg:
        raise ValueError('negative Mood requires its own local lower operator')
    return comment_phase(particle, before, now, negative=True,
                         comment=comment, scope=scope)


def reduced_description(tree):
    """Whether a labelled nested tuple is an internally licensed AspP.

    Operator adjuncts are inspected too: an AspP root cannot hide Op¬, Phas,
    comment, Mood or evidential structure inside a reduced description.
    External matrix structure is deliberately not passed to this selector.
    This checks the selection boundary only, not inner co-occurrence or the
    completeness of an independently licensed valency derivation.
    """
    def inner(node):
        return (isinstance(node, tuple) and bool(node)
                and node[0] in INNER_DOMAINS
                and all(inner(child) for child in node[1:]))
    return inner(tree) and tree[0] == 'AspP'


def check_clausal_sources(sources):
    """Bind the bounded calculus to the published surface/scope/status rows.

    Semantic counterexamples are tested separately; matching this prescription
    alone would not establish the intended interpretation.
    """
    source = sources.get('chapters/06-simple-sentence.tex', '')
    expected = []
    for negative, host in ((False, 'zdrávime'), (True, 'zazdrávime')):
        p = r'\neg P' if negative else 'P'
        for comment, operator in (('och', 'A'), ('kamo', 'E')):
            for phase, symbol in (('vy', 'V'), ('so', 'S')):
                expected.append((f'Marek {comment} {phase} {host}.',
                                 f'{operator}({symbol}({p}))', 'L'))
    for host, force in (('piašté', 'D'), ('piaštku', 'H'), ('piaštir', 'R')):
        for comment, operator in (('Och', 'A'), ('Kamo', 'E')):
            for phase, symbol in (('vy', 'V'), ('so', 'S')):
                status = 'M' if phase == 'vy' and force != 'R' else 'L'
                expected.append((f'{comment} {phase} {host}.',
                                 f'{force}({operator}({symbol}(\\neg P)))', status))
    rows = re.findall(r'\\ird\{([^{}]+)\}\s*&\s*\$([^$]+)\$\s*&\s*([LM])\s*\\\\', source)
    failures = []
    for form, scope, status in expected:
        matches = [row for row in rows if row[0] == form]
        if matches != [(form, scope, status)]:
            failures.append('clausal diagnostic: missing/conflicting surface-scope-status row ' + form)
    return failures

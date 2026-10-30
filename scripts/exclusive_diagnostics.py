"""Finite-model diagnostics for the grammar's exclusive/scalar analysis.

Alternative propositions, their truth values and a reflexive/transitive
strength ordering are supplied by the caller. No focus, QUD or lexical facts
are inferred from spelling. These checks supplement the older Boolean phasal
satisfaction checks; they distinguish failed MIN from false MAX.

Projection is an explicit hypothesis supplied by the caller, not an Iridian
rule inferred from this model. In particular, a negative Mood suffix is not
implemented as assertion negation, and modal worlds are not invented.
"""
from dataclasses import dataclass
from math import isfinite


@dataclass(frozen=True)
class ExclusiveContent:
    prejacent: bool
    minimum: bool
    maximum: bool

    @property
    def satisfied(self):
        return self.minimum and self.maximum


def exclusive_content(truths, prejacent, stronger):
    """MIN: some true q >= p; MAX: every true q <= p.

    `stronger` contains pairs (q, p) for q >= p, including reflexive pairs.
    Incomparable true alternatives violate MAX even if none is strictly
    stronger than p. The prejacent is reported independently: MIN does not
    generally assert or presuppose that particular proposition.
    """
    alternatives = set(truths)
    relation = set(stronger)
    if (not alternatives or prejacent not in alternatives
            or any(type(value) is not bool for value in truths.values())):
        raise ValueError('supply explicit Boolean alternatives and a prejacent')
    if (any(a not in alternatives or b not in alternatives for a, b in relation)
            or any((a, a) not in relation for a in alternatives)
            or any((a, c) not in relation for a, b in relation
                   for b2, c in relation if b == b2)):
        raise ValueError('strength ordering must be a reflexive transitive relation')
    true = {q for q, value in truths.items() if value}
    return ExclusiveContent(
        truths[prejacent],
        any((q, prejacent) in relation for q in true),
        all((prejacent, q) in relation for q in true))


@dataclass(frozen=True)
class ProgressContent:
    current_minimum: bool
    prior_maximum: bool
    current_maximum: bool
    advances: bool
    below_expected_goal: bool

    @property
    def presupposed(self):
        return self.current_minimum and self.prior_maximum

    @property
    def asserted(self):
        return self.current_maximum

    @property
    def context_licensed(self):
        return self.advances and self.below_expected_goal

    @property
    def satisfied(self):
        return self.presupposed and self.asserted and self.context_licensed


def low_progress(before, now, threshold, next_threshold, expected_goal):
    """A bounded scalar-SO model on a supplied cumulative degree scale.

    MIN is anchored only at the reference stage. SO's earlier upper-bound
    condition does not require the earlier stage to attain today's threshold.
    Advancing beyond the earlier stage and a higher expected goal are separate
    contextual licensing conditions. The interval [threshold, next_threshold)
    represents the attained alternative, rather than an exact numerical value.
    """
    values = (before, now, threshold, next_threshold, expected_goal)
    if (any(type(value) not in (int, float) or not isfinite(value) for value in values)
            or not threshold < next_threshold):
        raise ValueError('supply finite degrees and increasing alternative thresholds')
    return ProgressContent(now >= threshold, before < next_threshold,
                           now < next_threshold, before < now,
                           threshold < expected_goal)


def projection_probe(content, environment, *, project_minimum):
    """Expose a chosen projection hypothesis independently of at-issue scope.

    `environment` maps MAX to an opaque question/modal/Mood representation.
    `project_minimum` explicitly selects whether MIN survives that embedding.
    Neither parameter is a default claim about an Iridian construction.
    """
    if type(project_minimum) is not bool:
        raise ValueError('choose an explicit projection hypothesis')
    return {'prejacent': content.prejacent,
            'projected_minimum': content.minimum if project_minimum else None,
            'at_issue': environment(content.maximum)}

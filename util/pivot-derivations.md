# Predicate derivations: conditional implementation ledger

This ledger separates existing descriptive obligations from candidate machinery.
It accompanies Chapter 3 §§ `sec:vm-selection-domains` and
`sec:vm-pivot-derivations`, and does not establish new judgments. It is based on
master `16329d4`; integrated onto actual PR16 master `87c23bbcb8ea59f62e415cb315a45f79613e1dc6`.

## Notation and origin

`VP(T,V)` has the retained transitive theme as V's complement. `Act(A,Q)`
is shorthand for the existing inner actor layer, not an additional stipulated
projection. `Appl(B,Q)` introduces B in relation to Q's event, below Act.
`Caus(C,Q)` introduces a causer above its embedded event. `Orient(Q)` is above
Caus when present; finite aspect and Mood license the completed configuration.
`AP(V)` removes the separate lexical patient's core argument position;
conceptual thematic content is not a licensed patient DP. E is the base actor
or sole participant as causee, and cannot also be counted as a separate T.

Case notation is DIR, TRS, IND. `>` in the selection priority is priority,
not c-command or linear order. `X < Y` means precedes, with no adjacency claim.

| Construction | Underlying argument structure | Selected participant and required case output | Surface obligation / limit |
| --- | --- | --- | --- |
| Ordinary PF transitive | `Orient(Act(A,VP(T,V)))` | T DIR, A TRS | Canonical T A V; base origin alone gives only T<V |
| Active IPFV transitive | `Orient(Act(A,VP(T,V)))` | A DIR, T IND | Canonical A T V; short actor dependency possible |
| Simple indicative applicative | `Orient(Act(A,Appl(B,VP(T,V))))` | B DIR; A IND in NOM/TRS in ERG; T IND | Canonical B A T V; independent direct T excluded |
| PF causative of intransitive | `Orient(Caus(C,Q(E)))` | E DIR, C TRS | E C V; unergative actor E and unaccusative sole-participant E have distinct origins but same case rule |
| PF causative of transitive | `Orient(Caus(C,Act(E,VP(T,V))))` | T DIR, C TRS, E IND | T C E V |
| PF causative of applied transitive | `Orient(Caus(C,Act(E,Appl(B,VP(T,V)))))` | T DIR, C TRS, E/B IND | T C E B V; B's higher origin does not give it priority over T |
| PF causative of applied intransitive | `Orient(Caus(C,Act(E,Appl(B,VP(V)))))` | B DIR, C TRS, E IND | B C E V; no retained T exists |
| PF causative of antipassive | `Orient(Caus(C,Act(E,AP(V))))` | E DIR, C TRS; no core T | E C V; no patient restored by Caus |
| NOM patient-oriented passive | `Orient_PASS(Act_optional(A,VP(T,V)))` | T DIR; optional A IND agentive dependent | T (A) V in ordinary examples; not ordinary active NOM A DIR |
| Directive with retained T | `Mood_DIR(Orient(Act(A,VP(T,V))))`; Appl and/or Caus may occur inside Orient | T DIR; overt highest A/C TRS; B/E IND where licensed | T<V; overt contrastive subject may precede T (`Jí trava piaštím`), so do not impose universal pivot-first order |

The passive row's `Act_optional` abbreviates the passive external configuration,
not a conclusion that its agent is structurally identical to an active actor.
Agent omission, indirect case and patient selection alone do not establish
binding/control eligibility. In an outer passive causative the embedded causee
remains its own predicate's participant even if the causer is unexpressed.
Directive Appl requires an overt B and directive Caus requires an overt E;
ordinary indicative argument omission must not erase those restrictions.

## Five derivational checkpoints

These checkpoints are ordered analytically; their order does not establish a
particular derivational timing mechanism before the alternatives are tested.

1. **Ordinary PF:** merge T as V complement and introduce A above VP. Outer
   patient orientation plus PF requires T DIR and A TRS. Head-final VP gives
   T<V; it does not give T<A. A movement candidate must license T past A before
   pronouncing T A V. A base/restructuring control must independently explain
   this order while preserving actor-to-theme binding connectivity.
2. **Active IPFV:** retain the same thematic origin. Active NOM selects A;
   assign/realise A DIR and T IND under the relevant licensed configuration.
   A is already highest; its overt A T V order is compatible with no long
   movement or with short raising. This ambiguity is not resolved by the
   order alone.
3. **Simple Appl:** introduce B below A and above the lexical event. Simple
   indicative orientation selects B and makes T a residual IND argument. In
   ERG A depends on the distinct selected B and is TRS; in NOM A is IND.
   Raising B over A, if required, must not accidentally promote T or make B a
   high aboutness topic. The affix's existence does not prove low Appl.
4. **PF Caus-transitive:** build the event containing E and low T, then Caus
   with C, then outer orientation. T priority gives T DIR, C TRS, E IND.
   A nearest-DP probe from the outer domain would stop incorrectly at C or E;
   a role-filtered probe needs an independently specified accessibility
   implementation. If embedded Act is a phase, T must already be at an
   accessible edge when the outer computation accesses it.
5. **PF Caus-Appl-transitive:** retain E, B and T inside the caused event.
   Outer Caus supersedes simple Appl selection, selecting retained T rather
   than B. Hence T DIR, C TRS, E/B IND. A probe seeking the highest non-causer
   fails; a probe seeking the nearest nonactor can stop incorrectly at B.
   B remains beneficiary of the caused event, `CAUS[APPL[EAT]]`; the outer
   causing-event beneficiary requires the independent `my` strategy.

## Candidate paths and failure conditions

### A: SpecIP

Conditional path: T's thematic origin → each independently licensed phase edge
→ SpecIP. Phase-edge steps occur only when the adopted phase analysis requires
them; no step is licensed solely by drawing an arrow. Selection eligibility
must be recoverable from lexical frame, inner derivation, orientation,
aspectual domain and Mood before PF. Agree can make an argument accessible to
higher licensing without itself moving it. An independent displacement
requirement is needed to pronounce its higher occurrence.

Predictions requiring judgments: a pivot at SpecIP should be above lower
phasal and predicational operators unless independently moved; a scope reading
below those operators needs lower-copy interpretation or another independently
motivated semantic mechanism. Actor binding of a reflexive theme can survive
under pre-displacement licensing or lower-copy interpretation, but does not
choose between them.

### B: lower aspectual/orientation position

Conditional path: thematic origin → necessary accessible edges → an independently
identified specifier within the existing lower aspectual/orientation domain.
A placeholder XP is not a new projection or a licensed landing site. B must
identify an existing head and independently determine its dominance relative to
PhasP and other operators. The existential use of SpecAspP is evidence that
such a specifier is possible in a specific construction; it does not establish
ordinary finite verbal pivots in that position.

Discriminating prediction: stable ordinary pivots below phasal or comment-domain
operators favour B over a simple high-IP account, subject to actual PF placement
of operator exponents. Both A and B need a solution to actor/causee intervention
and transferred-domain inaccessibility.

### C: base/restructuring control

Preserve T as lexical complement and compare a restructuring/remnant derivation
rather than simply merging T above A. Surface order, scope and structural binding
must be derived jointly. Restructuring can reduce phase barriers only with an
independent account of which embedded configurations are transparent. It cannot
be invoked selectively to rescue causative theme access while treating the same
predicate as opaque for all other dependencies.

## Case implementation interface

The bounded configurational account and the successive-Agree account must take
identical role inventories and output frames (see `pivot-case-analysis.md`).
They are not interchangeable by definition. In particular:

- all-DP pairwise dependency risks erroneously marking the causee in the PF
  Caus-transitive as TRS;
- nearest-DP successive Agree risks stopping at the causee, missing T;
- evaluating only the pronounced DP heights risks losing the external-higher
  dependency after selected-first displacement;
- computing embedded finite DIR before Caus can create two direct participants,
  contradicting the completed causative domain;
- treating case as a PF exponent that selects a DP in syntax reverses the
  architecture.

The complete finite predicate is a **licensing domain**, not automatically a
single phase. Alternatives must state timing relative to transfer and movement.
The chapter states the descriptive mapping and these requirements; it does not
claim that one case algorithm or landing site has already been established.

## Integration dependencies

PR16 supplies the actual AspP/descriptive Comm-field inventory,
construction-specific existential trees and lower negation licensed by
negative Mood. These mechanisms are retained in the integrated branch. The
participant nominalisation statement that finite case valuation is inactive is
preserved: shared participant selection does not imply a finite case domain or
SpecIP in a nominal. The canonical new particle spelling is **kady**; the broad
lexical correction is inherited from PR16. No morphology or case
paradigm has been altered by this ledger.

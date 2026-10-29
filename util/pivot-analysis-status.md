# Pivot revision: structural baseline and decision record

This file records the implementation and review snapshots. Publication was
authorised after the second review; references below to uncommitted or
unpublished work describe its state at the relevant review stage. Commit, PR
and merge evidence is reported separately after publication verification.

Baseline: fresh remote `master`, 16329d482d621e09492badeaa654651975735a18,
29 October 2026. Brief: Library `libfile_30d5b0888420819184233f611f04d2cd`,
Pasted text(20261029-135417).txt, 72,160 bytes, all 632 extracted lines read
in contiguous paginated windows 1–90, 91–180, 181–265, 266–350, 351–435,
436–520, 521–585, 586–632. This record does not claim native-speaker elicitation.

## Integrated architecture

The branch is now based on actual PR16 merge `87c23bbcb8ea59f62e415cb315a45f79613e1dc6` (reviewed source
`e5565a3c5eefbfc03db9e5d916b29b44f3b908ab`). PR15 is included in that
history. A complete pre-integration source snapshot is preserved outside the
repository at `/workspace/pivot-pre-merge-updated.tar.gz`; no implementation
commit was needed to preserve the uncommitted work.

The actual merged patch supplies AspP versus descriptive Comm-field,
predicate-domain terminology, lower polarity licensed by negative Mood,
bounded exclusive composition and reduced AspP selection. Its topic-variable/
lower-copy convention, SpecAspP existential pivot, inactive finite case
valuation in participant nominals and canonical `kady` are preserved.
Three textual conflicts were reconciled explicitly: the Chapter 3 preverbal
table retains both the corrected Comm-field and the pivot/wh placement limits;
the bibliography keeps PR16's Cinque/Erlewine entries and the new source union;
the metahistory retains both dated research records.

## Inventory and construction types

| Layer, inner to outer | Content and evidence | Positional status |
|---|---|---|
| Root VP | Patient complement of lexical predicate; head-final | Thematic A-position; P before V does not entail P before actor |
| Appl / inner AP Voice | Event-related participant / suppression of lexical patient; mutually excluded in one base | Argument-introducing A-position; no productive simultaneous Appl+AP |
| Actor layer | Actor of lexical event, above event-related Appl | Thematic A-position; label not itself evidence for a phase |
| Caus | Causing event and causer; retains independently licensed base participants | Causer thematic A-position; accessibility must be specified independently |
| Outer orientation Voice | Selection in completed derived predicate; above Caus, below Asp.Align | Selection is not by itself displacement |
| Aspect / Asp.Align | Viewpoint and alignment domain | Independently projected lower competitor for placement; PF portmanteau not syntactic trigger |
| Neg | Single indicative negation, predicate-sensitive PF exponent | Operator domain; zad- is contextual existential suppletion |
| Phas | Positive or negative predication selected by vy/so | Operator domain; no agreement/argument site follows from phasal meaning |
| Comm-field | Additive/exclusive/affirmative/interim operators | Descriptive heterogeneous region, not a single established head or another lexical Asp.Align |
| Mood and inner Evid; abbreviated IP | Finite inflectional domain, including verbal -al/-l when present; no asserted person agreement or tense head | SpecIP candidate must identify an actual attracting head; the abbreviation is not a new projection |
| FocP | Marked focus dependency | A′-position; existing pre-by wh orders not derived by lower FocP alone |
| PolP | Head-initial by; interrogative typing | Head precedes complement; no arbitrary inversion repair |
| TopP | Independently licensed high aboutness topic, retained argument case | Linked A′-position; hanging topics are external frames |
| EvidP / SpeechActP | Evidential/epistemic and illocutionary framing | Upper operator specifiers |

These are dominance definitions, not a list of invariably overt heads or an
algorithm for every surface string. Ordinary finite verbal clauses have a full
inflectional field; zero-copula EquP lacks verbal aspect. Bare/presentational
existentials have a low aspectual pivot; PP-initial possession retains it in
ExistP. Reduced -ový clauses and -ou participant nominals project their
selected embedded predicate, without automatically adding finite I. Diagrams
showing only Exist/Asp/Neg are partial constituents, not competing full spines.

## Three placement implementations

A. SpecIP movement is the leading finite-clause hypothesis: lower argument
selection makes an independently described participant available, then an
independently identified head within the inflectional field has a separate
displacement requirement. Because IP abbreviates Mood and inner Evid, the
notation does not supply an additional I head. The proposed probe cannot
simply search for `[pivot]`, defined as the DP that moved. Candidate feature implementations must derive eligibility
from role, orientation and aspect; all interveners must be checked.

B. A specifier of the independently needed aspect/orientation domain is a
serious competitor. Its actual height must be stated: a low site below the
comment/phasal field predicts different pivot/operator order from SpecIP.
Relabelling a high site “Asp” without changing its predictions is no competitor.

C. Base/restructuring control: patient stays lexically low, and an independently
justified predicate or remnant configuration derives its pronounced precedence.
A high-base patient would lose the ordinary actor-over-patient binding relation;
a low-base remnant account must specify its extra steps and scope consequences.
Neither may be rejected merely because A seems familiar.

Agree is distinct from Internal Merge. A probe may interact with a DP without
moving it. A nonmatching actor may fail to satisfy a role-sensitive probe, but
that condition does not open a completed phase. A selected embedded theme needs
an accessible edge at every opaque boundary or an independently justified
transparent/restructuring domain. No current canonical example chooses between
those locality architectures. These conditions are hypotheses to test, not a
new universal Iridian `[pivot]` mechanism.

## Ten acceptance criteria

| Required criterion | Current result |
|---|---|
| Derive canonical neutral orders | A/B can schematise finite order; C needs independent restructuring. No unique site established |
| Preserve case/orientation | Existing paradigms retained; conditional case implementations compared on same frames |
| Non-circular attracting feature | Role/aspect/orientation eligibility identified; syntactic transmission not established |
| Causative intervention and phase access | Nominal matching separated from phase access; transparent/edge alternatives remain open |
| Preserve reflexive binding | Lower actor–patient connectivity required; pre-movement licensing vs copy interpretation undetermined |
| Predict operator/adverb positions | Controlled diagnostics supplied; existing particle hierarchy alone does not fix pivot height |
| Scope independent of PF order | Concord and bounded exclusivity retained; no unrestricted reconstruction rule |
| Preserve agent Top/wh | Construction-specific table; no general syntactic ergativity inferred |
| Distinguish reduced/existential | Lower existential and nonfinite selection retained; no universal finite I |
| Justify every added operation | No PivotP or forced new projection; remnant/edge alternatives expressly conditional |

These are necessary conditions, not scores. Present evidence is insufficient
for a definitive landing-site choice. New constructed specifications must not
be counted as independent confirmation of the analysis they instantiate.

## Completion and validation record

Implemented the evidence-preserving revision in Chapters 1 and 3–9, with five
main argument-structure schemata, ten construction-frame obligations and a
construction-specific extraction table. The full corpus contains exactly 72
records: 12 order/aspect, 12 binding/pronouns, 12 modifiers/scope, 16 derived
predicates, 12 information/extraction and 8 existential/reduced. Status counts:
43 canonical starting examples/constructions, 28 hypothetical schemata and one
proposed lexical test; new contrasts within canonical records remain unjudged.

Fresh independent review read all records, chapter diffs and executable models.
Five findings were fixed and independently rechecked: bibliography TeX group,
Agree licensing geometry, a reflexive test index, the overt-directive order
control and categorical wh landing-site statements. A separately noticed
directive model defect was also fixed with explicit external licensing.
See `pivot-independent-review.md`; no blocking issue remains within this
branch's independent scope.

Final `make check-source` passed: 17 source files, 461 labels, 737 references,
79 citations, 320 interlinear alignments, 15 valency paradigms and all morphology,
quantity, pronunciation and phasal regressions; 97 unit tests passed. Twelve
new model tests cover 23 literal case frames, false shortcuts, chain identity,
phase-access controls and finite scope countermodels. `git diff --check` passed.
A balanced bibliography group was independently checked. PDF build/render
validation was intentionally omitted under the standing instruction.

This was the initial validation on `revision/pivot-syntax-evidence`. The current
integration branch is `revision/pivot-syntax-integrated`, based on actual PR16
master. No commit, push, PR, merge or publication of the broad pivot work has
been performed. Final integrated review and test results are recorded below.

The outstanding theory choices are substantive, not implementation failures:
feature transmission, selected-goal intervention, causative phase accessibility,
several new judgments and the pre-by derivation do not yet select a unique
landing site. No missing judgment is silently supplied to force one.

## Second review and actual PR16 integration

Reviewed base: `87c23bbcb8ea59f62e415cb315a45f79613e1dc6`, the verified remote
master merge of PR16, containing PR15 and source commit
`e5565a3c5eefbfc03db9e5d916b29b44f3b908ab`. The current branch is
`revision/pivot-syntax-integrated`; the broad pivot work remains entirely
uncommitted and unpublished. The actual remote patch, not its summary, was
compared against every overlapping chapter and helper boundary.

Fresh independent corpus and theory reviewers found and rechecked three
additional issues: S06 varied discourse context as well as temporal-frame
position; B11 lacked an explicit nonfinite/silent-controller partner; the main
case discussion unnecessarily required pre-displacement computation instead of
allowing a specified lower occurrence/cycle. These are fixed without inventing
new accepted judgments. IP definitions now consistently include Mood and inner
Evid when present; the SpecIP hypothesis must still identify an actual attracting
head. See `pivot-integration-corpus-review.md` and
`pivot-integration-theory-review.md` for independent evidence and limits.

The three merge conflicts were resolved by retaining both intentions:

- Chapter 3 table: retain PR16's descriptive Comm-field, alongside the finite
  wh/pre-by limit and construction-dependent lower argument positions.
- Bibliography: retain PR16's Cinque metadata and Erlewine source, add the pivot
  references by key, preserve all original entries and the closing TeX group.
- Metahistory: retain both dated research records, then record actual integration
  rather than continuing to call the architecture work unpublished.

No existing clausal, phasal, morphology or epistemic helper/test was replaced.
The new pivot model remains a bounded comparison using explicitly supplied
selection, domain exclusions and accessibility; it is not a general parser or
a solved syntax. Canonical `kady`, its pronunciation and obsolete-spelling
rejections are inherited unchanged. SpecAspP existential pivots, the
variable/lower-copy convention for topics, bounded exclusive composition,
negative-Mood lower polarity licensing and inactive finite case valuation in
participant nominals all survive integration.

Final combined `make check-source` passed: 17 files, 464 labels, 746 references,
82 citations, 320 interlinear alignments and 15 valency paradigms, with all
boundary/evidential/quantity/pronunciation/contemplative/phasal regressions.
All **104 unit tests pass**, including the 12 pivot methods on 23 literal frames
and the merged clausal/phasal tests. Both reviewers independently passed the
24 clausal/phasal/pivot methods. All 72 corpus records, six category counts,
evidence-status labels and cited source labels remain valid. Bibliography group
balance, no conflict markers and `git diff --check` pass. PDF generation and
validation remain intentionally omitted.

No theoretical choice is manufactured by this integration: the attracting
feature/head, causative edge or restructuring architecture, some binding/scope
judgments and complete pre-by derivation remain genuinely unresolved. The
integrated implementation has no outstanding textual conflict or test failure;
those research limits are distinct from integration defects.

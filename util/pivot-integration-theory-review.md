# Second independent theory and correctness review

Reviewer: fresh agent not involved in authoring the broad revision. Initial
review on 29 October 2026 against `16329d4`; actual merged architecture review
is a separate stage and is not claimed complete below.

## Scope inspected independently

Read the chapter diffs for Chapters 1 and 3–9; the full case, derivation,
binding/scope and source-audit ledgers; executable case/locality/scope helper,
23 literal case fixtures and all 12 dedicated test methods. Checked relevant
canonical aspect, causative, directive, reflexive, reduced and existential
prose rather than relying on the earlier independent-review summary.

Independently opened the primary Clem 2024 joint-work handout, Fox 1999 article
and Jou 2026 article. Their actual stated scope matches the cautious source
audit: Shawi's mechanism depends on local feature transfer and person hierarchy;
Fox distinguishes A and A′ chains; Jou's cross-phase dependent-case evaluation
is expressly a loosened locality assumption. None supplies Iridian judgments.
The inaccessible monographs and final articles remain marked as such in the
research audit. No new claim of having read them is made by this review.

## Finding

**P2: avoid making pre-displacement case timing compulsory.** In Chapter 3
`sec:vm-selection-domains`, “A configurational implementation must ... evaluate
their relation before any ordinary finite displacement obscures it” can be read
as prematurely requiring early case computation. The case ledger correctly
allows an appropriate licensing occurrence/cycle. A later computation sensitive
to the lower chain occurrence should not be excluded merely by pronunciation
of a higher copy. Recommended wording: specify the licensing occurrence and
evaluation cycle; pronounced order alone cannot determine case. The executable
model can remain a deliberately pre-displacement candidate with supplied
selection/exclusions. Status: fixed and rechecked after integration. Chapter 3 now explicitly
allows a lower licensing occurrence/cycle, while the executable candidate
remains honestly limited to its supplied pre-displacement inputs.

## Substantive result before architecture integration

The role inventories and case frames preserve retained theme > applied
participant > causee in the outer perfective causative domain. A theme-like
sole argument is not double-counted as a separate retained patient. Simple
applicative selection is not inherited above Caus. Active NOM, NOM passive,
ERG and directive external licensing remain distinct. The explicit overt
contrastive directive actor precedes its direct theme, preventing accidental
extension of ordinary indicative pivot-first to every directive.

The two executable case candidates are intentionally conditionally equivalent
on the canonical frame inventory: both receive selection and residual IND
exclusions as supplied assumptions. This is not an implementation of the
still-open feature transmission mechanism. The configurational candidate
makes a different counterfactual prediction when all residual DPs compete;
the Agree candidate instead rejects its two-goal domain violation. Those
results compare specified algorithms, not evidence that Iridian has empirically
observed agreement. Documentation states that limitation clearly.

Phase accessibility is separated from nominal matching. Exported edges and
opaque boundaries are explicit model inputs; the helper does not invent an
edge licence. Canonical selected-theme order is not presented as a derivation
through transferred material. The conditional causative paths remain research
obligations. SpecIP, an independently identified lower site and restructuring
are maintained as serious alternatives; no primitive PivotP or circular
syntactic `[pivot]` feature is selected as the solution.

The reflexive retains current `védnik` quantity. Actor-over-patient thematic
connectivity is distinguished from lower-copy interpretation and obligatory
reconstruction. Passive, causer/causee, nominal and nonfinite antecedent
conditions are not silently supplied by the new schemata. Negative-concord
interpretation and local licensing are independent of raising; the finite
scope controls distinguish ¬∃ from ∃¬ and distributed from shared witnesses.
The bounded exclusive/phasal mechanism is retained rather than becoming free
scope permutation.

Reduced -ou nominal and -ový relative selection is kept distinct from finite
case and finite wh extraction. No universal finite I-landing position is imposed
on reduced/existential constructions. Linked DIR/TRS topics retain their own
A′ dependency; inaccessible reduced participants do not create a general
syntactic-ergativity claim. The four-way wh/by paradigm is preserved, with the
pre-by site explicitly unresolved rather than repaired by arbitrary movement.

## Required combined-patch checks

The imminent architecture merge must be examined as an actual diff. In
particular, reconcile the baseline CommP labels with the merged actual-AspP/
descriptive comment-field terminology; preserve negative-Mood composition,
bounded focus association, low existential SpecAspP, linked topic variable/copy
analysis and inactive finite case valuation under participant nominalisation.
The still-pending integration ledgers cannot stand as claims about the final
combined tree. `kady` must be canonical throughout current grammar and fixtures,
without damaging unrelated `-eškady`. Run the source/interlinear/morphology
regressions and the dedicated models again after reconciliation. No PDF build
is part of this review.

## Actual merged-architecture recheck

Reviewed the actual merged base `87c23bbcb8ea59f62e415cb315a45f79613e1dc6`
(PR16, descendant of already-merged PR15) on branch
`revision/pivot-syntax-integrated`. This is an actual-source review of the
combined working tree, not an inferred integration from the prior task summary.
Read the new Chapter 1 spine, Chapter 6 negative-Mood and focus calculus,
reduced-clause boundaries, and `clausal_diagnostics.py` plus its tests alongside
the broad revision's helper, fixture and test boundary.

The architecture retains one actual AspP below indicative Neg/Phas and treats
the Comm-field as descriptive, not a second lexical aspect head. The broad
lower-site candidate now refers to an independently identified aspect/orientation
position and does not reintroduce CommP. The existing low existential SpecAspP
survives. Parent is harmonising the short IP definitions with the explicit
Mood-plus-inner-evidential inventory; no theory choice can be inferred from
those editorial abbreviations.

Negative Mood licenses the lower negative proposition under Phas while its
clause-type contribution remains outside: the broad concord/scope discussion
does not introduce indicative NegP or duplicate negation. The ordinary and
bounded lower exclusive readings retain a fixed associate and alternatives;
topical association binds the lower variable (or appropriate interpreted copy),
without lowering the pronounced topic wholesale. The broad reconstruction
limits do not contradict that construction-specific mechanism.

Reduced -ou and -ový selection remains separately headed, and the selected
AspP excludes internal OpNeg/NegP, Phas, comment operators, Mood and both
clausal evidential layers. Matrix operators may take external scope without
entering that selected subtree. Participant nominal case is still supplied
by the nominal domain with finite case valuation inactive. The pivot case helper
has no reduced-case mechanism; the clausal reduced helper checks selection
boundaries rather than case or a complete derivation. Their limits are explicit
and compatible, so passing both is not presented as proof of complete syntax.

The source's current particle is kady; obsolete spellings are confined to
historical/status records being updated by the integrator. The unrelated
-eškady is not changed. No morphology/case-frame modification was found in
the broad additions after reconciliation. All 24 dedicated clausal, phasal and
pivot diagnostic test methods passed independently in the combined tree;
`git diff --check` passed. Full source/regression verification belongs to the
integrator's final run; no PDF build was performed.

No blocking academic or correctness mismatch remains in the inspected combined
implementation. The outstanding landing-site, feature-transmission,
causative-edge, antecedent and pre-by questions remain genuine unresolved
analysis choices, not falsely certified by the toy helpers or constructed
corpus. Integration status/history text must identify the actual merged base
rather than continuing to say the architecture patch is unpublished.

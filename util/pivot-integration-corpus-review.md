# Second independent corpus and prediction review

Reviewed 29 October 2026 on the uncommitted pivot revision based on
`16329d482d621e09492badeaa654651975735a18`. This reviewer did not author the
corpus, model, fixtures or chapter additions. This is a fresh reading of all
72 records and their predictions, not a restatement of the first review.
Integration with the newly merging architecture patch remains to be checked.

## Findings for the integrator

1. **P2 — S06 confounds discourse and position.** Its string pair contrasts
   `bych P A V` and `P bych A V`, while its context contrasts a neutral temporal
   frame with contrastively discussed yesterday. A positional diagnostic for
   landing-site height should hold discourse status fixed. Use the same neutral
   temporal-frame context in both orders; test contrastive fronting separately,
   explicitly as a discourse-conditioned comparison. Otherwise either movement
   candidate can explain a difference by the changed discourse operation rather
   than pivot height. Status: reported; correction pending integration.
2. **P2 — Nonfinite controlled binding is missing from the fixed corpus.**
   B11 is a finite complement and B12 contrasts nominal/reduced-relative
   domains; neither explicitly tests a nonfinite verbal complement with a
   controlled silent local actor. The brief separately requires that contrast.
   Extend B11 with a paired nonfinite schema keeping the two salient actors
   and an explicit candidate silent local actor/controller relation, or add it
   as a separately labelled subcondition of B12. This must remain H: the
   independent licensing of the complement, silent argument and controller
   cannot be supplied simply to rescue an anaphor. The associated binding
   research record already describes the correct methodological obligation,
   but it has not entered the 72-record test set. Status: reported; correction
   pending integration.

## Substantive audit

- All 72 records were read, with exact category counts 12 order, 12 binding,
  12 scope, 16 derived predicates, 12 information/extraction and 8 reduced/
  existential. Status counts are 43 C, 28 H and 1 P. C is expressly restricted
  to the starting canonical construction/example; a new contrast or discourse
  control is not presented as inherited empirical evidence. The corpus does
  not invent speakers or treat constructed judgments as independent proof.
- Canonical lexical spot checks against the chapter sources include O01–O05,
  B01–B02, V07–V13 and I10/E04. The current quantities `védnik`, `piaštník`,
  `zemácime`, `zemácek`, `ščénime`, `ščének`, `svórnime`, `svórnik`,
  `zemacébrime` and the participant nominal forms are preserved. The phrase
  `Svem Marku védnik` is not the stale brief form `vednik`.
- B09's lower antecedent now consistently bears index i; B07/B08 vary the
  causee/causer antecedent while keeping roles explicit. B05 does not invent
  a silent passive binder. B10 distinguishes a preserved local relation from
  the high discourse position itself licensing anaphora. None of these tests
  establishes obligatory reconstruction or a unique finite landing site.
- O11 now uses the canonical contrastive overt directive actor-before-theme
  control, explicitly barring an ordinary indicative pivot-first inference.
  V06 preserves Mood's retained-theme priority over the applied beneficiary.
  V10/V12/V13 keep retained-theme > applied > causee selection in the correct
  completed causative domain; the intransitive sole participant is not counted
  as a second retained theme. V16 distinguishes causing-event from caused-event
  benefaction without adding another productive Appl.
- S01/S03 correctly decline to infer overt pivot height from an actorless
  string. S05 treats event frequency separately from manner; S07/S08 state
  genuinely conditional operator-height consequences. S09 preserves concord
  interpretation independently of raising. S10/S11 compare shared and
  distributed witnesses without claiming that either reading has been
  established. S12 retains bounded exclusive/phasal composition, rather than
  an unrestricted scope-swapping rule.
- I01/I08 correctly preserve finite TRS-agent topicalisation/wh access,
  independently of reduced construction restrictions. I05/I07 retain both
  pre-by surface patterns and decline to hide a derivational repair in the
  pivot mechanism. I09/I10/E05 distinguish reduced -ový selection from -ou
  nominalisation and do not import finite I. E01/E03 preserve lower existential
  pivot positions and PP-initial possession; neither direct case nor shared
  selection entails a universal pronounced landing site.
- The A/B/C₀ comparison remains underdetermined. Many records constrain every
  candidate rather than discriminating them. This is appropriate coverage,
  but the number of records must not be reported as the number of confirmed
  empirical tests favouring A. A still needs an independently specified
  eligibility/transmission mechanism and actual causative phase access; B
  still needs an independently fixed height, and C₀ still needs a derivation
  preserving lower binding connectivity.

## Model and verification

The reviewer read `scripts/pivot_diagnostics.py`, all literal fixtures and the
12 model test methods. Both case candidates receive selection and residual
licensing exclusions as inputs; neither claims to derive them. The 23 fixtures
include overt directive external licensing separately from ERG dependent case.
Reversed ERG licensing geometry is rejected by both models. The all-DP control
explicitly overmarks causees/applied participants, and the copy controls preserve
chain identity. The phase-access controls do not confuse nonmatching DPs with
an accessible edge. Scope truth models distinguish ∃∀ from ∀∃ and ¬∃ from ∃¬;
they do not certify availability of either reading in Iridian.

Independent execution: all 12 model tests pass. A record/field audit confirms
72 unique records, required fields and no missing cited source labels. These
checks supplement semantic reading; they do not establish new judgments.

## Required post-merge check

Re-read the actual merged chapter hierarchy, negative-Mood licensing, comment
field/AspP distinction, bounded focus composition, reduced selection and `kady`
correction. Update the corpus's historical integration language only after the
actual patch is incorporated. Preserve the topic-variable/copy account and
inactive finite case valuation in participant nominals. No post-merge review is
claimed in this initial record.

## Final review on the actual merged architecture base

The branch `revision/pivot-syntax-integrated` now has actual merged base
`87c23bbcb8ea59f62e415cb315a45f79613e1dc6` (PR16, clausal architecture and
`kady`). The reviewer reread the corpus against that source, rather than
accepting a summary of the former unpublished patch.

Both initial P2 findings are resolved. S06 now keeps the temporal frame,
prosody and discourse context constant while varying order, reserving contrastive
fronting for a separate context pair. B11 now adds an explicit hypothetical
nonfinite partner with a candidate silent local actor and controller; its
licensing and reflexive realisation remain expressly unestablished. No control
relation is manufactured as canonical evidence.

The actual source now distinguishes lexical/orientation AspP from the
descriptive Comm-field and defines the latter as heterogeneous rather than a
single head. The corpus's A/B predictions remain conditional on the relevant
operator's independently fixed position; they do not reintroduce CommP as a
syntactic head. The ordinary finite pivot hypothesis does not overwrite the
merged SpecAspP existential analysis. Linked topics remain a separate A′
dependency, so a selected patient is not assigned aboutness topichood merely
by first position.

The merged negative-Mood account supplies lower negative interpretation below
Phas and the higher Mood's concord licence. Corpus S09 continues to concern
negative concord independently of raising; it adds no indicative Neg head to
a negative-Mood clause. S12's bounded exclusive/phasal comparison contains no
intervening Mood or clausal evidentiality and does not license arbitrary
operator lowering. Its schematic contrast is therefore compatible with the
merged, more explicit fixed-associate composition.

I09/I10/E05/E08 preserve the actual reduced selection of AspP, excluding Neg,
Phas, the Comm-field, Mood and clausal evidentiality internally. Neither -ou
nor -ový is treated as requiring finite I. Indirect dependents are still
licensed in the nominal/reduced domain; participant selection does not
reactivate finite case valuation. The same abstracted participant does not
turn the relative and participant nominal into one construction.

Useful combined-boundary checks were executed independently: all **24**
diagnostic tests pass (6 clausal, 6 phasal, 12 pivot). The 72 unique records
and required six category counts remain intact; every cited source label
resolves. No obsolete standalone `kday` or `ktady` occurs in the corpus or
pivot/phasal helpers. `git diff --check` passes. No PDF build was performed.

The reviewer also reported four historical integration-status statements in
the corpus for the integrator's documentation update (header, introductory
operator-field note, S07 and closing paragraph). These are documentation
staleness, not an unresolved architecture conflict. No new substantive blocker
was found in the integrated corpus/prediction scope. The unestablished
judgments, feature-transmission/locality mechanism, final landing site and
pre-by derivation remain research limits, not review failures.

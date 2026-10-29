# Stative reform: integration and independent review

Implemented locally on branch `stative-reform` in `/workspace/iridian-reference-grammar`.
Base: remote master `b6c87551397faa5d661e2690b2ee72745d7bae40` (PR #18), including the
reduced-relative suffix typesetting correction. No commit, push, PR, merge or PDF
build was performed for this reform.

## Decisions and scope

- Adopted StateP versus overt BecomeP below established valency, orientation and
  Asp.Align; ResP records independently licensed event-derived state entailments,
  without a universal new suffix or an untested target/resultant taxonomy.
- Adopted `-él-` after a short unprotected state and `-el-` with protected input
  quantity. The resulting local stem selects short outer endings. Dynamic free
  perfective is `-ek`, with ordinary bound `-ik-` before nominal/relative/linker
  morphology. This corrects the brief's experimental `-ik` free forms.
- Beauty root is `muž-`, stative `mužn-`, strong `múžn-`: state `mužna`,
  stage-level progressive `múžnime`, bounded state `múžnik`, inchoative
  `mužnéla / mužnélime / mužnélek`, bound `mužnélikou / mužnélikový`,
  linked `mužnélice`, manner `mužňe`, emphatic `mužňeská` and intensive
  `múž-`. Existing phonotactics licenses ž+n; no novel repair was introduced.
- Finite Class A principal parts are explicitly assigned to the seven short
  representative stems, separately from attributive class. Protected `tvírzn-`
  remains Class C; short relational suffix-strong stems retain their distinct
  class. Existing `četná` is recognised, rather than treated as unlisted.
- Simple progressive/perfective no longer necessarily eventivise a state.
  Their marked contextual licences are explicit; retrospective remains anterior
  state and contemplative remains projective. Lexical existential acquisition
  readings remain separately identified rather than deleted.
- Ordinary attribution retains its lexical classes. Continuous state `-ový`
  requires an explicit episodic/stage/temporal/contrastive context and holder
  abstraction under established participant selection. Neg, Phas, Comm, Mood
  and Evid remain excluded inside reduced descriptions. Participant `-ou` does
  not automatically denote a state, transition event or event result.
- Psychological perspective is selective and source-sensitive, not first-person
  only or obligatory evidentiality on every property predicate.
- State causatives retain expanded `-ér-/-er-`; liquid-final Become takes ordinary
  compact `-r-`, preserving quantity and outer `-an-` orientation. Sixteen
  causative paradigms are conditional on independently licensed causable meanings.
- Five scalar meanings use three morphological stems plus explicit semantic
  standards. No five-way overt exponent contrast is claimed. A comparative
  target introduced with `stá` is distinguished from mere increase relative
  to an individual's earlier degree; ongoing change does not entail attainment.

## Parallel work and fresh review

Three agents separately implemented Chapter 3, primary-source research, and
literal paradigms/diagnostics. Three different agents independently reviewed
PF/morphology, syntax/consistency, and academic/corpus claims. Findings fixed
and rechecked included:

1. Chapter 6 still expressed comparative becoming with simple `čétnime/čétnik`;
   these are now `četnélime/četnélek`, with inchoative glosses.
2. `četná` already established a suffix-strong attributive class.
3. Psychological evidence prose accidentally sounded obligatory; it is now
   conditional and consistent with a source-sensitive preference.
4. General perfective prose excluded bounded states by saying only event.
5. Smith et al.'s claim was too broad; it now specifically describes resistance
   to rate-adverb-triggered inchoative readings.
6. Prototype fixtures still marked combined Become+Caus as contingent; they now
   include ordinary compact derivations, conditional on semantic selection.
7. Property Class A short `-ik` and relational suffix-strong `-ík` are distinguished.

Final independent reviews found no remaining essential PF, syntax or academic
blocker. Reviews are of the explicit constructed specification, not native
speaker validation.

## Evidence

`make check-source` passed after integration: **122 tests** (104 original plus
18 new), 18 active source files, 467 labels, 753 references, 87 citations,
314 interlinear alignments, 15 existing valency paradigms, 80 stative aspect
cells and 16 conditional stative causative paradigms. Existing quantity,
boundary, evidential, case/pivot, phasal and shallow-heading checks remain
passing. `git diff --check` passed. No old beauty spellings remain in active
chapters or the curated lexicon. Historical `archive/` and `util/stub/` were
not edited; the obsolete-output detector deliberately retains `mrocně` as a
rejected regression spelling. The phasal diagram was not edited.

The source audit verifies eight primary references, distinguishes full text
from abstract/metadata access, corrects Sakaba to 2026 and records Sato/Cho's
online 2023 versus book 2024 dates. See `stative-source-audit.md` for details.

The full 302-line, 30,633-byte Library brief was read through the supported
Library read route. Optional local-byte materialisation of
`libfile_735673b884a8819195fe50a0b861c98b` failed in the supported transfer helper
with `library file transfer failed: download failed`; it was not retried or
replaced with a guessed URL. Complete readable source text supported the work,
so this transfer failure leaves no implementation blocker.

## Deliberately unadopted

Simple attributive grades for `ptakn-/všihn-/hvodn-`, a third attributive grade,
fabricated irregular histories, expanded analytic `neh-` selection, a dedicated
threshold exponent, and a universal Res exponent remain unspecified. The
paradigms report these limits rather than inventing forms. The diagnostics do
not claim a complete non-indicative analyser or automatic phonetic renderer.

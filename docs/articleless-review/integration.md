# Independent integration review: articleless reference

Reviewed reconstructed working tree against master `2ea86f3046beff0d55ee9f7f7e0f06bb31932e26` on 8 November 2026. This reviewer did not implement the grammar, migration fixtures or guards. Review was read-only; only this report was written.

## Outcome

No supported remaining grammatical integration defect was found in the inspected sources. Two regression-coverage gaps were independently reproduced, referred to the regression implementer, fixed and rechecked. Source readiness does not replace the lead's full-build and rendered-PDF acceptance.

## Resolved findings

1. **Raw anchoring heads/features escaped the new guard.** At `scripts/articleless_diagnostics.py:127`, the initial patterns rejected `AnchP` and `\\synhead{Anch}` but accepted `Anch\\textsuperscript{0}`, mathematical `Anch^0` / `Anch^{0}`, and `[\\pm\\mathrm{anch}]` / `[\\pm\\mathrm{shr}]`. Each was independently appended through an in-memory source override to the actively included `util/event-existential-comparison.tex`; initially no failure resulted. The expanded patterns and consolidated mutation tests now reject all five. No source-file exception was added. The active grammar contained none of these stale analyses; this was a regression gap.
2. **Cell comparison ignored lexical spaces.** The original `canonical_cell` removed all whitespace, allowing `\\ird{byl}` to change to `\\ird{by l}` without a paradigm failure. This was independently reproduced in `nm-plural-paradigm.tex`. At `scripts/articleless_diagnostics.py:93`, comparison now preserves cell contents after trimming outer formatting; the internal-space mutation is rejected and is covered in `util/tests/test_articleless_diagnostics.py:26`. Current production cells were already unchanged.
3. A newly added scope-mutation test initially made no change to the interlinear-only `Ščénikovy byl jeca` passage because it contained no `\\ird` macro. The fallback now mutates `ovy`, and the focused suite passes. This did not affect production semantics.

## Cross-file integration

- Followed the literal publication graph from `grammar.tex`, including style sources, every chapter, consolidated paradigms, the phasal diagram and `util/event-existential-comparison.tex`: **38 source files**. An independent label/reference sweep found **720 unique targets, 1,403 reference uses, zero unresolved targets and no duplicate nominal labels**. This static sweep is supplementary to LaTeX validation.
- Read the reconstructed Chapter 5, its nominal trees and semantic composition in full; checked against Chapter 4's nine-class descriptions, the shared tables and Appendix A. NP/PossP/NumP/KP/quantificational material/DemP are retained; DP is consistently an extended-nominal cover term, including predicative and pronominal uses, without entailing D or a silent article. No replacement marker was introduced.
- Checked the ordinary-case inventory across Classes I–IX, including Class V indirect `ráne`, Class II/VII citation versus bound grades, thematic Class VIII vowels, kinship vocatives and irregular `tóm`/`študent` quantities. The migration record's Class VII mapping is correctly `tězno / oblo → tězėň / obėl`; no erroneous long-vowel illustrative forms remain there. The exact 102-cell baseline is independently frozen and the focused tests exercise its mutations; the separate morphology reviewer independently parsed original master tables.
- Read affected Chapter 10 classification, identity and existential composition; checked their property/individual distinction against Chapter 5's existential composition, contextual uniqueness, assignments and cardinal semantics. Definiteness remains contextual/constructional and is neither direct case nor a topic requirement. The previously corrected initial-position/topicality paragraph and broadened DP definition are consistent with the rest of the architecture.
- Checked retained deverbal participant/event singulars, continuous `pjaštova` direct-only gap, finite/nominal case distinction, embedded event actuality and the related Ch08/10/16 passages. Ordinary `-ovy` nominal transitive material remains distinct from the protected relative exponent.
- Inspected the introductory profile and affected phonology, morphophonology, verbal, argument-structure, negation and clause-linking diffs for changes beyond anchoring dependencies. Reviewed unglossed examples and lexical-entry edits, including `Nuž`, `Byl`, `Veň`, `Marėk`, ordinary bread forms and independently documented `vlak`. No deletion of unrelated case/quantity or extension of a new lexical stem was found.
- Checked the controlled `Byl zdrávime` contexts and Chapter 17's introduction, bare resumption, licensed null continuation, competing antecedents and reactivation against Chapter 14's independent topic/pivot distinction. None makes lack of morphology obligatorily indefinite or licenses a categorical new anaphoric hierarchy.
- Reviewed remaining active matches for anchoring, definiteness and determiners in context. Temporal/Mood anchoring, phonological/TikZ anchors, negative indefinites and explicitly historical prose are independently motivated, not productive nominal anchoring. Schematic phonological `si/ši` remains the single exact exception rather than a retained proclitic.
- The final historical fixture covers **eleven** records, including `clause-linking-reform.md`. Historical bodies are retained below status preambles; historical material has not been repurposed as the current norm.

## Protection against weakening existing relative tests

Reviewed `scripts/check-grammar.py` changes: they add `check_articleless` to the existing checks without removing earlier checks. Reviewed the narrow adapter at `scripts/stative_scope_guard.py:214` and fixture `scripts/articleless-scope-migrations.json`.

For all **13 literal source-specific migrations**, independently verified that:

- each original passage occurs exactly once in pristine base `2ea86f3`;
- each revised passage occurs exactly once in its current named source;
- each original SHA256 matches its recorded string;
- inserting an unapproved selection rule inside every revised passage produces a scope failure;
- the original `scripts/stative-scope-freeze.json` has no git diff.

The adapter does not rewrite production grammar, globally strip suffixes, regenerate old hashes or allow arbitrary edits inside protected spans. Scope checks also reject changed relative selection, changed nominal case rules, additional relatives and edits to the canonical equative treatment. Tests validate unrelated-path rejection and unchanged original freeze provenance.

## Executed verification

`python -m unittest util.tests.test_articleless_diagnostics util.tests.test_stative_scope_guard`

Final result: **21 tests passed**, 6.864 seconds. In addition, independent in-memory probes confirmed rejection of the five raw-head/feature forms, internal lexical whitespace and unapproved selection rules in all thirteen reviewed migration passages. No repository production sources were mutated by these probes.

## Limits

This pass concentrated on source integration and guard correctness. It did not independently reread every sentence of all seventeen chapters, verify every bibliography item, establish natural-language or Iridian acceptability judgements, or inspect the rendered PDF. Full `make check-source`, `make check`, final PDF rendering/inspection and recoverable artifact publication are owned by the lead/validation agents. Automated checks protect known invariants; they do not prove exhaustive linguistic correctness.

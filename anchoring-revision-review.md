# Anchoring revision: implementation and evidence record

The six priorities in the supplied review are implemented in order, with an implementation agent, a literature agent and an independent reviewer for each phase. Each phase is validated and committed before the next begins. The supplied review is a proposal to assess against current sources, not an independent source of Iridian acceptability judgements. Current chapter names supersede its older references. Unrelated nominalisation proposals are outside this revision.

## Phase 1 — Semantic contributions

Clarified the conventional contribution of each feature bundle separately from its exponent, uniqueness, existential import, semantic type and scope. Preserved situational shared reference, bare anaphora, group selection and generic preferences. The independent reviewer found no factual blocker.

Sources checked: Schwarz (2019), §§2.1, 2.3–2.4, in the supplied volume; Coppock and Beaver (2015), publisher full text pp.377–380, DOI https://doi.org/10.1007/s10988-015-9178-8. The latter distinguishes definiteness, determinacy and existence; its English uniqueness semantics is not imported as the lexical meaning of Iridian anchoring. Existing Kagan (2011) is retained for speaker identifiability.

Source-critical observation: the survey overview p.viii reverses the German/Akan family-dog preferences given by Schwarz p.23, example (22). The detailed chapter governs any use of that comparison. No categorical German-style weak/strong distribution is imposed on Iridian.

Baseline: `make check` passed all 179 tests; full PDF log had two existing overfull boxes, with none in the cover. Local instruction files are excluded through `.git/info/exclude`.

Phase 1 validation: `make check` passed (179 tests); log checks passed with the same two baseline overfull boxes. Visually inspected PDF pp.72–73 and bibliography p.330: table, prose and added entries are legible without clipping. `git diff --check` passed.

## Phase 2 — Indices and situations

Added an explicitly analytical, property-returning indexed restriction. Access to an index and satisfaction of its nominal description are separate conditions. Situation-derived shared access and bare anaphora remain possible; accommodation is not made automatic. Relational bridging does not identify the antecedent with its related referent, and a possessor index remains distinct from the possessed referent's index. Covariation requires variable assignments/situations plus binding or update; the static schema is not presented as a complete dynamic theory.

Literature review checked Schwarz §§2.3–2.4, pp.10–13, including examples (11)–(12), note 10 and p.23; no new bibliography entries were required. The Lithuanian chapter §4.3.2, pp.104–106, reverses bridging labels in its introductory sentence, while its following sentence and examples give weak part–whole and strong producer patterns; producer judgements also vary. Pico pp.153–155 separates discourse salience from identifiability without supplying a full semantic analysis. These comparisons do not establish new Iridian distributions. Independent review approved the schema and evidential limits.

Phase 2 validation: `make check` passed all 179 tests and both log checks, retaining only the two baseline overfull boxes. Visually inspected PDF pp.73–74, including the equation and subsection boundaries; no clipping or overlap. `git diff --check` passed.

## Phase 3 — Types and composition

Specified Anch as a property-to-property function for all bundles, with null identity, shared indexed restriction and a speaker-selected witness parameter. Plural individuals are included in the domain. Referential and existential operations are kept separate from Anch; an already generalised-quantifier-denoting QP is not an accepted input without an independently motivated lift. A well-typed universal application does not license every overt-anchor combination: singleton identity restriction differs from restriction to a contextually supplied set. Speaker selection under modal dependencies remains an interpretative question, not a fixed actual-world or wide-scope commitment.

The cardinal scheme distinguishes plural denotation from singular morphological exponence. Existing Martí (2020), full publisher PDF, p.15 equation (28) and note 16, pp.24–25 equations (41),(44), supports atom counting, plural closure and separate existential composition. No wholesale number-feature analysis is imported. Etxeberria and Giannakidou (2019), §§2.1 and3, pp.426–428,435–437, supplies the comparison with non-saturating domain restriction; it does not establish a second Iridian Anch entry or Greek syntax for Iridian. Existing Coppock and Beaver (2015) §1 supports delayed argumental shifts. Independent review found the types, plural distinction and evidential restrictions coherent.

Phase 3 validation: `make check` passed all 179 tests and full/cover log checks; only the two baseline overfull boxes remain. Visually inspected PDF pp.74–76 and bibliography p.332: formulae, continuation, tree and references are legible with no clipping. `git diff --check` passed.

## Phase 4 — Nominal category terminology

DP now explicitly covers the extended argumental nominal expression, AnchP its particular D-layer, and NP its lexical constituent. Replaced the plain existential pivot's contradictory bare-NP description with an unanchored lexical nominal containing silent Anch. Explained the abbreviated pivot diagrams without removing their valid inner NP/nP constituents. The postpositional minimum-structure caveat is preserved. DP category is not identified with type-e interpretation, existential force or silent iota. Incoming derivational/negative treatments and the complete existential treatment were audited; no argument-structure or morphology changes were needed. Independent review approved.

Survey guidance: Despić (2019), §§1 and3, argues for D-less articleless nominals and type shifts; Borik and Espinal (2019), §3.2, argues for Russian bare definite-kind DPs using syntactic diagnostics. Both chapters and publisher metadata were checked. These are competing analyses, not a universal null-D consensus, and neither is treated as proof of Iridian category.

Phase 4 validation: `make check` passed all 179 tests and both PDF log checks, retaining only the baseline two overfull boxes. Visually inspected PDF pp.71–72,187,334: category discussion, anchoring table, pivot list and bibliography are legible without overlap. `git diff --check` passed.

## Phase 5 — Controlled contrasts and descriptive limits

Added `anchoring-diagnostics.md` with the current same-predicate child anchoring paradigm, deictic controls, bare kind/generic controls, direct singular/plural beer paradigms, same-predicate implicit/overt possessors, and English-only bridging/scope/covariation prompts. It explicitly distinguishes verified forms from unresolved contextual acceptability and controls case syncretism, number, topic and interpretation separately. No new Iridian judgement is inferred from comparative literature.

Chapter 5 now separates kind reference from generic predication, retains the ordinary bare-generic preference without banning overtly retrieved kinds, distinguishes mass morphology from portion/variety interpretation, and separates implicit possessor resolution from reference to the possessed head. Double marking's contextual effects are not presented as obligatory encoded meanings. Institutional weak definites have separate diagnostics from Schwarz's weak-article definites, without excluding kind-based analyses of institutional readings.

Sources checked: Williams (2019), §§1–2,4.1, pp.320–323,332, with terminology warning in note1; Despić and Borik/Espinal on kind analyses; Schwarz §5.2,pp.28–31,table3 on relational/functional nouns; Etxeberria/Giannakidou §§4.1–4.2,pp.438–443 on repeated marking with distinct functions. The survey's experimental Chapter11, §§4.6–5,pp.367–369, reports task differences between weak definites and generics but explicitly does not exclude all kind-based analyses; no unnecessary experimental claim or extra bibliography entry was added. Independent review approved after correcting the repeated-definiteness locator.

Phase 5 validation: `make check` passed all 179 tests and both log checks; only the two baseline overfull boxes remain. Visually inspected PDF pp.74,82,91,334: kind/mass discussion, double marking, implicit-possession continuation and references have no clipping or overlap. All diagnostic forms, glosses, direct-case syncretism and judgement status were independently reviewed. `git diff --check` passed.

## Phase 6 — Morphology and final consistency audit

Added `anchoring-morphology-audit.md`, with reproducible baseline comparisons and paradigm/domain controls. Chapters 4 and8 remain byte-identical to `c0b0410`; all existing Chapter5 gloss blocks and trees are identical. The si linearisation rules, scope of their pronunciation domains, clitic hosting, nested-possession predictions and cumulative cells are preserved. A short analytical cross-reference states that discourse indices and subsequent semantic type shifts add no pronounced exponent or Anch terminal. The final incoming-reference audit corrected Chapter14's null-head wording from “no anchoring feature” to “lacks [+anch]”, consistently preserving the explicit [−anch] bundle.

Existing Klavans (1985), §§1.2–1.3,pp.97–100, was checked in full for the distinction between clitic positioning and liaison. Booij (1996),p.220, supplies a compatible distinction but was not added redundantly. Embick and Noyer's author-hosted draft, §2.1 and §4.3, supports the limited PF/LF and adjacency distinctions; no published pagination was inferred from that draft. Harley's author publication page confirms the narrow affixation/head-movement distinction, while the full hosted PDF timed out; no broader new claim depends on it. Schwarz §2.5 treats alternative lexical/structural implementations rather than prescribing a universal morphological mapping. No new bibliography entry was needed. The literature agent also rechecked all new cross-phase citations and their locators.

Independent final review found the connected treatment consistent across Chapters5,10,14 and17, with no outstanding linguistic findings. Existence, type, accessibility, accommodation, scope, covariation, possession and topicality remain distinct. Unresolved distributional judgements remain diagnostic questions, rather than new Iridian facts.

## Ordered implementation commits

1. `7bfdb9f` — semantic contributions of nominal anchoring.
2. `4579fd7` — discourse indices and resource situations.
3. `7d13975` — property-preserving Anch and quantifier composition.
4. `e55a22a` — nominal category terminology and existential pivots.
5. `2426652` — controlled contrasts and interpretation diagnostics.
6. Final preservation audit — committed after the validation recorded below.

Phase 6 and final validation: `make check` passed all 179 tests and both PDF log checks; no undefined references, missing glyphs or fatal errors. The only overfull boxes are the two baseline 2pt boxes outside the edited treatment. Visually inspected final PDF pp.74–75,79,260, including semantic formulae, PF rule and topic-interface continuation. Earlier phase inspections covered the modified tables, pivot list, double marking, implicit possession and bibliography. `git diff --check` passed. All six phases completed with implementation, literature and independent-review work; each preceding phase was committed before the next began. The unrelated untracked nominalisation proposal was preserved, and no local instruction file was staged.

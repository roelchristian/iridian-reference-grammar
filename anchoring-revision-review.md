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

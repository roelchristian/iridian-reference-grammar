# Nominal syntax implementation

Base: `2ea86f3046beff0d55ee9f7f7e0f06bb31932e26`.
Owned source: `chapters/05-nominal-syntax.tex`; no other repository file edited by this agent.

## Changes

- Replaced the three grammatical anchoring bundles and their lexical semantics with an articleless reference account. The noun ordinarily supplies a property; existential composition, situation-relative identification, anaphoric assignment, cardinal/quantifier composition, generic/kind interpretation, and speaker-specific intention are distinguished without installing a silent article.
- Removed productive speaker-anchoring proclitic, its pronunciation-domain/PF instruction, nested domains and double-proclitic predictions in their entirety.
- Kept DP as a category cover term, explicitly declining to infer a D head from definite bare-noun interpretations. NP/PossP/NumP/KP, quantificational material and DemP remain; all four affected trees now omit the abolished layer.
- Added a controlled `Byl zdrávime` pair with identical surface/gloss under first-introduction and familiar-child contexts. The courier triple likewise keeps the exact same nominal cell under non-specific, speaker-specific and familiar contexts.
- Recast demonstrative `tak byl` as sufficient for 'this child', without nominal definiteness agreement. The full demonstrative paradigm, pronoun/reflexive/interrogative paradigm tables are byte-identical to baseline.
- Retained indirect possessors and implicit possession, keeping possessor and possessed referents distinct; number, case and reference remain independently resolved.
- Revised postpositional discussion and tree; `bylamo my` becomes ordinary `bylam my`. Retained temporal anchoring as reference-time terminology, distinct from nominal definiteness.
- Preserved existing bibliography, retaining comparative distinctions and explicitly not treating another language's analysis as Iridian acceptability evidence.

## Labels

Renamed, with semantic replacement:
- `sec:nm-anchor-types` → `sec:nm-semantic-types`
- `sec:nm-anchor-indices` → `sec:nm-reference-indices`
- `sec:nm-def-stacking` → `sec:nm-case-reference`
- `sec:nm-def-double` → `sec:nm-dem-reference`

Removed with their abolished analyses:
- `sec:nm-si-linearisation`
- `sec:nm-si-complex`

Kept the general reference/definiteness labels (`sec:nm-def`, `sec:nm-def-semantics`, `sec:nm-bare-noun`, `sec:nm-def-restrictions`, `sec:nm-spec`) because their targets retain the corresponding semantic subject matter. Added `ex:nm-contextual-reference` for the same-form pair. Parent notified so all incoming references can be migrated.

## Checks

- `git diff --check -- chapters/05-nominal-syntax.tex`: passed.
- Four baseline paradigm tables checked byte-for-byte: demonstratives, personal pronouns, reflexives, interrogatives: unchanged.
- No productive abolished projection, feature bundle, speaker-clitic token, DEF/SANCH gloss or retired `bylo`/`bylamo` surface remains in the chapter.
- `scripts/check-grammar.py` run during integration: current failures were cross-file reference migrations and parent-owned quantity/source-guard updates; no new local source syntax failure reported.

## Deliberate limits

The account does not assign a universal DP/NP choice to all articleless nominals. It preserves provisional institutional-reading, bridging, covariation and scope questions as questions rather than asserted acceptability facts. It changes no case-number, vowel, verbal, alignment or quantifier paradigm.

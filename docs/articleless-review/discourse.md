# Articleless reform: discourse implementation report

Base: `2ea86f3046beff0d55ee9f7f7e0f06bb31932e26`.
Owned files: `chapters/14-information-structure.tex` and `chapters/17-discourse.tex`.

## Changes

- Replaced only documented anchored name and bread forms: Marko → Marėk, Markuto → Marku, Janko → Janėk, Travó → Trava. Removed associated DEF glosses. Replaced productive `si byl`/`si hráť` with the bare noun and removed Sanch glosses, without altering the other words' order or the verbal paradigms.
- Recast the topic–anchoring section as the topic–reference interface. Removed the morphological harmony principle, Anch feature/Agree claims, PF dependencies, and the proposed correlation of silent Anch with topic drop.
- Preserved topic/pivot independence: a linked transitive agent remains Marku in Spec,TopP; the patient remains direct. Hanging topics retain ordinary direct Marėk. Progressive indirect travě and perfective direct trava follow the aspectual case frame, independent of reference.
- Replaced obsolete morphological minimal pairs with the identical `Byl zdrávime` under controlled introductory and already-discussed contexts. Recast the identical reading clauses as contextual focus comparisons rather than a morphological contrast.
- Replaced the three-way bare/speaker/shared demonstration with a connected introduction→bare anaphoric continuation, followed by same-string indefinite/definite comparisons. Discussed speaker-specific and generic readings without new markers or silent articles.
- Preserved controlled animate antecedent competition as predictions, not established judgments; preserved overt reactivation, construction-specific null restrictions, converb same-pivot restrictions and implicit-possession conditions.
- Existing word order, phasal material, examples outside direct anchoring dependencies and all žema paradigms remain unchanged.

## Cross-reference treatment

Existing labels `sec:tc-anchoring-interface`, `ex:tc-nondirect-anchoring`, `sec:disc-anchoring-controlled` and `ex:disc-anchoring-controlled` are retained as stable identifiers at their corresponding reference/discourse discussions. Their titles and substantive contents have been rewritten; no obsolete grammatical claim is retained. All local incoming references still target the same relevant subject. No references to removed `sec:nm-si-*` or `sec:nm-anchor-*` labels remain in these two chapters.

## Validation and limits

- Targeted stale-form/gloss audit found no anchored forms, grammatical si, DEF or Sanch glosses, Anch projections or anchoring principles in either file. Remaining `anchoring` strings are stable label identifiers only.
- `scripts/check-grammar.py` reports no new undefined references or interlinear errors from these two chapters. At implementation time the full integration still contained ongoing guard migrations and nominal-syntax edits owned by other agents; final full validation belongs to the integrating lead.
- No paradigm/phonology changes were introduced. Semantic interpretation examples implement the requested convention rather than establish empirical speaker judgments.
- No commit, push, PR or PDF work performed.

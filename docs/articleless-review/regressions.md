# Articleless reform: regression integration

Base: `2ea86f3046beff0d55ee9f7f7e0f06bb31932e26` (pristine master, including PR25 vowel reforms).
Branch: `reform/articleless-nominals`. No commit, push or publication performed.

## Changes

- Added `scripts/articleless-fixtures.json`: 102 original ordinary case--number cells across five tables, including mixed direct-plural variants, all nine classes, Class V `ráne`, Class II/VII citation stems and merged vowel spellings. Original table SHA-256 values record provenance; anchored counterparts are comparison evidence only. Added 11 byte-preserved historical body hashes and an explicit non-paradigm retired-form inventory with source/analysis, including `Veňo` and the documented replacement of unsupported `Zvěrato` illustration.
- Added `scripts/articleless_diagnostics.py` and integrated it into `check-grammar.py`. It follows the actual literal publication include graph, checks ordinary cells exactly (including internal lexical spaces), rejects known retired whole-word surfaces with or without glosses, abolished heads/features/glosses including TeX notational variants, and checks derived nominal singular cells plus the explicit continuous direct-only gap. No broad suffix deletion, blanket chapter exception or invented ordinary paradigm.
- The sole `si` exception is the exact schematic phonological `si/ši` contrast in Chapter 2. All other source text in that chapter remains checked. Ordinary homophones remain permitted, with exact table-cell checks preserving their independent inflection.
- Added `scripts/articleless-scope-migrations.json`: 13 literal, source-specific original/revised passages, original passage hashes and pristine baseline provenance. Added a comparison-only adapter in `stative_scope_guard.py` which applies those exact approved migrations before the existing original-hash checks. Every other change remains observable. The original `stative-scope-freeze.json` was not changed or regenerated.
- Updated quantity table fixtures by deleting anchored cells only, preserving every original ordinary cell; replaced the obsolete protected-anchor quantity licence with independently documented `tvírzná` (protected outer attributive domain), preserving tests for multiple long nuclei, non-target preservation and no third length. Replaced obsolete `nužo` IPA check with ordinary `nužam` and retained devoicing/voicing/quantity/velar mutation coverage.
- Updated the one valency fixture from `Travó ... bread.DIR.DEF` to ordinary `Trava ... bread.DIR`, preserving its exact causative/participant frame and English translation.
- Left the earlier protected `stative-fixtures.json` byte-for-byte unchanged. Its historical starred `*Nužo múžnime.` expectation has one exact source-specific comparison migration to `*Nuž múžnime.` in `stative_diagnostics.py`; the starred judgement, gloss and context requirements remain independently checked.

## Tests and actual results

`make check-source` PASS: 249 tests, no failures or skips, 40.913 seconds for unittest execution. Full log: `/tmp/articleless-check-source-regression-final.log`. Source and syntax inventory checks passed before the tests. Baseline was 240 tests; this implementation adds seven consolidated articleless tests and two original-freeze migration tests.

New consolidated coverage includes all 102 cell mutations, internal-space corruption, unglossed retired forms, raw/TeX head/feature/gloss forms, new nested literal utility includes, escaped-percent/comment semantics, exact schematic `si` exception versus a second injected `si`, derived cells and missing-form gaps, and mutation/removal of historical status/body evidence. Existing scope tests still reject altered relative selection, case frames, examples, finite-clause cross-references and new rules in protected regions; all 13 literal migrations additionally reject changed linguistic content.

Focused final runs after guard hardening: articleless module 7/7 PASS; scope module 14/14 PASS; quantity module 18/18 PASS; city/town module 3/3 PASS. Full source check passed during final integration; lead should run the final repository-wide gate after any further source changes from reviewers.

`git diff --check` PASS.

Original freeze SHA-256 in both pristine baseline and worktree:
`6659890c8b92dfccef409d308501dc2079413db81645a614f6247258c6f74668`.

## Independent review and limits

Integration reviewer independently verified the 13 original passages, hashes and uniqueness against pristine master, and confirmed unapproved rule insertions were rejected. Their raw/TeX feature-spelling and internal-lexical-whitespace probes exposed gaps that were corrected and included in consolidated tests.

These checks do not establish acceptability or semantic completeness, recognise every possible novel inflected word, or replace the morphological, syntax/semantics and discourse reviews. Their inventories intentionally distinguish ordinary homophones and preserve archived text. They guard known normative structures and literal includes rather than parsing arbitrary TeX macros into a complete linguistic model. No full PDF build or visual acceptance is claimed by this subagent; the lead's build/review work supplies that evidence. No remaining regression blocker identified.

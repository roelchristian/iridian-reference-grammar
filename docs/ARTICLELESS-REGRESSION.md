# Articleless reference: regression and acceptance report

Base: `2ea86f3046beff0d55ee9f7f7e0f06bb31932e26`; branch:
`reform/articleless-nominals`. All repository work remains local: no push,
PR, merge or deployment was performed.

## Baseline and preservation

A pristine archive of master passed `make check-source`: **240 tests**.
Independent reviewers re-parsed master and verified **102/102 ordinary nominal
case–number cells** in five shared tables unchanged. The ordinary deverbal
singular cells, direct-only continuous participant gap, demonstrative/pronoun
paradigms and aspect-conditioned argument frames retain their independent
constraints. Vowel realisation, boundary mappings and the original stative
scope-freeze file remain unchanged. The 2020 archive is unchanged, and the
complete original bodies of eleven research records are preserved beneath
explicit supersession notices.

## Source and test coverage

Final `make check-source` passed **249 tests**, no failures or skips. The nine
additional test methods consolidate the new checks rather than creating one
case per form:

- 102 independently recorded ordinary-cell mutations and internal spelling;
- retired surface forms without requiring DEF/Sanch glosses;
- abolished heads/features, including raw and TeX notational variants;
- literal nested utility inputs and failure when an input is missing;
- exact schematic si/ši exception, without excluding the surrounding chapter;
- retained derived singular cells and explicit unattested-cell boundaries;
- exact historical-body hashes and required status notices;
- thirteen literal, source-specific scope migrations, with further-edit
  rejection against the unchanged original hashes.

Existing quantity, stative, source, valency and scope assertions were migrated
only where their anchoring assumptions had become obsolete. Their independent
Voice, aspect, quantity, case and selection safeguards remain. No whole test
suite, ordinary cell or relative rule was disabled to obtain a pass.
See [detailed regression evidence](articleless-review/regressions.md).

## Full publication acceptance

The genuine missing TeX prerequisites were supplied in an isolated local tree;
no font fallback or incomplete-bibliography PDF was accepted. The full grammar
is **447 pages**, with a separate cover. Final full and cover diagnostic checks
report **zero overfull boxes, missing glyphs, unresolved references/citations or
fatal errors**. The one new ExPex whitespace overflow found during review was
fixed and rebuilt. All 66 TeX/Bib source hashes stayed stable during the final
render. Two existing bibliography data-model warnings remain: missing date/year
in cuni-sound-patterns, missing editor in lieber2018; the bibliography itself
is complete and unchanged by this reform.

Manual visual sampling covers nominal classes and irregulars, ordinary
paradigms in Chapter 4 and Appendix B, contextual bare-nominal examples,
nominal/possessive trees, participant nominalisation and its gaps, topic/reference
examples and discourse chains. The lead additionally inspected twelve
representative page renders and the corrected physical page 329. This is not
a page-by-page audit of all 447 pages.

PDF SHA-256:
`07d6ee9acffd0929d96479dfa7ed18e60b157193d6770c779bf796ed584e2ef6`.
See [PDF validation](articleless-review/pdf-validation.md) and
[environment provenance](articleless-review/tex-environment.md).

## Independent findings and remaining limits

Three fresh subject reviewers and a fresh integration reviewer found and
rechecked six substantive consistency/boundary issues: the DP cover definition,
the initial-position/topic inference, and four current-looking research records.
The integration reviewer also exposed two regression-coverage gaps, both fixed;
PDF inspection found and verified the whitespace correction. No supported
remaining blocker was identified. Full findings, sources, scope and limitations
are in [the independent reviews](articleless-review/independent-reviews.md) and
[the integration review](articleless-review/integration.md).

The reform implements a specified constructed-language norm. It does not prove
every possible acceptability judgement, settle all DP/NP architecture, supply
missing nominal paradigms, or establish unrestricted bridging, institutional
readings or covariation. These limits remain explicit in the grammar.

## Final gate and recovery

The final `make check lexicon lexicon-tsv` completed successfully: 249 tests
in 41.992 seconds, both PDF log checks green and both lexicon exports written.
`git diff --check` passed. A final fetch confirmed remote master still at the
recorded base. The complete log and delivery checks are recorded with the private
recovery archive. It contains the full maintained source tree, including new
untracked files, a patch applicable to the recorded base, migration/review
reports, build logs, the verified PDF and a checksum manifest. No remote
repository publication is part of this task.

# Articleless reform: PDF validation evidence

Final PDF render completed against a stable TeX/Bib source state. The complete source-test acceptance is reported separately by the lead agent after regression-guard migration.

## Environment

The baseline managed environment had LuaLaTeX/latexmk/kpsewhich but lacked Biber, BibLaTeX, ExPex, luaotfload, tracklang, and the required body/heading fonts. Genuine Debian/upstream dependencies were installed only under `/tmp/iridian-tex`; system configuration and repository sources were not edited. Setup provenance and activation are in `/tmp/iridian-tex/SETUP.md` and `env.sh`.

- `biber --version`: 2.20
- `make doctor`: exit 0, all 25 packages and eight required fonts found.
- Required fonts: Libertinus Serif regular/italic/bold/bolditalic and Source Sans Pro regular/regular italic/semibold/semibold italic. A local alias maps upstream's `SourceSansPro-It.otf` filename to the TeX-distribution contract filename `SourceSansPro-RegularIt.otf`; underlying font identity is unchanged.
- No alternate font substitution or bibliography-free build was used.

## Commands

```sh
source /tmp/iridian-tex/env.sh
make check LMKFLAGS='-lualatex -interaction=nonstopmode -halt-on-error -file-line-error -g'
```

The one-time `-g` forced rerun after initial missing-dependency failures, because latexmk otherwise reused the cached failed preamble invocation. Full console log: `/tmp/articleless-full-build.log`. The first missing-luaotfload attempt is preserved as `/tmp/articleless-full-build-first-attempt.log`.

## Known bibliography diagnostics

Biber completes. Two pre-existing bibliographic entries generate data-model warnings: `cuni-sound-patterns` lacks date/year and `lieber2018` lacks editor. No unrelated bibliographic source was modified for these warnings.

## Build result and final source hashes

The complete first `make check` built the full grammar and standalone cover successfully, then stopped at the then-pending source guard: `publication: frozen exponent-bearing paragraphs changed, lost or added`. It did **not** pass the whole target at that point. The lead agent is handling those source-guard migrations and the final complete-target rerun.

A subsequent final `make all` after the reviewed Chapter 14 whitespace correction exits 0. Both `scripts/check-log.py` checks pass:

- Full grammar: no missing glyphs, undefined references/citations, fatal errors or overfull boxes.
- Standalone cover: no missing glyphs, undefined references/citations, fatal errors or overfull boxes.
- All 66 TeX/Bib source hashes remained unchanged during the final render.
- Full PDF: `build/full/grammar.pdf`, 447 pages, 1,924,237 bytes.
- SHA256: `07d6ee9acffd0929d96479dfa7ed18e60b157193d6770c779bf796ed584e2ef6`.
- Cover SHA256: `27504c39407c0f9e8b86f562ab7b79c522906de20f9f171bfb04124654009c8f`.
- Final incremental render log: `/tmp/articleless-final-pdf-build.log`.
- Source-hash manifest: `/tmp/articleless-build-source-final-start.json`.
- Final PDF metadata summary: `/tmp/articleless-pdf-review/final-render.json`.

`pdffonts` confirms actual embedded Libertinus Serif and Source Sans Pro faces. Existing Computer Modern mathematical symbols and Latin Modern monospace are also present as the repository intentionally requests; no body/heading font fallback was substituted.

## Manual visual sample and repaired finding

PNG renders are in `/tmp/articleless-pdf-review/page-NNN.png` using physical, one-based PDF page numbers. Sampled pages:

- 71–74: all nine nominal classes, irregulars and city/town tables; ordinary singular/plural columns only.
- 78: identical-form contextual indefinite/definite contrast.
- 90: nominal and possessive structural trees, no dedicated AnchP.
- 176 and 178: participant nominalisation table, retained ordinary singular cells and explicit continuous-participant gaps.
- 319: ordinary topic examples.
- 329: non-direct-case identification example and topic/reference discussion.
- 394: connected discourse introduction and anaphoric continuation.
- 415–417: consolidated nominal paradigms.

These pages were visually inspected for table alignment, interlinear alignment, syntax-tree legibility, diacritics, clipping and overlap. No visual defect remains in this sample. This is a targeted sample, not inspection of all 447 pages.

The initial render exposed one new 2.0pt ExPex overfull box in Chapter 14, example `ex:tc-nondirect-anchoring`. It came from a newline space after `\ex\label{...}` before the full-width gloss box. The lead agent added the conventional trailing `%`; final render has zero overfull boxes. The context was also shortened without changing its interpretation.

No remaining PDF-validation blocker. The two bibliography metadata warnings listed above remain; their entries were preserved unchanged.

# Developing the reference grammar

The current description of Iridian is maintained in [grammar.tex](../grammar.tex)
and the [seventeen chapters](../chapters/). The sources in
`archive/2020/` preserve an earlier grammar, while `util/stub/` contains working
material; neither establishes rules for the current language. Research notes
and diagnostic reports record proposals, source access and unresolved questions,
whose status must be checked against the active grammar before they inform a
revision.

For an introduction to Iridian, see the [main README](../README.md). Installation,
compilation, output locations and troubleshooting are covered in the
[build guide](BUILDING.md).

## Source organisation

| Location | Role |
| --- | --- |
| `grammar.tex` | Book structure, shared macros, glossing conventions and central typesetting settings |
| `chapters/` | Current linguistic description, arranged in four parts |
| `util/paradigm-tables/` | Shared paradigm excerpts included by the chapters and appendices |
| `util/abbreviations.tex`, `util/paradigms.tex`, `util/lexicon.tex`, `util/historical-notes.tex` | The book's appendices |
| `util/references.bib`, `util/references.tex` | Bibliographic metadata and reference-list presentation |
| `styles/` | Shared fonts, monograph layout, cover artwork and lexicon typesetting |
| `cover.tex`, `design/cover/` | Standalone cover and design proofs |
| `scripts/` | Build and validation tools, bounded diagnostic models and regression data |
| `util/tests/` | Python regression tests for the utilities, diagnostics and selected source conventions |
| `util/collect_lexicon.py` | Extraction of explicitly tagged forms with source locations |
| `build/` | Generated PDFs, staging files, extracted inventories and local font caches |

`grammar.tex` assembles Foundations, Words and phrases, The clause, and Complex
syntax and discourse, followed by the appendices and references. Preserve this
include structure and the existing macros, labels and symbolic cross-references
when editing a treatment. Formatting shared across the book belongs in the
central settings or styles rather than in repeated local spacing adjustments.

## Editorial conventions

Use sentence case for the book title and all part, chapter, appendix, section
and subsection headings, including short titles, contents entries and running
heads. Capitalise the first word and retain proper names, language names,
acronyms, syntactic symbols and intentional Iridian spelling. Preserve the
capitalisation of cited work titles. Apply the same convention to captions
and front-matter list headings. For example, write “One title among many”.

Describe Iridian forms, distributions and interpretations before developing
their analysis, using connected scholarly prose and British spelling. Keep
established language facts distinct from the grammar's analytical assumptions
and from unresolved descriptive questions. A wording change should preserve
the language's rules; a substantive revision requires corresponding changes
throughout the affected treatment.

Read the complete relevant discussion, its examples and paradigms, and its
incoming and outgoing references. Prefer existing examples, checking surface
forms, segmentation, glosses, case frames, alignment, aspect, mood, translations
and contextual interpretations together. Prose, tables, trees and related
chapters must describe the same construction. Constructed examples and schematic
lexical slots should retain their stated status: they do not establish
attestation or new lexical licences.

Theoretical claims, typological generalisations and comparisons with other
languages require verified scholarly support. Use already cited works where
they support the particular claim, and consult the relevant passage before
adding or extending a citation. Preserve source access limits and unresolved
questions rather than supplying unsupported evidence or bibliographic details.

Keep revisions within their intended scope, preserve unrelated work, and inspect
the final diff. Archival analyses and working notes should remain identifiable
as such; their presence in the repository does not make them part of the current
description.

## Bibliography maintenance

Add or correct bibliographic metadata in
[util/references.bib](../util/references.bib), which `grammar.tex` loads through
BibLaTeX. Keep citation keys unique and use the existing citation conventions.
[util/references.tex](../util/references.tex) prints the numbered,
alphabetically sorted reference list; its `\nocite{*}` also includes database
entries not yet cited in the prose.

`latexmk` runs Biber with data-model validation when required, then reruns
LuaLaTeX to resolve citations, including in chapter builds. No separate manual
bibliography command is needed. Source checks catch undefined citation keys and
duplicate bibliography keys; Biber validates syntax and fields during the build.
Neither check verifies that a source supports the linguistic claim attached to
it, so bibliographic accuracy and evidential coverage require editorial review.

## Validation and regression fixtures

Run commands from the repository root. Builds must run sequentially, including
full, chapter, cover and watch builds, because they share font caches and other
build resources.

```sh
make check-source
```

This target runs three checks:

1. `scripts/check-grammar.py` follows the active book's literal inputs and checks
   labels, references, citation keys, environment pairing, interlinear word/gloss
   counts and selected linguistic regressions against prescribed forms and
   independent fixtures.
2. `scripts/check-syntax-inventory.py` checks Appendix A coverage of projection
   names and explicitly zero-marked heads found in the maintained sources. Its
   inventory includes provisional and rejected labels; coverage does not
   establish analytical status, semantic accuracy, or completeness of features
   and bare head names.
3. `python3 -m unittest discover -s util/tests -v` runs the existing utility and
   diagnostic tests, including collector and PDF-publication regressions.

The JSON fixtures under `scripts/` preserve independent expected outputs for
specified constructions. Diagnostic helpers implement bounded operations on
explicitly supplied inputs, rather than a general morphological analyser or a
source of new grammatical judgements. When revising an established rule, review
the related fixtures and tests together with its descriptive treatment; keep
expected results independently specified rather than generating them from the
implementation being checked. The [utility documentation](../util/README.md)
explains the individual models and their limits.

Some fixtures retain historical grammatical-domain identifiers, such as
`03-verbs`. [scripts/source_domains.py](../scripts/source_domains.py) assembles
these diagnostic views from the current chapters. They are compatibility names,
not obsolete files included in the book; publication links, label uniqueness
and heading checks inspect the actual active inputs.

For publication validation, run:

```sh
make check
git diff --check
```

`make check` builds the full grammar and standalone cover, runs the source checks
and tests, then checks both completed logs. To inspect an existing full-build
log separately, use:

```sh
python3 scripts/check-log.py build/full/grammar.log
```

The log checker rejects missing glyphs, unresolved references or citations,
duplicate labels, pending reference or bibliography reruns, empty bibliographies,
compilation errors and the absence of successful PDF output. It reports overfull
boxes for visual review. Read other compiler and Biber warnings in context, and
inspect affected PDF pages whenever layout changes, checking clipping, spacing,
float placement, legibility and heading continuity.

Chapter-only builds use `includeonly`, so references to omitted chapters may be
unresolved and numbering may differ from the full book. Use the full build for
publication and final reference checks. If a build fails, consult the latest log
in its output directory's `.staging/` subdirectory: the log beside the published
PDF belongs to the last successful build. The [build guide](BUILDING.md) explains
this publication mechanism and the relevant paths.

## Tagged lexicon inventories

```sh
make lexicon       # Write build/lexicon.json
make lexicon-tsv   # Write build/lexicon.tsv
```

These targets collect explicitly tagged forms from the current chapters with
their source locations. They support source review; the manually curated
`util/lexicon.tex` remains the book's lexicon appendix and is never overwritten
by extraction. See the [utility documentation](../util/README.md) for recognised
macros, command-line options, coverage and limitations.

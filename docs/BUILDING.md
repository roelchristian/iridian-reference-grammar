# Building the reference grammar

The current PDF is built from [`grammar.tex`](../grammar.tex) and the maintained
[`chapters/`](../chapters/). Run the commands below from the repository root.
For an introduction to Iridian, see the [main README](../README.md); source
organisation, editorial checks and contribution conventions are covered in the
[development guide](DEVELOPMENT.md).

## Prerequisites and first build

Install a full **TeX Live** distribution (**MacTeX** on macOS), with `latexmk`,
LuaLaTeX, Biber and `kpsewhich` on `PATH`, together with Make and Python 3.
The sources use TeX-distributed Libertinus Serif and Source Sans Pro fonts;
no separately installed system fonts are needed. Python supports safe PDF
publication, prerequisite checks, source validation and lexicon extraction.

```sh
make doctor              # Check executables, TeX packages and font files
make                     # Build build/full/grammar.pdf
make check               # Build book/cover, check sources and logs, run utility tests
```

The canonical current PDF is `build/full/grammar.pdf`. All outputs produced by
the current pipeline remain under `build/`; a pre-existing PDF in the repository
root or archive does not represent the current build.

LuaTeX uses a writable local font cache in `build/cache/`, configured by
[`.latexmkrc`](../.latexmkrc), so compilation also works in restricted workspaces
without writing font data to the home directory. The first build can take longer
while fonts are indexed; later builds reuse the cache. `latexmk` tracks nested
inputs and reruns LuaLaTeX until references and contents settle. Running `make`
again without source changes performs no TeX pass.

## Build targets

```sh
make cover               # Standalone front cover: build/cover/cover.pdf
make cover-design        # Cover concepts, review, specification and bleed export
make watch               # Rebuild the full grammar on changes; Ctrl-C stops watching
make check-source        # Source checks and utility tests without TeX compilation
make list                # List all chapter names
make help                # Show the main targets
```

Run builds sequentially, without `make -j`: full, chapter and cover builds share
the font cache, and repeated builds of the same target share auxiliary files.
The [development guide](DEVELOPMENT.md) explains the validation performed by
`make check` and `make check-source`.

### Chapter builds

Every chapter accepts its descriptive name, number or full file stem. For
Chapter 4, the equivalent commands are:

```sh
make ch-nominal-morphology
make ch-04
make ch-04-nominal-morphology
```

The corresponding watch commands use the same aliases:

```sh
make watch-nominal-morphology
make watch-04
make watch-04-nominal-morphology
```

Chapter PDFs are written to `build/chapters/<chapter>/grammar.pdf`, where
`<chapter>` is the full stem, such as `04-nominal-morphology`. Their output
directories are independent of the full book. Chapter builds use `includeonly`,
so references into omitted chapters may be unresolved and numbering may differ
from the complete grammar. Use the full build for publication and final
reference checks.

### Bibliography processing

Bibliographic metadata lives in [`util/references.bib`](../util/references.bib).
`grammar.tex` loads it with BibLaTeX, and
[`util/references.tex`](../util/references.tex) prints the numbered,
alphabetically sorted reference list. `latexmk` runs Biber with data-model
validation when the database or its control file changes, then reruns LuaLaTeX
to resolve citations. No separate manual bibliography command is needed,
including for chapter builds. `make doctor` checks for Biber and BibLaTeX.

## Published files and failed builds

Compilation runs in a `.staging/` subdirectory of each output directory.
[`scripts/build-pdf.py`](../scripts/build-pdf.py) replaces the published PDF
atomically only after a successful `latexmk` run and a basic completeness check.
The published PDF stays readable throughout a rebuild, and a failed or
interrupted build leaves the last successful PDF in place. The same arrangement
applies to full, cover, chapter and watch builds; watch mode previews the
published PDF.

The log alongside each published PDF belongs to its last successful build.
After a failure, inspect the latest log in `.staging/`, such as
`build/full/.staging/grammar.log`, where the compilation's auxiliary files also
remain. Successful full-book diagnostics can be checked separately with:

```sh
python3 scripts/check-log.py build/full/grammar.log
```

### Troubleshooting

- **Missing executables, packages or fonts:** run `make doctor`, install the
  listed prerequisites and ensure the TeX executables are on `PATH`, then retry.
- **A slow first build:** allow LuaTeX to populate `build/cache/`; subsequent
  builds reuse it.
- **A failed build with an unchanged PDF:** inspect the `.staging/` log rather
  than the log beside the preserved PDF, correct the reported error and rerun
  the target.
- **Unresolved chapter references:** check the full grammar before treating
  warnings from an `includeonly` build as publication failures.
- **Missing glyphs, unresolved references or duplicate labels in the full
  build:** resolve them before publication. The log checker rejects these
  diagnostics and compilation errors; overfull boxes are reported for visual
  review, as described in the [development guide](DEVELOPMENT.md).

## Clean-up and extracted lexicon files

```sh
make clean               # Remove full, chapter and cover outputs; retain font caches
make distclean           # Also remove the local font caches
make lexicon             # Write build/lexicon.json
make lexicon-tsv         # Write build/lexicon.tsv
```

Clean-up removes only the current pipeline's full, chapter and cover build
directories, with `distclean` additionally removing `build/cache/`. Older PDFs
and auxiliary files in the repository root or archive remain untouched.

The lexicon targets collect tagged forms from the maintained chapters with
their source locations. They leave the manually curated
[`util/lexicon.tex`](../util/lexicon.tex), the book's lexicon appendix, unchanged.
See the [utility documentation](../util/README.md) for coverage and limitations.

## Publication format

The PDF uses an A4 monograph layout with facing-page margins, a full-colour
vector front cover, a separate interior title page and running heads. Libertinus
Serif supplies the interior text with slightly open leading, while Source Sans
Pro supplies the heading hierarchy. IPA spans retain the surrounding font
through the semantic `\ipagloss` macro. Interlinear examples use 11-point type;
tables use tabular lining figures and booktabs rules. Sections, tables and
figures carry chapter-based numbers, and caption and table spacing are set
centrally.

[`styles/monograph.tex`](../styles/monograph.tex) controls chapter, heading,
contents and running-page styles. Font selection is shared in
[`styles/fonts.tex`](../styles/fonts.tex), which resolves fonts from the TeX
distribution. Microtype settings and example/caption spacing are in
`grammar.tex`. [`styles/cover.tex`](../styles/cover.tex) supplies the vector
cover shared by the book and the standalone [`cover.tex`](../cover.tex).

The standard front cover is A4 without bleed or spine. `make cover-design`
also produces `build/cover/concepts.pdf`, `review.pdf`, `specification.pdf` and
`print.pdf`; the last is an A4-trim front cover with 3 mm bleed on each side.
A printer-specific wraparound cover depends on the binding, stock and final
trim.

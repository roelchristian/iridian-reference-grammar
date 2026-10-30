# A reference grammar of the Iridian language

This is a rewrite of the (incomplete) reference grammar of Iridian I worked on in May/June 2019.

This work is licenced under an [MIT Licence](https://github.com/roelchristian/iridian-reference-grammar/blob/master/LICENSE). Some rights are reserved, but otherwise, feel free to fork this repository or adapt portions of the code for your personal use.

The current grammar is in `grammar.tex` and `chapters/`. Indicative verbal negation uses unstressed **za-** before consonants and **z-** before vowels; **ž-** is not a negative allomorph. The `archive/2020/` sources and working notes in `util/stub/` document earlier analyses and are not normative for the current system.

## Build the PDF

Install a full **TeX Live** distribution (MacTeX on macOS), with `latexmk`
and LuaLaTeX on `PATH`. The sources use TeX-distributed Libertinus Serif
and Source Sans Pro fonts; no separately installed system fonts
are needed. Python 3 is used for prerequisite checks and lexicon extraction.

```sh
make doctor              # Check executables, packages, and font files
make                     # Build build/full/grammar.pdf
make check               # Build book/cover, check diagnostics, run collector tests
make check-source        # Check source links, linguistic regressions and collector tests
make cover               # Standalone front cover: build/cover/cover.pdf
make watch               # Rebuild when sources change; Ctrl-C stops watching
make ch-nouns            # Build only chapter 4
make ch-04               # Equivalent numeric alias
make ch-04-nouns          # Equivalent full-name alias
make watch-nouns         # Watch only chapter 4
make list                # List all chapter names
```

The PDF uses an A4 monograph layout with facing-page margins, a full-colour
vector front cover, a separate interior title page, and running heads. All new
auxiliary files and PDFs live under `build/`. LuaTeX uses a
writable local font cache in `build/cache/`, so it also runs in restricted
workspaces without writing to your home directory. The first build can take
longer while it indexes fonts; later builds reuse that cache. `latexmk` tracks
nested inputs and reruns LuaLaTeX until references and contents settle. Running
`make` again without edits performs no TeX pass. `make check` rejects missing
glyphs, unresolved references, duplicate labels, and compilation errors, and
runs the collector tests. It reports overfull boxes for visual review.

Chapter PDFs are in `build/chapters/<chapter>/grammar.pdf`, independent of the
full book. They use `includeonly`, so references into omitted chapters may be
unresolved and their numbering may differ from the full book. Use the full
build for publication and final reference checks.

```sh
make clean               # Remove full/chapter outputs; retain font caches
make distclean           # Also remove the local font caches
```

Cleanup is limited to the current pipeline's build directories. Older PDFs
and auxiliary files in the repository root or archive are left alone. The
canonical current PDF is `build/full/grammar.pdf`, not a pre-existing root PDF.

## Gather tagged lexicon items

```sh
make lexicon             # Write build/lexicon.json
make lexicon-tsv         # Write build/lexicon.tsv
```

These collect tagged forms from the current chapters with their source
locations. See [the utility documentation](util/README.md) for coverage and
limitations. The manually curated `util/lexicon.tex` remains the book's lexicon
appendix; extraction does not overwrite it.

## Typography and cover

The interior uses Libertinus Serif with slightly open leading, Source Sans Pro
for the heading hierarchy. IPA spans retain the surrounding font through the
semantic `\ipagloss` macro. Interlinear examples use 11-point type; tables use
tabular lining figures and booktabs rules.
Sections, tables, and figures carry chapter-based numbers. Caption spacing and
table spacing are set centrally rather than added by individual chapters.

`styles/monograph.tex` holds the chapter, heading, contents, and running-page
styles. Font selection is shared in `styles/fonts.tex`; fonts resolve from the
TeX distribution rather than a user font directory. Microtype settings and
example/caption spacing are in `grammar.tex`. `styles/cover.tex` supplies one
vector cover shared by the book and the standalone `cover.tex` document. The front cover is A4 with no bleed or
spine; a printer-specific wraparound cover can be prepared once the binding,
stock, and final trim are specified.

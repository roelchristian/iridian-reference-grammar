# A reference grammar of the Iridian language

Work on the current version of this grammar started on May/June 2019.

You can learn more about this project by visiting https://lang.roelchristian.com

This work is licenced under an [MIT Licence](https://github.com/roelchristian/iridian-reference-grammar/blob/master/LICENSE). Some rights are reserved, but otherwise, feel free to fork this repository or adapt portions of the code for your personal use.

[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/roelchristian/iridian-reference-grammar/graphs/commit-activity) [![made-with-latex](https://img.shields.io/badge/Made%20with-LaTeX-1f425f.svg)](https://www.latex-project.org/)

## Building

Requires a TeX Live installation with LuaLaTeX, Biber, and `makeglossaries`. Run:

```sh
make        # full build (lualatex + biber + makeglossaries + two more passes)
make quick  # single lualatex pass
make clean  # remove auxiliary files
```

The main entry point is `iridian-grammar.tex`; chapters are in `chapters/` and loaded via `\input`.

## What Copilot can help with

- **Navigate document structure** — explain the `iridian-grammar.tex` entry point, how chapters are wired together with `\input`, and what each file in `chapters/` and `preamble/` does.
- **Improve TeX macros and environments** — refine custom commands in `preamble/commands.tex`, interlinear gloss layouts (`preamble/leipzig.tex`), example numbering schemes, and the `iridian-grammar.cls` class file.
- **Fix common LaTeX issues** — broken cross-references, overfull/underfull boxes, bad hyphenation, font or encoding problems with LuaLaTeX.
- **Enhance build tooling** — add or improve Makefile targets (e.g. `watch`, `spell`, `lint` with `chktex`/`lacheck`) and make the build more robust.
- **Add CI with GitHub Actions** — set up a workflow to compile the PDF on every push or pull request and upload it as a downloadable artifact.
- **Repo hygiene** — extend `.gitignore` to catch any missing TeX build artifacts, and keep the repository tidy.

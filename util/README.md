# Lexicon tools

## Morphophonological source checks

`make check-source` checks the active book's references, examples and prescribed
forms, then runs the utility tests. The boundary reference implementation in
`scripts/boundary_transducer.py` reads the four named grade bundles and IPA-token
correspondences from `scripts/boundary-mapping.json`. Its expected outputs and
negative cases are written separately in `scripts/boundary-fixtures.json`;
they are not generated from the mapping table.

The caller must supply the selected stem, its participating velar class, and a
licensed, exposed morphological boundary. The transducer maps that input edge
once before attaching the supplied exponent and records the boundary as consumed.
It does not infer licences from spelling or suffix vowels, choose lexical or
vocalic allomorphs, or perform antipassive exponence, coda phonetics or spelling.
Constructed multi-boundary tests establish conditional locality properties;
they do not add constructions to the language. Existing source-prescription
fixtures remain separate from this limited executable model.

## Collect forms marked in the grammar

From the repository root, run:

```sh
make lexicon       # build/lexicon.json
make lexicon-tsv   # build/lexicon.tsv, convenient for spreadsheet review
```

The collector needs Python 3.8 or newer and no third-party packages. It can also
run from any working directory:

```sh
python3 /path/to/repository/util/collect_lexicon.py --format json --output collected.json
python3 util/collect_lexicon.py chapters/04-nouns.tex --format tsv
python3 util/collect_lexicon.py util/lexicon.tex --output curated-entries.json
python3 -m unittest discover -s util/tests -v
```

With no source arguments it reads only `chapters/**/*.tex`, excluding the
historical archive, working notes, and the curated lexicon appendix. Pass files
or directories explicitly to inspect other sources. Directory arguments are
searched recursively for TeX files.

The collector recognizes these source macros:

| Macro | Collected data |
| --- | --- |
| `\ird{form}` | A marked form, without an inferred definition |
| `\irdp{form}{gloss}` | Form and explicit gloss |
| `\phon{form}{IPA}{gloss}` | Form, pronunciation, and explicit gloss |
| `\lexentry{form}{notes}{gloss}` | Curated form, notes, and gloss |

JSON groups exact forms, normalized to Unicode NFC, and retains every occurrence
with its macro, source path, and line number. Explicit glosses and pronunciations
are deduplicated in source order. TSV gives one row per form with glosses,
pronunciations, and source locations. Output is deterministic and files are only
rewritten when their contents change.

This is a source-review inventory, not an automatically authored dictionary.
Marked forms include inflected words, phrases, morphemes, and invented examples.
For instance, the current chapters explicitly gloss `byl` as both “ash” and
“child”; both readings remain visible with their source locations. Definitions
in prose and interlinear glosses are not inferred or aligned automatically.
TeX markup in arguments is preserved verbatim, nested braces and comments are
handled, and malformed macro arguments fail with a source location. The tool
does not expand TeX macros, evaluate conditionals, or parse verbatim environments.

`util/lexicon.tex` remains the curated PDF appendix. Collection never overwrites
it or the separate working JSON datasets.

## Generate new candidate words

`lexgen/` is a separate local Node.js word-generator UI, rather than a collector.
See [its README](lexgen/README.md) for phoneme inventories, presets, and startup
instructions. It is not required for the PDF build or collection targets.

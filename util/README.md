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

`scripts/evidential_realisation.py` separately selects the indirect-evidential
exponent on an already licensed phonological host: `/al/` after a consonant,
`/l/` after a vowel. It preserves the host and delegates plain attachment to
the existing boundary transducer. A subsequent front-grade linker acts on the
new final `/l/`, so it neither reaches an inner aspect ending nor selects the
linker-specific `-ice` or `-imně` allomorph through the evidential. The
consonantal mapping's rejection of vowel-final PAL inputs is unchanged.

Literal expectations in `scripts/evidential-fixtures.json` cover isolated and
linked forms, current retrospective `-áv/-av`, antipassive `-ek` retention,
causative hosts and vowel quantity. Conditional mood-host tests check segmental
attachment only; callers still supply evidential licensing. Source checks pair
the forms within their canonical Chapter 3 table rows, including the modal
and long-vowel examples, and retain the prefixed negative host/output/linker
triple in its prose derivation. They also distinguish the
separate broad pronunciations of final coda `[w]` and prevocalic `[ʎ]`. Neither
the helper nor the consonantal transducer computes coda phonetics, stress or
standard spelling.

The separate `scripts/contemplative-fixtures.json` checks long `-áž` and the
reviewed copular/existential forms. Its explicit pronunciation pairs distinguish
standalone final `[aːʃ]` from linked `[aːʒɛ]` and evidential `-ážal/-ážalě`,
while preserving quantity and initial stress. Boundary tests retain underlying
`/ʒ/` throughout suffixation; contextual devoicing is not an input allomorph or
an added `x → ʒ` PAL correspondence. Source checks also preserve the unrelated
quantifier `náh` ‘each’ and proper name `Báh`.

`scripts/quantity_grades.py` selects G0/G1/G2/G3 independently of consonantal
mapping. Its input is an already selected tuple of IPA tokens plus an explicit
licensed local domain, eligible nucleus indices and chosen target. Domain bounds
are token offsets, not written vowels: lexical labial palatality and the new
run stem `zemac-` therefore do not invite a spelling-based syllable heuristic.
`scripts/quantity-grades.json` records vowel membership independently of
short/long correspondences and the separately licensed mid-vowel raising pairs.
A selected `/ɨ/` stays `/ɨ/` under G1 without redirecting the target to an
earlier vowel. Retained `/ə/` is a nucleus even when its fleeting class excludes
it from the eligible target set. G0 preserves lexical length, G2 preserves
quantity while raising, and repeated strength does not create a third length.

Independent literal outputs in `scripts/quantity-fixtures.json` cover retained
bound nuclei, the second-nucleus target of `zemac-`, root-strong and suffix-strong
domains, valency morphology, irrealis locality, derivation, protected outer morphological domains
and evidential/linker attachment. The same file independently fixes the paired
nominal I--III and verbal A--C cells in the grammar's tables. These are bounded
regressions, not a general morphological analyser: the caller still selects
fleeting-vowel stems, lexically overridden targets, consonantal classes and
construction-specific short ending allomorphs. In particular, conditioned `-až`
after a locally strong stem is checked beside default `-áž`; there is no global
ban on multiple long vowels or on short contemplative spellings.

`scripts/phasal_diagnostics.py` checks the ordinary two-stage phasal
approximation on explicitly supplied truth values. Its exclusive diagnostic
compares `EXCL(Phas(P))` with the specifically licensed `Phas(EXCL(P))`
interpretation; it does not assign scope to arbitrary particle strings. Literal
positive and negative expectations in `scripts/phasal-fixtures.json` include
contexts in which the two exclusive readings diverge. The same fixture file
independently prescribes all four rows of the native TikZ illustration in
`util/phasal-polarity-diagram.tex`, which the active-source checker validates.
Neither the helper nor the time diagram derives scalar ordering, modal worlds,
reference-stage selection or pragmatic inferences from a sentence. Such inputs
remain explicit conditions on the grammatical examples.

`scripts/exclusive_diagnostics.py` supplements those satisfaction checks with
separate MIN and MAX contributions over caller-supplied alternative propositions
and a reflexive, transitive strength relation. Its tests cover ordinary
exclusivity, scalar bounds, incomparable alternatives, and low progress with
current MIN and preceding/current MAX. Advancement and the higher expected goal
are checked separately from those contributions. Projection probes require an
explicit hypothesis for each embedding environment; they do not prescribe
Iridian question, negative-Mood or epistemic projection rules. The gate schemata
are checked as English interpretation examples without Iridian surface forms.

`scripts/clausal_diagnostics.py` adds bounded checks for the specified lower
polarity input under negative Mood, high additive/exclusive scope, the exclusive
construction's low option, and reduced AspP selection. Its tests use contexts
that distinguish PHAS(¬P) from ¬PHAS(P), reject crossed licensing boundaries and
indicative Neg under negative Mood, and reject internal higher operators even
when hidden under an AspP label. Matrix operators leave the selected subtree
unchanged. The source checker separately binds the 20 diagnostic surface strings
to their prescribed scope and status rows. These tests evaluate supplied
prejacent stages, not modal force, actual-world truth, scalar meanings or
natural-language judgments; a reduced-domain tuple is a selection diagnostic,
not a general syntactic parser.
The Boolean result combines assertion satisfaction with the required background;
it does not distinguish a false assertion from a failed presupposition or model
presupposition projection under Mood. Locality is supplied explicitly: rejection
of a declared boundary does not establish automatic boundary detection.

## Stative design diagnostics

`scripts/stative_diagnostics.py` supplies bounded State/Become, scalar
and selection checks. Independent literal fixtures cover eight
stems, 64 licensed finite aspect cells, their negative/phasal and bound derivatives,
16 conditional causative paradigms and three reduced-Mood examples. See
`util/stative-paradigms.md` for the morphological and PF audit,
`util/stative-source-audit.md` for primary-source access limits, and
`util/stative-integration-review.md` for adoption decisions and independent
review. Simple states select continuous, retrospective or contemplative; progressive and perfective are rejected even with expressive or bounded-context flags. Dynamic derivatives retain their own aspectual licences. The model takes explicit licences and semantic standards; it does not
infer attestation, phonetic output or arbitrary lexical selection from spelling.

## Ordinary ATTR and experiential extension

`scripts/stative-lexicon.json` and `scripts/stative_lexicon.py` add explicit
lexical licences for the second pass. The latest ordinary attributive and
Manifest specifications are recorded in `util/stative-extension-paradigms.md`.
The current `util/stative-paradigms.md` and its fixture matrix implement the
restricted State inventory adopted on 2 November 2026. The earlier baseline
at `5a29478` remains the scope reference for unrelated relative construction
rules; the authorised aspect restrictions also apply to reduced derivatives.
The former unassigned happy-attributive and unadopted-third-class status is
superseded by the ordinary ATTR metadata. `scripts/stative_scope_guard.py` checks the preserved source spans
and earlier files against baseline hashes, including negative mutation tests.
See `util/stative-extension-source-audit.md` for primary-source access limits.

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
python3 util/collect_lexicon.py chapters/05-nominal-syntax.tex --format tsv
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
with its macro, source path, and line number. Canonical `ė` and `Ė` round-trip
through JSON and TSV; decomposed e plus combining dot is normalised at import,
while `e`, `ė` and `ě` remain distinct forms. Explicit glosses and pronunciations
are deduplicated in source order. TSV gives one row per form with glosses,
pronunciations, and source locations. Output is deterministic and files are only
rewritten when their contents change.

This is a source-review inventory, not an automatically authored dictionary.
Marked forms include inflected words, phrases, morphemes, and invented examples.
Conflicting explicit glosses, when supplied, remain visible with their source
locations rather than being reconciled automatically. Definitions
in prose and interlinear glosses are not inferred or aligned automatically.
TeX markup in arguments is preserved verbatim, nested braces and comments are
handled, and malformed macro arguments fail with a source location. The tool
does not expand TeX macros, evaluate conditionals, or parse verbatim environments.

`util/lexicon.tex` remains the curated PDF appendix. Collection never overwrites
it or the separate working JSON datasets.

The dictionary renderer in `styles/lexicon.tex` retains the three source
arguments of `\lexentry{form}{notes}{gloss}`. Optional trailing fields
`[category and class][homograph number]` supply print labels, for example
`\lexentry{po-}{...}{...}[prev.][1]`. The collector continues to retain the
literal headword, notes and gloss; it does not collect the optional print
fields. Unassigned-class diagnostics stay in the source notes but are omitted
in print, where the guide explains missing class labels. Class labels appear
beside the headword rather than being repeated in the morphological notes.
Entries are ordered without case, spaces, hyphens or vowel diacritics, with
caron consonants following their plain counterparts; alphabet headings mark
the resulting groups.

The [central-vowel migration record](../docs/CENTRAL-VOWEL-MIGRATION.md)
identifies the audited schwa slots, their unchanged reduced stems and baseline
source locations. It also distinguishes the nominal alternating `-ėk` from
verbal perfective `-ek ~ -ik-`.

## Generate new candidate words

`lexgen/` is a separate local Node.js word-generator UI, rather than a collector.
See [its README](lexgen/README.md) for phoneme inventories, presets, and startup
instructions. It is not required for the PDF build or collection targets.

## Pivot candidate diagnostics

`scripts/pivot_diagnostics.py` compares bounded configurational and successive-Agree
case computations on caller-supplied inventories, selection and residual licensing
exclusions. `scripts/pivot-fixtures.json` supplies independent literal case frames,
locality controls and finite scope countermodels. Tests reject all-DP case marking,
PF-order case computation, inherited applicative priority, restored antipassive
patients and access through an unexported opaque phase. The models do not derive
the still-open selection features or establish new grammatical judgments.

The 72 controlled records in `pivot-syntax-diagnostics.md` distinguish canonical
examples from proposed specifications and hypothetical predictions. Research,
source access limits, acceptance criteria and pending architecture integration are
recorded in `pivot-analysis-status.md` and its linked analysis files.

## Chapter reorganisation

The publication follows seventeen chapters in four parts. Reviewed linguistic
fixtures retain historical grammatical-domain identifiers through
`scripts/source_domains.py`; these are diagnostic views assembled from active
chapters, not files included in the book. Chapter heading checks apply to all
substantive chapters, while label and citation checks inspect actual inputs.

## Lexical valency selection

`scripts/valency-profiles.json` separates explicit lexical and constructional
licences from allomorph metadata. `scripts/valency_profiles.py` checks supplied
readings without generating forms or assigning case. Its bounded profiles cover
canonical causatives, restricted applied causatives, the `mar-` service reading,
NOM indicative activity uses of `pjašt-` and `kař-`, existing ambitransitives,
and selected applicative roles. A conditional causative requires an explicit
causability or individual lexical decision; psychological causation requires
the latter. An unresolved entry withholds a licence without
asserting ungrammaticality. Implement context remains a separate input, so the
presence of `-éb-` cannot establish an instrumental reading by itself. The
antipassive requires indicative ERG licensing. Service causation is indicative
and closes the performer role: an overt or anaphorically recovered causee selects
the ordinary construction instead. Applied service causatives have no separately
listed licence and are withheld, even where ordinary applied causation is listed.
The explicit `directive=True` input overrides the default indicative flag and
requires an overt causee and any retained applied participant; a nonindicative
input alone does not assert directive Mood.

The data are constructed grammatical specifications, not measured preferences,
usage frequencies or attestations. Listed causal/noncausal families use existing
principal parts; the named unresolved semantic families have no invented stems.
In particular, no inventory of twenty to thirty new verb pairs or die/kill
suppletion is implied. Finite form generation, passive/decausative licensing,
affected-possessor lexical entries and cross-clausal reflexive binding remain
outside this bounded interface. Tests hold lexical identity constant while
varying alignment domain, patient presence, causee recovery, service licensing
or applied role; the ordinary source-pair fixtures remain independent.

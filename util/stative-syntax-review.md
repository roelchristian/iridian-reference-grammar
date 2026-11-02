# Stative syntax: implementation and independent review

Revision date: 3 November 2026. Base: `3419e26`; branch:
`codex/stative-syntax-revision`.

## Scope and implementation

The eleven numbered revisions in the supplied detailed plan were implemented
as separate commits. Three drafting agents divided revisions 1–3, 4–6 and
7–11; the coordinating agent checked and integrated their contributions and
created the commits. The team used the current chapters as normative sources,
read the full stative treatment and its affected references, and checked
scholarly comparisons against the passages identified below.

| Revision | Commit | Treatment |
| --- | --- | --- |
| 1 | `d1bace5` | Stativisation, categorisation and holder licensing |
| 2 | `3fef467` | Psychological argument inventories |
| 3 | `3220c2d` | Relative hierarchy and lexical selection |
| 4 | `a2c5bc9` | Stimulus composition and experiencer case |
| 5 | `1e38d88` | Direct and inchoative causation |
| 6 | `e1ea3f5` | Manifest without an internal-state entailment |
| 7 | `741f3d2` | Aspect over the completed predicate |
| 8 | `ddf1782` | Withholding an unmotivated ResP |
| 9 | `ce823be` | Perspective and evidentiality |
| 10 | `35f0e9c` | Finite, attributive and adverbial predicates |
| 11 | `837574f` | Case selection and ordinary placement |

Chapter 10 changes begin at §10.1.3; §§10.1–10.1.2 remain unchanged.
Chapter 7 receives only the corresponding qualifications to applicative
case licensing and causative selection. Existing example forms, glosses,
translations and labels are preserved. No lexical bivalent psychological
paradigm, perspective projection, new morpheme or new aspect value is added.

Two assumptions in the supplied plan predate the current source. First,
§10.1.2 already gives the NOM stimulus-applicative case mapping; the revision
preserves that rule while identifying its individual NOM forms as
unillustrated applications of the general mapping. Second, the current
perspective treatment contains neither the plan's psychological question nor
an obligatory experiencer–perspective anchoring rule. The revision retains
the current attitude examples and treats perspective coincidence contextually.

The actual bibliography is `util/references.bib`, loaded by `grammar.tex`.
The obsolete bibliography path mentioned in the local writing guidance was
not recreated. The protected relative treatment in Chapter 15 remains
unchanged: its conditional reference to ResP does not establish such a
projection for the constructions described in §10.1.3.

## Scholarly verification and access limits

The four additions have independently verified publication metadata:

| Key | Publication | Passage and claim limit |
| --- | --- | --- |
| `cuervo2015causation` | Cuervo 2015, *Syntax* 18(4): 388–424, [DOI](https://doi.org/10.1111/synt.12115) | Publisher abstract: dynamic causative structure over a state and a distinct inchoative configuration. Cuervo's nonderivational causative–inchoative relation is expressly distinguished from Iridian Caus above Become. |
| `kennedylevin2008` | Kennedy and Levin 2008, in *Adjectives and Adverbs*, 156–182, [DOI](https://doi.org/10.1093/oso/9780199211616.003.0007) | [Author manuscript](https://web.stanford.edu/~bclevin/kl07-measure.pdf), §§3.1–3.3, checked for standards, measures of change and variable telicity; published year and pages checked separately against author and publisher records. |
| `embick2004resultative` | Embick 2004, *Linguistic Inquiry* 35(3): 355–392, [DOI](https://doi.org/10.1162/0024389041402634) | Indexed text of the [primary article](https://www.ling.upenn.edu/~embick/result.pdf), introduction: simply stative versus resultative participles with a represented event. Direct PDF retrieval was unavailable; no claim from inaccessible later sections is used. |
| `spathasmichelioudakis2021` | Spathas and Michelioudakis 2021, *Natural Language & Linguistic Theory* 39: 1253–1306, [DOI](https://doi.org/10.1007/s11049-020-09496-6) | Primary full text, §§1–3: additive-operator diagnostics require an accessible state constituent. Greek judgements are not transferred to Iridian. The volume year is 2021, although first online publication was in 2020. |

Existing references were reused for the remaining comparisons. Harley 2013
§1 supports separating categorisation and external-argument introduction;
Harley 2011 and Embick–Noyer 2007 support the distinction between syntactic
composition and exponence. Their author manuscripts and primary publication
records were checked without borrowing draft pagination for published citations.
Menon–Pancheva's official proceedings abstract and Hanink–Koontz-Garboden's
full primary introduction and §2 support the qualified discussion of roots.

Pylkkänen chapter 2 and Baker–Vinokurova were checked against primary
publisher abstracts; the state-related Appl interpretation and Iridian case
mapping remain language-specific specifications. Kim's official KCI abstract
supports the narrow argument-inventory and expressive-predicate comparisons;
its metadata also confirms issue **105**, correcting the bibliography's
previous volume field. Smith et al. §§3.2–3.3, Tham §3.3 pp. 668–670 and Nam
§2.2 were checked in primary article text. Park's comparison is limited to
the [author abstract reproduced by the journal distribution platform](https://scholar.kyobobook.co.kr/article/detail/4010072083799),
with metadata corroborated by KCI; the full paper was not available. Murray
chapter 5 was checked against its primary publisher abstract.

These are claim-specific checks, not an audit of the entire bibliography.
The sources motivate analytical distinctions; they do not supply Iridian
grammaticality judgements, lexical licences or case paradigms.

## Independent review

Three fresh agents, none involved in drafting, reviewed the integrated
eleven-commit series:

| Reviewer | Remit | Result |
| --- | --- | --- |
| `independent_syntax_review` | Argument structure, case, composition, morphology and linked chapter consistency | No blocking finding; recommended removing doubled reference parentheses and making the beauty causative's conditional licence local. |
| `independent_sources_review` | Primary-source support, bibliographic metadata, locators and empirical boundaries | No blocking finding; confirmed all four added references and the Kim issue-field correction within the stated access limits. |
| `independent_coverage_review` | All eleven requirements, scope, commit separation, prose and rendered pages | All eleven covered; no blocking finding. Recommended keeping the hierarchy lead-in with its display. |

The follow-up removes the doubled parentheses, states the conditional
causable-transition licence beside `mužn-él-r-ime`, keeps the hierarchy
introduction with its formula and prevents an automatic word break inside
the stimulus-applicative form in its case table.

The review concerns the explicit constructed grammar. The recognised lexical
bivalent psychological class still lacks an individual Iridian case paradigm;
the stimulus-applicative NOM forms still lack separate illustrations. Neither
gap is filled by invented evidence.

The syntax reviewer rechecked the corrections and confirmed that both minor
recommendations were resolved without introducing a grammatical issue. The
coverage reviewer inspected all nine final subsection/boundary proof pages
and confirmed that the hierarchy lead-in, reference punctuation and intact
stimulus form were corrected, with no remaining actionable presentation
finding.

## Validation

The baseline source checks passed all 211 existing utility tests before
revision. After the review corrections, builds were run sequentially:

- `make` produced `build/full/grammar.pdf` (429 pages).
- `python3 scripts/check-log.py build/full/grammar.log` passed, with no
  missing glyphs, undefined references, fatal errors or overfull boxes.
- `make check` passed all publication source checks, the protected relative
  scope guard, all 211 utility tests, and the full and cover PDF diagnostics.
  Both final logs report zero overfull boxes.
- The final source check covers 38 files, 694 labels, 1,221 references,
  248 citation occurrences and 581 interlinear alignments. Existing stative
  fixtures and lexical records remain unchanged.
- `git diff --check` passed for the implementation series and final corrections.

Visual inspection covered 23 final PDF pages: the nine subsection/boundary
pages (physical 208–216, printed 194–202), nine affected or adjacent Chapter 7
pages (physical 130, 133–134, 137–138, 143–144 and 151–152), and the five
bibliography pages containing or continuing the added entries and corrected
Kim entry (physical 419–420, 422–423 and 428). Tables, formulae, tree,
diacritics, references and section transitions were legible and unclipped.

No commit contains the local instruction files. No push was performed.

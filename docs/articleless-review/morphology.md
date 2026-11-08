# Articleless morphology implementation

Base: `2ea86f3046beff0d55ee9f7f7e0f06bb31932e26`.

Owned files: chapters 4 and 8, and the five nominal tables in
`util/paradigm-tables/`. No other files were changed by this implementer.

## Baseline and ordinary-cell preservation

`/tmp/articleless-morphology-baseline.json` records every ordinary cell and its
cell-specific anchored counterpart before editing. There are exactly **102**
ordinary cells, covering 17 lexical noun rows in the five tables; alternate
direct plurals within a cell remain together in their original TeX macros.
After editing, an independent exact-cell comparator confirmed all 102 ordinary
cells unchanged. This includes y/ė spelling and the restored é–í/ó–ú contrasts,
all grades, irregular plural stems and ordinary case exponents.

The tables now have four columns (noun, case, singular, plural). Only anchored
columns were removed. The Class II citation cells retain `lobėk` and `perėk`,
Class VII retains `tězėň` and `obėl`, and Class V indirect `ráne` remains intact.
No suffix-stripping or phonological regularisation was performed.

## Chapter 4

Removed the productive anchoring section and all cumulative-exponence/PF
analysis. Removed proper-name anchored alternatives, preserving Marku/Marka and
Marcí/Markovi. Replaced the case/number/anchoring template with case and number
alone. Syncretisms remain described in ordinary case–number terms. Proper-name,
vocative and noun-class discussions retain their independent distributions.

Reviewed examples:
- Travó → Trava, with `bread.DIR.DEF` → `bread.DIR`; the definite English
  translation remains because the discourse may identify the bread.
- Preso → Pres, with its DEF gloss removed and explicit contextual explanation.
- byle/bylo/si byle comparison → two identical `byle` forms in new versus known
  group contexts, with specific unshared reference explained without a marker.
- nužo IPA example → independently established indirect `nužam`, preserving
  the purpose of demonstrating prevocalic /ʒ/.
- ránete → ráne in the contextual hand example, keeping identical morphology
  across newly introduced and previously identified readings.

Removed obsolete labels, for root integration to repair incoming references:
`sec:nm-def-allomorph`, `tab:nm-cumulative-anchoring`, `sec:nm-def-nondirect`,
`sec:nm-def-history`, `ex:nm-slot-anchored-patient`, table alias labels
`tab:nm-def-allomorphy` / `tab:nm-def-pl-classiii`.
New relevant targets: `sec:nm-reference-inflection` and
`ex:nm-slot-contextual-patient`. Existing labels with unchanged grammatical
content remain.

## Chapter 8

Removed anchored alternatives from event/participant singular table, preserving
exact ordinary pjáščikou/pjáščikovy/pjáščikově and
pjaštou/pjaštovy/pjaštově. Continuous participant `pjaštova` remains DIRECT
SINGULAR ONLY, with all obliques/plurals unspecified. No new form was inferred.
Removed obsolete label `sec:nm-def-contraction` rather than attach it to an
unrelated claim. Contextual event identification now has no dependence on
anchoring. Ordinary thematic dependents retain indirect case and their prior
actor/theme ambiguity.

Reviewed non-table forms:
- Veňo ×2 → Veň and removed corresponding DEF glosses.
- Nužo ×4 → Nuž; Bylo ×2 → Byl in unglossed stative examples.
- travěte → travě in expanded event and temporal-nominal examples.
- Retired pjáščikovat/pjaštovat, pjáščikovyte/pjaštovyte,
  pjáščikověte/pjaštověte alternatives only in anchored functions.

The historical -ov- nominalisation hypothesis remains as a clearly tentative
hypothesis, but no obsolete -ovat anchoring claim remains in active prose.
No protected -ový selection boundary was changed. One protected section loses
only the independently identified Nužo/Bylo anchored surface forms; the
main agent is handling exact normalization rather than blanket hash updates.

## Verification and limits

- Exact ordinary-cell comparator: **102/102 preserved**.
- Targeted scans: no AnchP/Anch0, `si`, DEF/Sanch glosses, anchored tables or
  anchored deverbal alternatives remain in the owned active files.
- `git diff --check`: passed at this checkpoint.
- Full integrated source checks and tests are owned by lead after all parallel
  edits integrate. No PDF success is claimed here.

No unresolved morphological form was invented. Historical evidence outside
these owned files remains untouched for the integration audit.

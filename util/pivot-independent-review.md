# Independent pivot revision review

Historical first-review snapshot on 16329d4. The later actual PR16 integration
and its fresh independent reviews are recorded in `pivot-integration-corpus-review.md`
and `pivot-integration-theory-review.md`; pending-integration statements below
describe the first review, not the current branch.

Reviewed 29 October 2026, against baseline `16329d4`. This review was performed
by an agent that did not author the chapter, corpus, bibliography or model
changes. No chapter was edited by the reviewer. The reviewed files were the
complete chapter diffs 1 and 3–9, all seven pivot utility records, the executable
model and independent fixture/test files. A later architecture patch is outside
this review's scope.

## Findings sent to the integrator

1. **P1 — Bibliography TeX group left open.**
   `util/negation-references.tex` retained `\begingroup` at its opening while the
   bibliography sorting/rewrite removed its closing `\endgroup`. Restore the
   closing group after `\end{thebibliography}`. This is a source-format defect
   even when the citation/label checker passes; a PDF build was expressly out
   of scope. Status: resolved in the reviewed revision.
2. **P2 — Agree candidate does not enforce its supplied licensing geometry.**
   `scripts/pivot_diagnostics.py::successive_agree_case` initially checked the
   goal set but ignored their relative licensing order. Reversing ordinary ERG
   input to `['T','A']` still returned A TRS, unlike the configurational
   candidate; the documented expanding lower search was no longer instantiated.
   Validate the external-over-selected licensing geometry, or explicitly make
   order insensitivity a separate candidate with a discriminating expectation.
   A naive-PF control alone does not test this property of the candidate itself.
   Status: resolved; both candidates now reject reversed external/selected ERG geometry and an independent regression exercises that rejection.
3. **P2 — Reflexive-causer diagnostic index mismatch.**
   Corpus B09 initially wrote `Pₖ.DIR svěᵢ Eⱼ.IND` while offering embedded Eᵢ
   as the intended antecedent. This does not actually test the stipulated
   coindexed lower referent. Align the string and context. Status: resolved in the reviewed revision.
4. **P2 — Directive order cannot be imported from indicative pivot-first.**
   Corpus O11 initially wrote `P.DIR A.TRS V.DIR-MOOD` as its directive control,
   whereas canonical overt contrastive subject `Jí trava piaštím` is A before
   T. Its H status prevents a false claim of attestation, but the control should
   use the canonical order or explicitly identify the inversion as a separate
   unestablished test. Status: resolved in the reviewed revision.
5. **P2 — Remaining categorical wh landing-site statements.**
   The inherited Chapter 6 multiple-wh account and Chapter 3 summary rows
   categorically identified fronted wh with lower SpecFocP despite the new
   Chapter 8 limit on pre-by derivations. Qualify those cross-references rather
   than adding movements. Final recheck confirms both Chapter 3 summary rows and Chapter 6 multiple-wh
   prose qualified. Status: resolved.

## Substantive conclusions

The new role inventories preserve the existing retained-theme > applied >
causee priority and correctly avoid counting an intransitive's theme-like sole
participant twice. Optional passive external dependents remain distinct from
active indirect objects. Nominal participant selection remains independent of
finite case valuation. The case-candidate exclusions are acknowledged supplied
hypotheses; agreement is not claimed to have been empirically observed.

The five main structural schemata are explicitly checkpoints and required
outputs, not claimed completed derivations. Their edge paths state necessary
conditions without pretending that an arrow licenses an edge. This is an honest
limit: a definitive SpecIP or lower-position theory is **not yet established**.
No later publication should describe these schemata as proof that all ten
acceptance criteria have been satisfied.

Binding additions correctly preserve `Svem Marku védnik`, its current quantity,
and the distinction between local actor–patient connectivity, pre-displacement
licensing and lower-copy interpretation. Causative/passive/nonfinite/nominal
antecedent tests remain unestablished. Corpus frames are systematically marked
C/P/H, with canonical starting evidence distinguished from new controls.

The modifier additions separate manner, frequency and temporal framing without
inferring unique attachment from lexical semantics. Concord does not cause or
prove raising. Quantifier truth models distinguish shared from distributed
witnesses, and negative scope controls distinguish ¬∃ from ∃¬. The locality model
correctly keeps DP nonmatching separate from export through opaque boundaries.

The extraction table preserves linked DIR/TRS topics, finite in-situ/fronted
wh, reduced -ový and nominal -ou selection, and external hanging topics. It
introduces no general syntactic ergativity, invented cleft paradigm or universal
coordination rule. Existing reduced indirect licensing agrees with Chapters 4
and 8; shared participant selection does not force finite I.

## Independent checks and access

All 72 corpus records were read, including canonical strings, contexts,
controlled contrasts and conditional predictions. Spot checks confirmed the
unanchored PF bread example, stative/intransitive forms, nominal forms and
finite wh-agent pair against current chapter source. The initial dedicated
model suite passed 10 tests; the findings above concern properties not covered
by that initial suite. Source-format and semantic checks do not establish the
unjudged Iridian readings.

Primary-source spot checks independently corroborated the research audit:
[Cambridge's original issue metadata](https://www.cambridge.org/core/journals/language/article/abs/mayan-agent-focus-and-the-ergative-extraction-constraint-facts-and-fictions-revisited/7EBA1153EB80EDEB4C4A14DE08F58163)
places Coon, Baier and Levin in *Language* 97(2), June 2021, 269–332,
DOI 10.1353/lan.2021.0019, despite its later online migration date. The abstract
supports the attributed bundled Ā/D intervention proposal for a subset of Mayan
languages; full article text was not accessed independently. [Annual Reviews](https://www.annualreviews.org/content/journals/10.1146/annurev-linguistics-011724-121342)
confirms Deal 2026, volume 12:227–247, advance publication 29 October 2025;
[Deal's author homepage](https://amyrosedeal.github.io/amyrosedeal/index.html)
also labels the Shawi paper 2026. No comparative theory is treated as Iridian
evidence by analogy.

## Integration limit

The actual-AspP/comment-field reconciliation, existential diagram reconciliation,
negative-Mood architecture and repository-wide `kady` correction remain in the
separate unpublished architecture task. They were neither copied nor reviewed
here. SpecAspP existential pivots, the linked topic-variable/copy account and
inactive finite case valuation in participant nominals must survive integration.
The pivot revision is reviewable independently; publication requires reviewing
the actual combined patch and rerunning the full source/regression suite.

## Final recheck

All five findings are resolved in the reviewed working tree. The bibliography
has its closing group; both model candidates reject reversed ERG licensing
geometry; B09 coindexes its actual offered lower antecedent; O11 uses the
canonical overt directive actor-before-theme control and explicitly limits it;
wh-site qualifications now agree across Chapters 3, 6 and 8. The added directive
fixtures separately license TRS on overt external participants and reject a
missing Mood licence.

The reviewer reran the dedicated suite: **12 tests passed**, covering **23
literal case frames** under both candidates plus the countermodels. The final
integrator log `/tmp/pivot-final-check.log` records **97 tests passed** for the
full source/utility check; `git diff --check` also passed independently. No PDF
was built or visually validated, as instructed. No blocking correctness issue
remains within this independent branch's reviewed scope. The architecture
integration boundary above remains a genuine dependency, and the theoretical
landing-site choice remains genuinely underdetermined.

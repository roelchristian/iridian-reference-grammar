# Ordinary ATTR and experiential extension: integration review

This pass extends draft PR #19 on `stative-reform`, beginning at reviewed head
`5a29478c793f0f15234a2c062cb5c3cc6e74cd9b`. Remote master remained
`b6c87551397faa5d661e2690b2ee72745d7bae40`; its PR #18 typesetting fix is
preserved. The user authorised implementation, commit and push to the same draft,
with no merge or PDF build.

## Adopted decisions

- Eleven lexical records separately specify semantic subclass, morphological
  class, finite principal parts, eligible nucleus/protected quantity, argument
  frame, gradability, aspect licences, Become and Manifest classes, ordinary
  ATTR class, stimulus, perspective, manner and conditional causative availability.
  The four broad subclasses are not separate automatic conjugations.
- Become strength is explicitly assigned by EL-S/EL-P membership. A short
  root alone does not license strong -él-. Previous tested free dynamic -ek,
  bound -ik and stative -ik distinctions remain intact.
- Manifest is adopted only for všihn- as listed derived Class A, with its own
  exposed e target: všihneša / všihnéšime / všihnéšek / všihnešáv /
  všihnešáž. The selected state description is nonveridical: the display may
  be feigned. Bound participant všihnéšikou, linked všihnéšice and
  evidential všihnéšekal remain distinct. Conditional higher Caus gives
  všihnéšrime with local é, not root í. No automatic Become stacking,
  inherited stimulus Appl, bodily-condition or relational productivity follows.
- Ordinary ATTR selects a property/reduced state, rather than a finite verb
  with Asp removed. Class I múžna and Class II hradná/svorná remain;
  Class III is listed only for všihňa/žbirňa, selecting existing local
  n→ň plus short -a. Manner všihně/žbirně remains a separate boundary.
  No agreement, definiteness, temporal anchoring or universal episodic contrast
  is assigned by class. Emphatic productivity is not enlarged.
- Genuine internal experience has a perspective dependency, defaulting to the
  speaker in independent declaratives. A non-default anchor requires an
  independently licensed relation and an identified relevant holder. Clause
  type alone or third person alone supplies neither that relation nor an
  obligatory evidential. Observable display and observable bodily readings
  are distinguished from direct internal-state assertions. Existing -al/-l
  and Mood/Evid/attitude ordering are unchanged.
- Retrospective state need not have ceased; contemplative state need not be
  unstarted. Experiencer, stimulus/content and actual cause remain distinct.

## Protected construction scope

No construction rule, interpretation, distribution, derivation, selection,
morphology or example for the deferred relative construction was changed.
`scripts/stative-scope-freeze.json` records the exact reviewed baseline above.
The guard compares 37 exponent-bearing source blocks, four complete source
spans (including rule paragraphs without the exponent), and three earlier
fixture/selection files. Lexicon entries are individually compared so ordinary
lexical metadata outside those entries can be updated. Negative mutation tests
reject changed rules, changed examples, new relative material and changed earlier
paradigm fixtures. The complete Chapter 8 relative section is unchanged.

The earlier paradigm report and fixture matrix remain the historical first-pass
baseline. The new report supersedes only their former unassigned ordinary
happiness-attributive/third-class status, without editing their relative material.

Final scope comparison: **zero discrepancies**. `git diff --check` passed.

## Fresh independent review

Grammar implementation, primary research and lexical diagnostics had separate
owners. Four fresh reviewers independently checked PF, syntax, academic evidence
and lexical/corpus consistency. Supported findings fixed and rechecked were:

1. smrn- lacks a recorded eligible vowel. Its PF forms remain withheld;
   no new repair or syllabic liquid is supplied.
2. torban- has the phonologically licit stem /tɔr.ban/ and final-root a
   as quantity target. Its finite, Become and ordinary ATTR classes remain
   unassigned. Conditional Class A / EL-S outputs are separate from licensed
   expected outputs; both unresolved records are rejected by the selector.
3. Observable conditions were brought under the shared experiential-condition
   broad subclass, preserving distinct argument/perspective flags.
4. Manifest does not assert an actual internal state or inherit its perspective
   restriction. Shifted anchoring now requires an explicitly identified holder,
   rather than a clause label or an unbound shift flag.
5. Derived-operation tests now cover all nine resolved entries. Documentation
   distinguishes permitted simple-State G1 from root reach through intervening
   Become/Manifest.

No unresolved defect was found in the adopted Manifest/ATTR rules or protected
scope. The lexical gaps below remain deliberately unresolved.

## Evidence and limits

Final `make check-source`: **143 tests passed**, including 16 new lexical tests
and five scope-guard tests; 19 active source files, 469 labels, 755 references,
89 citations, 314 interlinear alignments and 43 explicit pronunciation examples.
Original case, pivot, quantity, evidential, phasal and shallow-heading regressions
remain passing. The extension contains 11 records, **90 validated State/Become
cells across nine resolved records plus five Manifest cells**, with ordinary
derived operations and conditional causative predictions. PF tables explicitly
record the other two entries as withheld. Tests do not claim native attestation
or automatic full phonetic analysis.

The complete 229-line, 20,148-byte Library brief was read through the supported
Library read route. Research verifies Nam, Song, Park, Kim, Frellesvig and Wandl,
with full-text versus abstract/metadata access limits recorded in
`stative-extension-source-audit.md`. Corrections include the Korean journal
Eoneohag rather than the international Linguistics, Kim's full title and author
romanisation, and Wandl's actual title/DOI/final pagination. Comparative research
does not establish any Iridian form or history.

Unadopted: smerňa, attributive doublets, an asserted -ja history,
new smrn- repairs, unassigned torban- principal parts, broader Manifest productivity,
unlisted ordinary ATTR classes and expanded analytic neh- selection. The
remaining PF gaps need independent lexical evidence rather than decorative
irregularity. The separate result-state/threshold exponent remains unintroduced.

No PDF, merge, deployment or approving GitHub review was performed. The previously
Forbidden check-runs endpoint was not retried or bypassed; hosted CI must not be
reported green without available evidence.

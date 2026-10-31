# Proposals for the remaining nominalisation gaps

Status: working proposals, not implemented in the reference grammar. Prepared 28 October 2026 against commit `fe7489524df4a171b760c4bfc64a6325171018e6`, which has been pushed to `origin/master`. This file is intentionally untracked.

## 1. Recommended decisions

Retain the established singular *-ou/-ov-* alternation, extend its stable *-ov-* stem through the plural, and use the existing Class III plural endings *-y*, zero, and *-ám*. Continuous participant nominals should share that stem and those case–number endings, with their existing direct singular *-ova* and a new regular anchored direct *-ovato*. This supplies complete paradigms without adding another set of plural endings.

For combined valency operations, preserve the established causative forms and specify participant selection after the complete derivation. Causativised applicatives should select the applied participant in the perfective and retrospective, but the causer in the three nominative-alignment aspects. This choice preserves the finite causative case rule and the existing progressive *piaštébnajime*. It deliberately restricts which participants a given derivation can nominalise: an indirect participant does not become an alternative referent merely because it can be expressed inside the nominal.

These decisions are additions to the constructed language. Existing morphology and comparative scholarship constrain their plausibility; neither establishes the proposed forms as pre-existing Iridian facts.

## 2. Existing constraints

The relevant current treatments are:

- [Nominal stem formation and declension](chapters/04-nouns.tex), labels `sec:nm-stemform`, `sec:nm-declension`, `sec:nm-stem-grades`.
- [Anchoring and number](chapters/04-nouns.tex), labels `sec:nm-def-allomorph`, `sec:nm-def-contraction`, `sec:nm-num`, `sec:nm-derived-inflection`.
- [Valency, nominalisation, and the two n-morphemes](chapters/03-verbs.tex), labels `sec:vm-antipassive-desc`, `sec:vm-appl`, `sec:aspect-caus`, `sec:vm-n`, `sec:nominalised`, `sec:vm-tension-n`.
- [Stress and /v/](chapters/02-phonology.tex), labels `sec:stress`, `sec:v-realisation`.

The grammar already specifies singular *piaščikou/piaščikovy/piaščikově* and anchored *piaščikovat/piaščikovyte/piaščikověte*, alongside the corresponding event-nominal paradigm. It extends this singular scheme to other *-ou*-final aspectual forms, but leaves their plurals and continuous inflection unspecified. Class III supplies singular *-a/-y/-ě* and plural *-y/zero/-ám*; quantity alternation belongs to specified lexical subclasses rather than applying automatically to every stem.

Case and number occupy one fused morphological slot. The *-ou* class therefore cannot acquire a separate, freely concatenated plural suffix without revising that account. Anchoring follows case–number, ordinarily using full *-to/-te* after a vowel and reduced *-o/-e* after a consonant; front/back selection is class-conditioned. The special *-ovat* exponent is currently restricted to anchored direct singulars in *-ou*.

The causative distinguishes lexical patient, causee, and causer. In the perfective and retrospective, its causer is transitive, its causee indirect with a transitive base, and its patient direct; with an intransitive base, the causee is direct. In the nominative-alignment aspects the causer is direct and lower participants are indirect. The written examples establish *piašt-na-n-ik*, *piašt-na-n-av*, and *piaštébnajime*, segmented *piašt-éb-naj-ime*. The applicative precedes the causative, while antipassive and applicative cannot combine.

## 3. Inflection of the deverbal family

### 3.1. Stem and case–number rules

Let **X** be the material preceding the nominalising family: *piaščik-* for perfective agent nominalisation, *piaštnik-* for perfective patient nominalisation, *piašt-* for the event noun, and *piašt-* for the continuous agent nominal. The last two have distinct internal structures despite sharing X.

| Case–number | Non-continuous participant or event nominal | Continuous participant nominal |
|---|---|---|
| Direct singular | X-*ou* | X-*ova* |
| Transitive singular | X-*ov-y* | X-*ov-y* |
| Indirect singular | X-*ov-ě* | X-*ov-ě* |
| Direct plural | X-*ov-y* | X-*ov-y* |
| Transitive plural | X-*ov-∅* | X-*ov-∅* |
| Indirect plural | X-*ov-ám* | X-*ov-ám* |

The non-continuous direct singular retains its specialised *-ou* grade. All remaining cells use *-ov-*, with continuous direct singular adding *-a*. The shared ordinary endings reproduce the stable-stem Class III pattern; this is a proposed constructional assignment, not a deduction from the spelling *-ova*. Treat the family as a derived subtype using Class III endings with specialised direct-singular exponence, rather than adding a seventh macroclass. This revises the current statement that continuous obliques are unspecified.

At Vocabulary Insertion, the case–number node selects *-y* for transitive singular or direct plural, *-ě* for indirect singular, zero for transitive plural, and *-ám* for indirect plural. Direct-singular exponence is construction-specific. There is no independent plural morpheme and no rule deleting an already inserted singular *-ou* before a plural suffix.

Keep X invariant across the nominal paradigm. Do not import the lexical length alternation of *trava/tráv*, raise a root vowel, or mutate a root consonant again. The inherited quantity in contemplative *-ách-* and applicative *-éb-* remains. Front-grade indirect *-ě* has the existing palatal effect on the adjacent labial *v*, without reaching back across *-ov-* to the lexical root.

### 3.2. Complete proposed paradigms

An asterisk is not used for proposed forms, since it would misleadingly mark them as ungrammatical. “Existing” below means explicitly specified by the current treatment; every remaining cell is a proposal.

| Case–number | Perfective agent: plain / anchored | Status |
|---|---|---|
| Direct singular | *piaščikou / piaščikovat* | Existing |
| Transitive singular | *piaščikovy / piaščikovyte* | Existing |
| Indirect singular | *piaščikově / piaščikověte* | Existing |
| Direct plural | *piaščikovy / piaščikovyte* | Proposed |
| Transitive plural | *piaščikov / piaščikove* | Proposed |
| Indirect plural | *piaščikovám / piaščikováme* | Proposed |

| Case–number | Continuous agent: plain / anchored | Status |
|---|---|---|
| Direct singular | *piaštova / piaštovato* | Plain existing; anchored proposed |
| Transitive singular | *piaštovy / piaštovyte* | Proposed |
| Indirect singular | *piaštově / piaštověte* | Proposed |
| Direct plural | *piaštovy / piaštovyte* | Proposed |
| Transitive plural | *piaštov / piaštove* | Proposed |
| Indirect plural | *piaštovám / piaštováme* | Proposed |

| Case–number | Event nominal: plain / anchored | Status |
|---|---|---|
| Direct singular | *piaštou / piaštovat* | Existing |
| Transitive singular | *piaštovy / piaštovyte* | Existing |
| Indirect singular | *piaštově / piaštověte* | Existing |
| Direct plural | *piaštovy / piaštovyte* | Proposed |
| Transitive plural | *piaštov / piaštove* | Proposed |
| Indirect plural | *piaštovám / piaštováme* | Proposed |

The same rule gives perfective patient plural *piaštnikovy/piaštnikov/piaštnikovám*, retrospective agent plural *piaščavovy/piaščavov/piaščavovám*, progressive agent plural *piaštimovy/piaštimov/piaštimovám*, and contemplative agent plural *piaštáchovy/piaštáchov/piaštáchovám*. Anchoring follows the same cell-specific rules throughout.

### 3.3. Anchoring

Preserve *X-ou → X-ovat* exclusively for non-continuous direct singulars. Continuous *X-ova* takes regular back-coded full *-to*, producing *X-ovato*. All other cells take front-coded anchoring, extending the established front-coded singular obliques and the Class III plural pattern: full *-te* after *-y* or *-ě*, reduced *-e* after zero-ended *-ov* or consonant-final *-ám*.

Thus *piaštovato* is continuous direct singular, while *piaštovat* is the anchored event nominal. The new continuous form follows *travato*; it does not spread the special *-ovat* realisation to every word containing *ov*. The Class V noun *ránou* remains outside this construction.

An anchored direct plural such as *piaščikovyte* identifies a discourse-relevant plurality; it does not thereby mean all eaters or the only eaters. Speaker anchoring with *si* remains an alternative realisation of Anch and cannot be added to a suffixally anchored form.

### 3.4. Syncretism and pronunciation

Transitive singular and direct plural are syncretic, as in existing Class III. In addition, event *piaštou* and continuous participant *piaštova* share their non-direct-singular forms. This is the principal cost of the recommended paradigm. Their interpretation must follow from syntactic position, lexical interpretation, modifiers, and context; no ending is claimed to disambiguate it categorically. If a unique form is essential, the proposition can be expressed as a finite clause rather than assigning a new meaning to anchoring.

Final /v/ in proposed *piaščikov* is a coda [w], while the added vowel of anchored *piaščikove* places /v/ in an onset. Written *v* is retained in both. Stress remains on the first syllable of the lexical prosodic word; *ou* is one nucleus and the *i* in initial *pia-* marks palatality rather than adding a syllable. Acute accents mark quantity. No new stress, vocalisation, or vowel-deletion rule is required. The longer causative strings likewise provide vowel nuclei at the suffix boundaries: *piašč-na-ji-kou*, for example, can distribute its obstruents across a coda and a nasal onset within the existing cluster limits, without a syllabic consonant or unlicensed consonant loss.

The tempting alternatives *-ovóv* and *-ovim*, modelled on other noun classes, would introduce another mixed paradigm without explaining the continuous singular. Giving continuous forms an extra oblique extension *-ovav-* would preserve more contrasts, but would add an otherwise unsupported stem grade. The shared stable *-ov-* paradigm is preferable if the resulting syncretism is accepted.

## 4. Number and interpretation

Participant plurals denote pluralities of individuals satisfying the participant description. Several eaters may share an event, or each may participate in a different event; plural morphology alone selects neither reading. A contemplative participant plural may denote existing people expected to eat without asserting that any eating has occurred.

Event plurals should denote at least two contextually individuated occurrences. Eventive *piaštovy* can consequently mean eating occasions when the context supplies suitable boundaries. This is a proposed count use alongside unbounded singular *piaštou* ‘eating’. Recurrence does not itself supply the event units: repeated bites within one meal need not count as several occasions, and grammatical plurality does not encode habitual aspect. Event-kind readings require an independently available generic or classificatory context.

Lexical *piaštou* ‘food’ retains its mass interpretation. A formally available plural does not automatically mean portions, dishes, or types of food. Preserve the current requirement for a measure interpretation with mass nouns; do not stipulate a new lexical count sense merely to populate the inflectional table.

Cardinals continue to select singular morphology. Accordingly, proposed direct-case phrases include *hroná piaščikou* ‘three individuals who ate’ and *hroná piaštova* ‘three individuals who eat’. In a count-event context, *hroná piaštou* can mean ‘three eating occasions’; it does not mean ‘three portions of food’ without a measure expression. These are constructed noun phrases, not attestations, and make no assumptions about finite agreement.

This separation of countability from eventhood is compatible with San Martin’s (2009) discussion of event plurals and mass-like event nominals (§§2–4). Her analysis does not supply the Iridian endings or entail that every event nominal must pluralise. The Iridian count-event rule proposed here is a language-specific choice.

## 5. Combined valency operations

### 5.1. Repair the structural account before extending the paradigm

The current prose places antipassive, applicative, and *-n-* in one Voice slot, although its applicative tree projects a separate ApplP. It also places Voice below CausP while spelling patient Voice after *-na-* in *piašt-na-n-ik*. These are architectural inconsistencies; assigning meanings to additional strings would not resolve them.

I recommend retaining distinct ApplP and VoiceP. A high applicative introduces an event-related participant above VP, with the agent-introducing Voice layer above it; CausP selects the resulting VoiceP. The schematic hierarchy is:

`nPART / Rel > Asp > Caus > Voice > Appl > v/VP`

Appl and Caus are optional. Antipassive Voice selects a complement without Appl; patient-oriented Voice *-n-* likewise excludes Appl. An applicative derivation uses the compatible zero Voice form. The existing exclusions thus become explicit feature-selection restrictions rather than an assertion that distinct heads literally occupy one node. Applied-participant privilege is supplied by Appl and interpreted by Asp, independently of the presence of another direct-case nominal in a finite applicative clause.

Pylkkänen’s high-applicative analysis supplies a model for an event-related applied participant, including with an unergative base. It does not make the Iridian incompatibility conditions necessary. Those restrictions must be stated independently. This represents a consequential clarification of the current framework: “high” means above the lexical event domain, not necessarily above Voice.

For causative patient forms, preserve underlying Voice below Caus but specify a narrowly restricted PF ordering rule:

`root–Voice[n]–Caus[na]–Asp → root–Caus[na]–Voice[n]–Asp`

The rule applies only to adjacent *n* and *na* in this construction. It yields established *piašt-na-n-ik* and *piašt-na-n-av*, without reversing semantic scope. Applicative *-éb-* and antipassive stem formation retain their existing positions before Caus. Glide insertion applies after this ordering: *-na-n-* contains no vowel hiatus, whereas *-na-* immediately before vowel-initial *-ik-*, *-av-*, *-ova*, *-imou*, or *-áchou* takes *-naj-*.

This is an added morphotactic stipulation. Hyman’s study of Bantu suffix ordering documents a relevant distinction between surface suffix order and semantic scope (§2, especially example 3 in the author manuscript); it does not establish this particular Iridian reordering rule. If that PF exception is adopted, the grammar’s categorical formulation that every suffix order transparently mirrors head order must be qualified at the corresponding overview passages.

### 5.2. A deterministic selection rule

After valency derivation, embedded Asp supplies the following participant-selection instructions. Finite case valuation remains inactive under nominalisation, and overt non-selected dependents receive nominal indirect case.

| Derivation | Perfective / retrospective referent | Continuous / progressive / contemplative referent |
|---|---|---|
| Simple intransitive | Sole participant | Sole participant |
| Simple transitive with antipassive | Agent | Derivation excluded |
| Simple active transitive | Bare derivation excluded | Agent |
| Patient Voice *-n-* | Lexical patient | Lexical patient |
| Applicative without Caus | Applied participant | Applied participant |
| Causative of intransitive | Causee | Causer |
| Causative of ordinary transitive, with patient Voice | Lexical patient | Lexical patient if *-n-* is present |
| Active causative of ordinary transitive | Bare patient-licensing derivation excluded | Causer |
| Causative of antipassive base | Causee, i.e. the lower agent | Derivation excluded |
| Causative of applicative base | Applied participant | Causer |

For causativised applicatives, the applied participant is the affected internal core participant privileged in the ergative domain. Causativisation introduces a higher causer, which becomes the default selected participant in the nominative domain. This follows the existing causative case description and progressive combined example, while adding the previously unspecified ergative combined rule. The lower theme, causee, and causer remain distinct roles; the applied participant need not be the causee or the lexical patient.

Do not add a second Voice or reverse Appl and Caus merely to make another participant accessible. Under the recommended restrictions, a perfective causative cannot freely nominalise its causer; a causative of a transitive base cannot freely nominalise its causee; and a nominative-domain causativised applicative cannot freely nominalise its applied participant. These are specified restrictions on participant nominalisation, replacing an open-ended gap rather than promising every conceivable orientation. Finite clauses with overt participants remain available for the corresponding propositions.

The *-ový* relative uses exactly the same selection table. Replacing the nominal head with Rel cannot change the referent from causee to causer or from applied participant to theme. A non-selected participant may constrain the description through nominal relational licensing, but that dependent does not determine which participant the head nominal or relative gap denotes.

### 5.3. Proposed forms and interpretations

The following direct singulars are new extrapolations, checked against the current bound aspect exponents, causal glide rule, applicative quantity, and antipassive stem *piašč-*.

| Form | Segmentation | Selected participant and interpretation |
|---|---|---|
| *piaštnanikou* | *piašt-na-n-ik-ou* | Lexical patient: ‘that which someone caused someone to eat’, perfective |
| *piaštnanavou* | *piašt-na-n-av-ou* | Lexical patient in a retrospective caused-eating event |
| *piaštnanova* | *piašt-na-n-ova* | Lexical patient of continuous causative passive |
| *piaštnanimou* | *piašt-na-n-im-ou* | Lexical patient of progressive causative passive |
| *piaštnanáchou* | *piašt-na-n-ách-ou* | Prospective lexical patient of caused eating |
| *piaštnajova* | *piašt-naj-ova* | Causer: ‘one who causes someone to eat’, continuous |
| *piaštnajimou* | *piašt-naj-im-ou* | Causer of an eating event in progress |
| *piaštnajáchou* | *piašt-naj-ách-ou* | Prospective causer of eating |
| *zmacnajikou* | *zmac-naj-ik-ou* | Causee: ‘one whom someone caused to run’, perfective |
| *piaščnajikou* | *piašč-naj-ik-ou* | Causee/lower eater after antipassive: ‘one whom someone caused to eat’, perfective |
| *piaštébnajikou* | *piašt-éb-naj-ik-ou* | Applied beneficiary or recipient of a caused eating/feeding event, perfective |
| *piaštébnajavou* | *piašt-éb-naj-av-ou* | Applied participant in a retrospective caused applicative event |
| *piaštébnajova* | *piašt-éb-naj-ova* | Causer of the applicative event, continuous |
| *piaštébnajimou* | *piašt-éb-naj-im-ou* | Causer: ‘one who is making someone feed someone’, progressive |
| *piaštébnajáchou* | *piašt-éb-naj-ách-ou* | Prospective causer of the applicative event |

English past-oriented perfective translations presuppose a suitable temporal context; the forms introduce no tense. The beneficiary reading of *-éb-* is the default. Goal, location, and instrument readings remain available where the existing lexical and contextual conditions license them. English ‘feed’ is an idiomatic rendering of the established eating-applicative construction, not evidence for an extra causative morpheme inside *-éb-*.

The table gives no independent causative agent prefix or invented inflection. Non-continuous *-ou* forms enter the proposed *-ov-* declension, and continuous *-ova* forms enter its continuous variant. For example, *piaštébnajikovy* is proposed transitive singular or direct plural of the perfective applied-participant nominal, whereas *piaštébnajovy* is the corresponding case–number form of continuous causer *piaštébnajova*.

## 6. Checks required if these proposals are adopted

The morphological proposals resolve the listed missing cells; the valency proposals additionally require coordinated theoretical revisions. Implementation should update the overview template, Appl and Voice trees, *-na-n-* discussion, nominalisation selection rules, case–number inventories, anchoring tables, and all incoming descriptions of unrestricted applicative orientation. The structural change should be explained once where Appl is introduced, with references from the other treatments.

Useful acceptance contrasts are:

1. Existing *piaščikou/piaščikovat* remain unchanged, while *piaštova/piaštovato* preserve the continuous direct vowel under regular anchoring.
2. New direct plural *piaščikovy* and transitive singular *piaščikovy* are morphologically identical but receive their interpretation from case licensing and number context.
3. Proposed *hroná piaščikou* retains singular morphology under a cardinal; free plural *piaščikovy* supplies no exact cardinality.
4. Event plural *piaštovy* counts contextually individuated occurrences without automatically pluralising mass ‘food’ or asserting habitual aspect.
5. *piaštébnajikou* and *piaštébnajimou* differ in selected participant as specified by aspect after Caus; an indirect nominal cannot silently reverse their orientation.
6. Existing finite *piašt-na-n-ik* retains its surface order. The derivation, reordering rule, and glide timing must jointly produce it without an extra *j*.
7. Antipassive forms remain excluded from the three nominative-alignment aspects; suppressed patients remain unavailable as finite arguments. Nominal Theme dependents remain licensed only by the nominal relational mechanism.
8. New *-ou/-ový* forms retain the AspP boundary and cannot acquire internal *za-* merely because their valency structure is larger.

Rebuild and run the log and publication checks sequentially, then inspect the expanded tables and revised trees. No such implementation or build change is included in this proposal file.

## 7. Research consulted and evidential limits

The current bibliography was checked first. Baker and Vinokurova already support the distinction between lexical agent nouns and richer relative-like participant descriptions. The additional research below addresses the newly proposed count-event rule and the structural problems exposed by combined valency operations; it does not license particular Iridian strings.

- **Baker, Mark C., and Nadya Vinokurova. 2009.** ‘On agent nominalizations and why they are not like event nominalizations.’ *Language* 85(3): 517–556. [DOI](https://doi.org/10.1353/lan.0.0144); [author manuscript](https://sites.rutgers.edu/mark-baker/wp-content/uploads/sites/199/2019/07/agent-nominals-web.pdf). The author manuscript was consulted for the existing structural distinction, which these proposals preserve; it supplies no Iridian inflectional or orientation rule.
- **San Martin, Itziar. 2009.** ‘Derived nominals from the nominal perspective.’ *Anuario del Seminario de Filología Vasca “Julio de Urquijo”* 43(1–2). [Publisher record](https://ojs.ehu.eus/index.php/ASJU/article/view/1764); [full text](https://ojs.ehu.eus/index.php/ASJU/article/download/1764/1396/5262); [DOI](https://doi.org/10.1387/asju.1764). Sections 2–4 were consulted for event pluralisation and nominal countability. The publisher record gives 831–845, while the PDF running citation gives 831–846; that pagination discrepancy should be resolved before adding a final bibliography entry. The narrow point used here is that event interpretation and telicity do not by themselves determine plural availability.
- **Pylkkänen, Liina. 2008.** *Introducing Arguments*. Cambridge, MA: MIT Press. [Publisher record](https://mitpress.mit.edu/9780262662093/introducing-arguments/). This is already named in the current applicative analysis, although not entered in its focused bibliography. The publisher overview confirms the compositional approach to additional arguments. For the particular high-Appl definition and position below Voice, the inspected source was the [MIT 24.953 Spring 2003 handout on Pylkkänen’s 2002 thesis](https://ocw.tau.edu.ng/courses/linguistics-and-philosophy/24-953-argument-structure-and-syntax-spring-2003/lecture-notes/applpylkkanenspring03.pdf), pp. 1–2, especially diagrams 5 and 11. The handout distinguishes an event-related high applicative from a transfer relation between individuals; no claim is made to have verified a page-specific passage in the 2008 book. The [MIT thesis record](https://dspace.mit.edu/entities/publication/ab4ea336-1d8f-4a9a-81ef-ce9bfa9335ff) independently confirms the underlying argument-introducer framework.
- **Hyman, Larry M.** ‘Suffix ordering in Bantu: a morphocentric approach.’ [Author manuscript, revised September 2002](https://linguistics.berkeley.edu/~hyman/Bantu_suffix_order_hyman.pdf); [published-paper scan](https://linguistics.berkeley.edu/~hyman/papers/2003-hyman-ordering.pdf). The [author’s publication list](https://linguistics.berkeley.edu/~hyman/) identifies the publication as 2003. Section 2, especially example 3, was consulted for fixed affix order across different scopes. This motivates distinguishing morphotactics from semantic composition; the specific Iridian PF swap is an independent proposal, and neither the Bantu template nor Hyman’s particular formal implementation is imported.

The recommended forms are internally derived design choices. There is no claim of speaker judgement, corpus attestation, or comparative proof that these are the uniquely natural continuations of Iridian. The most consequential choices are accepting event–continuous syncretism and adopting a restricted PF exception for causative patient Voice; both should remain explicit when this note is reviewed.

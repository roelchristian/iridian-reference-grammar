# Pivot syntax: controlled diagnostic corpus

Research began on `16329d482d621e09492badeaa654651975735a18`; integrated and reviewed against PR16 master `87c23bbcb8ea59f62e415cb315a45f79613e1dc6` (29 October 2026).

These 72 records compare analyses; they do not certify a landing site. The current grammar's constructed examples are canonical specifications, not independently elicited native-speaker evidence. **C** marks an existing canonical example or explicitly documented construction; **P** marks a new proposed test specification whose grammaticality and reading remain unestablished; **H** marks a hypothetical role-indexed prediction, not an Iridian sentence or proposed new paradigm. A C record can contain a new controlled contrast: only its cited starting fact is canonical. No star or rejection is added unless the source explicitly supplies it. English translations alone do not establish scope, binding, or entailment.

**A** is movement to SpecIP, the leading hypothesis for ordinary finite clauses. **B** is movement to an independently motivated lower Asp/orientation-related position; its height relative to the operator field must be fixed before evaluating a prediction. **C₀** is a base/restructuring control preserving the patient's low thematic origin. All three preserve participant selection and the case paradigms. Agree alone does not pronounce a DP higher. No record establishes a universal PivotP, obligatory reconstruction, general syntactic ergativity, or the claim that head-final VP derives patient-before-agent order. Case implementation is an additional axis, compared in the accompanying case analysis.

Notation: `A` actor, `P` retained lexical patient/theme, `B` applied participant, `C` causer, `E` causee, `M` matrix antecedent; subscripts identify referents, not surface positions. DIR/TRS/IND indicate case, PF/IPFV alignment domain, `TOP(...)` a linked topic, and `HT(...)` an external hanging topic. Role-indexed strings deliberately avoid inventing lexical allomorphs. `svem/svě/svy` retain the direct/transitive/indirect paradigm. An index on an anaphor specifies the reading being tested, not an established antecedent. `∅ᵢ` is a contextually supplied argument, not a newly licensed arbitrary pro. Square brackets identify construction domains. Each context is to be held constant across its contrast unless the varied factor is explicitly discourse context.

Sources are repository paths and stable section/example labels. Existing vowel quantity, `zemac-`, evidential `-al`, contemplative `-áž` and its conditioned allomorphs, `jas`, `hladě` and `mó` remain unchanged. Canonical **kady** and the actual AspP versus descriptive Comm-field distinction are retained from PR16. The comment field is not a single established attracting head; IP abbreviates Mood and inner evidentiality when present. A SpecIP hypothesis still needs a substantive head and an independently defined displacement condition.

For every unestablished contrast, record acceptance, intended reading, alternative readings and context separately before adopting any new specification. Absence of a judgment is an unresolved result, not evidence against a candidate. The predictions below are conditional consequences to test independently of the desired outcome.

## Basic order and aspect (12)

### O01 — C

- **Source:** `chapters/03-verbs.tex, sec:vm-asp-case`.
- **String/schema:** Marek travě piaštíme.
- **Context and target reading:** All-new eating report; Marek is eating bread.
- **Controlled contrast:** Compare O02, holding the same unanchored bread referent and actor; source PF counterpart is in tab:valency-base-contrasts.
- **Competing predictions:** A: actor may satisfy I locally; B: actor may satisfy lower selection; C₀: ordinary actor-high base order suffices. This row alone does not discriminate.

### O02 — C

- **Source:** `chapters/03-verbs.tex, tab:valency-base-contrasts`.
- **String/schema:** Trava Marku piaštník.
- **Context and target reading:** All-new completed eating report, with the same participants as O01.
- **Controlled contrast:** IPFV A.DIR P.IND V versus PF P.DIR A.TRS V; do not substitute anchored Travó without controlling definiteness.
- **Competing predictions:** A: P must cross A; B: selected P must precede A if the lower landing is high enough; C₀: requires a stated reordering/restructuring operation. VP head-finality explains only P<V.

### O03 — C

- **Source:** `chapters/03-verbs.tex, sec:vm-asp-case`.
- **String/schema:** Marek zemácime.
- **Context and target reading:** All-new activity report; only Marek runs.
- **Controlled contrast:** Compare Marek zemácek in tab:valency-base-contrasts.
- **Competing predictions:** A: no long dependency; B: same sole participant; C₀: same surface order. Aspect does not create an absent second argument.

### O04 — C

- **Source:** `chapters/03-verbs.tex, tab:valency-base-contrasts`.
- **String/schema:** Byl ščénime. / Byl ščének.
- **Context and target reading:** Child arrives, ongoing versus completed; same child and discourse status.
- **Controlled contrast:** Hold unaccusative base constant while varying aspect.
- **Competing predictions:** A: sole low participant may raise; B: lower raising may suffice; C₀: base position must still derive DP<V. Surface coincidence does not locate I.

### O05 — C

- **Source:** `chapters/03-verbs.tex, tab:valency-base-contrasts`.
- **String/schema:** Problem svórnime. / Problem svórnik.
- **Context and target reading:** A problem develops in size versus undergoes bounded growth.
- **Controlled contrast:** Hold the stative/change-of-state lexical base constant.
- **Competing predictions:** A/B: aspect switches need not switch the sole selected referent; C₀: same prediction. Do not infer an actor from an English subject.

### O06 — C

- **Source:** `chapters/07-information-structure.tex, ex:tc-neutral-top and ex:tc-marked-agent-top`.
- **String/schema:** Tak tóm Markuto koupnik. / Markuto tak tóm koupnik.
- **Context and target reading:** Book-topic versus Marek-topic contexts, with identical anchoring and aspect.
- **Controlled contrast:** Change linked aboutness relation only; book stays DIR and Marek TRS.
- **Competing predictions:** A: Top movement crosses the clause-internal pivot independently; B: same A′ access required; C₀: must separate discourse fronting from neutral order. None may change case.

### O07 — H

- **Source:** `chapters/06-simple-sentence.tex, sec:word-order; 07-information-structure.tex, sec:tc-marked-topics`.
- **String/schema:** P.DIR A.TRS V.PF / TOP(A.TRS) P.DIR t_A V.PF
- **Context and target reading:** Two reports of the same event; first all-new, second continues A.
- **Controlled contrast:** Hold anchoring, referents and PF fixed, unlike an uncontrolled new-topic contrast.
- **Competing predictions:** A/B: high topic above a distinct lower selected P; C₀: discourse operation cannot be the only source of neutral P-first order.

### O08 — H

- **Source:** `chapters/03-verbs.tex, sec:vm-asp-case`.
- **String/schema:** A.DIR P.IND V.IPFV / TOP(P.IND) A.DIR t_P V.IPFV
- **Context and target reading:** Continue a discussion of P during an ongoing event.
- **Controlled contrast:** Patient-linked topic with unchanged IPFV frame; grammaticality of the fully lexicalised test remains to be specified.
- **Competing predictions:** A/B: P-topic does not replace selected A; C₀: must preserve independent alignment and discourse ordering. No automatic DIR reassignment.

### O09 — C

- **Source:** `chapters/03-verbs.tex, sec:vm-antipassive`.
- **String/schema:** Marek piášček.
- **Context and target reading:** An eating activity is reported without an independently licensed patient.
- **Controlled contrast:** Compare ordinary Trava Marku piaštník with referential patient.
- **Competing predictions:** A/B: select sole actor, not a silent restored patient; C₀: cannot obtain the transitive order by treating the absent patient as an overt core DP.

### O10 — C

- **Source:** `chapters/03-verbs.tex, sec:vm-passive`.
- **String/schema:** Travó Marcí piaštníme. / Travó piaštníme.
- **Context and target reading:** Same ongoing eating event; agent overt versus contextually omitted.
- **Controlled contrast:** Patient remains anchored DIR in both variants.
- **Competing predictions:** A/B: passive patient selection survives agent omission; C₀: requires construction-specific passive configuration. IND agent is not an ordinary active IND patient.

### O11 — H

- **Source:** `chapters/03-verbs.tex, sec:vm-asp-case; sec:mood-directive-case`.
- **String/schema:** A.DIR P.IND V.IPFV / A.TRS P.DIR V.DIR-MOOD
- **Context and target reading:** Compare an assertion with a directive concerning the same participants.
- **Controlled contrast:** Mood-conditioned theme selection versus active IPFV actor selection. The directive control follows the canonical contrastive overt-agent order in Jí trava piaštím; it does not assert neutral directive pivot-first order. Overt A is supplied only where independently licensed. Do not use this as an aspect-only pair.
- **Competing predictions:** A/B: attracting eligibility must incorporate Mood without a [pivot] label; C₀: restructuring must reflect Mood rather than a PF suffix selecting retroactively.

### O12 — H

- **Source:** `chapters/03-verbs.tex, sec:vm-asp-case; 06-simple-sentence.tex, sec:word-order`.
- **String/schema:** P.DIR A.TRS V.PF / P.DIR A.TRS V.RETRO
- **Context and target reading:** Same completed event presented as bounded versus anterior; fixed referents and aboutness.
- **Controlled contrast:** PF/retrospective within ERG domain.
- **Competing predictions:** A/B/C₀: preserve P-first and cases under this within-domain change; a mechanism wrongly tying selection solely to completion fails.

## Binding and pronouns (12)

### B01 — C

- **Source:** `chapters/04-nouns.tex, sec:nm-pron-refl`.
- **String/schema:** Svemᵢ Markuᵢ védnik.
- **Context and target reading:** Marek sees his own person; local actor antecedent.
- **Controlled contrast:** Compare B02; index annotates the source reflexive reading.
- **Competing predictions:** A: pre-movement licensing or a lower interpreted copy can preserve A>P binding; B: same options; C₀: must preserve actor c-command or supply an independently justified anaphoric mechanism. No result singles out obligatory reconstruction.

### B02 — C

- **Source:** `chapters/04-nouns.tex, sec:nm-pron-refl`.
- **String/schema:** Iⱼ Markuᵢ védnik.
- **Context and target reading:** Marek sees another salient person.
- **Controlled contrast:** Source demonstrative permits disjoint reference; test i=j separately without presupposing rejection.
- **Competing predictions:** A/B/C₀: distinguish local anaphoric licensing from demonstrative reference. Discourse coreference is not a structural binding diagnostic by itself.

### B03 — H

- **Source:** `chapters/04-nouns.tex, sec:nm-pron-refl; 03-verbs.tex, sec:vm-asp-case`.
- **String/schema:** Aᵢ.DIR svyᵢ V.IPFV / svemᵢ Aᵢ.TRS V.PF
- **Context and target reading:** Same seeing event and self-directed reading; fix contextual antecedent.
- **Controlled contrast:** Change aspect and anaphor case together as required by the canonical case paradigm.
- **Competing predictions:** A/B: low patient connectivity can remain under both alignments; C₀: cannot place PF patient above its only structural antecedent without explaining binding. Both judgments remain unestablished.

### B04 — H

- **Source:** `chapters/03-verbs.tex, sec:vm-passive; 04-nouns.tex, sec:nm-pron-refl`.
- **String/schema:** svemᵢ Aᵢ.IND V.PASS.IPFV
- **Context and target reading:** Overt passive agent is the intended antecedent.
- **Controlled contrast:** Compare active B03 while holding role identities fixed; test local binding rather than mere shared reference.
- **Competing predictions:** A/B: patient raising cannot itself confer binder status on optional passive agent; C₀: also requires a defined agent position/binding domain. Agent case alone decides none of these.

### B05 — H

- **Source:** `chapters/03-verbs.tex, sec:vm-passive`.
- **String/schema:** svemᵢ ∅ᵢ V.PASS.IPFV
- **Context and target reading:** Discourse supplies a specific omitted actor versus no recoverable actor.
- **Controlled contrast:** Same passive reflexive with recoverable versus unspecified agent; no arbitrary silent binder is assumed.
- **Competing predictions:** A/B/C₀: require independent silent-antecedent licensing; lower-copy interpretation does not manufacture an antecedent.

### B06 — H

- **Source:** `chapters/03-verbs.tex, sec:vm-appl; 04-nouns.tex, sec:nm-pron-refl`.
- **String/schema:** Bⱼ.DIR Aᵢ.IND svyᵢ V.APPL.IPFV
- **Context and target reading:** Actor acts on self for a distinct beneficiary.
- **Controlled contrast:** Compare svyⱼ with applied participant as intended antecedent; keep roles fixed.
- **Competing predictions:** A/B: evaluate A and B c-command at their thematic positions, not shared IND morphology; C₀: specify equivalent local asymmetry. Neither alternative reading is established.

### B07 — H

- **Source:** `chapters/03-verbs.tex, sec:vm-caus; ex:val-caus-transitive`.
- **String/schema:** svemᵢ Cⱼ.TRS Eᵢ.IND V.CAUS.PF
- **Context and target reading:** Causee acts on self; causer is distinct.
- **Controlled contrast:** Compare B08 on the identical three-person configuration.
- **Competing predictions:** A/B: access from low theme through Caus must preserve causee binding if licensed; C₀: must preserve the low E>P relation. A phase edge used for movement does not automatically enlarge the binding domain.

### B08 — H

- **Source:** `chapters/03-verbs.tex, sec:vm-caus; ex:val-caus-transitive`.
- **String/schema:** svemⱼ Cⱼ.TRS Eᵢ.IND V.CAUS.PF
- **Context and target reading:** Causer is the intended antecedent; causee acts on causer.
- **Controlled contrast:** Compare B07; only the intended antecedent changes.
- **Competing predictions:** A/B/C₀: distinguish cross-causative anaphoric licensing from ordinary coreference. A causer reading would constrain the domain; its rejection cannot be presumed from theory.

### B09 — H

- **Source:** `chapters/03-verbs.tex, tab:causative-frames; 04-nouns.tex, tab:nm-reflexive`.
- **String/schema:** Pₖ.DIR svěᵢ Eᵢ.IND V.CAUS.PF
- **Context and target reading:** Reflexive occupies causer TRS position; only embedded Eᵢ or a discourse referent is offered as antecedent.
- **Controlled contrast:** Contrast a reflexive causee svyᵢ with a distinct higher Cᵢ.TRS.
- **Competing predictions:** A/B/C₀: predict an asymmetry only under a specified structural binding rule; morphological case is not the rule. Record possible logophoric/coreferential readings separately.

### B10 — H

- **Source:** `chapters/07-information-structure.tex, sec:tc-marked-topics; 04-nouns.tex, sec:nm-pron-refl`.
- **String/schema:** TOP(Aᵢ.TRS) svemᵢ t_A V.PF
- **Context and target reading:** Marek remains aboutness topic while seeing self.
- **Controlled contrast:** Compare B01 without linked topicalisation; keep actor anchoring fixed.
- **Competing predictions:** A/B: A′ movement may preserve a previously licensed local dependency; C₀: same connectivity requirement. High topic status alone must not license a nonlocal anaphor.

### B11 — H

- **Source:** `chapters/08-complex-sentences.tex, sec:poby; 04-nouns.tex, sec:nm-pron-refl`.
- **String/schema:** Mᵢ [Aⱼ svemᵢ/ⱼ V FIN] poby V.MATRIX / Mᵢ [∅ᵢ svemᵢ V NONFIN] V.MATRIX
- **Context and target reading:** Embedded actor j and matrix participant i are both salient in the finite control; in the nonfinite partner, explicitly test a construction with a licensed silent local actor controlled by Mᵢ, holding the intended action and theme constant.
- **Controlled contrast:** Local j versus nonlocal i reading in an independently finite complement, paired with a nonfinite-complement test of a silent local antecedent. The nonfinite licensing/control relation and reflexive form require independent specification; the schema does not assert their availability.
- **Competing predictions:** A/B/C₀: specify the finite binding domain first; matrix coreference does not demonstrate long-distance syntactic binding. If the nonfinite silent actor/control relation is independently licensed, a reading mediated by that local actor differs from direct long-distance binding by Mᵢ. Pivot movement within either complement cannot itself supply a missing antecedent or control relation.

### B12 — H

- **Source:** `chapters/04-nouns.tex, sec:nm-derived-participant; 08-complex-sentences.tex, sec:th-rel-structure`.
- **String/schema:** [Aᵢ.IND svyᵢ/ⱼ V-NMLZ] / [Aᵢ svyᵢ/ⱼ V-REL] Nⱼ
- **Context and target reading:** Nominal/relative internal actor versus host-noun referent as antecedent.
- **Controlled contrast:** Compare local nominal antecedent with external discourse antecedent; contrast event and participant nominal domains separately.
- **Competing predictions:** A/B: no finite I requirement may be imported; C₀: nominal licensing still needs an explicit mechanism. Existing finite B01 does not settle these judgments.

## Modifiers and scope (12)

### S01 — C

- **Source:** `chapters/06-simple-sentence.tex, sec:lexical-adverb-position`.
- **String/schema:** Skorňe zemácime.
- **Context and target reading:** Speaker runs quickly; actor is omitted and contextually first person.
- **Controlled contrast:** Compare an overt actor test in S02; do not infer pivot height from this actorless string.
- **Competing predictions:** A/B/C₀: compatible with low manner attachment; no overt pivot means no pivot-versus-manner precedence result.

### S02 — P

- **Source:** `chapters/06-simple-sentence.tex, sec:lexical-adverb-position`.
- **String/schema:** Marek skorňe zemácime. / Skorňe Marek zemácime.
- **Context and target reading:** All-new report with no adverb focus or frame-setting context.
- **Controlled contrast:** Only the placement of overt actor relative to manner varies.
- **Competing predictions:** A: predicts actor above low manner under I raising; B: prediction depends on lower-site height; C₀: must fix overt actor origin and linearisation. Acceptance of either new order remains unestablished.

### S03 — C

- **Source:** `chapters/06-simple-sentence.tex, sec:lexical-adverb-position`.
- **String/schema:** Skorňe travě piaštíme.
- **Context and target reading:** Speaker eats bread quickly; no overt actor.
- **Controlled contrast:** Compare hypothetical P.DIR skorňe A.TRS V.PF and skorňe P.DIR A.TRS V.PF.
- **Competing predictions:** A: PF selected P should precede genuinely low manner; B: depends on landing height; C₀: preserves the canonical low complement but must derive neutral P>A separately.

### S04 — H

- **Source:** `chapters/06-simple-sentence.tex, sec:lexical-adverb-position`.
- **String/schema:** P.DIR A.TRS skorňe V.PF / P.DIR skorňe A.TRS V.PF
- **Context and target reading:** All-new completed event with manner fixed and neither actor nor adverb focused.
- **Controlled contrast:** Actor-versus-manner placement after a constant initial P.
- **Competing predictions:** A/B: constrain the actor remainder independently of P landing; C₀: same requirement under restructuring. A successful P-first derivation alone is insufficient.

### S05 — H

- **Source:** `chapters/06-simple-sentence.tex, sec:lexical-adverb-position`.
- **String/schema:** P.DIR roca A.TRS V.PF / roca P.DIR A.TRS V.PF
- **Context and target reading:** Repeated completed events; frequency modifies events rather than degree of speed.
- **Controlled contrast:** Hold P and A fixed and vary frequency placement; compare S03 low manner separately.
- **Competing predictions:** A: predicts P above frequency only if roca attaches below I; B: can differ if between I and lower site; C₀: needs semantic event-quantification attachment, not a forced manner slot.

### S06 — H

- **Source:** `chapters/06-simple-sentence.tex, sec:word-order; 07-information-structure.tex, sec:tc-adverbials`.
- **String/schema:** bych P.DIR A.TRS V.PF / P.DIR bych A.TRS V.PF
- **Context and target reading:** Fix yesterday as an already supplied, neutral temporal frame in the same all-new event report for both orders.
- **Controlled contrast:** Vary frame–pivot order while holding frame salience, prosody, participants and discourse context constant; test contrastive frame-fronting in a separate context pair. Do not treat bych as low manner.
- **Competing predictions:** A/B/C₀: permit a frame outside the clause-internal pivot configuration where independently licensed. Frame-first is not evidence that P occupies TopP.

### S07 — H

- **Source:** `chapters/01-overview.tex, sec:grammatical-architecture; 06-simple-sentence.tex, sec:th-particle-framework`.
- **String/schema:** P.DIR COMM A.TRS V.PF / COMM P.DIR A.TRS V.PF
- **Context and target reading:** Additive/affirmative comment operator, no linked topic, fixed focus.
- **Controlled contrast:** Only pivot-versus-Comm-field order varies; preserve the PR16 working hierarchy, but do not infer a single Comm head or a uniform operator type from the shared field.
- **Competing predictions:** A: pivot above the field if I is above it; B: a lower site beneath it predicts opposite neutral order; C₀: must independently derive either order. Operator PF placement must be fixed first.

### S08 — H

- **Source:** `chapters/05-function-words.tex, sec:class1-particles; 06-simple-sentence.tex, sec:th-particle-framework`.
- **String/schema:** P.DIR vy/so A.TRS V.PF / vy/so P.DIR A.TRS V.PF
- **Context and target reading:** Same reference stages; use already and still contexts separately.
- **Controlled contrast:** Hold particle meaning and topiclessness fixed; do not equate vy with so.
- **Competing predictions:** A: high I pivot precedes genuinely lower Phas; B: distinguishes sites above versus below Phas; C₀: needs a structural attachment and linearisation independently of scope.

### S09 — C

- **Source:** `chapters/07-information-structure.tex, sec:tc-quantificational-pivots`.
- **String/schema:** Deno že zastráda.
- **Context and target reading:** Nothing is lacking to the speaker: no relevant thing lacks, not some thing escaping negation.
- **Controlled contrast:** Compare a positive indefinite in the same environment only after its licensed form is specified.
- **Competing predictions:** A: pronounced-high deno requires a lower semantic occurrence or another explicit concord interpretation; B: lower position can supply scope directly; C₀: same. Negative concord is not caused by raising.

### S10 — H

- **Source:** `chapters/07-information-structure.tex, sec:tc-quantificational-pivots`.
- **String/schema:** ∃P.DIR ∀A.TRS V.PF
- **Context and target reading:** Separate context: one common patient for all actors versus a possibly different patient per actor.
- **Controlled contrast:** Hold surface order constant; seek ∃>∀ and ∀>∃ readings with truth-conditionally distinct scenarios.
- **Competing predictions:** A/B: lower-copy interpretation may allow inverse scope but does not require it; C₀: semantic reconstruction cannot be assumed absent or present merely from no DP raising. Record actual readings before selecting a theory.

### S11 — H

- **Source:** `chapters/03-verbs.tex, ex:val-caus-transitive`.
- **String/schema:** ∃P.DIR C.TRS ∀E.IND V.CAUS.PF
- **Context and target reading:** One object caused to be acted on by everyone versus different objects per causee.
- **Controlled contrast:** Keep causee and causer readings distinct and test scope inside the caused event.
- **Competing predictions:** A/B: must combine movement locality with low interpretation through a Caus edge; C₀: low thematic position permits composition but neutral P-first still needs a derivation. Scope alone does not prove movement.

### S12 — H

- **Source:** `chapters/06-simple-sentence.tex, sec:th-exclusive-phasal; scripts/phasal-fixtures.json`.
- **String/schema:** TOP(A.TRS) P.DIR kamo vy V.PF
- **Context and target reading:** Compare EXCL(Phas(P)) with the specifically licensed Phas(EXCL(P)); use a context in which their truth values differ.
- **Controlled contrast:** Keep kamo pronounced in its established field and focus association fixed; contrast the two semantic compositions, not arbitrary particle reversal.
- **Competing predictions:** A/B/C₀: preserve the bounded licensed alternatives. Neither pivot height nor linear kamo-before-vy entails unrestricted inverse scope or converts focused P into TopP.

## Applicatives and causatives (16)

### V01 — C

- **Source:** `chapters/03-verbs.tex, ex:val-appl-transitive`.
- **String/schema:** Marek travě bylam my piaštíme. / Byl Marcí travě piaštébime.
- **Context and target reading:** Same actor, bread and child; child benefits but does not eat.
- **Controlled contrast:** Benefactive PP versus core applied DP; preserve event and role identities.
- **Competing predictions:** A/B: different selected argument but same low theme; C₀: event-related Appl structure must distinguish PP from core B. Affixhood does not establish low Appl.

### V02 — C

- **Source:** `chapters/03-verbs.tex, ex:val-appl-ergative`.
- **String/schema:** Byl Marcí zemacébime.
- **Context and target reading:** Running benefits the child; actor remains Marek.
- **Controlled contrast:** Compare transitive V01 with retained bread absent.
- **Competing predictions:** A/B/C₀: B.DIR A.IND without any retained P; no causee or second actor may be inferred.

### V03 — C

- **Source:** `chapters/03-verbs.tex, ex:val-appl-ergative`.
- **String/schema:** Byl Marku travě piaštébik.
- **Context and target reading:** Completed eating for child, distinct actor and theme.
- **Controlled contrast:** Compare V01 IPFV applicative; B stays DIR, A switches IND/TRS, P stays IND.
- **Competing predictions:** A/B: selected B may cross actor but P is not selected; C₀: same case frame must arise from event-related Appl. A two-DIR output is already excluded by source.

### V04 — C

- **Source:** `chapters/03-verbs.tex, ex:val-appl-goal`.
- **String/schema:** Marek hraďe de stojáž. / Hrad Marcí stojébaž.
- **Context and target reading:** Projected directed motion to the town, without benefit entailment.
- **Controlled contrast:** Goal PP versus applied goal; retain contemplative quantity and its conditioned short -až.
- **Competing predictions:** A/B/C₀: select applied town rather than mover in simple Appl. Do not equate all applied roles semantically or lengthen stojébaž mechanically.

### V05 — C

- **Source:** `chapters/03-verbs.tex, ex:val-appl-instrument`.
- **String/schema:** Marek travě ráne se piaštíme. / Rán Marcí travě piaštébime.
- **Context and target reading:** Hand is an implement for eating.
- **Controlled contrast:** Instrumental PP versus core instrument; fixed actor/theme.
- **Competing predictions:** A/B/C₀: preserve Rán.DIR with actor/theme IND in Appl; hand never becomes actor. A model assigning only beneficiary semantics overgenerates the wrong entailment.

### V06 — C

- **Source:** `chapters/03-verbs.tex, sec:mood-directive-valency; sec:vm-appl`.
- **String/schema:** Trava bylam piaštébím. / Trava bylam piaštébká.
- **Context and target reading:** Command versus inclusive exhortation to eat for child.
- **Controlled contrast:** Hold theme and applied beneficiary constant across directive Mood types.
- **Competing predictions:** A/B: Mood prioritises retained P and leaves B.IND; C₀: same output under a Mood-sensitive structure. Simple indicative B selection must not survive as a second DIR.

### V07 — C

- **Source:** `chapters/03-verbs.tex, ex:val-caus-intransitive`.
- **String/schema:** Marek bylam zemácrime. / Byl Marku zemác-r-an-ik.
- **Context and target reading:** Marek causes the same child to run; ongoing versus completed.
- **Controlled contrast:** Causer DIR/Causee IND versus Causee DIR/Causer TRS.
- **Competing predictions:** A/B: PF E dependency crosses C, not an imagined retained theme; C₀: must derive the same role reversal without changing the lexical base. Case domain must include the licensed causer.

### V08 — C

- **Source:** `chapters/03-verbs.tex, ex:val-unaccusative`.
- **String/schema:** Marek bylam ščenérime. / Byl Marku ščen-ér-an-ik.
- **Context and target reading:** Marek causes the child to arrive.
- **Controlled contrast:** Match V07 but vary unergative versus unaccusative base.
- **Competing predictions:** A/B/C₀: child remains causee despite its theme-like arrival role; no extra retained P may outrank B in an applied counterpart.

### V09 — C

- **Source:** `chapters/03-verbs.tex, ex:val-caus-transitive`.
- **String/schema:** Marek bylam travě piáštrime.
- **Context and target reading:** Causer causes child to eat bread, ongoing.
- **Controlled contrast:** Compare V10 with identical roles; control definiteness separately from aspect.
- **Competing predictions:** A: outer C may satisfy I locally; B: outer C selected under NOM; C₀: ordinary causer-high base order possible. E and P remain IND.

### V10 — C

- **Source:** `chapters/03-verbs.tex, ex:val-caus-transitive`.
- **String/schema:** Travó Marku bylam piášt-r-an-ik.
- **Context and target reading:** Same caused eating event completed, anchored bread.
- **Controlled contrast:** For strict aspect-only comparison use a role-indexed anchored P in V09 too.
- **Competing predictions:** A/B: P crosses E and C; a phase edge or justified nonphasal Caus is necessary if the lower domain closes; C₀: requires explicit restructuring. Neither bare matching nor suffix order removes locality.

### V11 — C

- **Source:** `chapters/03-verbs.tex, ex:val-caus-appl`.
- **String/schema:** Marek býlac bylam travě piaštébrime.
- **Context and target reading:** Children eat bread for a distinct child beneficiary under Marek causation.
- **Controlled contrast:** Compare V12, preserving four participant indices and anchoring.
- **Competing predictions:** A/B/C₀: C.DIR E.IND B.IND P.IND in NOM; embedded Appl cannot assign independent DIR.

### V12 — C

- **Source:** `chapters/03-verbs.tex, ex:val-caus-appl`.
- **String/schema:** Trava Marku býlac bylam piaštéb-r-an-ik.
- **Context and target reading:** Completed four-participant event, benefit of the caused eating.
- **Controlled contrast:** Identical inventory to V11; PF theme outranks beneficiary and causee.
- **Competing predictions:** A/B: selected P access must cross E and C without treating every intervening DP as phase; C₀: retains low P origin and separately derives pronunciation. Correct output P.DIR C.TRS E.IND B.IND.

### V13 — C

- **Source:** `chapters/03-verbs.tex, ex:val-caus-appl-intransitive`.
- **String/schema:** Marek býlac bylam zemacébrime. / Byl Marku býlac zemacéb-r-an-ik.
- **Context and target reading:** Children run for a distinct child beneficiary under Marek causation.
- **Controlled contrast:** Compare V12 after removing retained theme, without removing Appl.
- **Competing predictions:** A/B/C₀: PF B now selected before E, with C.TRS and E.IND. Failure to change selection after removing P falsifies the implementation.

### V14 — C

- **Source:** `chapters/03-verbs.tex, ex:val-caus-antipassive`.
- **String/schema:** Byl Marku piáščeranik.
- **Context and target reading:** Child eats under Marek causation; no independently licensed lexical patient.
- **Controlled contrast:** Compare V07 two-participant frame, but preserve lower AP restriction to ERG.
- **Competing predictions:** A/B/C₀: E.DIR C.TRS; patient cannot be restored to outrank E. A hypothetical NOM -aš- counterpart is excluded by source, not newly rejected here.

### V15 — C

- **Source:** `chapters/03-verbs.tex, sec:vm-passive`.
- **String/schema:** Trava Marcí bylam piášt-r-an-ime.
- **Context and target reading:** Bread is caused by Marek to be eaten by child; optional passive causer.
- **Controlled contrast:** Compare active V09 and omit only the optional causer in a second test.
- **Competing predictions:** A/B: outer passive selects P in NOM without assigning TRS to C; C₀: needs an explicit passive licensing difference. Shared IND on C/E does not prove identical status.

### V16 — H

- **Source:** `chapters/03-verbs.tex, ex:val-caus-appl and following scope account`.
- **String/schema:** CAUS[APPL_B[EAT(E,P)]] / [B my] CAUS[EAT(E,P)]
- **Context and target reading:** First context: child benefits from eating; second: beneficiary benefits from causing, even if eating itself is harmful.
- **Controlled contrast:** Distinguish caused-event benefaction from causing-event PP adjunct; do not insert a second productive Appl.
- **Competing predictions:** A/B/C₀: fixed inner -éb-r- structure predicts embedded-event benefaction; outer benefaction needs separately licensed my. Case/probe implementation must preserve this scope difference.

## Information structure and extraction (12)

### I01 — C

- **Source:** `chapters/07-information-structure.tex, ex:tc-marked-agent-top`.
- **String/schema:** Markuto tak tóm koupnik.
- **Context and target reading:** Continue discussion of Marek, not a correction of the book.
- **Controlled contrast:** Compare Tak tóm Markuto koupnik with identical morphology.
- **Competing predictions:** A/B: linked TRS agent crosses selected P under an A′ feature distinct from orientation; C₀: same discourse dependency remains available. A universal ergative extraction ban fails.

### I02 — C

- **Source:** `chapters/07-information-structure.tex, sec:tc-multiple-topics`.
- **String/schema:** Marko tak tóm bych ktářnik.
- **Context and target reading:** External Marek-topic, with ordinary contextual recovery of the lower agent.
- **Controlled contrast:** Contrast linked Markuto, not a case-changing operation on the same dependency.
- **Competing predictions:** A/B/C₀: HT is external with resumption/recovery; it does not establish an A′ chain crossing P. DIR-like topic form does not reassign argument case.

### I03 — C

- **Source:** `chapters/07-information-structure.tex, sec:tc-multiple-topics`.
- **String/schema:** Tak dvor Marko ten na býdlime.
- **Context and target reading:** Yard as external location frame; ten resumes it inside clause.
- **Controlled contrast:** Compare I01 linked argument topic, controlling discourse aboutness separately.
- **Competing predictions:** A/B/C₀: external/resumptive structure must be distinguished from argument extraction. No surface first-position diagnostic alone separates them.

### I04 — C

- **Source:** `chapters/06-simple-sentence.tex, ex:wh-four-combinations`.
- **String/schema:** Marek jena mulša?
- **Context and target reading:** Neutral information request about Marek residence.
- **Controlled contrast:** Null Pol, wh after Marek; compare I05–I07.
- **Competing predictions:** A/B/C₀: preserve the canonical order; neutral wh need not move to a high focus site. This is not an extraction restriction on any case.

### I05 — C

- **Source:** `chapters/06-simple-sentence.tex, ex:wh-four-combinations`.
- **String/schema:** Marek jena by mulša?
- **Context and target reading:** Interactionally explicit question, same residence information.
- **Controlled contrast:** Only overt versus null Pol differs from I04.
- **Competing predictions:** A/B/C₀: must preserve pre-by Marek and jena. Head-initial Pol above a sole lower FocP does not by itself derive this string; no arbitrary repair movement is stipulated.

### I06 — C

- **Source:** `chapters/06-simple-sentence.tex, ex:wh-four-combinations`.
- **String/schema:** Jena Marek mulša?
- **Context and target reading:** Where is salient/contrasted; Marek residence remains questioned.
- **Controlled contrast:** Only marked wh prominence differs from I04.
- **Competing predictions:** A/B/C₀: separate wh fronting from clause typing and pivot selection. Null Pol allows the order without settling the pre-by problem.

### I07 — C

- **Source:** `chapters/06-simple-sentence.tex, ex:wh-four-combinations`.
- **String/schema:** Jena by Marek mulša?
- **Context and target reading:** Both question and wh variable foregrounded.
- **Controlled contrast:** Compare I05, keeping overt by and meaning.
- **Competing predictions:** A/B/C₀: pre-by wh needs a justified higher site, construction-specific by placement or revised fronting analysis. None is selected solely to save a hierarchy.

### I08 — C

- **Source:** `chapters/06-simple-sentence.tex, sec:th-wh-interrogation`.
- **String/schema:** Tak tóm jeda koupnik? / Jeda tak tóm koupnik?
- **Context and target reading:** Ask who bought a fixed book; neutral versus salient agent variable.
- **Controlled contrast:** Wh agent is lower versus fronted while patient remains DIR.
- **Competing predictions:** A/B: a nonmatching selected P need not block a wh probe, but a causative phase still requires separate access; C₀: same finite accessibility. Not a reduced-relative paradigm.

### I09 — C

- **Source:** `chapters/08-complex-sentences.tex, sec:th-rel-structure; 04-nouns.tex, sec:nm-ovni`.
- **String/schema:** Canonical-construction paraphrase (not a verbatim example): [P-gap V.PF-REL(-ový)] N / [A-gap V.ANTIP.PF-REL(-ový)] N
- **Context and target reading:** Describe patient of completed action versus actor of an activity.
- **Controlled contrast:** Role-indexed rendering of documented orientation contrast; use listed morphological cells before lexicalisation.
- **Competing predictions:** A/B: reduced Rel selects an aspectual description without finite I; C₀: same construction restriction. A failed active PF agent relative does not entail failed finite agent wh.

### I10 — C

- **Source:** `chapters/04-nouns.tex, sec:nm-derived-participant`.
- **String/schema:** piaštníkou / piáščikou / piaštébikou
- **Context and target reading:** Identify eaten entity, eater, or beneficiary of eating.
- **Controlled contrast:** Keep participant nominal -ou distinct from prenominal relative -ový.
- **Competing predictions:** A/B/C₀: shared embedded selection, independent nominal dependent licensing. No shared finite landing position follows from participant identity.

### I11 — H

- **Source:** `chapters/03-verbs.tex, ex:val-caus-transitive; 06-simple-sentence.tex, sec:th-wh-interrogation`.
- **String/schema:** WH(E).IND P.DIR C.TRS t_E V.CAUS.PF
- **Context and target reading:** Ask for causee while patient is fixed and selected.
- **Controlled contrast:** Compare a wh causer and wh patient within the same causative; keep discourse prominence fixed.
- **Competing predictions:** A/B: specify which DPs match interrogative search and whether an embedded boundary closes; C₀: restructuring cannot silently create finite A′ access. New causative extraction judgments remain unestablished.

### I12 — H

- **Source:** `chapters/08-complex-sentences.tex, sec:th-complex-overview; sec:coordination`.
- **String/schema:** CLEFT(P) / EXTRACT(A) FROM [CONJ₁ & CONJ₂]
- **Context and target reading:** No canonical general cleft or coordination-extraction paradigm is supplied.
- **Controlled contrast:** Hold these schemata out of the accepted-language corpus; document the missing construction licensing before testing case accessibility.
- **Competing predictions:** A/B/C₀: no prediction can be counted as a success without independently licensed constructions. This record prevents an invented language-wide extraction rule.

## Existentials and reduced clauses (8)

### E01 — C

- **Source:** `chapters/06-simple-sentence.tex, sec:existential-constructions`.
- **String/schema:** Byl jeca. / Byl zada.
- **Context and target reading:** Introduce a child versus deny any child presence, without a prior aboutness topic.
- **Controlled contrast:** Hold existential construction and child description fixed.
- **Competing predictions:** A: ordinary finite I raising must not be imposed universally; B: low existential Asp position is independently supplied; C₀: low existential base remains possible. Negation conditions zad-, not pivot selection.

### E02 — C

- **Source:** `chapters/06-simple-sentence.tex, sec:existence-and-presence`.
- **String/schema:** Canonical-construction paraphrase (not a verbatim example): DP.DIR LOCATION.IND na jeca / DP.DIR LOCATION.IND na zada
- **Context and target reading:** Entity present versus absent at a named location.
- **Controlled contrast:** Role-indexed canonical locative frame; compare bare E01 without changing the root selection rule.
- **Competing predictions:** A/B/C₀: preserve DP as sole direct existential argument and location as oblique; PP placement alone cannot establish DP raising to I.

### E03 — C

- **Source:** `chapters/06-simple-sentence.tex, sec:existence-possession`.
- **String/schema:** Bylam na tóm jeca. / Bylam na tóm zada.
- **Context and target reading:** Child has a book versus lacks a book; possession is locative-style relation.
- **Controlled contrast:** PP-initial possessor with low direct book; contrast bare existential.
- **Competing predictions:** A: cannot force universal pivot-first surface order; B: construction-specific low domain compatible; C₀: same. Suppletion is independent of PP initiality.

### E04 — C

- **Source:** `chapters/06-simple-sentence.tex, sec:exst-vs-ident`.
- **String/schema:** Lúbcí piáščikou jeca. / Janek lúbcí piáščikou.
- **Context and target reading:** Introduce a participant satisfying an eating description versus identify Janek as that participant.
- **Controlled contrast:** Same nominal description, existential versus zero-copula identification.
- **Competing predictions:** A/B/C₀: distinguish matrix predication from internal nominal selection. Shared -ou does not impose one matrix movement derivation.

### E05 — C

- **Source:** `chapters/06-simple-sentence.tex, sec:existential-presentatives`.
- **String/schema:** Canonical-construction paraphrase (not a verbatim example): [V-REL(-ový) N].DIR jeca / [V-NMLZ(-ou)].DIR jeca
- **Context and target reading:** Introduce overt-headed individual versus headless participant description.
- **Controlled contrast:** Keep event and selected participant fixed; distinguish nominal internal head from matrix pivot.
- **Competing predictions:** A/B/C₀: matrix existential argument remains nominal in both, while Rel and NMLZ have different category/selection. No finite I inside either reduced predicate is inferred.

### E06 — H

- **Source:** `chapters/04-nouns.tex, sec:nm-derived-participant; 03-verbs.tex, tab:causative-frames`.
- **String/schema:** [CAUS(E,P).PF-NMLZ_P].DIR jeca / [CAUS(E).PF-NMLZ_E].DIR jeca
- **Context and target reading:** Present selected retained theme versus causee when no retained theme exists.
- **Controlled contrast:** Remove only P from the role inventory; corresponding morphological cells require independent listing.
- **Competing predictions:** A/B: embedded selection can survive without finite I; C₀: same. The priority P>B>E belongs to the complete derived predicate, not the matrix existential landing site.

### E07 — H

- **Source:** `chapters/06-simple-sentence.tex, sec:exst-indef-neg`.
- **String/schema:** [participant description].DIR zada / deno [finite NEG predicate]
- **Context and target reading:** Deny existence of an individual satisfying a description versus use a concord indefinite in an ordinary finite predicate.
- **Controlled contrast:** Separate existential negation and concord licensing; do not add deno automatically to -ou clauses.
- **Competing predictions:** A/B/C₀: zad- suppletion and deno concord need their own licensing; lower existential scope does not prove the same movement or binding domain as an ordinary finite clause.

### E08 — H

- **Source:** `chapters/04-nouns.tex, sec:nm-derived-participant; 08-complex-sentences.tex, sec:th-rel-structure`.
- **String/schema:** [B-selected APPL.PF-NMLZ] / [P-selected CAUS(APPL(P)).PF-REL] N
- **Context and target reading:** First identify beneficiary of simple applied event; then identify retained patient of causative applied event.
- **Controlled contrast:** Contrast shared participant-selection machinery under different highest orientation domains and different nominal heads.
- **Competing predictions:** A/B/C₀: do not reinstate embedded B selection above Caus or impose finite I on reduced predicates. Record selection separately from each construction’s pronounced gap/argument position.

## Evaluation and unresolved decisions

This corpus provides controlled questions and independently stated consequences, not 72 confirmed judgments. Canonical frames constrain all three analyses; C₀ is not dismissed merely because its overt-order derivation needs work. B must name an independently projected site before its operator-order predictions become falsifiable. A must supply noncircular eligibility, intervention conditions and actual phase access before a causative derivation is complete. A closer DP and an inaccessible phase complement are different obstacles.

| Acceptance criterion | Current result from this corpus |
| --- | --- |
| Canonical neutral orders without arbitrary permutations | A/B have candidate movement templates; C₀ needs an explicit restructuring derivation. O02 alone settles none. |
| Existing case/orientation paradigms | Fixed by O01–O12 and V01–V15; any implementation must reproduce these independently of its landing-site choice. |
| Noncircular attracting features | Not established by direct-case labels; test Mood/Appl/Caus changes on fixed inventories. |
| Causative intervention and phase access | V10/V12/I11 expose the requirement; no unestablished extraction judgment is counted as evidence of access. |
| Reflexive configurations | B01 establishes connectivity; B03–B12 leave cross-causative, passive and nominal antecedent domains open. |
| Pivot versus operators and low adverbs | S02–S08 require new controlled judgments and settled operator PF architecture. |
| Scope distinct from surface order | S09 fixes negative-concord interpretation; S10–S12 separate competing scope readings and restricted composition. |
| Agent topicalisation and wh extraction | I01/I08 preserve canonical finite agent accessibility; reduced restrictions cannot override it. |
| Reduced/existential construction differences | E01–E08 prohibit a universal finite landing site; exact reduced locality remains a separate question. |
| No gratuitous projection/operation | No PivotP added. B’s site and C₀’s restructuring must each earn independent motivation. |

No candidate yet meets all necessary conditions for a definitive landing-site decision. The open by/FocP derivation (I05/I07) is recorded separately and cannot be solved by hiding extra movements in a pivot analysis. The integrated corpus preserves PR16’s actual AspP versus descriptive Comm-field distinction, lower polarity licensed by negative Mood, bounded kamo/phasal composition with topic-variable/lower-copy association, and distinct reduced -ou/-ový selecting heads. The four-way wh surface paradigm remains unchanged. Those canonical mechanisms do not supply the still-missing pivot-height or causative-phase judgments.

# Case computation and locality: comparative working analysis

Research record, 29 October 2026. Baseline: `16329d4`. This file proposes bounded computational alternatives; it neither changes the canonical case frames nor establishes a final movement analysis. It is deliberately separate from normative description.

Integration check: actual PR16 master `87c23bbcb8ea59f62e415cb315a45f79613e1dc6`; canonical architecture and morphology retained.

## Shared input and independent expected outputs

Let A be a simple actor, T a retained lexical patient, B an applied participant, C a causer, and X the base's sole participant or actor under Caus. `IND*` below is the optional passive external dependent, not an ordinary core object. An antipassive's conceptual patient is absent from the argument inventory. A null recoverable core argument remains in that inventory.

The role hierarchy is schematic, not a claim that every dominating head is a phase:

```
Asp.Align [outer Voice [Caus C [inner actor X [Appl B [VP T V]]]]]
```

Appl and inner antipassive are alternatives. In a simple clause the external actor is A; under Caus the highest external participant is C. Appl relates B to the embedded event, not automatically to T. The retained theme originates as the low complement of V. A theme-like intransitive sole participant becomes X, not an additional retained T.

| Frame | Independent canonical expectation | Selected participant | Canonical neutral order of overt roles |
| --- | --- | --- | --- |
| Simple active NOM transitive | A DIR; T IND | A | A T V |
| Simple active ERG transitive | A TRS; T DIR | T | T A V |
| Simple intransitive, either domain | A DIR | A | A V |
| Simple ERG antipassive | A DIR; no T | A | A V |
| Simple NOM applicative transitive | A IND; B DIR; T IND | B | B A T V |
| Simple ERG applicative transitive | A TRS; B DIR; T IND | B | B A T V |
| Simple NOM applicative intransitive | A IND; B DIR | B | B A V |
| Simple ERG applicative intransitive | A TRS; B DIR | B | B A V |
| NOM Caus intransitive | C DIR; X IND | C | C X V |
| ERG Caus intransitive | C TRS; X DIR | X | X C V |
| NOM Caus transitive | C DIR; X IND; T IND | C | C X T V |
| ERG Caus transitive | C TRS; X IND; T DIR | T | T C X V |
| NOM Caus applied transitive | C DIR; X IND; B IND; T IND | C | C X B T V |
| ERG Caus applied transitive | C TRS; X IND; B IND; T DIR | T | T C X B V |
| NOM Caus applied intransitive | C DIR; X IND; B IND | C | C X B V |
| ERG Caus applied intransitive | C TRS; X IND; B DIR | B | B C X V |
| ERG Caus antipassive | C TRS; X DIR; no T | X | X C V |
| NOM simple patient-oriented passive | T DIR; A IND* | T | T (A) V |
| NOM causative passive | T DIR; X IND; C IND* | T, if retained | T (C) X V |
| Directive applied transitive | T DIR; B IND; addressee/actor supplied by Mood | T | T B V |

Orders are the baseline's descriptive neutral templates, not independent predictions that locate an A-position. Directive and passive licences must be represented separately; a general algorithm changing every nonselected argument to TRS is already false.

## Identical configurations for two case candidates

Both candidates need a prior argument-licensing stage. With an active causative, the completed predicate supplies one highest external participant E=C and an outer selected dependent S according to retained T > B > X. Simple indicative Appl instead supplies S=B even with a retained T. NOM active Caus selects E; NOM patient-oriented Voice selects the same embedded participant hierarchy but changes external licensing to passive. Directive Mood gives retained T priority. These are syntactic/constructional selection conditions whose spell-out is later morphological; the sound of `-n-`, `-an-` or `-éb-` cannot cause a previous selection.

**Candidate A: configurational dependent case.** Define an ERG evaluation domain as the completed finite orientation domain before its ordinary finite argument displacement. Its eligible pair is E and S, both independently licensed in that orientation domain. The lower core roles R are licensed IND in the derived construction before this pair is evaluated. They are therefore excluded from the competing set, as are P complements, nominal-internal DPs and optional passive agents. When E and S are distinct, E asymmetrically c-commands S in their licensing configuration and receives TRS; S receives independently licensed DIR. In a one-participant domain no dependent TRS arises. A construction selecting its only actor as DIR does not create a distinct lower competitor. NOM active ordinary transitive uses E DIR with T IND and no upward dependent case. The simple NOM applicative uses B DIR and A/T IND. This is a bounded candidate specification, not a demonstration that role-based IND assignment is inherent case or that these exact competitors are independently motivated.

**Candidate B: successive Agree.** Evaluate the same argument inventory and domain before ordinary finite displacement. An outer probe must interact with E and the selected dependent S, while R is unavailable for this particular interaction after its constructional licensing. Interaction with one goal does not satisfy the two-goal requirement; satisfaction requires both goals in the same accessible orientation domain. A two-goal dependency licenses TRS on E; independently licensed DIR belongs to S. An expanding lower probe can first access S, then expand to E; a downward-only upper probe needs a justified ordering/feature geometry to pass nonmatching X/B before finding S. Either implementation must specify that search and feature transfer independently of the desired case output. Writing `[pivot]` on S merely restates the answer. General phi-features shared by every DP are insufficient. This is therefore an underdetermined candidate, not a completed Agree derivation. Shawi provides a real case of multiple agreement underlying dependent morphology, but its person hierarchy and object-feature transfer have no established Iridian counterpart.

The two candidates agree on the table only with these explicit exclusions and access assumptions. Matching a fixed list of case frames does not show that the exclusions are correct, or that Agree has been empirically observed. Potentially distinguishing evidence includes independent case visibility of lower causees, whether residual IND can participate in other agreement, movement feeding new case on a later cycle, and the status of lower phases. No such new Iridian judgment is imposed here.

## Counterfactuals that reject tempting shortcuts

1. **All core DPs as competitors.** In ERG Caus of a transitive, C > X > T, a rule assigning upward TRS to every higher DP predicts both C TRS and X TRS. Canonical expectation is C TRS, X IND, T DIR. An applied transitive also incorrectly marks B TRS above T. The failure cannot be repaired by ignoring overtly omitted X, since argument omission is not valency reduction.
2. **Nearest DP as selected goal.** From above Caus, the first nominal may be C or X; neither is selected in the retained-T ERG causative. A probe cannot skip them by saying that the desired pivot must be found. Independently specified licensing/features or a lower selection dependency is required.
3. **Inherited inner Appl selection.** Applying B > T inside a completed causative predicts B DIR and T IND. Canonical outer Caus requires T DIR, B IND. Conversely, removing retained T in the applied intransitive must produce B DIR, not X DIR. The two frames jointly test whether the algorithm uses an outer selection domain.
4. **Movement before unqualified dependent case.** Simple ERG T raised above A, followed by a rule assigning TRS to the highest DP of the pronounced configuration, predicts T TRS, A DIR. The canonical result is T DIR, A TRS. The case algorithm must use an appropriate licensing occurrence/cycle; reading PF order as the case configuration fails.
5. **Upper-cycle recomputation.** Once C TRS/X IND/T DIR is established, raising T above C must not add TRS to T through a new pairing. Compare a candidate that retains valued case and excludes copies from a second independent competitor with a counterfactual counting every copy as a new DP. The latter wrongly creates extra pairs. This control tests the model's chain identity, not an attested Iridian case-stacking prohibition beyond the documented paradigm.
6. **Passive treated as active ERG.** A NOM passive must not produce A TRS just because T is selected. The optional external agent is licensed IND by the passive configuration.
7. **Antipassive restoration.** ERG Caus antipassive selects X and contains no T. An algorithm reinserting the conceptual theme to win T > B > X predicts a nonexistent argument and is rejected.
8. **Phase-edge shortcut.** With an opaque embedded phase, an unexported T is inaccessible. A case or movement model predicting success nonetheless has assumed away locality. Either an independently justified edge occurrence must be available before transfer or a smaller restructuring domain must be defended. This differs from an intervening DP: a nonmatching X can cease to intervene without making an opaque complement accessible.

## Locality derivation obligations

For a retained-theme causative, build VP(T), optionally Appl(B), and the base actor X. Complete inner licensing without prematurely making T inaccessible; if the lower actor layer is phasal, provide an accessible occurrence of T at its edge while preserving X's thematic relation to its low occurrence. Merge Caus and C, then outer orientation. Only then can the outer retained-theme priority be evaluated. A later ordinary finite movement hypothesis must reach that accessible T occurrence, then the proposed lower orientation site or SpecIP. Case can precede the final displacement, but that alone does not explain how the low theme is accessible.

Three conditional paths remain: an edge requirement on the lower phase independently licensing eligible internal arguments; a restructuring causative whose embedded event predicate is not a separate opaque phase; or another explicitly defined locality architecture. None is established merely by suffix order. A model permitting a thematic DP to leap directly from transferred VP to I is not an acceptable fourth alternative. For active NOM Caus the highest C may already satisfy the positional requirement, but that economy does not rescue the ERG theme derivation.

Sources and access limits are audited in `pivot-source-audit.md`. No PDF build or publication is part of this analysis.

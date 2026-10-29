# Binding, modifier placement and scope: investigation record

Revision baseline: `16329d4`; checked 29 October 2026. This file records
alternatives and tests, not additional canonical judgments. The controlled
corpus is `pivot-syntax-diagnostics.md`. Its labels distinguish inherited
evidence, proposed specifications and unresolved predictions.

Integration check: actual PR16 master `87c23bbcb8ea59f62e415cb315a45f79613e1dc6`; canonical architecture and morphology retained.

## Canonical evidence and its limits

Chapter 4 gives **Svem Marku védnik**, ‘Marek saw himself’, against **I Marku
védnik**, ‘Marek saw him’. The current quantity is **védnik**: the brief's
`vednik` is stale, and `vedník` would be another erroneous revision. Preserve
the direct/transitive/indirect reflexive paradigm **svem/svě/svy**.

Use indices for interpretations, not for new morphological distinctions:
`svem_i Marku_i védnik` requires the actor–patient anaphoric dependency;
`i_j Marku_i védnik` has a distinct patient referent. The latter establishes
that a demonstrative allows disjoint reference, not that every demonstrative
is obligatorily disjoint in every construction.

The argument-structure relation is schematically:

```text
[VoiceP actor_i [VP patient_i V] Voice]
```

If the patient is pronounced above the actor, retain this lower thematic
configuration in the derivation. At least three accounts remain separable:

1. A local anaphor is licensed at a derivational stage before displacement.
2. A relevant lower occurrence is interpreted in a movement chain; specify
   which occurrence supplies binding and which supplies quantificational scope.
3. A separately defined local anaphoric relation supplies connectivity without
   making the assumed displacement responsible for it. Such a relation needs
   explicit locality and antecedent conditions; discourse salience is inadequate.

The canonical pair cannot choose among these. It also cannot select SpecIP
over a lower orientation/aspect site, establish obligatory reconstruction of
all pivots, or identify a causative phase. A base configuration placing the
patient above its actor must supply an independent local relation; a remnant
analysis retaining the actor's higher origin must state its additional movement.

## Antecedent contrasts still requiring specification

These are role-indexed test frames, not grammaticality judgments or newly
approved Iridian sentences. Fix lexical participants, aspect, nominal anchoring,
discourse context and intended identity before choosing their realisation.
Do not obtain a judgment by drawing a tree that already assumes it.

| Construction | Controlled readings | What would discriminate |
| --- | --- | --- |
| Active progressive versus perfective | actor_i … theme-REFL_i; same actor/theme inventory | Stable binding with a changed pivot tests connectivity independently of initial position. |
| NOM patient-oriented passive, overt agent | agent_i … theme-REFL_i | Availability must be checked against the passive agent's actual structural position, not its translation. |
| NOM passive, omitted agent | implicit-actor_i … theme-REFL_i | An understood event participant is not automatically an available syntactic antecedent. |
| Applicative | actor_i, beneficiary_j, theme-REFL_i versus theme-REFL_j | Compare actor binding with applied-participant binding; establish the latter independently before calling it intervention. |
| Causative transitive | causer_i, causee_j, theme-REFL_i versus theme-REFL_j | A causer-only, causee-only or ambiguous result imposes different binding-domain requirements. No result is yet established. |
| Reflexive causee | causer_i, causee-REFL_i, theme_j | Tests structural role and domain independently of which case the causee receives. |
| Reflexive causer | causer-REFL_i, causee_i | A lower coreferent is not automatically an antecedent; test the intended local dependency rather than assume symmetry. |
| Linked topicalisation | topic-actor_i … theme-REFL_i | Test preservation of an independently licensed relation; do not treat a high discourse position itself as an anaphor licensor. |
| Finite embedded clause | matrix-actor_i … [embedded-actor_j … theme-REFL_i/j] | Separate local binding from discourse coreference and possible long-distance anaphoric licensing. |
| Nonfinite complement | matrix-controller_i … [silent-actor_i … theme-REFL_i] | Establish the silent local argument and its control relation before inferring long-distance binding. |
| Participant nominal | possessor_i … [actor_j … theme-REFL_i/j] | Nominal possession, event participation and local binding are separate relations; finite locality cannot simply be inherited. |
| Discourse continuation | Marek_i/Janek_j … ; null_i/null_j sleep-PROG | Tests contextual recovery, not Condition A or obligatory cross-clausal identity. |

An explicit null antecedent is a structural proposal requiring a licensed
argument position. It must not be inserted merely to rescue an otherwise
unsupported reading. Positive readings need negative controls with the same
referents and a local demonstrative, and contexts distinguishing accidental
identity from the anaphoric dependency.

## Modifier and scope controls

Keep **skorňe** ‘quickly’ (event manner), **roca** ‘often’ (event frequency)
and **bych** ‘yesterday’ (temporal frame) separate. None belongs to the closed
particle series merely because it is preverbal. A low manner adjunct and a
temporal frame need not mark the same attachment boundary. Their semantics
alone does not fix a unique syntactic height.

For each modifier, compare `pivot modifier actor V` with `modifier pivot actor
V`, controlling discourse topic and prosody. Record the surface-order judgment
separately from the reading. A SpecIP candidate above the operator field and
a genuinely lower candidate make different positional predictions only once
the modifier's attachment is independently fixed. The lower candidate cannot
be moved ad hoc above each diagnostic. Conversely, the SpecIP candidate must
explain narrow interpretation rather than equate first pronunciation with
wide scope.

Canonical **Deno že zastráda** has the intended interpretation
`¬∃x[thing(x) ∧ lack(x, me)]`. Its direct theme is interpreted within negation;
its indirect experiencer is not an ergative/transitive actor. Strict concord
requires local negative licensing irrespective of pivot placement. Under a
raising analysis, specify the lower interpretation; under a lower-position
analysis, it is available without raising. This example by itself does not
distinguish the candidates.

Test quantified pivots with universal actors in contexts distinguishing
`∃ > ∀` from `∀ > ∃`; test a causative theme against both the causing and
caused events. Do not infer these readings from English translations or
introduce unrestricted quantifier raising to obtain every desired result.
Retain the independently bounded **kamo/kam** scope specifications and the
difference between LF composition and PF placement. Movement of a nominal
does not license arbitrary reversal of phasal/exclusive operators.

## Primary-source audit

The following verification was independent of the brief. These sources supply
comparative methods and theoretical alternatives, not Iridian judgments.

| Work | Verified primary evidence and access | Bounded application |
| --- | --- | --- |
| Chomsky (1995), *The Minimalist Program* | [MIT Press original-edition page](https://mitpress.mit.edu/9780262531283/the-minimalist-program/) confirms title, author, 28 September 1995 and ISBN 9780262531283. Publisher description inspected; no claim to a page-specific reading of the whole book. | Background for derivations and interfaces; the book's existence is not evidence that an Iridian pivot moves. |
| Fox (1999), ‘Reconstruction, Binding Theory, and the Interpretation of Chains’, *Linguistic Inquiry* 30(2):157–196 | [Primary article text hosted by Chicago](https://semantics.uchicago.edu/kennedy/classes/nu/460/S04/fox99.pdf), title page and opening sections inspected. Publisher article endpoint returned 403; that did not prevent access to the article text. | Distinguishes pronunciation, scope and binding interpretation, and explicitly distinguishes A- and A′-chains. It does not establish universal obligatory A-reconstruction. |
| Lebeaux (2009), *Where Does Binding Theory Apply?* | [MIT Press Scholarship Online](https://academic.oup.com/mit-press-scholarship-online/book/17342), DOI 10.7551/mitpress/9780262012904.001.0001, confirms author/title, 13 February 2009 and abstract. Full book not accessed. | The abstract proposes different evaluation conditions for positive and negative binding constraints. Use as a competing derivational architecture, not as a settled Condition A rule for Iridian. |
| Cinque (1999), *Adverbs and Functional Heads: A Cross-Linguistic Perspective* | [Oxford Academic](https://academic.oup.com/book/48079), DOI 10.1093/oso/9780195115260.001.0001, confirms 18 March 1999, author/title and publisher abstract. Full book access restricted. | The publisher describes a hierarchy of functional specifiers. This motivates controlled height tests, not an automatic functional head for every Iridian lexical adverb. |
| Ernst, *The Syntax of Adjuncts* (conventionally cited 2002) | [Cambridge publisher record](https://www.cambridge.org/core/books/syntax-of-adjuncts/9F3825F8978CA4271A1B9297627F17D1), DOI 10.1017/CBO9780511486258. Description and metadata inspected; page lists print publication 20 December 2001 and digital publication 12 October 2009. Neither is to be silently represented as the 2002 citation date. Full book not accessed. | The publisher describes composition and selection as constraints on adjunct attachment, providing a genuine alternative to fixed cartographic positions. Date discrepancy remains explicitly recorded. |
| Matthewson (2004), ‘On the Methodology of Semantic Fieldwork’, *International Journal of American Linguistics* 70(4):369–415 | [Chicago publisher record and abstract](https://www.journals.uchicago.edu/doi/10.1086/429207), DOI 10.1086/429207, confirms October 2004, title, author, volume/issue/pages. Full article access restricted. | Abstract supports distinguishing judgments, translation tasks and controlled discourse contexts. For this constructed language, a new specification is not speaker elicitation or an independent empirical discovery. |

A further primary author manuscript, Fox and Nissenbaum,
[‘Condition A and Scope Reconstruction’](https://mit.edu/fox/www/fox_nissenbaum.pdf),
was inspected at its opening. It contrasts syntactic with semantic
reconstruction and proposes Condition A as a discriminator. The inspected
copy does not establish its publication date; no guessed date or complete
bibliographic entry has been added. Its comparative argument is useful only
after Iridian's local antecedent conditions are independently fixed.

# Grammar metahistory: editorial questions and superseded analyses

**Record date:** 29 October 2026. **Source:** the active Iridian reference grammar following the newer evidential and quantity-grade pass. This is a record of editorial alternatives and incomplete investigations, **not a second normative grammar**. Source passages below are archival, even where their phrasing once treated a now-resolved matter as a live question.

## Status register

| Subject | Status | Editorial disposition |
| --- | --- | --- |
| Asp.Align and a separate Align head | Adopted analysis | Single Asp.Align head with fused aspect/alignment exponent; a separate Align projection is a theoretical alternative, not canonical additional morphology. |
| Rhotic causative and higher orientation Voice | Adopted analysis | CausP precedes orienting VoiceP; conditioned -n-/-an- already specified. |
| Negative za- versus higher NegP | Adopted analysis | The root-preceding negative exponent is attached post-syntactically; ellipsis behaviour is not independently demonstrated. |
| Ergative/transitive case theory | Preferred analysis; implementation partly open | Dependent case within the aspectually licensed domain; implementation alternatives do not imply separate suffixes. |
| Reduced Mood-conditioned Asp.Align | Partially settled | The IPFV/PFV opposition is canonical; lexical/pragmatic restrictions on -ov-, effects of information structure, and the interaction with predicate telicity need systematic paradigms. |
| Absolutive pivot versus topicalisation | Distinction adopted; diagnostics incomplete | Case licensing and high A′ topicalisation are distinct; lower positions, island and binding diagnostics are underdetermined. |
| Conjunctive and complement linker -e | Unified clause-edge analysis adopted; syntactic tests open | Alternative homophone and pure boundary-marker accounts archived; null-C, binding and scope predictions unverified. |
| Indirect evidential and linker | Resolved by newer grammar pass | The old -ejte + -e adjacency question is superseded: -al after consonants and -l after vowels precede linker -e; local PAL of evidential /l/ yields -aľe and -ľe. See the current section sec:vm-evid. Do not reintroduce -ejte or infer an unresolved vowel clash. |
| AnchP, DemP and nominal DP | Order adopted; higher projection theory open | Anchoring and demonstrative positions are separate in the nominal description; DP articulation, phasehood and K/Case accessibility need further formalisation. |
| Participant-oriented -ový RelP and PossP | Attachment height open | Relative case licensing is described; the exact relative/possessor ordering within the extended nominal projection remains undecided. |
| Pre-by wh phrase and PolP > FocP | Open formal derivation inconsistency | Four surface strings remain described, but the stated hierarchy with head-initial Pol alone does not derive all pre-by orders. |
| Adjacent nested si terminals | Untested prosodic behaviour | The current domain-linearisation rule predicts si si; no additional coalescence or clitic-host-sharing rule is licensed. |
| Continuous -ou participant nominals | Paradigm incomplete | Only the unanchored direct singular piaštova is specified. Do not invent other cells. |
| Focus displacement / embedded hanging topics | Distributional tests open | Object–adverb movement, embedded topic locality, recursion and intonational diagnostics need controlled contexts. |
| Lexical sabo versus negative-concord žemě | Licensing question open | The latter requires local negation; the former's concord behaviour is not inferred from its lexical-adverb classification. |
| Particle dlí | Distributional question open | Propositional-layer status is adopted; interactions with directives, future reference and chaining remain uncharacterised. |
| Existential jec-/zad- and Neg | Formal locality question open | Polarity-conditioned root suppletion described; locality across Asp requires explicit derivation. |
| Denominal -it- | No productive PAL licence established | Only -ěvat- is independently specified as front-grade-selecting; i in -it- by itself cannot determine a mutation. |
| navad- content realisation | Lexical-selection question open | Cognitive valency is described, but nominal or clausal realisation of content is not. |
| Selected complement plus phasal particle | Illustrative example missing | Existing adjacency predicts order, without a direct multi-construction example. |

The relevant distinction is between an analysis *adopted by the grammar* and a derivation or distribution *independently demonstrated*. Do not retain the word ‘unresolved’ merely because more empirical tests could be imagined, nor declare a formerly undecided form canonical solely because its question has been archived.

## Archival source extracts

The following sections preserve the text actually displaced in this PR, including competing hypotheses. Each transcription is an historical snapshot of its chapter and does not override present morphophonology, inflection, or the evidential's current -al/-l paradigm.

### 03-verbs: Verb chapter: Analytical questions

Original location: `chapters/03-verbs.tex`.

```tex
\section{Analytical questions}
\label{sec:vm-tensions}

The relation between aspect, alignment, and the position of the absolutive
leaves several analytical choices open. The following distinctions concern the
formal representation of the described paradigms rather than additional
morphological contrasts.

\subsection{The Asp.Align portmanteau and the Mirror Principle}
\label{sec:vm-tension-asp}

Asp.Align jointly realises viewpoint and an alignment-domain value. The
analysis treats this as one aspectual head whose case-licensing properties
interact with the completed valency and orientation configuration
(§\,\ref{sec:vm-asp-case}). A separate Align head is consequently unnecessary
for the described paradigm, although a morphological fusion account could
represent the same exponence with more structure.

The Mirror Principle concerns the relation between morphological order and
syntactic composition; it does not independently require a distinct segment
for every syntactic feature. Affix-specific linearisation and post-syntactic
attachment must also be distinguished from syntactic head movement
\cite[§2.4]{harley2011}. In Iridian, the order of causative and outer
Voice supports their relative height, while the Voice alternation
\ird{-n-}/\ird{-an-} illustrates conditioned allomorphy. The forms do not decide
between every possible implementation of these mappings. Argument building
precedes higher selection in the analysis: Asp supplies the ordinary alignment
domain, while applicative orientation,
patient-selecting \ird{-n-}, and directive Mood impose their specified
constructional requirements.

\subsection{Mood and the reduced Asp.Align: open questions}
\label{sec:vm-tension-mood-asp}

Non-indicative Mood licenses a two-way IPFV/PFV-domain opposition and
conditions its morphological realisation (§\,\ref{sec:vm-mood-asp}).
The reduced aspectual contrast and the construction's orientation requirements
belong to the syntactic configuration; PF impoverishment restricts the
features available for insertion of an Asp exponent. Asp.Align remains
present in finite clauses, without requiring the full indicative viewpoint
inventory or assigning a new case frame after spell-out.
The description leaves three distributional questions unresolved: the lexical
and pragmatic restrictions on \ird{-ov-} in directives and irrealis clauses,
the contribution of information structure to the IPFV/PFV distinction in
directives, and the extent to which irrealis boundedness depends on predicate
telicity. The viewpoint contrast specified in §\,\ref{sec:vm-mood-asp}
does not by itself settle these distributions.

\subsection{The Voice head and the rhotic causative: distinct positions}
\label{sec:vm-tension-n}

Patient-selecting Voice and the rhotic causative occupy distinct positions.
Causative \synhead{CausP} introduces a causer above the inner predicate,
while the outer orientation head selects a participant of the resulting
predicate. Their order in \ird{piášt-r-an-ik} follows their composition:
the caused event is built before its higher orientation is specified.
Voice takes \ird{-an-} immediately after a rhotic causative and ordinary
\ird{-n-} elsewhere, while zero orientation supplies the active NOM frame.

A causative of an antipassive can contain both inner \ird{-aš-} and outer
\ird{-an-}, since the former suppresses the lexical patient and the latter
selects the causee in a newly transitive predicate. Without an intervening
causative, \ird{-n-} cannot restore a patient to an antipassive. Applicative
\ird{-éb-} likewise introduces an inner participant, whose pivot privileges
can be superseded by a higher causative or directive configuration.

\subsection{The absolutive--topic mapping: Agree or movement?}
\label{sec:vm-tension-abs-top}

Case licensing and linked topicalisation belong to separate dependencies.
 Asp.Align and Voice establish the direct-case pivot in the lower domain,
 while a referential topic enters an A$'$-relation with that domain through
 \synhead{TopP}. Top does not value direct case: a transitive-case agent may
 be topicalised while a direct-case patient remains inside the comment.

The examples establish this dissociation, but do not identify every lower
 pivot position or provide binding and island diagnostics for all topic
 dependencies. Agree may relate a functional head to a nominal without
 displacing it; such a relation alone cannot explain an independent change
 of word order. Null argument recovery and the external resumptive strategy
 likewise do not require the silent expression to occupy the same high
 position in every clause (§\,\ref{sec:tc-multiple-topics}).

\subsection{Ergative case: dependent, structural, or inherent?}
\label{sec:vm-tension-erg}

The transitive case of an ergative-domain agent is analysed here as
 dependent on a distinct participant licensed in the direct case
 (§\,\ref{sec:vm-asp-case}). Asp.Align conditions the alignment domain and
 orientation selects the privileged participant of the completed predicate;
 the dependent-case relation determines the highest actor's transitive case
 within that domain. These
 operations do not require Asp to assign two cases simultaneously, or Top
 to assign either case.

The case pattern alone does not decide every implementation detail of
 dependent-case computation or the exact configuration in which a selected
 participant is licensed. It does, however, require the analysis to preserve the
 aspect-conditioned domain and the distinction between participant-selecting
 orientation and independent topicalisation.

\subsection{The conjunctive linker \ird{-e}: see §\,\ref{sec:conjunctive-linker}}

The formal analysis of the conjunctive linker \ird{-e} --- including its
phonological characterisation, morphosyntactic distribution, the competing
unified \synhead{CP}-edge, PF boundary-marker, and two-homophone analyses, and
the outstanding empirical questions --- is developed in full in the conjunctive
linker section above (§\,\ref{sec:conjunctive-linker}).

\subsection{The NEG prefix vs.\ \synhead{NegP} position: see
§\,\ref{sec:vm-neg}}
\label{sec:vm-tension-neg}

The indicative negative marker \ird{za-} is prosodically dependent on the
verb and precedes the root, although Neg is analysed as a head-final
projection above Asp (§\,\ref{sec:vm-neg}). Post-syntactic attachment places
the exponent at the host's left edge, while a syntactic attachment analysis
would require the same surface order to be specified through linearisation.
The Mirror Principle permits either prefixal or suffixal realisation of the
higher head \cite{harley2011}; the marker's behaviour under ellipsis remains
undocumented.
```

### 04-nouns: Noun chapter: Theoretical tensions and open questions

Original location: `chapters/04-nouns.tex`.

```tex
\section{Theoretical tensions and open questions}
\label{sec:nm-tensions}

\subsection{The projection of \synhead{AnchP}: \synhead{DP} or a separate anchoring layer?}
\label{sec:nm-tension-dp}

The standard \synhead{DP} Hypothesis (Abney 1987) places D\textsuperscript{0} as
the single highest head of the nominal extended projection, unifying articles,
demonstratives, and similar functional elements under one projection. An
alternative tradition (Longobardi 1994; Alexiadou et~al. 2007) distinguishes a
dedicated definiteness layer from a higher \synhead{DP} layer (which may encode
referential anchoring, logophoricity, or other discourse properties).

The grammar represents the two overt anchoring strategies within a single
functional layer, Anch\textsuperscript{0}, with suffixal
exponents \ird{-to}/\ird{-te}, cumulative case-number--anchoring
endings, and proclitic exponent \ird{si}
(§\,\ref{sec:nm-spec}). The demonstrative system occupies its own projection,
\synhead{DemP}, above \synhead{AnchP}. Whether \synhead{AnchP} and
\synhead{DemP} should be unified under an articulated \synhead{DP} along the
lines of Longobardi (1994) or kept as separate projections within the nominal
left periphery remains unspecified; the morphological ordering alone does not
determine whether the upper nominal domain contains a single articulated
projection or several distinct layers.

\subsection{The anchoring suffix and Case theory}
\label{sec:nm-tension-case}

A potential tension arises within Case theory. In the standard Minimalist
account (Chomsky 2001), case is assigned to DPs by an Agree relation with a
functional head (v*, T, or an applicative head). If the nominal extended
projection is capped by \synhead{AnchP}, then the outermost head of the
\synhead{DP} is D\textsuperscript{0}, not K\textsuperscript{0}. Case should in
principle be visible on the \synhead{DP} as a whole (from the perspective of the
external clause structure), but the morphological encoding of case is on the K
layer inside the \synhead{DP}, below D\textsuperscript{0}.

This can be resolved by one of two strategies: (a) the D head is transparent to
case, meaning the Agree probe from the clausal head targets K\textsuperscript{0}
or the \synhead{NP} root directly through \synhead{AnchP}; or (b) case features
percolate from K\textsuperscript{0} to D\textsuperscript{0} by feature
inheritance within the \synhead{DP}, and D presents the valued case feature to
the external probe. Strategy (b) has the advantage of preserving the standard
Agree architecture; strategy (a) requires relaxing the usual opacity of
\synhead{DP} boundaries.

\subsection{The anchoring suffix and phase theory}
\label{sec:nm-tension-phase}

Nominal-domain linearisation applies when $D_a$ is complete, including the
higher quantificational and demonstrative material associated with its noun
(§\,\ref{sec:nm-si-linearisation}). The PF derivation therefore retains the
anchoring terminal until that domain has been assembled; \synhead{AnchP}
alone does not close a separate pronunciation cycle. Embedded possessors
receive their own ordering before they are incorporated as dependents in the
containing nominal string.

This PF commitment does not identify \synhead{AnchP} with the edge of a
syntactic DP phase. Whether the completed outer nominal domain is also a phase,
and how its internal case features remain accessible to clausal probes,
concern syntactic locality (§\,\ref{sec:nm-tension-case}). The precedence of
\ird{si} follows from its source-conditioned linearisation within $D_a$,
without requiring the possessor to move to a phase edge merely to supply a
phonological host.

\subsection{Participant-oriented relatives and their nominal embedding}
\label{sec:nm-tension-rel}

The \ird{-ový} relative forms an independent case domain within the host
\synhead{DP}, while the head noun remains in the matrix nominal spine
(§\,\ref{sec:nm-ovni}). Its matrix case and optional anchoring are therefore
independent of the participant gap inside \synhead{RelP}. The exact attachment
of \synhead{RelP} relative to \synhead{PossP} is unresolved; the common
analysis in Chapter~\ref{ch:complex} requires only a prenominal modifier with
its own participant-selection and case relations.
```

### 03-verbs: Linker: competing syntactic/PF interpretations

Original location: `chapters/03-verbs.tex`.

```tex
\subsubsection{Competing analyses}

Three main analyses are available; they diverge principally on whether \ird{-e}
has a unified syntactic identity across its two main environments (complement
and conjunctive chain).

\begin{description}[leftmargin=2em, labelwidth=!, labelindent=0em]
  \item[\upshape Unified \synhead{CP}-edge analysis.] Under this analysis,
    \ird{-e} is a single morpheme throughout: the phonological exponent of a
    \textsc{[+fin, +sub]} feature complex that is valued on the embedded
    \synhead{TP} when it enters the scope of a C head. In the complement
    construction, C is overt (\ird{po} or \ird{poby}). In the conjunctive chain,
    C is a null clause-juncture head (following the general principle that
    coordination in head-final languages may involve a null C$^0$ that takes a
    finite \synhead{TP} as its specifier or complement). The linker is the
    spell-out of the embedded T's contact with this C head, and its
    selection of the front grade is the PF signature of \textsc{[+fin,
    +sub]} in Iridian. The absence of \ird{-e} in independent clauses follows
    without stipulation: no C head is present to value the feature on T.

    The central challenge for the unified analysis is the distributional
    asymmetry: in the complement construction, \ird{-e} co-occurs with an overt
    C head (\ird{po}/\ird{poby}); in the conjunctive construction, no overt C
    appears. The unified analysis must postulate a null conjunctive C$^0$ whose
    presence is evidenced only by the linker itself, which risks circularity
    unless independent evidence for this head can be adduced.

  \item[\upshape PF boundary-marker analysis.] Under this analysis, \ird{-e} is
    not a syntactic morpheme but a phonological convention: a boundary signal
    inserted at any right edge of a finite clause when that clause is followed
    by further clausal material. Its selection of a front grade is
    then a phonological property of the boundary diacritic rather than a reflex
    of any syntactic feature. This account handles the conjunctive environment
    straightforwardly (every non-final finite clause is followed by another
    clause) and is empirically efficient.

    A PF boundary-marker account must independently specify the segmental
    effects associated with this clause edge. The palatalisation caused by
    \ird{-e} shares its PAL mappings with front-coded nominal endings
    \ird{-ě} and \ird{-í}, whereas yod-grade \ird{-ěv} has a different
    velar output; the linker also selects the construction-specific ending
    allomorphs in Table~\ref{tab:linker-paradigm}. A boundary diacritic would
    therefore need these same grade and allomorph specifications. The
    correspondences favour the suffixal treatment adopted here, although
    segmental mutation alone does not establish the syntactic status of the
    linker.

  \item[\upshape Two-homophone analysis.] Under this analysis, \ird{-e}$_1$ (the
    complement linker) and \ird{-e}$_2$ (the conjunctive linker) are distinct
    morphemes that happen to be phonologically identical and share the
    palatalising trigger class. \ird{-e}$_1$ is the exponent of the
    \synhead{TP}-\synhead{CP} boundary in complement clauses; \ird{-e}$_2$ is a
    clause-chaining morpheme lexically specified for the conjunctive domain.
    Their shared form and mutation class are specified separately in the two
    lexical entries.

    This analysis avoids the null-C problem but is the most stipulative: it
    requires two separate lexical entries sharing phonological form and the same
    segmental-mutation property, with their distribution jointly covering the
    environments of both complement embedding and clause chaining. The burden of
    proof falls on demonstrating that the two environments are syntactically disjoint in a way that the unified analysis cannot
    accommodate.
\end{description}
```

### 03-verbs: Linker: null conjunctive C diagnostics

Original location: `chapters/03-verbs.tex`.

```tex
\paragraph{The null conjunctive C$^0$.}
The postulated null C head in the conjunctive construction should in
principle be detectable through its interaction with the argument structure
of the chained clauses. If conjunctive C$^0$ takes the finite \synhead{TP}
as its specifier and itself projects a \synhead{CP}, the chained clause
is a \synhead{CP} adjunct. Binding and scope across conjunctive-chain
clauses should then pattern with embedding rather than flat coordination;
the outcome of this diagnostic remains unspecified.
```

## Shorter editorial notes displaced from the chapters

These passages were research prompts, redundant expressions of already adopted rules, or unresolved theoretical qualifications. The main grammar retains actual examples, licensed forms and explicit paradigmatic limits.

### 03-verbs: Linker: author-facing heading

Original location: `chapters/03-verbs.tex`.

```tex
\subsubsection{Preferred account and outstanding questions}
```

### 03-verbs: Linker: obsolete comparison to removed alternatives

Original location: `chapters/03-verbs.tex`.

```tex
consonant-mutation class; their different syntactic environments remain
relevant to the comparison with a two-morpheme account below.
```

### 03-verbs: Linker: explicit adopted analysis

Original location: `chapters/03-verbs.tex`.

```tex
The unified \synhead{CP}-edge analysis is preferred here on parsimony grounds.
```

### 03-verbs: Linker: redundant competing analyses

Original location: `chapters/03-verbs.tex`.

```tex
This local realisation is compatible with the
clause-edge analysis, although it does not by itself decide whether the
complement and conjunctive uses contain one morpheme or two.
```

### 03-verbs: Linker: undecided status sentence

Original location: `chapters/03-verbs.tex`.

```tex
analysis as a suffix; they do not by themselves resolve the choice between one
clause-edge morpheme and two distributionally distinct morphemes.
```

### 03-verbs: NEG deleted-label citation

Original location: `chapters/03-verbs.tex`.

```tex
(§\,\ref{sec:vm-neg}; §\,\ref{sec:vm-tension-neg}).
```

### 03-verbs: Voice deleted-label citation

Original location: `chapters/03-verbs.tex`.

```tex
metathesis of Voice and Caus (§\,\ref{sec:vm-tension-n}).
```

### 03-verbs: Complement–phasal example research gap

Original location: `chapters/03-verbs.tex`.

```tex
precedes that particle; a direct example of this combination remains to be
established.
```

### 04-nouns: Nested si terminals research note

Original location: `chapters/04-nouns.tex`.

```tex
Its acceptability and the prosodic integration of adjacent
\ird{si} remain unspecified: the rule supplies no haplology, reduction, or
special clitic-cluster repair, and the single-clitic host rule alone does not
determine whether both clitics share one host.
```

### 05-function-words: Sabo concord question

Original location: `chapters/05-function-words.tex`.

```tex
(§\,\ref{sec:nm-negative-concord}); the relation between this paradigm
member and lexical \ird{sabo}, including the latter's concord behaviour,
remains unspecified.
```

### 05-function-words: Dlí distributions

Original location: `chapters/05-function-words.tex`.

```tex
The broader interaction of \ird{dlí} with imperatives, future-oriented
contexts, and clause chaining remains to be worked out in detail. The working
analysis, however, is that \ird{dlí} belongs to the propositional layer because
```

### 06-simple-sentence: Pre-by wh-order unresolved note

Original location: `chapters/06-simple-sentence.tex`.

```tex
Their acceptability establishes the independence of those choices, although
it leaves the structural position of the pre-\ird{by} wh-phrase unresolved.
```

### 06-simple-sentence: Wh paradigm editorial question

Original location: `chapters/06-simple-sentence.tex`.

```tex
the position of overt \ird{by} raises a separate structural question:
```

### 06-simple-sentence: Pre-by wh-order derivation conflict

Original location: `chapters/06-simple-sentence.tex`.

```tex
\noindent Both overt-\ird{by} examples place \ird{jena} before the
 question particle. This order is not derived by the hierarchy
 \synhead{PolP} $>$ \synhead{FocP} $>$ \synhead{IP} with head-initial
 Pol\textsuperscript{0}, which would place \ird{by} before both an in-situ
 wh-phrase and one moved to Spec,\synhead{FocP}. The established strings
 therefore show that overt interrogation combines with either nominal order,
 while their derivation within that hierarchy remains unresolved. The
 null-Pol contrast is compatible with focus movement, but the paradigm as a
 whole does not independently identify Spec,\synhead{FocP} as the landing site.
```

### 06-simple-sentence: Duplicate sabo/žemě note

Original location: `chapters/06-simple-sentence.tex`.

```tex
The relation of \ird{sabo} to concord-bearing
\ird{žemě} \trsl{never} remains unspecified
(§\,\ref{sec:lex-adv}); lexical-adverb placement alone does not determine
negative licensing.
```

### 06-simple-sentence: Neg-to-Exist formal locality

Original location: `chapters/06-simple-sentence.tex`.

```tex
The locality relation between Neg
and Exist across the intervening Asp head remains unspecified.
```

### 07-information-structure: Wh/FocP diagnostic issue

Original location: `chapters/07-information-structure.tex`.

```tex
\synhead{FocP} represents marked displacement in the clause-spine analysis,
 although the position of overt \ird{by} in the wh-fronting paradigm remains
 unresolved (§\,\ref{sec:th-wh-interrogation}). Neither that paradigm nor
 the narrow-focus reading of these nominals independently identifies the
 landing site.
```

### 07-information-structure: Object–adverb focus diagnostic

Original location: `chapters/07-information-structure.tex`.

```tex
Displacement of an object across such an adverb would provide a positional
 diagnostic if it correlated with a stable focus interpretation. Its
 grammaticality and interpretation remain unspecified.
```

### 07-information-structure: Conjectured Iridian focus judgements

Original location: `chapters/07-information-structure.tex`.

```tex
\cite[§\,4.4.2]{ozkangrigoras2020}; it offers a comparative model for this separation,
 without supplying the missing Iridian judgements.
```

### 07-information-structure: Embedded hanging topic diagnostics

Original location: `chapters/07-information-structure.tex`.

```tex
In Iridian, the availability of embedded hanging topics and their locality
 and intonational properties remain unspecified; the examples establish the
 coexistence of the two constructions without requiring unrestricted
 recursion of identical topic projections.
```

### 07-information-structure: Topic/focus limits

Original location: `chapters/07-information-structure.tex`.

```tex
The pre-\ird{by} position of wh-phrases remains unresolved within the
 stated clause spine (§\,\ref{sec:th-single-wh}). The examples also leave open
 controlled contrasts for focus displacement,
 competition between animate antecedents, extraction locality, or distinct
 topic contours.
```

### 10-derivational: Denominal -it- PAL diagnostics

Original location: `chapters/10-derivational.tex`.

```tex
The grade selected
by \ird{-it-} remains unspecified pending paradigmatic evidence: its initial
\ird{i} alone does not establish a categorical mutation rule.
```

### 10-derivational: Navad complement shape

Original location: `chapters/10-derivational.tex`.

```tex
The stem \ird{navad-} preserves the cognitive frame of \ird{vad-}; the
nominal or clausal realisation of its content remains unspecified.
```

## Editorial policy

Keep established forms, illustrative paradigms, formal commitments that are actually part of the grammatical account, and necessary bounds on attested/specified morphology in the main book. Record historical alternatives, unresolved tests, old questions, and speculative derivational repairs here. Corrections to the canonical grammar require separate substantive changes and validation; a status-table update alone is not such a correction.


## Clausal architecture review: source audit (29 October 2026)

This is a new research record; the historical quotations above remain verbatim.

- Hsieh and Erlewine (2023), *On the scope and position of Tagalog clitic adverbs*, JSLS handbook pp. 109–112: read the complete author-hosted contribution at https://mitcho.com/research/clitics-jsls.pdf. It distinguishes fixed interpretive positions from postsyntactic clitic order; its §3 also considers covert operators paired with pronounced particles. Its restricted Tagalog scope results do not establish Iridian ambiguity.
- Hsieh and Erlewine (January 2024), *Determining the scope of Tagalog clitic adverbs*: read the 12-page author-hosted LSA handout at https://mitcho.com/research/handout-lsa2024.pdf, especially §§3–6. It places na/pa above negation and lang, and accounts for lang/negation variation using Foc and two negation positions. This is a revised conference analysis, not an interchangeable citation for the 2023 contribution.
- Persohn (2024), *German schon and noch as scalar additives with a marginality twist*: consulted the publisher's complete article/PDF, especially §§2–4 and 6, at https://doi.org/10.1017/S1470542724000084. The phasal, time-scalar, marginality and scalar-sufficiency distinctions support careful comparative separation of uses, not a universal clausal spine or Iridian judgments.
- Cinque (1999), *Adverbs and Functional Heads*: verified the publisher's record, abstract and contents at https://academic.oup.com/book/48079. Chapters 1, 3 and 4 respectively concern adverb order, head order and their comparison. Full chapter text was unavailable through the accessible publisher interface. No page-specific claim from the inaccessible full text has been added. The bounded Iridian hierarchy does not inherit Cinque's stronger universal claim.
- Erlewine (2016), *Focus association into copies and the scope of even*: the initial published-article link returned 404, but independent review located the complete 19-page proceedings article at https://journals.linguisticsociety.org/proceedings/index.php/SALT/article/download/26.855/3686/5352 and checked its account in §§3–4 and the conclusion, alongside the two-page author-hosted conference handout at https://mitcho.com/research/handout-even-salt.pdf. The paper explicitly distinguishes English *only* from *even*: p. 863, fn. 9 explains why its lower-copy mechanism does not license the same backwards association for *only*. This is therefore a comparative illustration of how pronounced and interpreted focus positions can differ, not a derivation of Iridian kamo's exclusive-topic association or a claim that all topics have movement copies. The latter remains the separately specified Iridian convention.

The grammar's lower polarity licensing and bounded exclusive composition are explicit Iridian design conventions. Comparative works motivate distinctions and possible mechanisms; they supply neither natural-language attestation for these Iridian examples nor a derivation of every optional layer in every clause. Further splits within the heterogeneous comment field require separate distributional and scope diagnostics rather than an automatic projection per particle.

### 03-verbs: Superseded negative-Mood derivational alternative

The main grammar now adopts lower polarity-operator licensing rather than leaving this alternative open. Original text retained verbatim:

```tex
the exclusion of \ird{za-}; an alternative derivation through post-syntactic
fusion of Neg and Mood would yield the same morphological pattern.
```

Whether a fusion analysis can independently derive the same phasal scope remains a research question, not a second licensed derivation in the normative grammar.

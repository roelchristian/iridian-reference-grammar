# A reference grammar of the Iridian language

Iridian (*ircevná malno*) is a naturalistic constructed language conceived as
a language isolate in a fictional Central European setting. Within that
setting, the Iridian Republic lies between the Czech Republic, Slovakia,
Poland and Ukraine, and its language has developed through sustained contact
with its Slavic neighbours. Its vocabulary, sound system and orthography
bear a distinctly West Slavic character, while its grammatical organisation
combines predominantly head-final syntax, extensive verbal morphology and a
central role for discourse topics.

*A reference grammar of the Iridian language*, by Roel Christian Yambao,
describes the language's phonology, morphology, syntax and discourse. The
current work is an ongoing scholarly project whose descriptive chapters
develop both the forms of Iridian and the analyses through which their
distribution is understood.

## Linguistic profile

Iridian distinguishes short and long vowels independently of stress, which
falls on the first syllable of the lexical word. Its Latin orthography uses
acute accents to mark vowel length and a háček in letters such as *š*, *č*
and *ě*. Hard and soft consonant stems participate in palatalisation and
other alternations, while final devoicing and voicing assimilation shape
pronunciation. The
[phonology chapter](chapters/02-phonology.tex) distinguishes these contextual
processes from the contrasts and stem grades that carry lexical or
grammatical information.

Nouns have three productive cases—direct, transitive and indirect—and
distinguish singular from plural through endings distributed across nine
declension classes. A restricted vocative survives in particular words used
for direct address. There is no grammatical gender. Inflection frequently
combines an ending with a change in the stem: vowels may disappear, change
height or alternate in length, and consonants may take a different grade.
Nominal morphology also expresses shared anchoring, which marks a referent
as accessible within the discourse. These patterns give the nominal system
considerable variety despite its small inventory of productive cases.

The finite verb marks aspect rather than grammatical tense, so temporal
location depends on context and adverbials. Its five aspectual categories
are perfective, retrospective, continuous, progressive and contemplative,
although individual predicate classes admit particular subsets. Aspect also
conditions split ergativity: ordinary perfective and retrospective
transitives place the patient in direct case and the agent in transitive
case, whereas ordinary active imperfective clauses place the agent
in direct case and the patient in indirect case. Antipassive, applicative,
causative and patient-selecting constructions interact with this system,
altering the available participants or their grammatical selection. The
relationship between verbal morphology and argument structure therefore
extends well beyond the expression of an event's temporal contour.

The finite predicate ordinarily closes the clause, nominal modifiers precede
their noun, and adpositions follow their complements. Within this head-final
organisation, the direct-case argument serves as a grammatical pivot and is
a default candidate for the discourse topic. Topicalisation remains
independent: another participant can become the topic while retaining its
case, and presentational clauses need no referential topic. Pronominal
arguments are commonly omitted when recoverable from discourse, although
the verb carries no person agreement. Particles contribute further
distinctions of phase, polarity, interrogation, evidentiality and speaker
stance.

## An illustration of Iridian

The following pair, used in the grammar's treatments of nominal case,
argument structure and information structure, illustrates the aspectual
alignment split:

| Iridian | English |
| --- | --- |
| *Marek travě pjaštíme.* | ‘Marek is eating bread.’ |
| *Travó Marku pjaštník.* | ‘Marek ate the bread.’ |

In the progressive sentence, *Marek* is direct and *travě* ‘bread’ is
indirect. In the perfective sentence, *Marku* is transitive and the anchored
form *travó* is direct. Marek remains the eater in both, although the
grammatical pivot changes. The English present and past suit the illustrated
contexts; Iridian expresses the aspectual contrast without tense inflection.
Neither aspect by itself requires the agent or the bread to be the discourse
topic. The fuller examples and their glosses appear in
[Chapter 7](chapters/07-argument-structure.tex), with their discourse
interpretation developed in [Chapter 14](chapters/14-information-structure.tex).

## About the grammar

The grammar comprises seventeen chapters in four parts. *Foundations*
introduces the language, its sounds and orthography, and the interactions
between phonology and morphology. *Words and phrases* develops nominal
morphology and syntax, verbal inflection, argument structure, derivation and
nominalisation. *The clause* treats clause structure, predication, negation,
particles, clause types and information structure, while *Complex syntax and
discourse* brings together embedding, clause linking and discourse
organisation. Appendices provide glossing abbreviations, paradigms, a
lexicon and historical notes.

Descriptive exposition, paradigms and interlinear examples are accompanied
by formal analyses of how words and clauses are organised. These analyses
connect case, aspect and participant selection with the broader structure of
the language; their assumptions and unresolved questions are distinguished
from the established grammatical patterns. The
[introductory chapter](chapters/01-overview.tex) provides a fuller overview
and explains the conventions used throughout.

## Development and current status

The project began with an incomplete grammar written in May and June 2019,
followed by revisions preserved in the repository. The present 2026 rewrite
substantially develops the description and its theoretical treatment. This
project history is separate from the fictional history of Iridian and its
neighbours.

The current chapters and `grammar.tex` constitute the operative description.
Earlier sources in `archive/2020/` and working material in `util/stub/`
preserve previous analyses and proposals; they have historical value but do
not establish rules for the current language.

## Reading and documentation

- Begin with the [Introduction and grammatical overview](chapters/01-overview.tex),
  browse the [source chapters](chapters/), or consult the
  [complete book source](grammar.tex).
- To produce the full PDF, follow the [build guide](docs/BUILDING.md).
- For source organisation, editorial conventions and validation, see the
  [development guide](docs/DEVELOPMENT.md); lexicon extraction has its own
  [utility documentation](util/README.md).
- The work is distributed under the [MIT licence](LICENSE).

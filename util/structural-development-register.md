# Structural migration and descriptive development register

The book now follows the seventeen-chapter, four-part arrangement in the structural review. This migration reorganises the current normative grammar; it does not supply new Iridian rules for the review's proposed descriptive completion pass.

## Principal treatments

| System | Principal exposition | Related treatment |
| --- | --- | --- |
| Sound system and writing | Chapters 2–3 | Historical hypotheses in Appendix D |
| Nominal inflection | Chapter 4 | Syntax and reference in Chapter 5 |
| Verbal inflection | Chapter 6 | Argument structure and voice in Chapter 7 |
| Derivation and nominalisation | Chapter 8 | Nominal modification in Chapter 5; clausal relatives in Chapter 15 |
| Clause architecture and placement | Chapter 9 | Local applications in Chapters 12–14 |
| Predication | Chapter 10 | Negative counterparts in Chapter 11 |
| Polarity and concord | Chapter 11 | Mood forms and constructions in Chapters 6 and 13 |
| Particles and scope | Chapter 12 | Clause typing in Chapter 13; discourse particles in Chapter 17 |
| Topic and focus | Chapter 14 | Reference tracking in Chapter 17 |
| Complementation and relativisation | Chapter 15 | Converbs and clause linking in Chapter 16 |

## Topics omitted from the published hierarchy

Empty headings have been removed, while any existing descriptive statements remain in their relevant treatment:

- Sentence chains as discourse units and tail-head linkage.
- Register and formality, politeness and the T–V distinction, and honorifics.
- Phatic and idiomatic expressions.
- Fixed expressions with converbs.
- Place nouns in `-(i)mašt`, for which the former heading supplied no productive rule or examples.

## Further descriptive work

The proposed completion pass remains distinct from this structural migration. Causal and concessive linkage, coordination, lexical compounding, and register require fuller established descriptions before expansion. Prosody must be assessed against the current grammar, which already contains more extensive secondary-stress and phrasing treatments than the reviewed outline assumed. Existing uncertainty about lexical selection, aspect, and interpretation must remain explicit; new examples require independent verification against the normative chapters.

## Apparatus and checks

Appendix A collects glossing abbreviations and notation, Appendix B consolidates paradigms, Appendix C contains the lexicon, and Appendix D separates historical hypotheses. Consolidated tables share their TeX source with the principal chapter tables. The bibliography is now `util/references.tex`.

The publication checker follows the actual includes for label, citation, environment and heading validation. Reviewed linguistic fixtures retain their historical grammatical-domain keys through `scripts/source_domains.py`, which assembles the relevant active chapter text without retaining obsolete chapter files. This preserves mutation-based checks when a single former chapter has been distributed across several new chapters.

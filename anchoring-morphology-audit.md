# Anchoring morphology and linearisation audit

Baseline: `c0b0410`, before the six-phase anchoring revision. This audit compares current normative sources, not the older chapter paths named in the supplied review. The semantic analysis preserves the established exponent inventory, case-number paradigms, stem selection, prosodic attachment, and feature-conditioned `si` precedence rule.

## Source preservation

| Normative source | Baseline and current SHA-256 | Result |
| --- | --- | --- |
| `chapters/04-nominal-morphology.tex` | `425939e2c804437896728790b0e5dce2d0bbc1831114e6cb6587d16509eaf9a6` | Byte-identical. All nominal declensions and anchoring tables preserved. |
| `chapters/08-derivation-nominalisation.tex` | `abc6e6a15d1fc44f920817b7080e4513103d62038e94a846641373557f91946b` | Byte-identical. Construction-conditioned deverbal anchoring preserved. |

All 20 `begingl`/`endgl` example blocks and all five `forest` trees in Chapter 5 are identical to the baseline, including their order. All six glossed example blocks in Chapter 4 are likewise identical; Chapter 8 contains neither of these block types. This comparison supplements the complete-file comparison for Chapters 4 and 8 and does not imply that every Iridian form is contained in a gloss block.

The Chapter 5 span from “Nominal-domain linearisation and prosodic attachment” through the end of “Complex nominals and nested anchoring domains” is unchanged except for a short cross-reference paragraph explaining that semantic indices and type shifts add no pronounced exponent or additional Anch terminal. Before that paragraph was inserted, its SHA-256 was `89004faf11a537fdf826e189d41e08250fff2b25d9f390ecb3650ca00177b53f`, identical to the baseline span. The PF equation, derivational schemata, domain definition, prosodic instructions, and judgement-status qualifications remain unchanged.

Reproduce the complete-file comparison with `git diff c0b0410 -- chapters/04-nominal-morphology.tex chapters/08-derivation-nominalisation.tex`; it produces no diff. Reproduce the Chapter 5 structural-block comparison with:

```python
import re
import subprocess
from pathlib import Path

path = 'chapters/05-nominal-syntax.tex'
before = subprocess.check_output(['git', 'show', 'c0b0410:' + path], text=True)
after = Path(path).read_text()
for pattern in (r'\\begingl\b.*?\\endgl\b',
                r'\\begin\{forest\}.*?\\end\{forest\}'):
    old_blocks = re.findall(pattern, before, re.S)
    new_blocks = re.findall(pattern, after, re.S)
    print(len(old_blocks), len(new_blocks), old_blocks == new_blocks)
```

Expected results: `20 20 True` and `5 5 True`.

## Selected paradigm controls

These forms are already specified in Chapter 4, chiefly `sec:nm-def-allomorph`, `sec:nm-def-nondirect`, and `tab:nm-cumulative-anchoring`. `DEF` is the traditional gloss for shared anchoring, not an additional semantic uniqueness operator.

| Class and cell | Unmarked form | Shared-anchored form | Preserved realisation |
| --- | --- | --- | --- |
| I direct singular | byl — child.DIR.SG | bylo — child.DIR.SG.DEF | Consonant-context `-o`. |
| I transitive singular | byla — child.TRS.SG | bylato — child.TRS.SG.DEF | Vowel-context `-to` follows the case form. |
| I indirect singular | bylam — child.IND.SG | bylamo — child.IND.SG.DEF | Consonant-context `-o`; the vowel inside the case ending does not select `-to`. |
| I direct plural | býle — child.DIR.PL | býlete — child.DIR.PL.DEF | Full `-te` remains after the vowel. |
| III regular direct singular | trava — bread.DIR.SG | travó — bread.DIR.SG.DEF | Cumulative ending, not general `-ato` contraction. |
| III indirect singular | travě — bread.IND.SG | travěte — bread.IND.SG.DEF | Separate suffix despite a cumulative cell elsewhere in the paradigm. |
| IV indirect singular | redě — blade.IND.SG | reďé — blade.IND.SG.DEF | Class-conditioned cumulative exponent. |
| VIII direct singular | pivo — beer.DIR.SG | pivó — beer.DIR.SG.DEF | Cumulative mass-singular form; no automatic portion interpretation. |
| VIII direct plural | piva — beer.DIR.PL | pivá — beer.DIR.PL.DEF | Cumulative plural; serving/variety count interpretation independent of anchoring. |
| VIII transitive singular | piva — beer.TRS.SG | pivato — beer.TRS.SG.DEF | Separate suffix; not confused with direct plural `pivá`. |

Bound-stem alternations such as `Marek/Marko` and `lobek/lúbko` remain lexical/class-conditioned; stable `byl/bylo` does not acquire raising. Coda vocalisation still follows allomorph selection: bare `byl` ends phonetically in a glide but selects consonant-context `-o`, with prevocalic lateral in `bylo`.

Chapter 8, `sec:nm-def-contraction`, retains the special direct anchored `-ovat` exponent in the deverbal construction. It does not license general contraction of `-ou` plus `-to`; Class V transitive `ránou` retains `ránouto`. Continuous participant `pjaštova` has only its unanchored direct singular specified, so the semantic account supplies no additional anchored or plural cells.

## Speaker anchoring and domain controls

| Existing expression or schema | Status | Preserved distinction |
| --- | --- | --- |
| si byl; si býle | Established minimal singular/plural forms. | `si` spells out `[+anch,−shr]`; the noun retains lexical stress. |
| si hradná byl | Existing constructed phrase using independently established modifier and noun. | Initial `si` precedes the modifier, which is its prosodic host. |
| [si bylam] tóm | Existing constructed nominal schema. | Speaker selection belongs to the possessor's own nominal domain. |
| si [bylam tóm] | Existing constructed nominal schema. | Speaker selection belongs to the containing book nominal. |
| si bylam tóm | Surface identity predicted by the PF rule. | The two ownership analyses are not an independently established ambiguity judgement. |
| si si bylam tóm | Explicit prediction of two nested speaker-anchor domains. | Not an independently established acceptability judgement; no new haplology or cluster-repair rule. |

The feature alternatives remain incompatible on one nominal spine. A possessor nevertheless has its own Anch terminal and pronunciation domain. PF orders a completed possessor as a block, then assigns left-edge precedence to the containing nominal's own speaker-anchor terminal. Structural ownership, linear precedence, and prosodic hosting remain distinct; a clitic can attach phonologically to a word inside the possessor without becoming that possessor's anchor.

The template does not independently license `si` with every quantifier or demonstrative. In particular, the new property-preserving denotations do not remove the unresolved status of those combinations or make the PF rule a wide-scope operation. Semantic indices have no additional exponent, and delayed type shifts do not add another pronounced nominal head.

## Scholarly framework and limits

Existing Klavans (1985), §§1.2–1.3, supports distinguishing clitic positioning domain from phonological host. Existing Embick and Noyer (2007) supplies the Distributed Morphology framework and adjacency restriction on Local Dislocation; it does not independently establish Iridian's nonlocal domain-edge precedence instruction. The current grammar already marks that instruction as an explicit language-specific analytical commitment. Existing Baker (1985) and Harley (2011, 2013) support the restricted morphological-structure discussion, whose text continues to distinguish hierarchy, attachment, and postsyntactic realisation. No new external morphological generalisation is needed for this preservation phase.

The semantic survey guides the distinction between reference and exponence, rather than supplying evidence to replace the Iridian morphology. The theoretical interpretation and diagnostic questions developed in Phases 1–5 introduce no new nominal suffix, fusion cell, case frame, stress rule, or obligatory weak/strong article distribution.

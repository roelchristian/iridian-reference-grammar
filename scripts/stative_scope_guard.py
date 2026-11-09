"""Compare the explicitly frozen relative scope with reviewed PR19 content.

Hashes record the reviewed baseline, rather than regenerated current text.
Whole source spans cover rules whose paragraphs do not repeat the exponent.
All exponent-bearing paragraphs are compared as a multiset after migration,
rejecting additions, losses and edits while allowing chapter relocation.
This scope guard supplements independent linguistic review.
"""
from collections import Counter
import hashlib
import json
from pathlib import Path
import re

from source_domains import DOMAIN_CHAPTERS


ROOT = Path(__file__).resolve().parents[1]


def digest(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


# Reviewed finite-clause cross-references inside the frozen relative treatment.
# Normalise only these exact replacements; reduced selection, examples and
# morphology remain compared with the original reviewed hashes.
FINITE_REFERENCE_REVISIONS = (
    (" content questions permit in-situ and fronted interrogative expressions",
     " content questions permit interrogative expressions with ordinary placement\n"
     " or marked wh-fronting"),
    ("Finite content question & Interrogative expression in situ or overtly fronted &\n"
     r"Interrogative licensing independent of displacement; pre-\ird{by} landing site" "\n"
     "not established by the surface paradigm",
     "Finite content question & Ordinary placement or marked wh-fronting &\n"
     "Lower occurrence interpreted under Pol; marked focus lands above the ordinary\n"
     "placement field"),
)


# User-authorised retrospective replacement. Reverse only these exact forms
# and descriptions when comparing protected relative material with its original
# hashes; surrounding selection, case and interpretation remain significant.
RETROSPECTIVE_REVISIONS = (
    (r'\ird{mužnávovy nuž}', r'\ird{mužnaisovy nuž}'),
    (r'\ird{pjáščavou}', r'\ird{pjáščaisou}'),
    (r'\ird{pjaštnávou}', r'\ird{pjaštnaisou}'),
    (
        "aspect exponents are short " r"\ird{-a}, \ird{-ime}, free perfective" "\n"
        r"\ird{-ek}, \ird{-av} and \ird{-až}. Inchoative perfective selects the",
        "aspect exponents are short " r"\ird{-a}, \ird{-ime}, free perfective" "\n"
        r"\ird{-ek} and \ird{-až}, alongside invariant retrospective \ird{-ais}." "\n"
        "Inchoative perfective selects the",
    ),
    (
        r"Retrospective \ird{-av}/\ird{-áv} similarly gives" "\n"
        r"\ird{-avou}/\ird{-ávou}. Continuous Asp together with",
        r"Retrospective \ird{-ais} similarly gives \ird{-aisou}." "\n"
        "Continuous Asp together with",
    ),
    (
        "blocks outer causative root lengthening. Immediately following aspect endings\n"
        r"are short: \ird{-ime, -ek/-ik, -av, -až}. This restricted rhythmic",
        "blocks outer causative root lengthening. Immediately following progressive,\n"
        r"perfective and contemplative endings are short: \ird{-ime, -ek/-ik, -až};" "\n"
        r"retrospective \ird{-ais} is invariant. This restricted rhythmic",
    ),
)


# Preserve both the prior spelling-migrated digests and the exact replacement
# digests. This does not regenerate the original freeze or admit further edits.
RETROSPECTIVE_FILE_REVISIONS = {
    'scripts/stative-fixtures.json': (
        'bd915250b9c2882245d5c03089c97395e78f1642acaf95ed9f0a49cfcbb5914e',
        'cf178e0d981f14a6c3563fecea7e6980cc6ec28d4f6905c81a81644822a63c5f'),
    'util/stative-paradigms.md': (
        '0cdf34305d68f21819504ae41d909cd7dda00dff566a4c46bae32aec4cf21f59',
        '4314fc15582e991ca4b29b15e79cf2abf6a4b01c22d1f5834e65babb25f17f7f'),
}


# The source postposition and open conditional were explicitly renamed.
# Normalise only their exact phrases in the protected example and overview;
# the surrounding case rules and relative constructions remain significant.
LEXICAL_FORM_REVISIONS = (
    (r"\ird{Marcí travěte pjaštově z} \trsl{since/after Marek's eating of the" "\n"
     r"bread}, the event head bears the case required by \ird{z}, while",
     r"\ird{Marcí travěte pjaštově cy} \trsl{since/after Marek's eating of the" "\n"
     r"bread}, the event head bears the case required by \ird{cy}, while"),
    (r"Non-finite converb suffixes (\ird{-u}, \ird{-ení}, \ird{-ěc}," "\n"
     "\t\t" r"\ird{-ic}, \ird{-ezmy}, \ird{-it}, \ird{-ouc}, \ird{-esny})",
     r"Non-finite converb suffixes (\ird{-u}, \ird{-ení}, \ird{-ěc}," "\n"
     "\t\t" r"\ird{-ej}, \ird{-ezmy}, \ird{-it}, \ird{-ouc}, \ird{-esny})"),
    (r"Event nominal in indirect case + \ird{z}, \ird{do}, \ird{na}, or \ird{u}",
     r"Event nominal in indirect case + \ird{cy}, \ird{do}, \ird{na}, or \ird{u}"),
)


# Everyday cooking examples replace benefactive eating in the presentational
# pairs; the news example gains a conversational context. Normalise only each
# complete reviewed illustration, preserving the original relative-rule hashes
# and detecting any further change to its frame.
PRESENTATIONAL_EXAMPLE_REVISIONS = (
    (
        r"\gla Kářnikový senica zada.//" "\n"
        r"\glb read-\textsc{trs}-\Pf{}-\textsc{rel} news.\Dir{} \NegExst{}-\Cont{}//" "\n"
        r"\glft \trsl{There is no news that (I) read.} \lingcontext{\ird{zad-} obligatory in the negative presentational}//",
        r"\gla Kářnikový senica zada.//" "\n"
        r"\glb read-\textsc{trs}-\Pf{}-\textsc{rel} news.\Dir{} \NegExst{}-\Cont{}//" "\n"
        r"\glft \trsl{There is no news that I read.}" "\n"
        r"\lingcontext{asked about the morning's news, the speaker reports having read none}//",
    ),
    (
        r"\gla Pjaštébikový byl jeca.//" "\n"
        r"\glb eat-\Appl{}-\Pf{}-\textsc{rel} child.\Dir{} \Exst{}-\Cont{}//" "\n"
        r"\glft \trsl{There is a child for whose benefit someone ate.} \lingcontext{promoted participant introduced}//",
        r"\gla Staženě marébikový byl jeca.//" "\n"
        r"\glb dinner.\Ind{} cook-\Appl{}-\Pf{}-\textsc{rel} child.\Dir{} \Exst{}-\Cont{}//" "\n"
        r"\glft \trsl{There is a child for whom someone cooked dinner.} \lingcontext{promoted participant introduced}//",
    ),
    (
        r"\gla Pjaštébikový byl zada.//" "\n"
        r"\glb eat-\Appl{}-\Pf{}-\textsc{rel} child.\Dir{} \NegExst{}-\Cont{}//" "\n"
        r"\glft \trsl{There is no child for whose benefit someone ate.} \lingcontext{negative presentational; promoted participant denied}//",
        r"\gla Staženě marébikový byl zada.//" "\n"
        r"\glb dinner.\Ind{} cook-\Appl{}-\Pf{}-\textsc{rel} child.\Dir{} \NegExst{}-\Cont{}//" "\n"
        r"\glft \trsl{There is no child for whom someone cooked dinner.} \lingcontext{negative presentational; promoted participant denied}//",
    ),
)


# Exact user-authorised State-selection edits in relative-bearing prose are
# normalised; every earlier relative rule and example remains compared with
# the reviewed baseline, as do further edits to these passages.
STATE_SELECTION_REVISIONS = (
    (
        "Inchoative perfective is eventive:\n"
        r"\ird{mužnélek}, not a mechanical extension of the stative \ird{-ik}.",
        "Inchoative perfective selects the\n"
        r"ordinary eventive exponent, as in \ird{mužnélek}.",
    ),
    (
        r"\subsection{Nominalisation and aspectual attribution of statives}" "\n\n",
        r"\subsection{Nominalisation and aspectual attribution of statives}" "\n\n"
        "Aspectual selection is preserved under participant nominalisation and\n"
        "relative formation: a simple state admits continuous, retrospective and\n"
        "contemplative viewpoint, while progressive and perfective require an\n"
        "independently licensed dynamic predicate.\n\n",
    ),
    (
        r"other relatives. \synhead{StateP}, \synhead{BecomeP} and event-derived",
        "other relatives. Relative embedding preserves the aspectual restrictions of\n"
        "its selected predicate: a stative output admits continuous, retrospective or\n"
        "contemplative aspect, while an eventive derivative has its independently\n"
        r"licensed viewpoint inventory. \synhead{StateP}, \synhead{BecomeP} and event-derived",
    ),
)


# Exact nominal-predication revisions preserve the frozen relative rules and
# examples while repairing semantic composition and the derivational reference.
# Only these reviewed complete passages are normalised; further changes to
# their analysis or any relative construction remain visible to the guard.
NOMINAL_PREDICATION_REVISIONS = (
    (
        r"""When the predicative complement of a zero-copula equative clause is a
\term{participant nominal} (a nominalised verb form,
§\,\ref{sec:nmlz-predicative}), the construction is
\term{identificational}: the topic \synhead{DP} is identified with the referent
of the nominal description, which is interpreted as definite in the following example.
The English definite descriptions here and in the related existential examples
presume contextually recoverable referents; neither unanchored indirect
\ird{lúbcí} nor participant \ird{-ou} itself encodes definiteness or uniqueness:""",
        r"""A participant nominal can predicate an event-participant description of an
independently supplied referent. Its internal derivation supplies a property
rather than an obligatorily definite individual
(§\,\ref{sec:nm-derived-participant}); in an identificational context,
the clause relates a candidate to the participant description supplied by an
established event. The finite clause and the participant-nominal
construction differ in the following pair:""",
    ),
    (
        r"""\noindent In both clauses, bare \ird{lobek} permits the contextually
recoverable reading expressed by English \trsl{the apple}; shared-anchored
\ird{lúbko} would explicitly mark retrieval through the common discourse
model (§\,\ref{sec:nm-def}). That anchoring contrast leaves the predication
type unchanged: transitive \ird{Janku} with finite \ird{pjaštník} forms the
verbal clause, whereas indirect \ird{Jancí} with participant nominal
\ird{pjaštníkou} forms the equative. In (b), the apple is identified with the
referent of the nominalised description. An
agent-nominal equative identifies the topic as the agent of the nominalised
event:""",
        r"""\noindent In both clauses, bare \ird{lobek} permits the contextually
recoverable reading expressed by English \trsl{the apple}; shared-anchored
\ird{lúbko} would explicitly mark retrieval through the common discourse
model (§\,\ref{sec:nm-def}). Transitive \ird{Janku} with finite
\ird{pjaštník} forms the verbal clause, whereas indirect \ird{Jancí}
with participant nominal \ird{pjaštníkou} forms the non-verbal
predication. The latter's event reference frame remains internal to the
nominal description, independently of the matrix zero-copula relation.

Let \(j\) denote Janek, \(a\) the apple and \(R_e\) the embedded
event reference frame. At a fixed evaluation situation, the patient nominal
supplies the following property, whose application to \(a\) states that
the apple satisfies the description:
\[
\begin{aligned}
 P_{R_e}&=\lambda x\,\exists e[\operatorname{eat}(e)
   \land\operatorname{Theme}(e,x)\\
   &\qquad\land\operatorname{Agent}(e,j)
   \land\operatorname{PF}(e,R_e)],\\
 \mathrm{Eq}(P_{R_e})(a)&=P_{R_e}(a).
\end{aligned}
\]
The nominal relational head supplies the agent restriction before event
closure (§\,\ref{sec:nm-derived-participant}). Where the context
identifies a unique relevant satisfier, the description can instead receive
the individual interpretation \(y=\iota x P_{R_e}(x)\), with the identity
composition \(\mathrm{IDENT}(y)(a)=[a=y]\)
(§\,\ref{sec:nominal-predicate-semantics}). This definite shift requires
a context supporting its definedness; neither participant \ird{-ou} nor
the indirect dependent supplies uniqueness. The English free relative
\trsl{what Janek ate} is compatible with the contextual identification, but
does not by itself distinguish property application from referential
equation in Iridian.

The agent-nominal counterpart characterises Janek as a participant in an
eating event whose theme is the contextually recoverable apple:""",
    ),
    (
        r"""Identificational negation rejects the proposed participant identification;
its interpretation and its contrast with finite verbal negation are illustrated
in §\,\ref{sec:negative-identificational-constructions}.""",
        r"""The agent nominal similarly supplies a property of eaters, with its theme
restriction introduced in the nominal domain. In its property interpretation,
the clause asserts that Janek satisfies this description; an identity
interpretation additionally requires a contextually identified individual
satisfying it. Identificational use thus concerns the relation between a
candidate and an event-participant description, without automatically
constituting a distinct specificational construction. The examples do not
independently establish the property--value organisation described in
analyses of specificational clauses \cite[§4.1]{djarv2021}.

Identificational negation rejects satisfaction of the description or the
contextually licensed equation, according to its interpretation; it does not
itself presuppose an event or a unique participant. The established-event
contexts that support the English definite readings, and the contrast with
finite verbal negation, are illustrated in
§\,\ref{sec:negative-identificational-constructions}.""",
    ),
)



def articleless_reference_text(path, text, root=ROOT, migrations=None):
    """Undo only literal reviewed anchoring edits for original-hash comparison.

    This is a comparison adapter, never a production surface realiser. Source
    paths prevent a matching quotation elsewhere from acquiring a licence;
    logical-domain overrides are limited to their established chapter inputs.
    Additional edits defeat the exact match and remain visible to the frozen
    relative-source checks. The original freeze fixture is never regenerated.
    """
    # Restore the retrospective wording before matching older complete passages.
    for original, revised in RETROSPECTIVE_REVISIONS:
        text = text.replace(revised, original)
    if migrations is None:
        fixture = root / 'scripts/articleless-scope-migrations.json'
        if not fixture.exists():
            return text
        migrations = json.loads(fixture.read_text(encoding='utf-8'))
    allowed = {path}
    if path.startswith('chapters/'):
        allowed.update(f'chapters/{chapter}.tex'
                       for chapter in DOMAIN_CHAPTERS.get(Path(path).stem, ()))
    for passage in migrations['passages']:
        if passage['source'] in allowed:
            text = text.replace(passage['revised'], passage['original'])
    return text

def frozen_reference_text(path, text):
    for original, revised in RETROSPECTIVE_REVISIONS:
        text = text.replace(revised, original)
    # Migration comparison uses reviewed old spellings, never newly generated
    # hashes of current grammatical content. These exact lexical replacements
    # and the relative suffix alone are reversible within the frozen material.
    # Old characters here are historical comparison input, not modern forms.
    for modern, original in (
            ('Janėk', 'Janek'), ('janėk', 'janek'), ('perėk', 'perek'),
            ('lobėk', 'lobek'), ('obėl', 'obel'), ('sviňėk', 'sviňek'),
            ('tězėň', 'tězeň'), ('kolėn', 'kolen'), ('razėň', 'razeň'),
            ('stólėk', 'stólek'), ('Merėk', 'Merek'), ('berėl', 'berel'),
            ('pěštėl', 'pěštel'), ('Marėk', 'Marek'), ('marėk', 'marek'),
            ('uzėl', 'uzel')):
        text = text.replace(modern, original)
        text = text.replace(modern[0].upper() + modern[1:], original[0].upper() + original[1:])
    # The separately inflected nominal transitive -ovy was already short.
    # Preserve its exact reviewed row when reversing relative -ovy spellings;
    # a changed cell or an added example still changes the protected unit hash.
    nominal_row = (r'Transitive singular & \ird{pjáščikovy / pjáščikovyte} '
                   r'& \ird{pjaštovy / pjaštovyte}')
    text = text.replace(nominal_row, 'FROZEN_NOMINAL_TRANSITIVE_ROW')
    # Lexical novy 'new' already had short y and is not the relative exponent.
    text = re.sub(r'(?<!\w)novy(?!\w)', 'FROZEN_LEXICAL_NEW', text)
    text = re.sub(r'ovy(?=\W|$)', 'ový', text)
    text = text.replace('FROZEN_LEXICAL_NEW', 'novy')
    text = text.replace('FROZEN_NOMINAL_TRANSITIVE_ROW', nominal_row)
    if path == 'chapters/08-complex-sentences.tex':
        for original, revised in FINITE_REFERENCE_REVISIONS:
            text = text.replace(revised, original)
    for original, revised in (LEXICAL_FORM_REVISIONS + PRESENTATIONAL_EXAMPLE_REVISIONS
                              + STATE_SELECTION_REVISIONS
                              + NOMINAL_PREDICATION_REVISIONS):
        text = text.replace(revised, original)
    return text


def structural_text(text):
    """Ignore headings/labels/spacing, plus two exact migrated cross-references.

    Every linguistic form, gloss, example, rule and citation remains significant.
    The cross-reference replacements are deliberately phrase-specific.
    """
    text = re.sub(r'\\(?:section|subsection|subsubsection|paragraph)\*?\{((?:[^{}]|\{[^{}]*\})*)\}', '', text)
    text = re.sub(r'\\label\{[^}]+\}(?:%[^\n]*)?', '', text)
    text = text.replace(r'\noindent', '')
    text = text.replace(
        r'in \ird{-(h)ár} and \ird{-ist} (§\,\ref{sec:lexical-agent-nouns}) classify a',
        r'in \ird{-(h)ár} and \ird{-ist} (Chapter~\ref{ch:derivational}) classify a')
    text = text.replace(
        r'is the ordinary property modifier (§\,\ref{sec:stative-attr}).',
        r'is the ordinary property modifier (Chapter~\ref{ch:verbs}).')
    return re.sub(r'\s+', ' ', text).strip()


def publication_sources(root, overrides):
    """Read actual included chapters, supporting legacy logical-domain mutations."""
    paths = re.findall(r'^\\include\{(chapters/[^}]+)\}',
                       (root / 'grammar.tex').read_text(), re.MULTILINE)
    sources = {path + '.tex': (root / (path + '.tex')).read_text()
               for path in paths}
    for path, text in overrides.items():
        key = Path(path).stem
        if path.startswith('chapters/') and key in DOMAIN_CHAPTERS:
            for chapter in DOMAIN_CHAPTERS[key]:
                sources.pop(f'chapters/{chapter}.tex', None)
            sources[path] = text
        elif path.startswith('chapters/'):
            sources[path] = text
    return sources


def check_scope(root=ROOT, fixtures=None, overrides=None):
    """Check migrated content against units verified from the reviewed baseline.

    The original raw span/paragraph digests remain in the fixture as provenance.
    Migration hashes derive from those verified originals, with one explicitly
    documented consolidation into the canonical equative treatment.
    """
    if fixtures is None:
        fixtures = json.loads((root / 'scripts/stative-scope-freeze.json').read_text())
    overrides = {} if overrides is None else overrides
    migration = fixtures['migration']
    failures = []
    paragraphs = []
    units = []
    scope_migration = root / 'scripts/articleless-scope-migrations.json'
    if scope_migration.exists():
        provenance = json.loads(scope_migration.read_text(encoding='utf-8'))
        if hashlib.sha256((root / 'scripts/stative-scope-freeze.json').read_bytes()).hexdigest() != provenance['freeze_sha256']:
            failures.append('articleless: original stative-scope freeze fixture changed')
        if any(digest(p['original']) != p['original_sha256'] for p in provenance['passages']):
            failures.append('articleless: exact source-migration provenance changed')
    sources = {path: frozen_reference_text('chapters/08-complex-sentences.tex',
                                         articleless_reference_text(path, text, root))
               for path, text in publication_sources(root, overrides).items()}
    for path, text in sources.items():
        # Exact reviewed revisions retain the original migration hashes.
        text = frozen_reference_text('chapters/08-complex-sentences.tex', text)
        for block in re.split(r'\n\s*\n', text):
            normal = structural_text(block)
            if normal:
                units.append(digest(normal))
                if 'ový' in block:
                    paragraphs.append(digest(normal))
    lexicon = overrides.get('util/lexicon.tex')
    if lexicon is None:
        lexicon = (root / 'util/lexicon.tex').read_text()
    lexicon = frozen_reference_text('util/lexicon.tex', lexicon)
    paragraphs.extend(digest(structural_text(line)) for line in lexicon.splitlines()
                      if 'ový' in line and structural_text(line))
    if Counter(paragraphs) != Counter(migration['paragraphs']):
        failures.append('publication: frozen exponent-bearing paragraphs changed, lost or added')
    observed = Counter(units)
    replacements = {item['original_span']: item
                    for item in migration['editorial_consolidations']}
    for span in migration['spans']:
        expected = Counter(span['units'])
        replacement = replacements.get(span['original_sha256'])
        if replacement:
            expected.subtract(replacement['original_units'])
            expected.update(replacement['replacement_units'])
        if expected - observed:
            failures.append('publication: protected relative source units changed or lost '
                            + span['original_sha256'][:12])
    # These current bounded regions retain the old whole-span protection
    # against adding an unreviewed rule even when it does not repeat -ový.
    # Region units were verified against the original chapters individually.
    for region in migration['regions']:
        candidates = [text for text in sources.values()
                      if region['start'] in text and region['end'] in text]
        if len(candidates) != 1:
            failures.append(region['source'] + ': protected region markers changed')
            continue
        text = frozen_reference_text('chapters/08-complex-sentences.tex', candidates[0])
        start, end = region['start'], region['end']
        if text.count(start) != 1 or text.count(end) != 1:
            failures.append(region['source'] + ': protected region markers are not unique')
            continue
        block = text[text.index(start):text.index(end)]
        current = Counter(digest(structural_text(unit))
                          for unit in re.split(r'\n\s*\n', block)
                          if structural_text(unit))
        if current != Counter(region['units']):
            failures.append(region['source'] + ': protected relative region changed or added')
    for path, expected in fixtures['files'].items():
        text = overrides[path] if path in overrides else (root / path).read_text()
        spelling = fixtures.get('vowel_spelling_migration', {}).get('files', {}).get(path)
        if spelling:
            if spelling['original_sha256'] != expected:
                failures.append(f'{path}: spelling migration lost its reviewed provenance')
            expected = spelling['migrated_sha256']
        retrospective = RETROSPECTIVE_FILE_REVISIONS.get(path)
        if retrospective:
            if retrospective[0] != expected:
                failures.append(f'{path}: retrospective migration lost its prior provenance')
            expected = retrospective[1]
        if digest(text) != expected:
            failures.append(f'{path}: earlier protected fixture or selection file changed')
    return failures

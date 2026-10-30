"""A partial reference transducer for an independently licensed suffix boundary.

Inputs are IPA segment tokens of an already selected stem, not written letters.
The caller supplies morphological licensing and velar-class membership; this
module does not discover them from a word or suffix vowel. It neither selects
lexical/vocalic allomorphs nor performs antipassive exponence, syllabification,
contextual phonetics or spelling. Constructed test chains assert operator
properties, not the existence of additional Iridian constructions.
"""
from dataclasses import dataclass
import json
from pathlib import Path
from typing import Tuple


class BoundaryError(ValueError):
    """An input lies outside this explicitly bounded mapping."""


@dataclass(frozen=True)
class BoundaryState:
    segments: Tuple[str, ...]
    history: Tuple[str, ...] = ()


@dataclass(frozen=True)
class BoundaryLicence:
    identifier: str
    grade: str
    licensed: bool
    velar_member: bool = False
    exposed_edge: bool = True


class BoundaryTransducer:
    def __init__(self, rules):
        self.rules = rules
        grades = rules['grades']
        if set(grades) != {'plain', 'front', 'mixed', 'restricted'}:
            raise BoundaryError('only the four named grade bundles are supported')
        for grade in grades.values():
            if (set(grade) != {'coronal_labial_pal', 'velar_output'}
                    or type(grade['coronal_labial_pal']) is not bool
                    or grade['velar_output'] not in {'identity', 'ts', 'tʃ'}):
                raise BoundaryError('invalid grade declaration')
        self.consonants = set(rules['consonants'])
        self.vowels = set(rules['vowels'])
        self.inventory = self.consonants | self.vowels
        if self.consonants & self.vowels:
            raise BoundaryError('consonant and vowel tokens must be distinct')
        mapping = rules['pal_correspondences']
        if ('k' in mapping or not set(mapping) <= self.consonants
                or not set(mapping.values()) <= self.consonants):
            raise BoundaryError('PAL correspondences cannot replace the separate velar instruction')

    @classmethod
    def from_file(cls, path=None):
        path = Path(path) if path is not None else Path(__file__).with_name('boundary-mapping.json')
        return cls(json.loads(path.read_text(encoding='utf-8')))

    def _validate_segments(self, segments):
        if not isinstance(segments, tuple) or any(not isinstance(item, str) for item in segments):
            raise BoundaryError('provide a tuple of phonological segment tokens, not orthographic text')
        unknown = set(segments) - self.inventory
        if unknown:
            raise BoundaryError('unsupported phonological segment: ' + ', '.join(sorted(unknown)))

    def apply(self, state, licence, suffix=()):
        """Map the original exposed edge once, then attach the supplied exponent.

        A consumed boundary cannot be replayed. A genuinely new, independently
        licensed boundary can act on the current edge, never on an earlier root
        through an intervening segment. Vowel-final mutation needs separately
        selected ending allomorphy, outside this consonantal transducer.
        """
        self._validate_segments(state.segments)
        self._validate_segments(suffix)
        if not state.segments:
            raise BoundaryError('the selected input must have an edge')
        if type(licence.licensed) is not bool or not licence.licensed:
            raise BoundaryError('the morphological boundary is not licensed')
        if type(licence.exposed_edge) is not bool or not licence.exposed_edge:
            raise BoundaryError('the selected edge is not structurally exposed')
        if type(licence.velar_member) is not bool:
            raise BoundaryError('velar-class membership must be specified as a boolean')
        if not isinstance(licence.identifier, str) or not licence.identifier.strip():
            raise BoundaryError('a morphological boundary identifier is required')
        if licence.identifier in state.history:
            raise BoundaryError('this morphological boundary has already been interpreted')
        if not isinstance(licence.grade, str) or licence.grade not in self.rules['grades']:
            raise BoundaryError('unlicensed grade; free feature combinations are not accepted')
        grade = self.rules['grades'][licence.grade]
        original = state.segments[-1]
        if original in self.vowels and licence.grade != 'plain':
            raise BoundaryError('vowel-final mutation requires independently selected ending allomorphy')
        if original == 'k' and licence.velar_member:
            output = grade['velar_output']
            if output == 'identity':
                output = original
        elif grade['coronal_labial_pal']:
            output = self.rules['pal_correspondences'].get(original, original)
        else:
            output = original
        # No lookup is applied to output: /k/ -> /ts/ cannot feed PAL here.
        return BoundaryState(state.segments[:-1] + (output,) + suffix,
                             state.history + (licence.identifier,))


def check_boundary_fixtures(transducer, fixtures):
    """Compare transduction against separately authored, literal expectations."""
    failures = []
    for fixture in fixtures['cases']:
        state = BoundaryState(tuple(fixture['input']))
        try:
            for step in fixture['boundaries']:
                state = transducer.apply(
                    state, BoundaryLicence(step['identifier'], step['grade'],
                                           step['licensed'], step.get('velar_member', False),
                                           step.get('exposed_edge', True)),
                    tuple(step.get('suffix', [])))
        except BoundaryError as error:
            if 'error_contains' not in fixture or fixture['error_contains'] not in str(error):
                failures.append(f"boundary fixture {fixture['id']}: unexpected rejection: {error}")
        else:
            if 'error_contains' in fixture:
                failures.append(f"boundary fixture {fixture['id']}: expected rejection")
            elif list(state.segments) != fixture['expected']:
                failures.append(f"boundary fixture {fixture['id']}: {list(state.segments)} != {fixture['expected']}")
    return failures

"""Local quantity-grade selection on an explicitly selected phonological stem.

The caller supplies the eligible nucleus and its morphological domain. This
module neither finds roots in written words nor selects fleeting-vowel stems,
consonantal grades, aspect endings, or rhythmic allomorphs. Its output can be
passed separately to the consonantal boundary mapper. The selected nuclei
retain traditional, conservative vowel classes: eː and oː are not additional
phonemes of the principal spoken variety. Apply vowel_realisation.realise_vowel_classes after
morphological selection to obtain the chosen variety's vowel categories.
"""
from dataclasses import dataclass
import json
from pathlib import Path
from typing import Tuple


class QuantityError(ValueError):
    """A requested selection exceeds the licensed local quantity operation."""


@dataclass(frozen=True)
class QuantityLicence:
    identifier: str
    grade: str
    licensed: bool
    domain: Tuple[int, int]
    eligible: Tuple[int, ...]
    target: int
    raising_licensed: bool = False


class QuantityGrades:
    def __init__(self, rules, inventory):
        self.rules = rules
        self.inventory = set(inventory)
        if set(rules) != {'long_pairs', 'raised_pairs'}:
            raise QuantityError('quantity rules require length pairs and licensed raising pairs')
        pairs = rules['long_pairs']
        if any(source not in self.inventory or output not in self.inventory
               or 'ː' in source or output.count('ː') != 1
               for source, output in pairs.items()):
            raise QuantityError('length pairs must map short nuclei to one ordinary long degree')
        self.vowels = set(pairs) | set(pairs.values()) | {'ou̯'}
        if not set(rules['raised_pairs']) <= self.vowels:
            raise QuantityError('raising input must be a vowel nucleus')
        if not set(rules['raised_pairs'].values()) <= self.vowels:
            raise QuantityError('raising output must be a vowel nucleus')
        if any(source.count('ː') != output.count('ː')
               for source, output in rules['raised_pairs'].items()):
            raise QuantityError('raising alone must preserve vowel quantity')
        if set(rules['long_pairs']) & set(rules['long_pairs'].values()):
            raise QuantityError('lengthening must not generate a third quantity degree')

    @classmethod
    def from_file(cls):
        directory = Path(__file__).resolve().parent
        rules = json.loads((directory / 'quantity-grades.json').read_text(encoding='utf-8'))
        inventory = json.loads((directory / 'boundary-mapping.json').read_text(encoding='utf-8'))
        return cls(rules, inventory['vowels'] + inventory['consonants'])

    def apply(self, segments, licence):
        """Return one selected grade, preserving every non-target token.

        Domain bounds are token offsets [start, stop), not written-letter or
        syllable counts. Eligibility excludes fleeting nuclei and morphological
        material outside the selected root/stem; its lexical assignment belongs
        to the caller. G0 preserves the input, including lexical length.
        """
        if (not isinstance(segments, tuple) or not segments
                or any(not isinstance(token, str) for token in segments)):
            raise QuantityError('provide a nonempty tuple of phonological segment tokens')
        if set(segments) - self.inventory:
            raise QuantityError('unsupported phonological token; spelling is not an input')
        if type(licence.licensed) is not bool or not licence.licensed:
            raise QuantityError('quantity selection is not morphologically licensed')
        if not isinstance(licence.identifier, str) or not licence.identifier.strip():
            raise QuantityError('an explicit local-domain identifier is required')
        if not isinstance(licence.grade, str) or licence.grade not in {'G0', 'G1', 'G2', 'G3'}:
            raise QuantityError('only G0, G1, G2 and G3 are defined')
        if (not isinstance(licence.domain, tuple) or len(licence.domain) != 2
                or any(type(i) is not int for i in licence.domain)):
            raise QuantityError('domain must specify two integer token offsets')
        start, stop = licence.domain
        if not 0 <= start < stop <= len(segments):
            raise QuantityError('quantity domain lies outside the selected input')
        if (not isinstance(licence.eligible, tuple) or not licence.eligible
                or any(type(i) is not int or not start <= i < stop
                       or segments[i] not in self.vowels for i in licence.eligible)
                or len(set(licence.eligible)) != len(licence.eligible)):
            raise QuantityError('eligible nuclei must be distinct vowels inside the local domain')
        if type(licence.target) is not int or licence.target not in licence.eligible:
            raise QuantityError('target must be an explicitly eligible local nucleus')
        if type(licence.raising_licensed) is not bool:
            raise QuantityError('raising membership must be an explicit boolean')
        vowel = segments[licence.target]
        if licence.grade in {'G2', 'G3'}:
            if not licence.raising_licensed or vowel not in self.rules['raised_pairs']:
                raise QuantityError('this nucleus has no licensed raised grade')
            vowel = self.rules['raised_pairs'][vowel]
        if licence.grade in {'G1', 'G3'}:
            vowel = self.rules['long_pairs'].get(vowel, vowel)
        return segments[:licence.target] + (vowel,) + segments[licence.target + 1:]

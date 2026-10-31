"""Resolve traditional vowel classes after morphological grade selection.

This bounded mapping supplies vowel categories, not a phonetic transcription.
Consonantal grades, contextual labial and /x/ allophony, stress assignment,
syllabification and spelling remain separate. Stress and boundary tokens already
present in a sequence are preserved; no register-specific ý–í merger is applied.
"""


def realise_vowel_classes(segments, variety='principal'):
    """Map traditional long mid classes in one explicitly selected variety.

    `principal` has both mergers; `back-merged` retains the front mid class;
    `conservative` retains both. Existing high vowels and every short vowel
    remain unchanged. Inputs are segment tokens, never orthographic strings.
    """
    mappings = {
        'principal': {'eː': 'iː', 'oː': 'uː'},
        'back-merged': {'oː': 'uː'},
        'conservative': {},
    }
    if not isinstance(variety, str) or variety not in mappings:
        raise ValueError('choose principal, back-merged or conservative realisation')
    if (not isinstance(segments, tuple)
            or any(not isinstance(token, str) or not token for token in segments)):
        raise ValueError('provide a tuple of nonempty phonological segment tokens')
    mapping = mappings[variety]
    return tuple(mapping.get(token, token) for token in segments)

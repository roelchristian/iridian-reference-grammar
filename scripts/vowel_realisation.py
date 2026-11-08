"""Resolve traditional vowel classes after morphological grade selection.

This bounded mapping supplies vowel categories, not a phonetic transcription.
Consonantal grades, contextual labial and /x/ allophony, stress assignment,
syllabification and spelling remain separate. Stress and boundary tokens already
present in a sequence are preserved. The separate central-y renderer requires
an explicit lexical-stress specification and preserves one token per nucleus.
"""
from boundary_transducer import BoundaryTransducer


def realise_vowel_classes(segments, variety='principal'):
    """Map traditional long mid classes in one explicitly selected variety.

    `principal` and `conservative` retain both long-mid contrasts. Regional
    `front-merged` and `back-merged` each merge one series; `fully-merged`
    merges both. Existing high vowels, short vowels and the atomic /uɔ/
    nucleus remain unchanged. Inputs are segment tokens, never orthographic strings.
    """
    mappings = {
        'principal': {},
        'front-merged': {'eː': 'iː'},
        'fully-merged': {'eː': 'iː', 'oː': 'uː'},
        'back-merged': {'oː': 'uː'},
        'conservative': {},
    }
    if not isinstance(variety, str) or variety not in mappings:
        raise ValueError('choose principal, conservative, front-merged, back-merged or fully-merged realisation')
    if (not isinstance(segments, tuple)
            or any(not isinstance(token, str) or not token for token in segments)):
        raise ValueError('provide a tuple of nonempty phonological segment tokens')
    mapping = mappings[variety]
    return tuple(mapping.get(token, token) for token in segments)


def lexical_stresses(nucleus_count):
    """Return ordinary stress for one already delimited lexical prosodic word.

    Primary stress is initial. Alternating secondary feet require a following
    syllable: a final unpaired third, fifth, etc. nucleus remains unstressed.
    The caller selects the word domain after stem selection and repair; this
    helper neither parses clitics/negation nor reads acute quantity accents.
    """
    if type(nucleus_count) is not int or nucleus_count < 1:
        raise ValueError('provide a positive count of retained vowel nuclei')
    return tuple('primary' if index == 0 else
                 'secondary' if index % 2 == 0 and index < nucleus_count - 1 else
                 'unstressed' for index in range(nucleus_count))


def realise_central_y(segments, stress, trajectory='back-central'):
    """Realise /ɨ/ from explicit stress, leaving other segment tokens intact.

    `stress` supplies primary/secondary/unstressed for each retained nucleus,
    in order. `back-central` selects [ɯ̯ɨ]; `central-front` selects [ɨi̯]. Both
    are single short-nucleus tokens. No /j/ is inserted or deleted and no PAL,
    fleeting-vowel deletion, coda process or grade retargeting is performed.
    Coda compression is not modelled: the deterministic default permits the
    back-to-central trajectory without constructing an extra offglide.
    """
    trajectories = {'back-central': 'ɯ̯ɨ', 'central-front': 'ɨi̯'}
    if not isinstance(trajectory, str) or trajectory not in trajectories:
        raise ValueError('choose back-central or central-front y realisation')
    inventory = BoundaryTransducer.from_file()
    if (not isinstance(segments, tuple) or not segments
            or any(not isinstance(token, str) for token in segments)
            or set(segments) - inventory.inventory):
        raise ValueError('provide a nonempty tuple of modern phonological segment tokens')
    nuclei = sum(token in inventory.vowels for token in segments)
    if (not isinstance(stress, tuple) or len(stress) != nuclei
            or any(value not in ('primary', 'secondary', 'unstressed') for value in stress)):
        raise ValueError('supply explicit lexical stress for every vowel nucleus')
    output = []
    index = 0
    for token in segments:
        if token in inventory.vowels:
            if token == 'ɨ' and stress[index] in ('primary', 'secondary'):
                token = trajectories[trajectory]
            index += 1
        output.append(token)
    return tuple(output)

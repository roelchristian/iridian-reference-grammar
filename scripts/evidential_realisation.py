"""Select the indirect-evidential exponent on an independently licensed host.

Inputs are selected phonological segment tokens before coda realisation, not
written words. This helper chooses /al/ after a consonant and /l/ after a
vowel. It does not establish evidential scope, select an aspectual allomorph,
perform spelling, or add stress. A later linker uses the ordinary front-grade
boundary mapper on the resulting final /l/.
"""
from boundary_transducer import BoundaryLicence, BoundaryTransducer


def attach_indirect_evidential(state, identifier, licensed, transducer=None):
    """Attach plain-grade Evid, preserving the complete selected host.

    Licensing and boundary-identity validation remain those of the existing
    transducer. Plain attachment already supports vowel-final inputs; this
    does not extend consonantal PAL mapping to vowel-final boundaries.
    """
    transducer = transducer if transducer is not None else BoundaryTransducer.from_file()
    edge = state.segments[-1] if state.segments else None
    exponent = ('l',) if edge in transducer.vowels else ('a', 'l')
    return transducer.apply(state, BoundaryLicence(identifier, 'plain', licensed), exponent)

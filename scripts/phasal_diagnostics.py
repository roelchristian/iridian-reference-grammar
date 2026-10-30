"""Small context-licensing diagnostics for the ordinary phasal approximation.

These functions test a supplied, contextually relevant pair of stages. They do
not infer reference time, presupposition projection, scalar ordering, modal
worlds or focus association from an Iridian string. The exclusive diagnostic
uses a fixed focus alternative at index zero and an explicitly supplied set.
It compares the two interpretations licensed for kamo, not free scope movement.
"""
import re


def ordinary_phase(particle, before, now):
    if particle not in ('vy', 'so'):
        raise ValueError('ordinary phasal diagnostic requires vy or so')
    if type(before) is not bool or type(now) is not bool:
        raise ValueError('stages must be explicitly supplied truth values')
    return now and (not before if particle == 'vy' else before)


def exclusive(values):
    if not values or any(type(value) is not bool for value in values):
        raise ValueError('exclusive diagnostic needs explicit alternatives')
    return values[0] and not any(values[1:])


def exclusive_phase(particle, before, now, scope):
    if len(before) != len(now) or len(before) < 2:
        raise ValueError('the two stages need the same nontrivial alternative set')
    # Validate all truth values even if a later expression would short-circuit.
    previous_exclusive, current_exclusive = exclusive(before), exclusive(now)
    if scope == 'low-exclusive':
        return ordinary_phase(particle, previous_exclusive, current_exclusive)
    if scope == 'high-exclusive':
        return exclusive([ordinary_phase(particle, old, new)
                          for old, new in zip(before, now)])
    raise ValueError('only the two specified exclusive readings are diagnosed')


def check_phasal_diagram(source, fixtures):
    rows = re.findall(r'\\PhasalRow\{([^{}]+)\}\{([^{}]+)\}\{([^{}]+)\}'
                      r'\{([^{}]+)\}\{([^{}]+)\}\{([^{}]+)\}', source)
    expected = [tuple(row[key] for key in ('y', 'particle', 'scope', 'before', 'now', 'reading'))
                for row in fixtures['diagram_rows']]
    failures = [] if rows == expected else ['phasal diagram: unexpected particle, scope, transition or reading']
    # Independent fixture bindings protect what the macro actually draws,
    # rather than accepting correct row arguments rendered in reversed columns.
    for binding in fixtures['diagram_bindings']:
        if binding not in source:
            failures.append('phasal diagram: changed truth-column binding ' + binding)
    return failures


def check_phasal_sources(sources, fixtures):
    """Pair prescribed readings with their actual examples and local conditions."""
    source = sources.get('chapters/05-function-words.tex', '')
    failures = []
    normalise = lambda value: ' '.join(value.split())
    blocks = re.findall(r'\\begingl(.*?)\\endgl', source, re.S)
    for case in fixtures['source_examples']:
        matches = [block for block in blocks if
                   re.search(r'\\gla\s+' + re.escape(case['form']) + r'//', block)]
        if not matches:
            failures.append('phasal source: missing example ' + case['form'])
        for block in matches:
            for value in case['context'] + [case['gloss'], case['translation']]:
                if normalise(value) not in normalise(block):
                    failures.append('phasal source: context/gloss/reading changed for ' + case['form'])
    for case in fixtures['source_paragraphs']:
        sections = source.split(case['anchor'])[1:]
        if not sections:
            failures.append('phasal source: missing bounded explanation ' + case['anchor'])
        for section in sections:
            section = normalise(section.split(case['end'], 1)[0])
            for value in case['required']:
                if normalise(value) not in section:
                    failures.append('phasal source: lost qualification ' + value)
    syntax = sources.get('chapters/06-simple-sentence.tex', '')
    # English interpretation schemata deliberately have no invented Iridian
    # surface/gloss lines. Keep each subexample's scope and context together.
    exclusive_blocks = re.findall(r'\\begingl(.*?)\\endgl', syntax, re.S)
    exclusive_blocks += re.findall(
        r'\\a\s+\\trsl\{.*?(?=\\a\s+\\trsl|\\xe)', syntax, re.S)
    for case in fixtures.get('exclusive_source_examples', []):
        matches = [block for block in exclusive_blocks if
                   normalise(case['translation']) in normalise(block)]
        if not matches:
            failures.append('phasal scope: missing paired exclusive example ' + case['translation'])
        for block in matches:
            for value in case['context'] + [case['scope'], case['diagnostic']]:
                if normalise(value) not in normalise(block):
                    failures.append('phasal scope: changed paired diagnostic ' + value)
    return failures

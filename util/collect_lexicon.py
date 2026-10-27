#!/usr/bin/env python3
"""Collect explicitly marked Iridian forms without inferring dictionary entries."""

import argparse
import csv
import io
import json
from pathlib import Path
import re
import sys
import unicodedata

REPOSITORY = Path(__file__).resolve().parents[1]
MACROS = re.compile(r"\\(irdp|ird|phon|lexentry)(?![A-Za-z@])")
ARITY = {"ird": 1, "irdp": 2, "phon": 3, "lexentry": 3}


def strip_comments(text):
    """Blank comments while keeping offsets and line numbers unchanged."""
    result = list(text)
    cursor = 0
    while cursor < len(text):
        if text[cursor] == "\\":
            cursor += 2  # An escaped percent is data; a doubled slash is not.
        elif text[cursor] == "%":
            end = text.find("\n", cursor)
            if end < 0:
                end = len(text)
            result[cursor:end] = " " * (end - cursor)
            cursor = end
        else:
            cursor += 1
    return "".join(result)


def group(text, offset):
    while offset < len(text) and text[offset].isspace():
        offset += 1
    if offset >= len(text) or text[offset] != "{":
        return None
    start = offset + 1
    depth = 1
    cursor = start
    while cursor < len(text):
        char = text[cursor]
        if char == "\\":
            cursor += 2
            continue
        if char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                return text[start:cursor], cursor + 1
        cursor += 1
    raise ValueError("unclosed argument")


def normalize(value):
    # Preserve TeX markup; stripping it would silently change lexical data.
    return unicodedata.normalize("NFC", re.sub(r"\s+", " ", value).strip())


def extract(text, source):
    clean = strip_comments(text)
    cursor = 0
    while match := MACROS.search(clean, cursor):
        macro = match.group(1)
        offset = match.end()
        arguments = []
        line = clean.count("\n", 0, match.start()) + 1
        try:
            for _ in range(ARITY[macro]):
                parsed = group(clean, offset)
                if parsed is None:
                    break
                argument, offset = parsed
                arguments.append(normalize(argument))
        except ValueError as error:
            raise ValueError(f"{source}:{line}: \\{macro}: {error}") from error
        cursor = max(offset, match.end())
        # A command name in a macro definition or prose is not an invocation.
        if not arguments:
            continue
        if len(arguments) != ARITY[macro]:
            raise ValueError(f"{source}:{line}: \\{macro} expects {ARITY[macro]} braced arguments")
        if not arguments[0] or "#" in arguments[0]:
            continue
        record = {"form": arguments[0], "macro": macro, "path": source, "line": line}
        if macro == "irdp":
            record["gloss"] = arguments[1]
        elif macro == "phon":
            record.update(pronunciation=arguments[1], gloss=arguments[2])
        elif macro == "lexentry":
            record.update(notes=arguments[1], gloss=arguments[2])
        yield record


def collect(paths, root=REPOSITORY):
    entries = {}
    for path in sorted(set(paths)):
        try:
            source = path.resolve().relative_to(root.resolve()).as_posix()
        except ValueError:
            source = str(path.resolve())
        for occurrence in extract(path.read_text(encoding="utf-8"), source):
            form = occurrence.pop("form")
            entry = entries.setdefault(form, {"form": form, "glosses": [], "pronunciations": [], "occurrences": []})
            for key, plural in (("gloss", "glosses"), ("pronunciation", "pronunciations")):
                value = occurrence.get(key)
                if value and value not in entry[plural]:
                    entry[plural].append(value)
            entry["occurrences"].append(occurrence)
    return sorted(entries.values(), key=lambda entry: (entry["form"].casefold(), entry["form"]))


def render(entries, output_format):
    if output_format == "json":
        return json.dumps(entries, ensure_ascii=False, indent=2) + "\n"
    output = io.StringIO(newline="")
    writer = csv.writer(output, delimiter="\t", lineterminator="\n")
    writer.writerow(["form", "glosses", "pronunciations", "sources"])
    for entry in entries:
        writer.writerow([entry["form"], " | ".join(entry["glosses"]), " | ".join(entry["pronunciations"]),
                         " | ".join(f"{item['path']}:{item['line']}" for item in entry["occurrences"])])
    return output.getvalue()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("sources", nargs="*", type=Path, help="TeX files or directories (default: current chapters only)")
    parser.add_argument("--format", choices=("json", "tsv"), default="json")
    parser.add_argument("--output", type=Path, help="write only if content changes; otherwise print to stdout")
    args = parser.parse_args()
    paths = []
    for source in args.sources or [REPOSITORY / "chapters"]:
        if source.is_dir():
            paths.extend(source.rglob("*.tex"))
        elif source.is_file():
            paths.append(source)
        else:
            parser.error(f"source does not exist: {source}")
    if not paths:
        parser.error("no TeX source files found")
    try:
        content = render(collect(paths), args.format)
    except (OSError, UnicodeError, ValueError) as error:
        parser.exit(1, f"collect_lexicon: {error}\n")
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        if not args.output.exists() or args.output.read_text(encoding="utf-8") != content:
            args.output.write_text(content, encoding="utf-8")
    else:
        sys.stdout.write(content)


if __name__ == "__main__":
    main()

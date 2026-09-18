#!/usr/bin/env python3
"""ST-12 preflight validator for authored UNSC market IDs.

Validates the fixed Epsilon Eridani market construction in UNSCStar.java against
real Starsector registry CSVs and the exact API source constants used by the
build. Optionally validates Industrial Evolution's Reach artillery industry
against a supplied IndEvo industries.csv.

This is build/preflight tooling only; it is not packaged into the runtime mod.
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Tuple

STRING_CONST_RE = re.compile(
    r"(?:public|private|protected)?\s*static\s+final\s+String\s+([A-Za-z_$][\w$]*)\s*=\s*\"([^\"]*)\"\s*;"
)


def strip_comments(text: str) -> str:
    # Preserve newlines so line numbers remain meaningful.
    out = []
    i = 0
    in_string = False
    in_char = False
    while i < len(text):
        ch = text[i]
        nxt = text[i + 1] if i + 1 < len(text) else ""
        if in_string:
            out.append(ch)
            if ch == "\\" and i + 1 < len(text):
                out.append(text[i + 1])
                i += 2
                continue
            if ch == '"':
                in_string = False
            i += 1
            continue
        if in_char:
            out.append(ch)
            if ch == "\\" and i + 1 < len(text):
                out.append(text[i + 1])
                i += 2
                continue
            if ch == "'":
                in_char = False
            i += 1
            continue
        if ch == '"':
            in_string = True
            out.append(ch)
            i += 1
            continue
        if ch == "'":
            in_char = True
            out.append(ch)
            i += 1
            continue
        if ch == "/" and nxt == "/":
            while i < len(text) and text[i] != "\n":
                out.append(" ")
                i += 1
            continue
        if ch == "/" and nxt == "*":
            out.extend("  ")
            i += 2
            while i < len(text):
                if text[i] == "*" and i + 1 < len(text) and text[i + 1] == "/":
                    out.extend("  ")
                    i += 2
                    break
                out.append("\n" if text[i] == "\n" else " ")
                i += 1
            continue
        out.append(ch)
        i += 1
    return "".join(out)


def extract_calls(text: str, needle: str) -> List[Tuple[int, str]]:
    calls: List[Tuple[int, str]] = []
    pos = 0
    while True:
        idx = text.find(needle, pos)
        if idx < 0:
            break
        open_idx = text.find("(", idx + len(needle))
        if open_idx < 0:
            raise ValueError(f"Malformed call for {needle}: no opening parenthesis")
        depth = 0
        in_string = False
        in_char = False
        i = open_idx
        while i < len(text):
            ch = text[i]
            if in_string:
                if ch == "\\":
                    i += 2
                    continue
                if ch == '"':
                    in_string = False
                i += 1
                continue
            if in_char:
                if ch == "\\":
                    i += 2
                    continue
                if ch == "'":
                    in_char = False
                i += 1
                continue
            if ch == '"':
                in_string = True
            elif ch == "'":
                in_char = True
            elif ch == "(":
                depth += 1
            elif ch == ")":
                depth -= 1
                if depth == 0:
                    body = text[open_idx + 1 : i]
                    line = text.count("\n", 0, idx) + 1
                    calls.append((line, body))
                    pos = i + 1
                    break
            i += 1
        else:
            raise ValueError(f"Malformed call for {needle}: no closing parenthesis")
    return calls


def split_top_level(text: str) -> List[str]:
    parts: List[str] = []
    start = 0
    paren = bracket = brace = 0
    in_string = False
    in_char = False
    i = 0
    while i < len(text):
        ch = text[i]
        if in_string:
            if ch == "\\":
                i += 2
                continue
            if ch == '"':
                in_string = False
            i += 1
            continue
        if in_char:
            if ch == "\\":
                i += 2
                continue
            if ch == "'":
                in_char = False
            i += 1
            continue
        if ch == '"':
            in_string = True
        elif ch == "'":
            in_char = True
        elif ch == "(":
            paren += 1
        elif ch == ")":
            paren -= 1
        elif ch == "[":
            bracket += 1
        elif ch == "]":
            bracket -= 1
        elif ch == "{":
            brace += 1
        elif ch == "}":
            brace -= 1
        elif ch == "," and paren == 0 and bracket == 0 and brace == 0:
            parts.append(text[start:i].strip())
            start = i + 1
        i += 1
    tail = text[start:].strip()
    if tail:
        parts.append(tail)
    return parts


def parse_java_string_constants(path: Path) -> Dict[str, str]:
    text = strip_comments(path.read_text(encoding="utf-8"))
    return dict(STRING_CONST_RE.findall(text))


def load_registry(paths: Sequence[Path]) -> set[str]:
    result: set[str] = set()
    for path in paths:
        with path.open("r", encoding="utf-8-sig", newline="") as f:
            reader = csv.DictReader(f)
            if reader.fieldnames is None or "id" not in reader.fieldnames:
                raise ValueError(f"Registry has no 'id' column: {path}")
            for row in reader:
                value = (row.get("id") or "").strip()
                if value:
                    result.add(value)
    return result


def unquote(expr: str) -> str | None:
    expr = expr.strip()
    if len(expr) >= 2 and expr[0] == expr[-1] == '"':
        # Authored IDs here are plain ASCII strings; decode common Java escapes.
        return bytes(expr[1:-1], "utf-8").decode("unicode_escape")
    return None


def resolve_expr(expr: str, maps: Dict[str, Dict[str, str]], locals_map: Dict[str, str] | None = None) -> str:
    expr = expr.strip()
    lit = unquote(expr)
    if lit is not None:
        return lit
    if locals_map and expr in locals_map:
        return locals_map[expr]
    m = re.fullmatch(r"([A-Za-z_$][\w$]*)\.([A-Za-z_$][\w$]*)", expr)
    if m:
        cls, const = m.groups()
        if cls not in maps:
            raise ValueError(f"Unsupported constant class in authored ID expression: {expr}")
        if const not in maps[cls]:
            raise ValueError(f"Unknown constant {expr} in supplied exact API source")
        return maps[cls][const]
    raise ValueError(f"Unsupported authored ID expression: {expr}")


def parse_as_list(expr: str, maps: Dict[str, Dict[str, str]]) -> List[str]:
    expr = expr.strip()
    if expr == "null":
        return []
    marker = "Arrays.asList"
    idx = expr.find(marker)
    if idx < 0:
        raise ValueError(f"Expected Arrays.asList(...) or null, got: {expr}")
    calls = extract_calls(expr[idx:], marker)
    if len(calls) != 1:
        raise ValueError(f"Could not parse Arrays.asList in: {expr}")
    values = split_top_level(calls[0][1])
    return [resolve_expr(v, maps) for v in values]


def validate_ids(kind: str, market: str, ids: Iterable[str], registry: set[str], errors: List[str], checked: List[Tuple[str, str, str]]) -> None:
    for value in ids:
        checked.append((market, kind, value))
        if value not in registry:
            errors.append(f"{market}: invalid {kind} ID '{value}'")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--unsc-star", type=Path, required=True)
    ap.add_argument("--unsc-indevo", type=Path, required=True)
    ap.add_argument("--conditions-java", type=Path, required=True)
    ap.add_argument("--industries-java", type=Path, required=True)
    ap.add_argument("--submarkets-java", type=Path, required=True)
    ap.add_argument("--conditions-csv", type=Path, action="append", required=True)
    ap.add_argument("--industries-csv", type=Path, action="append", required=True)
    ap.add_argument("--submarkets-csv", type=Path, action="append", required=True)
    ap.add_argument("--indevo-industries-csv", type=Path, required=True)
    args = ap.parse_args()

    maps = {
        "Conditions": parse_java_string_constants(args.conditions_java),
        "Industries": parse_java_string_constants(args.industries_java),
        "Submarkets": parse_java_string_constants(args.submarkets_java),
    }
    condition_ids = load_registry(args.conditions_csv)
    industry_ids = load_registry(args.industries_csv)
    submarket_ids = load_registry(args.submarkets_csv)
    indevo_industry_ids = load_registry([args.indevo_industries_csv])

    star_text = strip_comments(args.unsc_star.read_text(encoding="utf-8"))
    errors: List[str] = []
    checked: List[Tuple[str, str, str]] = []

    # 1) The five normal authored markets built through UNSC_AddMarketplace.
    market_calls = extract_calls(star_text, "UNSC_AddMarketplace.addMarketplace")
    if len(market_calls) != 5:
        errors.append(f"Expected exactly 5 UNSC_AddMarketplace call sites, found {len(market_calls)}")

    for line, body in market_calls:
        args_list = split_top_level(body)
        if len(args_list) != 11:
            errors.append(f"line {line}: expected 11 addMarketplace arguments, found {len(args_list)}")
            continue
        market_id = unquote(args_list[1]) or f"line-{line}"
        if args_list[9].strip() not in {"true", "false"}:
            errors.append(f"{market_id}: withJunkAndChatter must be literal true/false, got {args_list[9].strip()}")
        if args_list[10].strip() not in {"true", "false"}:
            errors.append(f"{market_id}: pirateMode must be literal true/false, got {args_list[10].strip()}")
        try:
            conditions = parse_as_list(args_list[6], maps)
            submarkets = parse_as_list(args_list[7], maps)
            industries = parse_as_list(args_list[8], maps)
            validate_ids("condition", market_id, conditions, condition_ids, errors, checked)
            validate_ids("submarket", market_id, submarkets, submarket_ids, errors, checked)
            validate_ids("industry", market_id, industries, industry_ids, errors, checked)
        except ValueError as exc:
            errors.append(f"{market_id}: {exc}")

    # 2) Uncolonized authored condition markets made through addUncolonizedConditions().
    condition_calls = extract_calls(star_text, "addUncolonizedConditions")
    # The method declaration itself also matches the name; exclude it structurally.
    condition_calls = [(line, body) for line, body in condition_calls if not body.lstrip().startswith("PlanetAPI planet")]
    if len(condition_calls) != 6:
        errors.append(f"Expected exactly 6 addUncolonizedConditions call sites, found {len(condition_calls)}")
    for line, body in condition_calls:
        vals = split_top_level(body)
        if len(vals) < 2:
            errors.append(f"line {line}: malformed addUncolonizedConditions call")
            continue
        body_name = vals[0].strip()
        try:
            conditions = [resolve_expr(v, maps) for v in vals[1:]]
            validate_ids("condition", f"uncolonized:{body_name}", conditions, condition_ids, errors, checked)
        except ValueError as exc:
            errors.append(f"uncolonized:{body_name}: {exc}")

    # 3) Direct Vanilla industry additions outside the helper (currently Reach Orbital Works).
    for line, body in extract_calls(star_text, ".addIndustry"):
        vals = split_top_level(body)
        if not vals:
            continue
        expr = vals[0]
        try:
            industry = resolve_expr(expr, maps)
            validate_ids("industry", f"direct-add:line-{line}", [industry], industry_ids, errors, checked)
        except ValueError as exc:
            errors.append(f"direct-add:line-{line}: {exc}")

    # 4) Optional IndEvo Reach artillery industry, validated only against exact IndEvo data.
    indevo_text = strip_comments(args.unsc_indevo.read_text(encoding="utf-8"))
    local_consts = parse_java_string_constants(args.unsc_indevo)
    indevo_calls = extract_calls(indevo_text, ".addIndustry")
    if len(indevo_calls) != 1:
        errors.append(f"Expected exactly 1 IndEvo direct addIndustry call, found {len(indevo_calls)}")
    for line, body in indevo_calls:
        vals = split_top_level(body)
        if not vals:
            continue
        try:
            industry = resolve_expr(vals[0], maps, local_consts)
            validate_ids("IndEvo industry", f"optional-IndEvo:line-{line}", [industry], indevo_industry_ids, errors, checked)
        except ValueError as exc:
            errors.append(f"optional-IndEvo:line-{line}: {exc}")

    unique = {(kind, value) for _, kind, value in checked}
    print(f"ST-12 market-ID preflight: checked {len(checked)} references ({len(unique)} unique category/ID pairs)")
    print(f"  normal authored markets: {len(market_calls)}")
    print(f"  uncolonized condition-market calls: {len(condition_calls)}")
    print(f"  Vanilla registry sizes: conditions={len(condition_ids)}, submarkets={len(submarket_ids)}, industries={len(industry_ids)}")
    print(f"  IndEvo industry registry size: {len(indevo_industry_ids)}")

    if errors:
        print("FAIL:")
        for error in errors:
            print(f"  - {error}")
        return 1

    print("PASS: every authored condition/submarket/industry ID resolves in its intended exact registry, and all helper booleans are literal true/false.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

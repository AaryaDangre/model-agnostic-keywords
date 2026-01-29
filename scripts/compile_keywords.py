#!/usr/bin/env python3
"""Compile vendor keyword files into combined JSON/YAML outputs.

Usage:
    python -m scripts.compile_keywords

Outputs:
    prompt-keywords/combined_keywords.json
    prompt-keywords/combined_keywords.yml
"""
from __future__ import annotations

import json
import os
import re
from collections import defaultdict
from pathlib import Path

try:
    import yaml
except Exception:
    yaml = None


ROOT = Path(__file__).resolve().parents[1]
PK_DIR = ROOT / "prompt-keywords"
PREFIX = "Model Agnostic Prompting Keywords_"


def parse_metadata(text: str) -> dict:
    """Extract metadata from top of file (vendor, version, source, tags)."""
    metadata = {}
    for line in text.split('\n')[:10]:  # check first 10 lines
        if line.startswith('# '):
            key_val = line[2:].strip()
            if ':' in key_val:
                key, val = key_val.split(':', 1)
                metadata[key.strip()] = val.strip()
        elif not line.startswith('#'):
            break
    return metadata


def parse_keywords_from_text(text: str) -> list[str]:
    items = []
    skip_metadata = True
    for raw in text.splitlines():
        line = raw.strip()
        # skip metadata header
        if line.startswith('#'):
            if not line.startswith('# '):
                skip_metadata = False
            continue
        if not line:
            continue
        # remove list markers
        line = re.sub(r"^[\-*+]\s*", "", line)
        # remove leading bullets like '##' or headings
        line = re.sub(r"^#+\s*", "", line)
        # split comma-separated
        parts = [p.strip() for p in re.split(r",|;", line) if p.strip()]
        for p in parts:
            # ignore short artifact lines
            if len(p) < 2:
                continue
            items.append(p)
    return items


def main() -> int:
    vendor_map = defaultdict(dict)
    if not PK_DIR.exists():
        print("prompt-keywords directory not found")
        return 1

    for p in sorted(PK_DIR.glob("Model Agnostic Prompting Keywords_*")):
        if p.is_file():
            name = p.name
            label = name[len(PREFIX) :]
            # strip extension
            label = re.sub(r"\.[^.]+$", "", label)
            text = p.read_text(encoding="utf-8")
            metadata = parse_metadata(text)
            keywords = parse_keywords_from_text(text)
            vendor_map[label] = {
                "metadata": metadata,
                "keywords": keywords
            }

    combined = {"vendors": {}, "combined": [], "metadata": {}}
    all_set = set()
    
    for vendor, data in vendor_map.items():
        kws = data["keywords"]
        meta = data["metadata"]
        combined["vendors"][vendor] = {
            "metadata": meta,
            "keywords": sorted(kws)
        }
        all_set.update(kws)

    combined["combined"] = sorted(all_set)

    out_json = PK_DIR / "combined_keywords.json"
    out_yaml = PK_DIR / "combined_keywords.yml"

    out_json.write_text(json.dumps(combined, indent=2, ensure_ascii=False), encoding="utf-8")
    if yaml is not None:
        out_yaml.write_text(yaml.safe_dump(combined, sort_keys=False, allow_unicode=True), encoding="utf-8")
    else:
        out_yaml.write_text("# PyYAML not installed; install with `pip install pyyaml`\n", encoding="utf-8")

    print(f"Wrote {out_json} and {out_yaml}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

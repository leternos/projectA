"""Merge per-page extracted entries into a single validated pilot/data/index.json.

Usage:
    python -m src.merge_entries pilot/data/extracted pilot/data/index.json --schema schema/entry.schema.json
"""

import argparse
import json
from pathlib import Path

import jsonschema


def load_schema(schema_path: Path) -> dict:
    return json.loads(schema_path.read_text())


def merge(extracted_dir: Path, schema: dict) -> list[dict]:
    entries: list[dict] = []
    seen_ids: set[str] = set()

    for page_file in sorted(extracted_dir.glob("page-*.json")):
        page_entries = json.loads(page_file.read_text())
        if not isinstance(page_entries, list):
            raise ValueError(f"{page_file} must contain a JSON array of entries")

        for entry in page_entries:
            jsonschema.validate(entry, schema)
            if entry["id"] in seen_ids:
                raise ValueError(f"duplicate entry id {entry['id']!r} found in {page_file}")
            seen_ids.add(entry["id"])
            entries.append(entry)

    return entries


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("extracted_dir", type=Path)
    parser.add_argument("out_path", type=Path)
    parser.add_argument("--schema", type=Path, required=True)
    args = parser.parse_args()

    schema = load_schema(args.schema)
    entries = merge(args.extracted_dir, schema)

    args.out_path.write_text(json.dumps(entries, indent=2, ensure_ascii=False))
    print(f"Merged {len(entries)} entries into {args.out_path}")


if __name__ == "__main__":
    main()

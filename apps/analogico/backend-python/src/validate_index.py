"""Integrity checks for pilot/data/index.json, run before manual sampling.

Usage:
    python -m src.validate_index pilot/data/index.json pilot/data --schema schema/entry.schema.json
"""

import argparse
import json
from pathlib import Path

import jsonschema


class ValidationReport:
    def __init__(self) -> None:
        self.errors: list[str] = []

    def add(self, message: str) -> None:
        self.errors.append(message)

    @property
    def ok(self) -> bool:
        return not self.errors


def validate(entries: list[dict], data_dir: Path, schema: dict) -> ValidationReport:
    report = ValidationReport()
    seen_ids: set[str] = set()
    referenced_images: set[str] = set()
    all_page_images: set[str] = set()

    for image_path in (data_dir / "pages").glob("page-*.jpg"):
        all_page_images.add(f"pages/{image_path.name}")
    for image_path in (data_dir / "pages").glob("page-*.png"):
        all_page_images.add(f"pages/{image_path.name}")

    for entry in entries:
        try:
            jsonschema.validate(entry, schema)
        except jsonschema.ValidationError as exc:
            report.add(f"entry {entry.get('id', '?')}: schema violation: {exc.message}")
            continue

        if entry["id"] in seen_ids:
            report.add(f"duplicate entry id: {entry['id']}")
        seen_ids.add(entry["id"])

        image_rel_path = entry["page_image"]
        if not (data_dir / image_rel_path).exists():
            report.add(f"entry {entry['id']}: page_image not found on disk: {image_rel_path}")
        referenced_images.add(image_rel_path)

    orphan_images = all_page_images - referenced_images
    for orphan in sorted(orphan_images):
        report.add(f"page image has no entries referencing it: {orphan}")

    return report


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("index_path", type=Path)
    parser.add_argument("data_dir", type=Path, help="pilot/data directory (contains pages/ and index.json)")
    parser.add_argument("--schema", type=Path, required=True)
    args = parser.parse_args()

    entries = json.loads(args.index_path.read_text())
    schema = json.loads(args.schema.read_text())

    report = validate(entries, args.data_dir, schema)
    if report.ok:
        print(f"OK: {len(entries)} entries validated, no issues found")
    else:
        print(f"FAILED: {len(report.errors)} issue(s) found")
        for error in report.errors:
            print(f"  - {error}")
        raise SystemExit(1)


if __name__ == "__main__":
    main()

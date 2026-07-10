"""Merge a verification patch (exported from viewer.html) back into pilot/data/index.json.

Patch format: {"id": {"verification_status": "verified", "verified_by": "...", "verified_at": "..."}, ...}

Usage:
    python -m src.apply_verification pilot/data/index.json patch.json
"""

import argparse
import json
from pathlib import Path


def apply_patch(entries: list[dict], patch: dict[str, dict]) -> tuple[list[dict], list[str]]:
    entries_by_id = {entry["id"]: entry for entry in entries}
    unknown_ids = [entry_id for entry_id in patch if entry_id not in entries_by_id]

    for entry_id, changes in patch.items():
        if entry_id not in entries_by_id:
            continue
        entries_by_id[entry_id].update(changes)

    return entries, unknown_ids


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("index_path", type=Path)
    parser.add_argument("patch_path", type=Path)
    args = parser.parse_args()

    entries = json.loads(args.index_path.read_text())
    patch = json.loads(args.patch_path.read_text())

    entries, unknown_ids = apply_patch(entries, patch)

    args.index_path.write_text(json.dumps(entries, indent=2, ensure_ascii=False))
    print(f"Applied verification patch for {len(patch) - len(unknown_ids)} entries")
    if unknown_ids:
        print(f"Warning: {len(unknown_ids)} id(s) in patch not found in index: {unknown_ids}")


if __name__ == "__main__":
    main()

import json
from pathlib import Path

import pytest

from src.validate_index import validate

SCHEMA_PATH = Path(__file__).parent.parent / "schema" / "entry.schema.json"


@pytest.fixture
def schema():
    return json.loads(SCHEMA_PATH.read_text())


def make_entry(**overrides):
    entry = {
        "id": "abacaxi-p0007-01",
        "headword": "Abacaxi",
        "entry_type": "index",
        "raw_text": "Abacaxi, V. Ananás",
        "references": ["Ananás"],
        "related_terms": None,
        "pdf_page_index": 7,
        "printed_page_number": "12",
        "page_image": "pages/page-0007.jpg",
        "verification_status": "unverified",
        "verified_by": None,
        "verified_at": None,
        "extraction_notes": None,
    }
    entry.update(overrides)
    return entry


def make_data_dir(tmp_path: Path, image_names: list[str]) -> Path:
    pages_dir = tmp_path / "pages"
    pages_dir.mkdir()
    for name in image_names:
        (pages_dir / name).write_bytes(b"fake-jpg")
    return tmp_path


def test_valid_index_has_no_errors(tmp_path, schema):
    data_dir = make_data_dir(tmp_path, ["page-0007.jpg"])
    report = validate([make_entry()], data_dir, schema)
    assert report.ok


def test_missing_page_image_is_flagged(tmp_path, schema):
    data_dir = make_data_dir(tmp_path, [])
    report = validate([make_entry()], data_dir, schema)
    assert not report.ok
    assert any("not found on disk" in e for e in report.errors)


def test_duplicate_id_is_flagged(tmp_path, schema):
    data_dir = make_data_dir(tmp_path, ["page-0007.jpg"])
    report = validate([make_entry(), make_entry()], data_dir, schema)
    assert not report.ok
    assert any("duplicate entry id" in e for e in report.errors)


def test_orphan_page_image_is_flagged(tmp_path, schema):
    data_dir = make_data_dir(tmp_path, ["page-0007.jpg", "page-0008.jpg"])
    report = validate([make_entry()], data_dir, schema)
    assert not report.ok
    assert any("page-0008.jpg" in e for e in report.errors)


def test_schema_violation_is_flagged(tmp_path, schema):
    data_dir = make_data_dir(tmp_path, ["page-0007.jpg"])
    bad_entry = make_entry(entry_type="not-a-real-type")
    report = validate([bad_entry], data_dir, schema)
    assert not report.ok
    assert any("schema violation" in e for e in report.errors)

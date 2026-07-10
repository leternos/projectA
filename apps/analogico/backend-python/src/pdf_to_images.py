"""Render a PDF page range to page images for the analogico extraction pilot.

Usage:
    python -m src.pdf_to_images SOURCE.pdf OUT_DIR --start 10 --end 39 --dpi 300 --format jpg
"""

import argparse
import hashlib
import json
from pathlib import Path

import fitz  # PyMuPDF


def sha256_of(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def render_pages(pdf_path: Path, out_dir: Path, start: int, end: int, dpi: int, fmt: str) -> list[str]:
    out_dir.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(pdf_path)
    if start < 0 or end >= doc.page_count or start > end:
        raise ValueError(
            f"invalid page range [{start}, {end}] for a {doc.page_count}-page PDF"
        )

    zoom = dpi / 72
    matrix = fitz.Matrix(zoom, zoom)
    filenames = []
    for page_index in range(start, end + 1):
        page = doc.load_page(page_index)
        pixmap = page.get_pixmap(matrix=matrix)
        filename = f"page-{page_index:04d}.{fmt}"
        pixmap.save(out_dir / filename, jpg_quality=90 if fmt == "jpg" else None)
        filenames.append(filename)
    doc.close()
    return filenames


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdf_path", type=Path)
    parser.add_argument("out_dir", type=Path)
    parser.add_argument("--start", type=int, required=True, help="0-based inclusive start page")
    parser.add_argument("--end", type=int, required=True, help="0-based inclusive end page")
    parser.add_argument("--dpi", type=int, default=300)
    parser.add_argument("--format", choices=["jpg", "png"], default="jpg")
    args = parser.parse_args()

    filenames = render_pages(args.pdf_path, args.out_dir, args.start, args.end, args.dpi, args.format)

    manifest = {
        "source_filename": args.pdf_path.name,
        "source_sha256": sha256_of(args.pdf_path),
        "pdf_page_range": [args.start, args.end],
        "dpi": args.dpi,
        "format": args.format,
        "pages": filenames,
    }
    (args.out_dir / "pages_manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False))
    print(f"Rendered {len(filenames)} pages to {args.out_dir}")


if __name__ == "__main__":
    main()

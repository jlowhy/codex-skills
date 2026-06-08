#!/usr/bin/env python3
"""Create a Reddit community research note from the skill template."""

from __future__ import annotations

import argparse
import datetime as dt
import re
from pathlib import Path


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", value.strip().lower()).strip("-")
    return slug or "reddit-community-research"


def read_template() -> str:
    skill_dir = Path(__file__).resolve().parents[1]
    return (skill_dir / "RESEARCH-TEMPLATE.md").read_text(encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Create a structured Reddit community research note."
    )
    parser.add_argument("brief", help="Short product/category brief for the research.")
    parser.add_argument(
        "--output-dir",
        default=".",
        help="Directory where the research note should be written.",
    )
    parser.add_argument(
        "--filename",
        help="Optional filename. Defaults to YYYY-MM-DD-<brief-slug>.md.",
    )
    args = parser.parse_args()

    today = dt.date.today().isoformat()
    filename = args.filename or f"{today}-{slugify(args.brief)}.md"
    if not filename.endswith(".md"):
        filename += ".md"

    output_dir = Path(args.output_dir).expanduser().resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / filename

    if output_path.exists():
        raise SystemExit(f"Refusing to overwrite existing file: {output_path}")

    note = read_template().replace("{Brief}", args.brief)
    note = note.replace("- Product/category:", f"- Product/category: {args.brief}")
    note = note.replace("- Artifact date:", f"- Artifact date: {today}")

    output_path.write_text(note, encoding="utf-8")
    print(output_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

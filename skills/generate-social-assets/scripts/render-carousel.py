#!/usr/bin/env python3
"""Render slides.json to HTML preview, PNG slides, and a PDF carousel."""

from __future__ import annotations

import argparse
import html
import json
from pathlib import Path

from playwright.sync_api import Error as PlaywrightError
from playwright.sync_api import sync_playwright
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas


def esc(value: object) -> str:
    return html.escape(str(value or ""), quote=True)


def rich_text(value: object) -> str:
    return esc(value).replace("\n", "<br />")


def slide_markup(slide: dict, index: int, total: int, deck: dict) -> str:
    kind = esc(slide.get("kind") or "point")
    hide_top = bool(deck.get("hide_top"))
    top = ""
    if deck.get("top") == "brand":
        logo = (
            f'<img src="{esc(deck.get("logo_src"))}" alt="" />'
            if deck.get("logo_src")
            else ""
        )
        top = f'<div class="top brand-top">{logo}<span>{esc(deck.get("brand") or "")}</span></div>'
    elif not hide_top:
        eyebrow = (
            f'<div class="eyebrow">{esc(slide.get("eyebrow"))}</div>'
            if slide.get("eyebrow")
            else ""
        )
        top = f'<div class="top">{eyebrow}<div class="count">{index + 1}/{total}</div></div>'
    title = f"<h1>{esc(slide.get('title'))}</h1>" if slide.get("title") else ""
    body = f"<p>{rich_text(slide.get('body'))}</p>" if slide.get("body") else ""
    bullets = ""
    if isinstance(slide.get("bullets"), list):
        items = "".join(f"<li>{esc(item)}</li>" for item in slide["bullets"])
        bullets = f"<ul>{items}</ul>"
    footer = esc(slide.get("footer") or deck.get("author") or "")
    return f"""
    <section class="slide {kind}" data-slide>
      {top}
      <main>{title}{body}{bullets}</main>
      <footer>{footer}</footer>
    </section>
    """


def build_html(deck: dict) -> str:
    width = deck.get("format", {}).get("width", 1080)
    height = deck.get("format", {}).get("height", 1350)
    slides = deck.get("slides") or []
    slide_html = "\n".join(
        slide_markup(slide, index, len(slides), deck) for index, slide in enumerate(slides)
    )
    return f"""<!doctype html>
<html>
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{esc(deck.get("title") or "Carousel")}</title>
  <style>
    :root {{
      --w: {width}px;
      --h: {height}px;
      --ink: #111827;
      --muted: #5b6472;
      --line: #d8dee8;
      --accent: #0f766e;
      --paper: #f7f5ef;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      padding: 32px;
      background: #e5e7eb;
      font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      color: var(--ink);
    }}
    .deck {{ display: grid; gap: 32px; justify-content: start; }}
    .slide {{
      width: var(--w);
      height: var(--h);
      padding: 72px;
      background: linear-gradient(180deg, rgba(15, 118, 110, 0.08), transparent 34%), var(--paper);
      border: 1px solid var(--line);
      display: grid;
      grid-template-rows: {"1fr auto" if deck.get("hide_top") and deck.get("top") != "brand" else "auto 1fr auto"};
      overflow: hidden;
    }}
    .top {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      min-height: 40px;
      color: var(--muted);
      font-size: 28px;
      font-weight: 650;
    }}
    .brand-top {{
      justify-content: flex-start;
      gap: 16px;
      color: #063f33;
      font-size: 30px;
    }}
    .brand-top img {{
      width: 44px;
      height: 44px;
      object-fit: contain;
    }}
    .eyebrow {{
      color: var(--accent);
      text-transform: uppercase;
      font-size: 24px;
      letter-spacing: 0;
    }}
    main {{ align-self: center; max-width: 880px; }}
    h1 {{
      margin: 0 0 34px;
      font-size: 86px;
      line-height: 0.98;
      letter-spacing: 0;
      text-wrap: balance;
    }}
    p {{
      margin: 0;
      max-width: 820px;
      color: #263241;
      font-size: 44px;
      line-height: 1.18;
      letter-spacing: 0;
    }}
    ul {{
      margin: 0;
      padding: 0;
      list-style: none;
      display: grid;
      gap: 24px;
    }}
    li {{
      border-left: 8px solid var(--accent);
      padding-left: 28px;
      color: #263241;
      font-size: 40px;
      line-height: 1.15;
    }}
    footer {{ color: var(--muted); font-size: 28px; font-weight: 600; }}
    .cover h1 {{ font-size: 96px; }}
    .cover p {{ font-size: 42px; }}
    .cta {{ background: linear-gradient(180deg, rgba(15, 118, 110, 0.14), transparent 44%), #eef6f2; }}
  </style>
</head>
<body><div class="deck">{slide_html}</div></body>
</html>"""


def write_pdf(image_paths: list[Path], pdf_path: Path, width: int, height: int) -> None:
    doc = canvas.Canvas(str(pdf_path), pagesize=(width, height))
    for image_path in image_paths:
        doc.drawImage(ImageReader(str(image_path)), 0, 0, width=width, height=height)
        doc.showPage()
    doc.save()


def launch_browser(playwright):
    try:
        return playwright.chromium.launch()
    except PlaywrightError as first_error:
        for channel in ("chrome", "msedge", "chromium"):
            try:
                return playwright.chromium.launch(channel=channel)
            except PlaywrightError:
                continue
        raise SystemExit(
            "Could not launch Chromium. Install Playwright browsers with:\n"
            "uv run --with playwright playwright install chromium\n\n"
            f"Original error:\n{first_error}"
        )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("slides_json")
    parser.add_argument("--out", default="social-assets-out")
    args = parser.parse_args()

    input_path = Path(args.slides_json).expanduser().resolve()
    out_dir = Path(args.out).expanduser().resolve()
    slides_dir = out_dir / "slides"
    slides_dir.mkdir(parents=True, exist_ok=True)

    deck = json.loads(input_path.read_text(encoding="utf-8"))
    if deck.get("logo_path"):
        logo_path = (input_path.parent / str(deck["logo_path"])).resolve()
        deck["logo_src"] = logo_path.as_uri()
    slides = deck.get("slides")
    if not isinstance(slides, list) or not slides:
        raise SystemExit("slides.json must include a non-empty slides array")

    width = int(deck.get("format", {}).get("width", 1080))
    height = int(deck.get("format", {}).get("height", 1350))

    html_path = out_dir / "preview.html"
    html_path.write_text(build_html(deck), encoding="utf-8")

    image_paths: list[Path] = []
    with sync_playwright() as p:
        browser = launch_browser(p)
        page = browser.new_page(viewport={"width": width, "height": height}, device_scale_factor=1)
        page.goto(html_path.as_uri())
        page.evaluate("document.fonts && document.fonts.ready")
        locators = page.locator("[data-slide]")
        for index in range(locators.count()):
            image_path = slides_dir / f"slide-{index + 1:02d}.png"
            locators.nth(index).screenshot(path=str(image_path), animations="disabled")
            image_paths.append(image_path)
        browser.close()

    pdf_path = out_dir / "carousel.pdf"
    write_pdf(image_paths, pdf_path, width, height)
    print(json.dumps({"preview": str(html_path), "slides": [str(p) for p in image_paths], "pdf": str(pdf_path)}, indent=2))


if __name__ == "__main__":
    main()

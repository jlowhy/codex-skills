---
name: generate-social-assets
description: Generate local social media assets from notes, drafts, articles, transcripts, or briefs. Use when the user wants LinkedIn carousel PDFs, social images, or short-video-ready storyboards created from source material, especially from the notes vault or founder-led content drafts.
---

# Generate Social Assets

Use this to turn source material into local, reviewable social assets. V0 is LinkedIn carousel-first: storyboard, renderable slides, PNG exports, and a PDF document carousel for manual upload.

## Workflow

1. If the source is in the notes vault, work from `~/Notes` and follow its local `AGENTS.md`.
2. Inspect the source before drafting. Preserve the user's voice and distinguish sourced facts from inferred framing.
3. Choose the smallest asset type that fits the source: LinkedIn carousel, single image, or video storyboard. For V0, default to LinkedIn carousel when the user asks for images/PDF/carousels.
4. Create an asset brief before rendering: audience, intended reader change, channel, format, source links, claim risk, and CTA.
5. Write a storyboard with one idea per slide. Prefer 5-10 slides for LinkedIn; use `1080x1350` portrait unless the user asks otherwise.
6. Use `scripts/create-carousel-brief.py` to create a `slides.json` starting point when helpful.
7. Edit `slides.json` directly until the slide sequence is coherent and scannable.
8. Use `scripts/render-carousel.py` to create HTML preview, PNG slides, and a PDF bundle.
9. Verify the output: dimensions, readable text, no overlaps, complete PDF, reasonable file size, and source/CTA accuracy.
10. Save final assets outside the skill directory. If the user wants notes-vault storage, put exported files under `~/Notes/Attachments/` and link them from the relevant note.

## Content Standard

- Lead with a concrete hook, not a generic title.
- Make each slide self-contained enough to survive a fast mobile swipe.
- Keep body copy short; split dense reasoning across slides.
- Use visual hierarchy instead of decorative filler.
- Do not invent stats, quotes, logos, screenshots, or claims.
- Do not automate publishing unless the user explicitly asks and the account/API path is already approved.

## Local Carousel Commands

From this skill directory, create a starter file:

```bash
python3 scripts/create-carousel-brief.py --title "Carousel title" --out /tmp/slides.json
```

Render a carousel locally:

```bash
uv run --with playwright --with reportlab python scripts/render-carousel.py /tmp/slides.json --out /tmp/social-assets
```

The render command writes:

- `preview.html`
- `slides/slide-01.png`, etc.
- `carousel.pdf`

## `slides.json` Shape

```json
{
  "title": "Internal asset title",
  "author": "Jonathan Low",
  "brand": "Mistle",
  "slides": [
    {
      "kind": "cover",
      "eyebrow": "LinkedIn",
      "title": "Hook goes here",
      "body": "Short supporting line",
      "footer": "Swipe"
    }
  ]
}
```

## Closeout

Report where the assets were written, what source was used, and any unresolved manual checks. If rendering was not run, say exactly why and leave the user with the command to run.

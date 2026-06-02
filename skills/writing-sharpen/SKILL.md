---
name: writing-sharpen
description: Cleanup and sharpening pass for existing writing that removes AI-ish phrasing, filler, weak scaffolding, vague synthesis, and unnecessary polish while preserving the writer's meaning and voice. Use when the user asks to clean up, sharpen, tighten, de-AI, edit, revise, or improve a draft, article, post, thread, memo, announcement, or paragraph.
---

# Writing Sharpen

Use this when the user already has draft text and wants it cleaner, sharper, or less AI-like. This is an editing pass, not a brainstorming session.

Preserve the writer's intended meaning, point of view, and voice. Improve force, clarity, specificity, sequence, and sentence economy.

If the narrative spine is unclear, say so briefly and either ask one question or use `writing-grill` instead when the user wants deeper development.

## Editing Order

Work in this order:

1. Understand the narrative structure and what each paragraph is doing.
2. Identify the core claim of the passage.
3. For each weak sentence, state the job it is trying to do.
4. Remove scaffolding that delays the claim.
5. Replace vague synthesis with concrete claims.
6. Cut filler, throat-clearing, and generic polish.
7. Make nouns, verbs, examples, and stakes more specific.
8. Tighten sentence order and paragraph flow.
9. Preserve or restore the writer's natural cadence.

Do not start with copy polish if the claim is weak or buried.

## Variation Loop

For meaningful rewrites, use subagents when available:

1. Reconstruct the scope: format, reader, intended effect, core claim, narrative role of the passage, and constraints to preserve.
2. Ask subagents for distinct rewrite approaches. Each subagent must explain what it changed, what it cut, and what tradeoff it made.
3. Vet the variants yourself. Reject rewrites that sound smooth but lose meaning, specificity, voice, or technical precision.
4. Synthesize the final version from the best parts. The main agent owns the final edit and quality judgment.

Do not use subagents for tiny line edits unless the user asks for variations.

## Style Smells

Flag and fix these patterns:

- **Negative setup**: "not X, but Y", "no longer X", "not just X" when Y is the real claim.
- **Vague synthesis**: "points to", "signals", "reflects", "underscores", "speaks to", "represents", "shows the same thing" when the actual claim can be stated directly.
- **Doublet emphasis**: "safe, observable, repeatable, and scalable" when the list is decorative rather than precise.
- **Generic elevation**: "core capability", "critical unlock", "step change", "game changer", "seamless", "robust", "transformative".
- **Essay throat-clearing**: "In today's world", "The reality is", "At its core", "The key is", "What matters is".
- **Contrast without stakes**: a before/after frame where the before does not matter to the reader.
- **Over-smoothed transitions**: "Moreover", "Additionally", "Ultimately", "That said" when the sentence can just follow.
- **Abstract nouns**: "alignment", "leverage", "workflow", "infrastructure", "capability" without concrete referents.
- **Fake universality**: "teams are realizing", "companies are starting to", "everyone is moving toward" without evidence.

When one appears, name the smell, explain the issue in one sentence, and offer a sharper version.

## Rewrite Rules

- Put the important claim first unless suspense is doing real work.
- If a sentence's job is just to connect examples to a claim, consider splitting it into examples first, then the claim.
- Cut the negative half of a contrast unless it changes the meaning.
- Replace "examples point to a trend" with "trend claim, then examples as evidence."
- Prefer the shortest sentence that preserves the thought. Less is often stronger.
- Prefer concrete actors and verbs over abstract categories.
- Replace summary labels with the thing that actually happened.
- Keep useful imperfection; do not make the prose sound uniformly polished.
- Preserve strong weirdness, specificity, and personal judgment.
- Keep technical precision when editing technical writing.

## Output Modes

If the user asks for a cleanup pass, return:

- **Sharpened version**: the revised text
- **Cuts made**: the main removed patterns
- **Still weak**: any remaining structural or evidence problem

If the user asks for critique only, return:

- the buried claim
- the top style smells
- the highest-leverage rewrite move

If the user asks for multiple options, provide distinct versions by intent, not tiny wording variants.

Do not rewrite beyond the user's scope. If they provide one paragraph, edit that paragraph.

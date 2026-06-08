---
name: research-reddit-communities
description: Researches Reddit communities through agent-led discovery, public inspection, and optional read-only API helpers, then recommends one first community to participate in. Use when the user wants to find, compare, evaluate, or choose subreddits for posting, community participation, launch research, feedback-seeking, or distribution without spamming.
---

# Research Reddit Communities

Use this to identify Reddit communities where a product, project, or idea can learn from serious discussion and participate credibly. The goal is not to automate promotion; it is to choose one first community from evidence.

## Operating Standard

Start with manual-first research. Do not block on API credentials. Use Reddit pages, subreddit rules, search results, top/recent posts, comments, pinned threads, sidebars, and wikis before treating API helpers as necessary.

Use scripts as investigation aids only. They may gather bounded evidence or create templates, but the agent owns the judgment. Do not let a script produce final suitability scores, rankings, or the first-channel recommendation.

Never automate posting, commenting, voting, DMs, account actions, or moderation actions. Keep all Reddit interaction read-only unless the user explicitly asks to draft a post or comment for manual posting.

## Intake

Before research, establish the research brief. Infer obvious answers from context; ask one concise question only when a missing fact would change the candidate set.

Capture:
- product, project, or category
- target users and adjacent users
- pain terms, competitor/tool names, and job-to-be-done phrases
- communities already considered and why they were weak
- promotion constraints and reputational risks
- selection goal for the first community
- desired research artifact location

Default the selection goal to learning quality plus low reputational risk over reach or immediate conversion.

## Expectation Alignment

Before discovery, grill the user until the selection criteria are explicit. Ask one question at a time, recommend an answer, and wait for feedback when the answer could change the research direction.

Resolve:
- what "suitable" means for this research
- whether learning quality, posting acceptability, reach, conversion, or reputation risk matters most
- what community behaviors are disqualifying
- whether the first move should be a comment, a weekly-thread post, a direct post, or observation only
- what outcome would make the first community worth continuing

If the user has not decided, recommend learning quality plus low reputational risk as the primary criterion, with promotion acceptability as a gate rather than the main objective.

## Discovery Workflow

1. Build a seed map from native Reddit search, web search scoped to Reddit, related subreddit sidebars, competitor/tool mentions, and user-pain phrases.
2. Inspect candidate communities manually before summarizing them. Read rules, pinned posts, recent posts, top posts, high-comment posts, and examples of product/project posts.
3. For each viable candidate, record evidence source links and short observations. Distinguish what was observed from what is inferred.
4. Classify each candidate qualitatively: `avoid`, `observe only`, `comment first`, `weekly thread only`, or `candidate for first channel`.
5. Shortlist the few communities with the best learning quality and lowest participation risk.
6. Recommend exactly one first community unless the evidence is too weak; if evidence is too weak, recommend the next research action instead.

## What To Look For

Prefer communities where people share advice, compare approaches, discuss real workflows, and respond substantively. Avoid communities dominated by complaints, low-effort launch posts, generic AI hype, zero-comment links, or narrow edge cases that do not match the brief.

Check promotion posture from rules and observed behavior. A community may allow promotion only in weekly threads, only with flair, only for open-source work, only after participation, or not at all. Treat unclear rules as risk.

Look for native post shapes: technical teardown, lessons learned, question seeking examples, architecture discussion, benchmark, incident story, resource list, or showcase thread. Recommend participation formats that match what the community already rewards.

## Optional Helpers

Use `scripts/make_research_note.py` to create a structured research artifact from a brief.

Use `scripts/inspect_with_praw.py` only when official Reddit API credentials are available and appropriate. The helper is read-only and bounded; it fetches subreddit metadata, rules, and sampled posts. If credentials are missing or access is unclear, continue manually.

## Output

Write the research artifact outside the skill directory, usually in the current project or notes vault. If the user says "notes vault" or the work is durable GTM research, use `~/Notes` and follow its local `AGENTS.md`.

Use `RESEARCH-TEMPLATE.md` as the report shape. Keep the final recommendation qualitative. Do not use numeric scores.

Close with:
- the recommended first community
- why this community is better than the alternatives
- the safest first participation move
- the post/comment angle to test
- confidence and what to observe next

## Critique Pass

Before finalizing, challenge the recommendation:
- Did the research inspect actual posts and comments, not just subscriber counts?
- Is the community acceptable for participation without looking spammy?
- Is promotion posture based on rules or observed examples?
- Is the first action small enough to preserve trust?
- Did the agent choose one community instead of hiding behind a broad list?

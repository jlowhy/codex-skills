---
name: research-reddit-communities
description: Researches Reddit communities through broad discovery, public inspection, staged narrowing, and optional read-only API helpers, then recommends one first community to participate in. Use when the user wants to find, compare, evaluate, or choose subreddits for posting, community participation, launch research, feedback-seeking, or distribution without spamming.
---

# Research Reddit Communities

Use this to identify Reddit communities where a product, project, or idea can learn from serious discussion and participate credibly. The goal is not to automate promotion; it is to discover broadly, narrow deliberately, and choose one first community from evidence.

## Operating Standard

Start with manual-first research. Do not block on API credentials. Use Reddit pages, subreddit rules, search results, top/recent posts, comments, pinned threads, sidebars, and wikis before treating API helpers as necessary.

Use scripts as investigation aids only. They may gather bounded evidence or create templates, but the agent owns the judgment. Do not let a script produce final suitability scores, rankings, or the first-channel recommendation.

Never automate posting, commenting, voting, DMs, account actions, or moderation actions. Keep all Reddit interaction read-only unless the user explicitly asks to draft a post or comment for manual posting.

## Intake

Before research, establish the research brief. Infer obvious answers; ask one concise question only when a missing fact would change the candidate set.

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

1. Build a broad seed map from native Reddit search, web search scoped to Reddit, related subreddit sidebars, competitor/tool mentions, user-pain phrases, adjacent roles, and category synonyms.
2. For non-trivial GTM/community research, collect at least 50 candidate communities before judging fit. If fewer than 50 are findable, state the search paths tried and why the candidate universe is smaller.
3. Group the longlist by audience and job-to-be-done, such as buyers, practitioners, adjacent operators, tool-specific users, architecture/infrastructure, founder/project sharing, and excluded launch surfaces.
4. Do a fast triage pass over all candidates. Record size/activity if available, why it entered the map, obvious exclusion reasons, and whether deeper inspection is warranted.
5. Select 10-15 semi-finalists for manual inspection. Read rules, pinned posts, recent posts, top posts, high-comment posts, and examples of product/project posts.
6. For each semi-finalist, describe what the community actually likes: native post shapes, popular-comment patterns, disagreement style, moderation posture, and repeated pain language.
7. Classify each semi-finalist qualitatively: `avoid`, `observe only`, `comment first`, `weekly thread only`, or `candidate for first channel`.
8. Shortlist 3-5 communities with the best learning quality and lowest participation risk.
9. Recommend exactly one first community unless the evidence is too weak; if evidence is too weak, recommend the next research action instead.

## What To Look For

Prefer communities where people share advice, compare approaches, discuss real workflows, and respond substantively. For B2B or team-adoption research, prioritize communities where the buyer, manager, senior practitioner, or adoption owner discusses rollout, training, governance, budgets, standards, risk, and organizational friction.

Do not treat a community as suitable only because the topic label matches. Popular posts and comments must relate to the brief's user, problem, or adoption context. Tool-user communities can be evidence sources without being participation targets.

Avoid communities dominated by complaints, low-effort launch posts, generic AI hype, zero-comment links, or narrow edge cases that do not match the brief.

Check promotion posture from rules and observed behavior. A community may allow promotion only in weekly threads, only with flair, only for open-source work, only after participation, or not at all. Treat unclear rules as risk.

Look for native post shapes: technical teardown, lessons learned, question seeking examples, architecture discussion, benchmark, incident story, resource list, or showcase thread. Recommend participation formats that match what the community already rewards.

When evaluating comments, look for who is speaking and what earns agreement: senior engineers, engineering managers, founders, practitioners, buyers, beginners, vendors, or hobbyists. Record examples of popular comments in paraphrase, including their argument pattern and why they mattered.

## Optional Helpers
Use `scripts/make_research_note.py` for a structured artifact, and `scripts/inspect_with_praw.py` only when official Reddit API credentials are available. If credentials are missing or access is unclear, continue manually.

## Output

Write the research artifact outside the skill directory, usually in the current project or notes vault. If the user says "notes vault" or the work is durable GTM research, use `~/Notes` and follow its local `AGENTS.md`.

Use `RESEARCH-TEMPLATE.md` as the report shape. Keep recommendations qualitative; do not use numeric scores.

Close with:
- the recommended first community
- why this community is better than the alternatives
- the safest first participation move
- the post/comment angle to test
- confidence and what to observe next

If the research was a first pass that did not complete the broad 50-community funnel, label it explicitly as incomplete and name the missing discovery work.

## Critique Pass

Before finalizing, challenge the recommendation:
- Did the research inspect actual posts and comments, not just subscriber counts?
- Did discovery start broad enough, with at least 50 candidates for non-trivial research?
- Did the report show how the longlist was narrowed, not just present a shortlist?
- Are popular posts and comments related to the actual product/user/adoption context?
- Is the community acceptable for participation without looking spammy?
- Is promotion posture based on rules or observed examples?
- Is the first action small enough to preserve trust?
- Did the agent choose one community instead of hiding behind a broad list?

---
name: file-issues
description: Files handoff-ready issues in an issue tracker, including duplicate and related-issue research, from bug reports, audits, notes, chats, PRs, docs, screenshots, or URLs. Use when the user asks to add, file, create, ticket, track, deduplicate, research, or hand off issues in Linear, Jira, GitHub Issues, or an unspecified tracker.
---

# File Issues

Use this when the user wants issue material turned into tracked work that another person or agent can pick up without reconstructing the past context. An **issue tracker** is the system where work is tracked; an **issue** is one tracked unit of work. Use "ticket" only when the user or tracker uses that word.

## Find The Tracker

Infer the issue tracker from, in order:

1. the user's explicit tracker name, project, team, issue key, or URL
2. repository docs, existing issue references, branch names, PR links, commit messages, or local config
3. available MCP/tools and authenticated workspaces
4. recent conversation context

If the tracker is not known, ask one concise question: which issue tracker and project/team should receive these issues?

If required fields are missing, infer conservative defaults from nearby issues. Ask only for fields that block creation or update.

If labels, components, statuses, milestones, or other organization fields are missing or inconsistent, do not invent them silently. Use confident existing matches; otherwise create the issue with native required fields only, note the missing organization, recommend a minimal taxonomy or placement, and ask before creating new labels/components or changing tracker structure.

## Gather Context

Before mutating the tracker, inspect every accessible source the user referenced:

- chat details and pasted text
- URLs, existing issues, PRs, review threads, docs, comments, specs, screenshots, logs, traces, commits, branches, or files
- local codepaths when the issue depends on implementation behavior
- nearby issues when they establish style, labels, components, statuses, priority, or acceptance-criteria format

Do not duplicate material already captured in durable artifacts. Reference the path or URL, then summarize only the details needed for handoff.

If a referenced artifact cannot be accessed, say so in the issue and include the unavailable reference instead of silently dropping it.

## Research Related Work

Before creating new issues, search for existing or past work that may duplicate, supersede, block, or contextualize the issue:

- tracker issues by title keywords, error messages, feature names, customer names, labels, components, teams, projects, and likely synonyms
- closed, canceled, archived, or completed issues when the current issue may be recurring or previously deferred
- linked PRs, commits, release notes, incidents, support threads, docs, and code comments when they may explain prior decisions or partial fixes
- local repository history when the issue mentions a file, behavior, regression, or removed feature

Record the search terms and surfaces checked when the result affects handoff quality.

If a duplicate exists, do not create a new standalone issue unless the user asked for it or the existing issue cannot accept the new context. Prefer updating, commenting on, linking to, reopening, or marking the new issue as duplicate according to the tracker's native workflow.

If related work exists but is not a duplicate, link it and summarize the relationship: blocked by, blocks, related to, follows up, regression of, split from, or supersedes.

If the research changes the right action, pause before mutating the tracker. Recommend one course of action, explain why, and ask the user to confirm. Common recommendations include update the existing issue, reopen it, add a comment with new context, create a follow-up linked to it, merge several findings into one issue, or create a new issue marked as related.

## Shape The Issues

Create one issue per independently grabbable unit of work unless the user explicitly asks for one umbrella issue or the issues share the same fix and acceptance criteria.

Classify each issue as **Ready** only when expected behavior, current behavior, scope, acceptance criteria, and verification are clear, and the expected behavior is settled. Use **Needs shaping** when product or design decisions, workflow policy, runtime parity, validation cost tradeoffs, defaults, ownership, repro, or acceptance criteria are missing, or where reasonable teams could choose different outcomes. Use **Investigation** when the symptom is real but root cause or fix path is unknown.

For **Needs shaping** issues, capture the decision needed, options, tradeoffs, evidence needed, open questions, and acceptance criteria for settling the decision. Do not invent certainty or convert unresolved decisions into implementation tasks. If details are incomplete, capture the unknowns explicitly and assign a suitable status, label, section, or first task for triage.

## Issue Content Standard

Every created or updated issue should include:

- **Title**: specific, outcome-oriented, and searchable.
- **Summary**: what needs to change and why it matters.
- **Source context**: links, chat references, file paths, PRs, issues, commits, screenshots, logs, customer reports, or quoted snippets with dates when relevant.
- **Current behavior / problem**: the observed failure, gap, risk, or user pain.
- **Expected behavior / goal**: the desired state or decision needed.
- **Scope**: what is included and what is explicitly out of scope.
- **Acceptance criteria**: concrete checks or outcomes; mark missing criteria as open questions instead of fabricating them.
- **Verification notes**: commands, manual flows, repro steps, datasets, environments, or screenshots to use.
- **Dependencies and relationships**: blockers, duplicates, parent/child links, related issues, PRs, or rollout constraints.
- **Open questions**: unresolved facts the assignee should not have to rediscover.

Prefer the tracker's native fields for team, project, component, labels, status, priority, estimate, due date, parent, milestone, sprint, relations, and attachments. Put anything that does not map cleanly into the description.

## Creation Workflow

1. Gather and inspect context until the issue boundaries are clear.
2. Search for duplicates, related work, previous attempts, and existing decisions.
3. Draft the issue set mentally and merge/split/update/link issues before creating anything new.
4. Use the tracker tool/API when available. For Linear, use the Linear MCP tools. For Jira or other systems, use the available authenticated tool, CLI, or browser session.
5. If no creation tool is available, provide complete tracker-ready issue bodies and state exactly what blocked creation.
6. After creation or update, read back or verify the affected records when possible.
7. Report the created or updated issue identifiers/URLs, duplicate decisions, related links, missing organization, and any unresolved handoff risks.

## Quality Bar

The assignee should not need to ask "where did this come from?" or "what was already checked?" after reading the issue.

Do not compress away provenance. Keep references close to the claim they support. If the source was chat-only, name it as conversation context and summarize the relevant details.

Do not over-specify implementation when the issue is a product or investigation issue. Capture the decision needed, likely owner, and the smallest next step.

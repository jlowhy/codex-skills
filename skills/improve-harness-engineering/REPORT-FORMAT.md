# Harness Engineering Report Format

The report must show the whole harness before narrowing to an implementation brief.

## 1. Repo Topology

Summarize the repo shape, runtime, package manager, test framework, CI model, release/deploy model, current agent workflow, and commands verified or skipped.

## 2. Harness Map

Create one subsection for each audit dimension:

- **Feedforward guides**
- **Feedback sensors**
- **Human workflow**
- **Harnessability**

Each subsection must include:

- **Current behavior**: how the relevant guide, feedback sensor, workflow, or architecture works today. Include the exact files, commands, config paths, and conditions where it does or does not apply.
- **Observed gap**: the mismatch, missing route, contradiction, weak signal, or navigation friction. State the condition that exposes it.
- **Candidate improvements**: viable options, not only the favorite
- **Preferred recommendation**: the best option for this dimension and why
- **Expected new behavior**: what will be true after the recommendation is implemented
- **Proof plan**: checks, dry-runs, file reads, or runtime observations that would prove the gap is closed
- **Do not build yet**: tempting controls to defer and why

## 3. Prioritized Recommendations

Rank the cross-dimension top recommendations. Explain the ordering using leverage, confidence, effort, time-to-feedback, and maintenance cost.

For each top recommendation, include a concise current-to-future delta: how it works today, what changes, and what proof will show the improvement.

Group lower-priority items by audit dimension so the user can still see the full option space.

## 4. Implementation Brief

Only write this after every harness-map dimension is covered. Include preferred option, why it moves the needle, alternatives considered, files and commands likely to change, verification plan, do-not-build-yet items, and open alignment questions.

## 5. Alignment Questions

Ask one question at a time when alignment is needed. Include the recommended answer or preferred direction with each question.

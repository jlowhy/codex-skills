# Skills

This context defines the language used for authoring personal Codex skills in this repository.

## Language

**Agent-led community research**:
A workflow where the agent investigates candidate communities through sampled evidence, uses tools to gather facts, and makes a judgment-backed recommendation.
_Avoid_: automated community ranking, bulk subreddit export

**Investigation aid**:
A script or API helper that fetches bounded evidence for the agent to inspect during research.
_Avoid_: automation pipeline, ranking engine

**First-channel recommendation**:
The single community the agent recommends for the first focused participation attempt after comparing candidate communities.
_Avoid_: channel list, launch plan

**Learning quality**:
The expected usefulness of a community's discussion for understanding real user pain, objections, vocabulary, and participation norms.
_Avoid_: reach, audience size

**Research brief**:
The product, audience, pain terms, constraints, and selection goal supplied to an agent-led community research session.
_Avoid_: hardcoded product context

**Light signal**:
A simple computed observation that helps the agent navigate evidence without deciding suitability.
_Avoid_: suitability score, final rank

**Manual-first research**:
A research workflow that begins with public page, search, rule, post, and comment inspection without requiring API credentials.
_Avoid_: API-first research

**Research template**:
A reusable note structure that helps the agent record candidate-community evidence consistently.
_Avoid_: generated report, final recommendation

**Research artifact**:
A run-specific community research note or report created from a research session.
_Avoid_: skill reference file, reusable template

**Action-style skill name**:
A skill slug that starts with the action the agent should perform.
_Avoid_: noun label

**Expectation alignment**:
A pre-research grilling step that resolves what matters, what does not matter, and what tradeoffs the recommendation should make.
_Avoid_: preference capture, loose intake

**Asset brief**:
A short run-specific definition of the audience, intended reader change, channel, format, source links, claim risk, and call to action for a social asset.
_Avoid_: generic prompt, content request

**Storyboard**:
The ordered slide or scene sequence that converts source material into a scannable social asset before rendering.
_Avoid_: final design, transcript dump

**Local renderer**:
A deterministic script that turns structured asset input into local preview/export files without publishing them.
_Avoid_: social media automation, scheduling agent

**Export bundle**:
The local files produced for review or manual upload, such as HTML preview, PNG slides, PDF carousel, or MP4.
_Avoid_: published post, campaign

## Relationships

- **Agent-led community research** uses one or more **Investigation aids**.
- An **Investigation aid** supports judgment but does not decide the recommendation.
- A **First-channel recommendation** prioritizes **Learning quality** and low reputational risk over immediate distribution.
- A **Research brief** configures **Agent-led community research** for a specific product or category.
- An **Investigation aid** may return **Light signals** but should not produce a final suitability score.
- **Manual-first research** keeps **Agent-led community research** unblocked when API credentials or approval are unavailable.
- A **Research template** structures evidence capture during **Agent-led community research**.
- A **Research artifact** belongs in the project or notes location for the specific research session, not in the skill repository.
- An **Action-style skill name** should make the agent's main job explicit at trigger time.
- **Expectation alignment** happens before discovery so the agent does not optimize for the wrong definition of suitability.
- An **Asset brief** configures a **Storyboard** for one source and channel.
- A **Local renderer** turns a **Storyboard** into an **Export bundle**.
- An **Export bundle** is reviewed manually before any publishing workflow is considered.

## Example Dialogue

> **Dev:** "Should this skill crawl every subreddit and auto-rank the best one?"
> **Domain expert:** "No. The skill should guide **Agent-led community research** and call **Investigation aids** only when they help inspect specific communities."

## Flagged Ambiguities

- "script" was used to mean both a full automation pipeline and an **Investigation aid**; resolved: scripts are bounded helpers for agent-led discovery.
- "suitable channel" could mean high-reach distribution or high-quality learning surface; resolved: the first channel should optimize for **Learning quality** with low reputational risk.
- The Reddit research skill should stay general-purpose; Mistle belongs in the **Research brief**, not as hardcoded skill behavior.
- "score" was considered for helper output, but resolved against for this skill: helpers should expose **Light signals**, while the agent owns suitability judgment.
- Reddit API access was considered as the default entrypoint, but resolved against: the skill should use **Manual-first research** and treat API helpers as optional accelerators.
- "reddit-community-research" was considered as a noun label; resolved: use the **Action-style skill name** `research-reddit-communities`.
- "what matters" should not stay implicit in the research brief; resolved: use **Expectation alignment** to grill the selection criteria before discovery.

# Jeremiah Lowin — Episode 1 proposals

Jeremiah is the founder/CEO of Prefect and core maintainer of FastMCP. His segment focused on agent-driven open-source maintenance, personal/just-in-time software, and the anatomy of skills. Blog: *Mostly Harmless: Truly Artificial Intelligence*.

## Skills

Jeremiah screen-shared his skills folder live and read several of these files on camera — they were demoed, not just described.

### `explain` skill
His "workhorse" skill, referenced by most of his other skills (`use your explain skill to...`). It is ~80 lines but the one sentence that matters is: *"Talk to me like you're explaining this to your colleague who knows about your project but wants to understand what you just did."* Solves the "I'm running 10 agents on 10 things, what is this branch actually doing?" problem. [00:46:00–00:47:00] He offered to make it public "under the banner of this podcast."

### `ship-it` skill
His first-ever skill. Exists purely so he can type "ship it" and get the right outcome: **open a PR, do NOT merge.** Most LLMs interpret "ship it" as merge. Lesson: skills as a personal-vocabulary bridge to deterministic agent behavior. [00:54:00–00:55:00]

### `github-reply` skill
Shapes tone of GitHub replies in his voice — e.g., "don't say 'Great work' followed by a rejection." Not about masquerading as him; about treating contributors decently. [00:54:00]

### `create-skill` / skill-for-writing-skills
A meta-skill cobbled together from sources online. Embodies his "skills are living documents" philosophy. [00:55:00]

## Workflows

### Voice-memo-driven second brain
Records a voice memo almost every morning (often during the school-run / commute, ~30 min) teeing up the day, plus meeting recordings. Pours info in so the agent can pull threads together later. Uses OpenClaw as the primary personal interface specifically because he can muck with its memory. [00:36:00–00:38:00]

### Hybrid agent-human OSS maintenance
Spins up agents to write and review code, but always steps in manually for FastMCP. Pet peeve: review agents are biased toward "accept the PR if you just change X" — wrong stance for a framework. [00:39:00–00:46:00]

### Editor/agent split
OpenClaw for memory-bound, asynchronous personal work; Claude Desktop + Codex Desktop for code. Migrated from CLIs to desktops for better parallel-session management. [01:02:00–01:03:00]

## Tools / projects he showed

### Prefab (Python generative-UI DSL)
Python front-end framework that needs no backend — designed for MCP apps and internal dashboards. Started inside FastMCP, spun out a couple of weeks ago. Anders at dbt Labs styled MySpace and Windows themes on it. Real (if quick) on-screen walkthrough — project page plus Anders's themed examples. [00:57:00–01:00:00]

### Cardboard
His personal, just-in-time slide software. Organizes talks as acts → beats → slides with color-coded speaker notes (blue/gray/yellow/pink). Read-only UI; edited exclusively via API/MCP from any agent, often by voice memo. Built for PyAI keynote, will use for PyData London. Fullest on-screen walkthrough of the three projects — navigated the acts/beats layout, scrolled to slides, showed speaker notes. [01:00:00–01:02:00] May open-source if there's interest.

*FastMCP was on screen as a backdrop (the GitHub repo + CONTRIBUTING doc) while he talked about OSS maintenance, but he didn't walk through the framework itself. Dropped from this list — it's context, not a demo.*

## Explainers

Concept-explanation passages — places where Jeremiah was *teaching* the audience what something is or how it works, with enough density to seed a short pedagogical post.

### What is a skill? (anatomy + progressive disclosure)
Jeremiah walked through skills structurally: two frontmatter fields (name + description), description is always in the agent's context, body is only loaded on demand. He named **progressive disclosure** as the "genius" of skills and contrasted them with canned prompts. ~2 minutes of pure exposition — definition, anatomy, mechanism, why descriptions matter. [00:50:00–00:52:00] *Sidebar candidate: "skills as living documents" — his folder of ~20 skills that he constantly edits as he discovers what doesn't work [00:53:00]*.

### Skills vs MCP — when to use which
Direct answer to Hugo's question. Clean one-line distinction: **skills steer agent behavior by injecting into context like a user message; MCP distributes business logic from a central place.** Extends into a non-obvious second beat — MCP's real product-market fit is internal enterprise distribution, not third-party fan-out. ~2 minutes of teaching-mode content. [00:48:00–00:50:00]

### MCP vs CLI — when to use which
For individuals: pick whichever; uninteresting debate. For enterprises: non-starter — you distribute business logic centrally via MCP, not by installing CLIs on every machine. Same shape as the Skills-vs-MCP explainer, with a sharper POV on enterprise distribution. [00:49:00–00:50:00]

## Dropped from the proposal

Items the first pass surfaced that don't earn a place in this repo:

- ***Saying No* blog post** — already exists at his blog, repo would just be linking. No artifact to build.
- **"Best contribution is a great issue"** — one-line policy plus a link to FastMCP's CONTRIBUTING. Same problem: nothing for the repo to add.

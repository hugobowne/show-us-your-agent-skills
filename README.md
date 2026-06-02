![Show Us Your Agent Skills](images/skillz-1.jpg)

What are people at the top of the game building with AI agents, and how are
they doing it?

Are they Claudemaxxing with 8 terminals open at once? Or adversarially
testing Opus 4.7 generated code with OpenAI Codex? Do they define suites
and swarms of sub-agents, or use AGENTS.md and agent skills?

What do they love about building with agents? What do they hate? What tips
and tricks do they use to supercharge their workflows?

Thomas Wiecki (PyMC Labs) and Hugo Bowne-Anderson (Vanishing Gradients) are
on a mission to find out. Think Excel World Championships meets Eurovision.

This repo turns each episode into browsable, forkable artifacts: markdown
skills, workflow writeups, and tool references you can read, copy, and
adapt to your own setup.

## Installation (npx skills)

You can install the skills in this repo with:

```
npx skills add https://github.com/hugobowne/show-us-your-agent-skills
```

Install one skill only:

```
npx skills add https://github.com/hugobowne/show-us-your-agent-skills --skill explain
```

Check for updates:

```
npx skills check
npx skills update
```

These skills are snapshots from the corresponding live streams. Creators often iterate on their own versions afterwards, so check each skill's README for instructions to pull the latest from the creator when one is linked.

## Episode 1: Wes McKinney, Jeremiah Lowin, Randy Olson

[Watch on YouTube](https://youtube.com/live/Pq3xuChdwxQ)

Field notes: [Wes McKinney](episode-field-notes/ep-1/wes.md), [Jeremiah Lowin](episode-field-notes/ep-1/jeremiah.md), [Randy Olson](episode-field-notes/ep-1/randy.md).

| Skill | What it does | Guest | Watch |
|-------|--------------|-------|-------|
| [explain](skills/explain) | Agent narrates what it just did, like a teammate handing off. | Jeremiah Lowin (Prefect, FastMCP) | [00:46:14](https://youtube.com/live/Pq3xuChdwxQ?t=2774) |
| [github-reply](skills/github-reply) | Replies to GitHub contributors in your voice, no "Great work, but rejected" sandwiches. | Jeremiah Lowin (Prefect, FastMCP) | [00:54:08](https://youtube.com/live/Pq3xuChdwxQ?t=3248) |
| [ship-it](skills/ship-it) | Re-trains "ship it" to mean *open a PR*, not merge. | Jeremiah Lowin (Prefect, FastMCP) | [00:54:52](https://youtube.com/live/Pq3xuChdwxQ?t=3292) |
| [high-signal-chart-workflow](skills/high-signal-chart-workflow) | Turns a one-line idea into a Tufte-style chart, with an LLM-as-judge verifier loop. | Randy Olson (Goodeye Labs, r/dataisbeautiful) | [01:12:37](https://youtube.com/live/Pq3xuChdwxQ?t=4357) |
| [8-bit-video-gen](skills/8-bit-video-gen) | Turns guest headshots into short 8-bit pixel-art video clips for livestream intros and cutaways. | Show Us Your Agent Skills | [Episode 1](https://youtube.com/live/Pq3xuChdwxQ) |

| Workflow | What it does | Guest | Watch |
|----------|--------------|-------|-------|
| [agentic-software-factory](workflows/agentic-software-factory) | Run several agent projects in parallel while background review agents read every commit and maintain a fix queue. | Wes McKinney (Posit, pandas) | [00:27:14](https://youtube.com/live/Pq3xuChdwxQ?t=1634) |
| [second-brain](workflows/second-brain) | Feed a personal agent memory with daily voice memos and use an editable memory substrate for asynchronous work. | Jeremiah Lowin (Prefect, FastMCP) | [00:35:50](https://youtube.com/live/Pq3xuChdwxQ?t=2150) |

## Episode 2: Hilary Mason, Bryan Bischof, Eric Ma, Tomasz Tunguz

[Watch on YouTube](https://youtube.com/live/l37PR-OkYKA)

Field notes: [Hilary Mason](episode-field-notes/ep-2/hilary.md), [Bryan Bischof](episode-field-notes/ep-2/bryan.md), [Eric Ma](episode-field-notes/ep-2/eric.md), [Tomasz Tunguz](episode-field-notes/ep-2/tom.md).

| Skill | What it does | Guest | Watch |
|-------|--------------|-------|-------|
| [prompt-refinement](skills/prompt-refinement) | Interview the user's intent, ask for three variations at different magnitudes of change, score against a rubric you wrote up front. | Hilary Mason (Hidden Door) | [01:01:00](https://youtube.com/live/l37PR-OkYKA?t=3660) |
| [marimo-pair](skills/marimo-pair) | A coding agent drives a reactive Marimo notebook through a bash bridge into the Python kernel, for human-in-the-loop EDA. | Eric Ma (Moderna) | [00:11:57](https://youtube.com/live/l37PR-OkYKA?t=717) |

| Workflow | What it does | Guest | Watch |
|----------|--------------|-------|-------|
| [agentic-eda](workflows/agentic-eda) | Human-in-the-loop EDA: agent renders the next plot, human picks the next question, every claim backed by an artifact. | Eric Ma (Moderna) | [00:23:27](https://youtube.com/live/l37PR-OkYKA?t=1407) |
| [eval-driven-charts](workflows/eval-driven-charts) | Build an agent-facing chart library by generalising eval failures into features; the package can never regress on an eval it once passed. | Bryan Bischof (Theory Ventures) | [01:25:11](https://youtube.com/live/l37PR-OkYKA?t=5111) |
| [weekly-gremlins](workflows/weekly-gremlins) | Three agent personas pull from a bad-ideas backlog, pitch and critique each other, and write design docs for moonshots no roadmap would schedule. | Hilary Mason (Hidden Door) | [01:14:20](https://youtube.com/live/l37PR-OkYKA?t=4460) |
| [local-first-agents](workflows/local-first-agents) | Default to a local model and thin harness, reaching for cloud inference only for named exceptions. | Tomasz Tunguz (Theory Ventures) | [02:07:42](https://youtube.com/live/l37PR-OkYKA?t=7662) |

## Episode 3: Matthew Honnibal, Eleanor Berger, Nico Gerold, Alan Nichol, Vincent Warmerdam, Paul Iusztin

[Watch on YouTube](https://youtube.com/live/ud2WzkKeDZs)

Field notes: [Matthew Honnibal](episode-field-notes/ep-3/matt.md), [Eleanor Berger](episode-field-notes/ep-3/eleanor.md), [Nico Gerold](episode-field-notes/ep-3/nico.md), [Alan Nichol](episode-field-notes/ep-3/alan.md), [Vincent Warmerdam](episode-field-notes/ep-3/vincent.md), [Paul Iusztin](episode-field-notes/ep-3/paul.md).

| Skill | What it does | Guest | Watch |
|-------|--------------|-------|-------|
| [try-except](skills/try-except) | Reads a Python codebase and tightens every `try/except` so the `try` covers only what can fail and the `except` catches the right exception. | Matthew Honnibal (spaCy, Explosion) | [00:12:09](https://youtube.com/live/ud2WzkKeDZs?t=729) |
| [pre-mortem](skills/pre-mortem) | Reads production code, finds where it is fragile, and writes post-mortems for bugs that have not happened yet but a plausible change could introduce. | Matthew Honnibal (spaCy, Explosion) | [00:14:10](https://youtube.com/live/ud2WzkKeDZs?t=850) |
| [mutation-testing](skills/mutation-testing) | Measures test-suite strength by introducing deliberate bugs one at a time and reporting which ones no test caught. | Matthew Honnibal (spaCy, Explosion) | [00:14:10](https://youtube.com/live/ud2WzkKeDZs?t=850) |
| [here-now](skills/here-now) | Publishes HTML pages, files, and whole sites to live URLs without leaving the terminal. | Eleanor Berger (Jimini Health) | [00:45:55](https://youtube.com/live/ud2WzkKeDZs?t=2755) |
| [anki-connect](skills/anki-connect) | Drives Anki through the AnkiConnect API, gating every note- or card-modifying operation behind explicit confirmation. | Eleanor Berger (Jimini Health) | [00:49:46](https://youtube.com/live/ud2WzkKeDZs?t=2986) |
| [impeccable](skills/impeccable) | Hands a coding agent a full frontend design language so it builds production-grade interfaces instead of generic ones. | Eleanor Berger (Jimini Health) | [00:50:02](https://youtube.com/live/ud2WzkKeDZs?t=3002) |
| [youtube-watch-later-gist-summaries](skills/youtube-watch-later-gist-summaries) | Reads your YouTube Watch Later playlist, summarises every video from its transcript, and publishes each summary as a secret gist. | Eleanor Berger (Jimini Health) | [00:52:57](https://youtube.com/live/ud2WzkKeDZs?t=3177) |
| [thread-postmortem](skills/thread-postmortem) | Introspects a thread that went sideways, traces each misstep to the instruction behind it, and proposes edits biased toward deletion. | Nico Gerold (Sourcegraph, Amp) | [01:59:04](https://youtube.com/live/ud2WzkKeDZs?t=7144) |
| [remotion-video](skills/remotion-video) | Encodes a builder's design judgment for programmatic video, so Claude turns a few minutes of recorded audio into a finished explainer. | Alan Nichol (Rasa) | [02:46:00](https://youtube.com/live/ud2WzkKeDZs?t=9960) |
| [research](skills/research) | Builds and queries a persistent LLM-curated research wiki from Obsidian, Readwise, NotebookLM, GitHub repos, and supplied sources. | Paul Iusztin (Decoding AI) | [02:19:52](https://youtube.com/live/ud2WzkKeDZs?t=8392) |

| Workflow | What it does | Guest | Watch |
|----------|--------------|-------|-------|
| [personal-agent-harness](workflows/personal-agent-harness) | Run a personal agent on isolated spare hardware, reachable through Discord or WhatsApp, with autonomy granted gradually. | Eleanor Berger (Jimini Health) | [00:47:50](https://youtube.com/live/ud2WzkKeDZs?t=2870) |

Still to come from this episode:

- **Vincent Warmerdam** showed notebooks as a shared canvas for humans and agents; his Marimo Pair skill already shipped in Episode 2 ([marimo-pair](skills/marimo-pair)).

## Episode 4: Hamel Husain, Chris Fonnesbeck, Doug Turnbull

[Watch on YouTube](https://youtube.com/live/XaYQFtca798)

Field notes: [Hamel Husain](episode-field-notes/ep-4/hamel.md), [Chris Fonnesbeck](episode-field-notes/ep-4/chris.md), [Doug Turnbull](episode-field-notes/ep-4/doug.md).

| Workflow | What it does | Guest | Watch |
|----------|--------------|-------|-------|
| [skill-scepticism](workflows/skill-scepticism) | Review shared agent skills before trusting, adapting, replacing, or rejecting them. | Hamel Husain (Parlance Labs) | [00:22:32](https://youtube.com/live/XaYQFtca798?t=1352) |
| [plan-review-implementation-review](workflows/plan-review-implementation-review) | Ask an agent for a plan, audit it with `review plans`, implement only after the plan is clean, then audit the finished code with `review implementation`. | Chris Fonnesbeck (PyMC Labs) | [01:05:53](https://youtube.com/live/XaYQFtca798?t=3953) |
| [auto-research-agentic-search](workflows/auto-research-agentic-search) | Let an agent experiment with search-code patches while hidden validation decides what survives. | Doug Turnbull | [01:41:07](https://youtube.com/live/XaYQFtca798?t=6067) |

## Upcoming Episode 5: John Berryman, Isaac Flath, Matt Palmer

[Register on Luma](https://luma.com/0t8kiodw)

Friday, June 19, 2026, 9:00 AM - 10:30 AM AEST (GMT+10), live on YouTube.

Joined by John Berryman (Arcturus Labs, early engineer on GitHub Copilot, O'Reilly author), Isaac Flath (Kentro Tech, ex-Answer.AI), and Matt Palmer (Conductor, ex-Replit).

## More from us

Vanishing Gradients is a podcast, workshop series, blog, and newsletter focused on what you can build with AI right now. Over 70 episodes with expert practitioners from Google DeepMind, Netflix, Stanford, and elsewhere. Hundreds of hours of free, hands-on workshops. All independent, all free. [Subscribe on Substack](https://hugobowne.substack.com/).

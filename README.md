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

| Skill | What it does | Guest | Watch |
|-------|--------------|-------|-------|
| [explain](skills/explain) | Agent narrates what it just did, like a teammate handing off. | Jeremiah Lowin (Prefect, FastMCP) | [00:46:14](https://youtube.com/live/Pq3xuChdwxQ?t=2774) |
| [github-reply](skills/github-reply) | Replies to GitHub contributors in your voice, no "Great work, but rejected" sandwiches. | Jeremiah Lowin (Prefect, FastMCP) | [00:54:08](https://youtube.com/live/Pq3xuChdwxQ?t=3248) |
| [ship-it](skills/ship-it) | Re-trains "ship it" to mean *open a PR*, not merge. | Jeremiah Lowin (Prefect, FastMCP) | [00:54:52](https://youtube.com/live/Pq3xuChdwxQ?t=3292) |
| [high-signal-chart-workflow](skills/high-signal-chart-workflow) | Turns a one-line idea into a Tufte-style chart, with an LLM-as-judge verifier loop. | Randy Olson (Goodeye Labs, r/dataisbeautiful) | [01:12:37](https://youtube.com/live/Pq3xuChdwxQ?t=4357) |
| [8-bit-video-gen](skills/8-bit-video-gen) | Turns guest headshots into short 8-bit pixel-art video clips for livestream intros and cutaways. | Show Us Your Agent Skills | [Episode 1](https://youtube.com/live/Pq3xuChdwxQ) |

Workflow writeups are coming next, starting with Wes McKinney's stack:

- **Agents reviewing agents.** A daemon reads every commit your agents make, so by the time a PR merges, code has been read by agents 4–5 times.
- **A fleet of long-running sessions.** 4–5 Superpowers projects spec'd and implementing in parallel, unattended; one plan ran 14 hours and 45 tasks without him touching it.
- **"Off the rails?" review.** No line-level reading. The only question Wes asks is whether the agent strayed structurally or chased scope creep.

## Episode 2: Hilary Mason, Bryan Bischof, Eric Ma, Tomasz Tunguz

[Watch on YouTube](https://youtube.com/live/l37PR-OkYKA)

| Skill | What it does | Guest | Watch |
|-------|--------------|-------|-------|
| [prompt-refinement](skills/prompt-refinement) | Interview the user's intent, ask for three variations at different magnitudes of change, score against a rubric you wrote up front. | Hilary Mason (Hidden Door) | [01:01:00](https://youtube.com/live/l37PR-OkYKA?t=3660) |
| [marimo-pair](skills/marimo-pair) | A coding agent drives a reactive Marimo notebook through a bash bridge into the Python kernel, for human-in-the-loop EDA. | Eric Ma (Moderna) | [00:11:57](https://youtube.com/live/l37PR-OkYKA?t=717) |

| Workflow | What it does | Guest | Watch |
|----------|--------------|-------|-------|
| [agentic-eda](workflows/agentic-eda) | Human-in-the-loop EDA: agent renders the next plot, human picks the next question, every claim backed by an artifact. | Eric Ma (Moderna) | [00:23:27](https://youtube.com/live/l37PR-OkYKA?t=1407) |
| [eval-driven-charts](workflows/eval-driven-charts) | Build an agent-facing chart library by generalising eval failures into features; the package can never regress on an eval it once passed. | Bryan Bischof (Theory Ventures) | [01:25:11](https://youtube.com/live/l37PR-OkYKA?t=5111) |
| [weekly-gremlins](workflows/weekly-gremlins) | Three agent personas pull from a bad-ideas backlog, pitch and critique each other, and write design docs for moonshots no roadmap would schedule. | Hilary Mason (Hidden Door) | [01:14:20](https://youtube.com/live/l37PR-OkYKA?t=4460) |

Still to come from this episode:

- **Local-first inference.** Tom Tunguz runs Qwen 35B on a Mac M5 at 120 to 140 tokens per second with a 256K context window; cloud only comes in for multi-file rearchitectures or hard bugs.

## Episode 3: Matthew Honnibal, Eleanor Berger, Nico Gerold, Alan Nichol, Vincent Warmerdam, Paul Iusztin

[Watch on YouTube](https://youtube.com/live/ud2WzkKeDZs)

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

Still to come from this episode:

- **Paul Iusztin's writing loop.** Diff a hand-edit against the agent's draft, extract the signal, and fold it back into a markdown style profile the agent reads next time.
- **Vincent Warmerdam** showed notebooks as a shared canvas for humans and agents; his Marimo Pair skill already shipped in Episode 2 ([marimo-pair](skills/marimo-pair)).

## Upcoming episodes

Register on Luma to join live, or get the recording after.

### Episode 4: Hamel Husain, Chris Fonnesbeck, Doug Turnbull

[Register on Luma](https://luma.com/ltpzpqgw)

Joined by Hamel Husain (Parlance Labs), Chris Fonnesbeck (PyMC Labs, veteran analyst for the Mets, Brewers, and Yankees), and Doug Turnbull (led Search at Shopify and Reddit).

## More from us

Vanishing Gradients is a podcast, workshop series, blog, and newsletter focused on what you can build with AI right now. Over 70 episodes with expert practitioners from Google DeepMind, Netflix, Stanford, and elsewhere. Hundreds of hours of free, hands-on workshops. All independent, all free. [Subscribe on Substack](https://hugobowne.substack.com/).

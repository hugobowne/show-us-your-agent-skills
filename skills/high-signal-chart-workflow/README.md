# high-signal-chart-workflow

A phase-structured agent skill that turns a one-line idea into a publication-quality, Tufte-style chart. Pairs a deterministic image and code linter with an LLM-as-judge verifier loop that scores the rendered chart against Tuftean principles and feeds failures back as fix-it instructions until the chart actually carries the data story.

This skill is `randalolson/high-signal-chart-workflow` from [Goodeye Labs](https://goodeyelabs.com), captured as a frozen snapshot from **2026-05-06**. The living, maintained version is at [**app.goodeyelabs.com/templates/randalolson/high-signal-chart-workflow**](https://app.goodeyelabs.com/templates/randalolson/high-signal-chart-workflow).

## What it does

1. **Intake and environment.** Slugifies the idea, creates an isolated working directory, bootstraps a Python venv, drops a programmatic verifier (`verify_chart.py`) into the directory.
2. **Dataset discovery.** Web-searches for authoritative public datasets, biased toward government and institutional sources (CDC, Census, BLS, OECD, USDA, EIA). Cross-checks at least one figure against the source's own page before proceeding.
3. **Three parallel variants.** Dispatches sub-agents to produce three different chart types (for example: line, slope, small multiples), each conforming to a baked-in design checklist (no default gridlines, direct labels instead of legends, axis titles with units, muted palette with one accent color, `dpi=300`, `bbox_inches="tight"`, width at least 1200 px).
4. **Variant selection.** Scores variants against the checklist, picks a winner, keeps the losing scripts as a run log.
5. **Verifier loop.** Up to five outer iterations of (programmatic check + LLM-as-judge against Truesight's public chart-design evaluator at `api.truesight.goodeyelabs.com/api/eval/tufte-test`). Failures come back as fix-it instructions; the chart is rewritten and re-rendered until the evaluator passes or the iteration budget is exhausted.
6. **Done.** Final artifacts: `chart.png`, `chart.py`, the raw dataset, and `run.json` with the evaluator verdict.

Runtime: Python 3.11+, `curl`, internet access. No Goodeye account required to run this snapshot; the Truesight evaluator endpoint and the default image upload (litterbox.catbox.moe) are both anonymous.

## How to use it

`SKILL.md` is the artifact. Copy this whole folder into the location your agent harness expects, then prompt the agent to use the skill. Common locations:

- **Claude Code:** `.claude/skills/high-signal-chart-workflow/` (project) or `~/.claude/skills/high-signal-chart-workflow/` (user)
- **Cursor, Codex, and other harnesses with skill support:** see your harness's documentation for the expected directory

Then ask your agent:

> "Use the high-signal-chart-workflow skill to make a chart of *(your one-line idea here)*."

## Customize it, or get future updates

The version in this folder is frozen at the date stamped above. The maintained version lives on Goodeye and evolves as the verifier criteria and design checklist improve. To pull future updates, or to make a private, customizable copy you own, install the Goodeye CLI and fork the template:

```bash
pipx install goodeye    # or: pip install goodeye
goodeye login           # opens a browser; new and existing accounts both work
goodeye templates fork @randalolson/high-signal-chart-workflow
```

Once forked, the workflow body is yours to edit. Re-publish your customized version with `goodeye workflows publish`, share it with teammates, or pull future upstream improvements by forking again.

## Watch the segment

Randy demoed this skill live on episode 1 of *Show Us Your Agent Skills*.

- [**01:12:37**](https://youtube.com/live/Pq3xuChdwxQ?t=4357): Live run on US marriage and divorce rates over time.
- [**01:16:39**](https://youtube.com/live/Pq3xuChdwxQ?t=4599): Skill design walkthrough; phases, progressive disclosure, reflect-and-improve.
- [**01:29:32**](https://youtube.com/live/Pq3xuChdwxQ?t=5372): The Tufte test, *"tell it how to check it."*
- [**01:33:24**](https://youtube.com/live/Pq3xuChdwxQ?t=5604): Daily cron with human-in-the-loop on the last 5%.
- [**01:38:05**](https://youtube.com/live/Pq3xuChdwxQ?t=5885): Eval as a living document.

> *"You don't wanna just tell it what to do, you also wanna tell it how to check it."*

> *"I run this skill every single morning, and that's how I make that post series."*

## Author

Randal S. Olson, co-founder and CTO of Goodeye Labs. Longtime moderator of r/dataisbeautiful; early AutoML researcher (TPOT). Posts AI-generated data visualization stories daily, powered by this same workflow.

## Ownership and license

Owned by **Goodeye Labs** (https://goodeyelabs.com). Workflow authored by Randal S. Olson.

Licensed under [**CC BY-NC-ND 4.0**](https://creativecommons.org/licenses/by-nc-nd/4.0/) (Attribution-NonCommercial-NoDerivatives 4.0 International). Full license text is in [`LICENSE`](LICENSE) alongside this file.

In plain English:

- **You may** read this skill, run it for personal or noncommercial use, and share unmodified copies with attribution.
- **You may not** use it for commercial purposes, or publish modified versions of it.
- **For commercial use, or to customize the workflow privately,** install Goodeye and fork the template (commands above).

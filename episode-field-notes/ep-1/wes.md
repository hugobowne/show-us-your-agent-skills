# Wes McKinney — Episode 1 proposals

Wes is the creator of pandas and has shipped ~1M lines of agent-generated code across ~a dozen projects in the last six months. His segment was a live tour of an integrated "agentic engineering" stack he has built around Jesse Vincent's Superpowers framework: async code review, agent-session observability, a local GitHub dashboard, a local issue tracker, and Git-worktree management. Burns ~1.3–1.4B tokens/day [00:10:00].

## Skills

Wes did not screen-share his own skill markdown files. The skill he repeatedly invokes on stream is part of a tool he built:

### `RoboRev fix` skill
The agent-facing entry point into RoboRev. Wes instructs Claude/Codex to invoke this skill periodically during long Superpowers runs; it reads the open-reviews ledger, fixes them, and commits the fixes. For very large plans he asks Superpowers' sub-agent-driven implementation skill to invoke `RoboRev fix` "every five tasks." [00:17:00, 00:20:00–00:21:00]

## Workflows

### Continuous async code review
Wes's core practice, the thing his whole stack is organised around. Three rules/parameters shape it:
- **Commit every turn** — a hard rule in CLAUDE.md / AGENTS.md across all his projects. Each commit fires post-commit hooks that RoboRev installs via `roborev init`.
- **Async review by Codex Exec, GPT 5.5, reasoning xHigh.** Every commit gets reviewed in the background. Wes: *"Codex is like the strongest code reviewer out there."* He uses both Claude Code and Codex for *generation* (~75/25 Claude/Codex by his macOS widget), but Codex does the review.
- **Drain the ledger explicitly via the `RoboRev fix` skill.** Reviews accumulate as open items; fixes don't happen until the skill is invoked. The skill picks up open reviews, fixes them, commits the fixes. For long Superpowers plans, Wes asks the sub-agent-driven implementation skill to invoke `RoboRev fix` every ~5 tasks so the queue stays drainable mid-run.

Net effect: by the time a PR merges, code has been read by agents four or five times, minimum. [00:15:00–00:21:00, 00:27:00]

### Parallel spec interviews across 4–5 projects
*"I work on four or five projects during the day, I'll run parallel spec interviews with superpowers, and so I'll be bouncing... from different terminals... I'll just participate in these spec interviews, build the implementation spec with superpowers, and then set it implementing."* [00:20:00] One Superpowers plan ran 14 hours / 45 tasks unattended [00:21:00].

### Structural-only human review
Wes almost never reads code line-by-line — RoboRev does that. His own review sits one level up: *"I look at the code in terms of, like, structural detail. Like, does it look right? Like, is it too complex? Does it need to be simplified? Does it have scope creep that's inappropriate?... Sometimes the agents will go off the rails and build something that's completely inappropriate, and so you have to nuke that."* [00:27:00–00:28:00] He poses these questions back to the agent rather than fixing things himself.

## Tools / projects he showed

### RoboRev
Background daemon + terminal UI that reviews every commit your agents produce. Maintains a ledger of open reviews; agents fix them via the `RoboRev fix` skill. Set up per-repo with `roborev init` to install post-commit hooks. Demoed live on the show repo and on Spicy Takes. [00:15:00–00:19:00]

### Agents View
A "fancy agent session database" with full-text search and token-usage analytics across all his agent sessions; web + desktop app; supports many agents. Used to find context from previous sessions and to track spend. Not shown live (private data on screen) but website walked through. [00:19:00–00:21:00]

### Middleman
Local GitHub dashboard. Single pane of glass across repos, threaded activity view in reverse-chronological order (Wes: *"GitHub is in leagues with big scroll"*), inline diff viewer, merge-PR-without-leaving-the-app, RoboRev wired up as a CI reviewer on PRs. Demoed live. [00:21:00–00:24:00]

### Kata — https://github.com/wesm/kata
Local terminal issue tracker, built after Beads *"destroyed some of my Git repositories, very annoyingly."* Positioned as a simpler local replacement for Beads / GitHub Issues. `kata init` per project; agents read `kata quickstart` to learn the commands. Briefly demoed. (Transcript renders the name as "Qoda" — it's "kata".) [00:12:00, 00:24:00–00:25:00]

### spicytakes.org
His personal site that summarises and pulls the spiciest quotes from 11,773 blog posts across 34 blogs he follows. Built with AI. Used on stream as the demo target for a Superpowers spec ("a simple dashboard showing frequency of recent spicy takes"). [00:10:00, 00:17:00]

### Token-usage macOS widget (his own, mentioned in passing)
A small widget that shows his Claude vs Codex split over 30 days and what he'd be paying at API rates (~$21k/month). Not demoed in depth; flagged here in case Wes wants to share. [00:16:00]

### Third-party tools he relies on
- **Superpowers** (Jesse Vincent) — the agentic-engineering framework his stack sits on top of. Does spec interviews → sub-agent-driven implementation. Wes's stated tradeoff: *"It generates amazing software, but it also takes a long time to generate very detailed implementation plans. The idea is that it doesn't really trust leaving that much up to the agent in terms of making decisions."* [00:26:00] Quoted Jesse: *"The difference between vibe coding and agentic engineering is planning, architecture, and caring about the output."* [00:11:00]
- **Superset** — terminal workspace manager that creates Git worktrees; every worktree has its own stack of Claude Code / Codex / RoboRev terminals. [00:25:00]
- **Ghosty** — the terminal he was using on stream. [00:14:00]

## Explainers

Wes's segment was overwhelmingly live demo, not exposition. One passage qualifies:

### Vibe coding vs agentic engineering
Framed via Jesse Vincent's quote and then Wes's own gloss: *"Essentially I've been building systems to do agentic engineering and not just vibe coding... at a certain point you're like, 'Okay, this is not creating things that are good.' How do you manage all this at scale?"* The whole stack tour that follows is the answer. Short but clean teaching beat — distinguishes a term, motivates the rest. [00:11:00–00:12:00]

## Dropped from the proposal

Items the first pass surfaced that don't fit our categories:

- **Decision-budget as the real bottleneck** — *"I'm bandwidth-limited in terms of my ability to make decisions throughout the day... I can't make another decision today."* [00:29:00–00:30:00] A sharp observation about himself, not a practice or artifact. Worth quoting in a writeup, not capturing in the repo.
- **YOLO mode + back up your home dir** — *"I'm just YOLO mode all the time... back up, try not to store too much sensitive data in my home directory."* [00:30:00–00:31:00] A security posture / honest tradeoff statement, not a workflow.

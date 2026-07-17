---
name: goal-rider-author
description: Draft a goal+rider document pair to brief the next agentic turn on a project. Two documents — a ≤4000-char goal (the spine) and an unbounded rider (the prescriptive detail with eleven phases and depth-tests-first discipline). Run when user says "draft a goal", "new goal", "write a goal+rider", "goal+rider for the next agentic turn", "rider for X", or anything in the shape of "brief the next agent on Y".
license: Apache-2.0
metadata:
  author: SpecStory, Inc.
  version: "1.0.0"
  argument-hint: "<topic for the new goal>"
allowed-tools: Bash, Read, Write, Edit, Glob, Grep
---

> **Project:** [SpecStory, Inc. / `goal-rider-author`](https://www.gregceccarelli.com/goal-engineering). "Draft a goal+rider document pair to brief the next agentic turn on a project."
>
> **License:** [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0). Full license text is in [`LICENSE`](LICENSE) alongside this file.
>
> **Snapshot:** Frozen copy of [Greg Ceccarelli's published skill](https://www.gregceccarelli.com/goal-engineering/skill.md) as of 2026-07-18. The maintained version lives upstream and may have evolved since this snapshot.

# Goal & Rider Author

A two-document pattern for briefing an autonomous coding agent
(Claude Code, Codex CLI, or any agentic harness) on the next round of
work. The **goal**
is the ≤4000-char spine: what to do, what to read first, the posture,
the verification, the stop conditions. The **rider** holds the
prescriptive detail: data schemas, phase plans, depth-test names,
verb signatures, error footers, out-of-scope lists.

The pattern's superpower is that the goal stays small enough to paste
into a Codex `/goal` or a Claude run prompt, while the rider can be
arbitrarily detailed without bloating the executor's working memory.

This skill is project-agnostic. It works for any codebase that has a
`docs/goals/` (or equivalent) directory, conventional commits, and
some form of AS-BUILT / architecture doc. Substitute the project's
own toolchain commands wherever the templates say
`<project's ... command>`.

## When to invoke

The user is about to start a new round of agentic work and wants
goal+rider files written into a project's `docs/goals/` directory.
Triggers include "draft a goal that addresses X", "write a goal+rider
for Y", "new goal for the next agentic turn", "rider for X".

## Pre-work — do not skip

Before drafting, gather context. Read in this order, skipping items
the project doesn't have:

1. **Project architecture doc** — `AS-BUILT-ARCHITECTURE.md`,
   `ARCHITECTURE.md`, `docs/architecture.md`, or whatever the project
   uses. Look for a "what's shipped vs thin" section if one exists;
   it grounds the goal in reality.
2. **Prior goal+rider pairs** in `docs/goals/` (or wherever the
   project keeps them). Their invariants compose forward; do not
   duplicate verbatim. Skim the most recent two pairs to absorb
   voice and section conventions.
3. **Recent commits**: `git log --oneline -30 -- docs/goals/` and
   `git log --oneline -30`. Reveals delivery cadence and the
   conventional-commit format the project uses.
4. **Source code at HEAD** for any data structures, file paths, or
   function names you'll quote in the rider. Verify they match HEAD
   before citing.
5. **Research or pain-point reports** the project has (e.g.,
   unmet-needs, user-research, retro docs). They ground the
   ergonomics in real pain.

If you can't find prior pairs or an architecture doc, **ask the user**
for a pointer — don't invent one.

## Goal document recipe (≤4000 chars)

**Path:** `<project>/docs/goals/<YYYY-MM-DD>-<HHMM>-<project-slug>-<topic>-goal.md`

The `<HHMM>` is the local 24-hour clock time when the file is created
(e.g., `1444` for 2:44 PM). It makes `ls docs/goals/` sort in true
authoring order rather than alphabetical by topic. When two pairs land
within the same minute, secondary alphabetical sort handles the tiebreak;
that's fine.

**Hard cap:** `wc -c <file>` must be ≤4000 (prior precedents: 3929–4112).
Re-check after every edit pass. Note the `-HHMM-` insert costs ~5 chars
per internal rider reference, so leave a small buffer when riders cross-cite.

**Skeleton** — fill each section, cut to fit:

```markdown
GOAL: <one-sentence headline>. <one paragraph: current pain → what the goal lands → headline word (Friendliness / Multi-agent / Self-documenting / Default mode / …)>.

**Read first.**

- `<absolute path to project architecture doc>` — substrate; one line.
- `<absolute path to the rider being written>` — schemas, signatures, depth tests.
- `<absolute paths to exemplars or research reports>` — grounding.
- Prior riders in `<absolute path to docs/goals/>` — invariants hold.

**Posture.** Stays `<tier>`. No `<struct>` schema changes (if applicable). No `git push`. Edits inside `<project root>`. Major architectural decisions → `<V1-CANDIDATES path>`.

<DOMAIN BODY — one or two of these, depending on the goal:>

**<N> modes / verbs / artifacts, auto-resolved.**

- **`<name>`** — <one line of behavior>.

**New verbs.**

- `<verb> <args>` — <one line>.

**Friendliness as a verifiable contract.**

- Auto-detect, don't ask (the obvious case is the default).
- Preflight + preview before any state change.
- Refuse with `try: <command>` lines.
- Rollback is one command.
- Lifecycle hints after every action.

**Phases.** Eleven (P1–P11) in the rider. Each: depth test first → implement → `<project's build+test+lint+fmt command>` green → conventional-commit → CHANGELOG. P11 adds a `<new section>` to the project architecture doc.

**Verification.**

- Commands green every commit; every rider depth test present and passing.
- <Smoke 1>: <verifiable command + assertion>.
- <Smoke 2>: <verifiable command + assertion>.
- No edits outside `<project>`. No `git push`. No schema changes.

**Stop when** verification passes, AS-BUILT updated, CHANGELOG has a "<Milestone name> (alpha)" section, committed locally.
```

**Trim priority when over budget:**

1. Drop parenthetical detail that's already in the rider.
2. Shorten Read-first descriptions to bare absolute paths.
3. Compress Posture to one or two lines.
4. Cut verification smoke bullets to two.
5. Drop cross-rider "do not preempt" notes; those live in the rider.

## Rider document recipe (no char cap; typically 10–35K)

**Path:** `<project>/docs/goals/<YYYY-MM-DD>-<HHMM>-<project-slug>-<topic>-rider.md`

Use the **same** `<YYYY-MM-DD>-<HHMM>` prefix as the matching goal so
the pair sorts together. Author the goal first, then mirror its
timestamp on the rider — never split them across minutes.

**Skeleton:**

```markdown
# <project> — <Slug> Rider (<short framing>)

This rider holds the prescriptive constraints for the goal at
`<absolute path to goal>`. It supersedes nothing in prior riders
(<list dated rider filenames>) — their invariants still apply.
This rider adds <one-line summary of what's new>.

**All paths absolute.** Source `<project root>`, runtime `<runtime root>`.

## Posture (decided — do not redesign)

- **Maturity stays `<tier>`** (alpha / beta / stable; mirrors what
  the project calls the current milestone).
- **No `<struct>` schema changes** (if applicable). State lives in
  files at `<path>`.
- **<Other domain-specific invariants — be explicit>.**
- **No `git push`.** Phased local commits only.
- **No V1 / next-tier invention.** If a phase reveals a major
  architectural decision, log it in `<V1-CANDIDATES path>` (or
  equivalent) and continue.
- **Edits stay inside `<project root>`.**

## Data model (files, not fields)

<JSON schemas for any new file-based state. One block per file.
Inline-comment each field if the meaning isn't obvious.>

## <Algorithms / Mode resolution / Detection rules>

<Pseudocode for non-obvious logic. The rider IS the spec — match it
in the implementation.>

## Verb signatures

```
<verb> <args>
    [--flag]                  # description
    [--other-flag <type>]     # description
```

For each verb: refusal cases table.

## Phases (eleven)

Each phase: write the named depth test(s) **first** and watch them
fail; implement; green on
`<project's build+test+lint+fmt command, green on each commit>`;
conventional-commit local commit; one-line CHANGELOG entry.

### P1 — <name>

- <bulleted prescriptions>

Depth tests (in `<test path>`):
- `snake_case_descriptive_name_that_would_have_caught_the_thin_behavior`
- `another_named_test`

### P2 — <name>

...

### P11 — Architecture doc update + CHANGELOG (doc only; no depth test)

- Insert a new top-level section into `<architecture doc path>`:
  ```
  ## NN. <Section title>

  NN.1 <subsection>
  NN.2 <subsection>
  ...
  ```
- If the architecture doc has a "what's shipped vs thin" section,
  update it:
  - Add to the "shipped" side: <items this rider lands>.
  - Note explicitly whether this rider closes prior thin items or
    only adds capability.
- Append to `<CHANGELOG path>`:
  ```
  ## <Milestone name> (<tier>) — <YYYY-MM-DD>

  - <bullet>
  ```

## Integration matrix (when multi-mode or multi-verb)

| <axis> | <feature 1> | <feature 2> | … |
|---|---|---|---|
| ... | ... | ... | ... |

## Error-footer canonical pairs

| Error | `try:` |
|---|---|
| `<terse description>` | `<one specific command or fix>` |

(Parameterized over a depth test so every error case is exercised.)

## Config additions (when relevant)

```toml
[defaults]
<new_knob> = "<default>"
```

## Out of scope (explicitly not in this milestone)

- <one bullet per V1-candidate scope item>
- <…>

## Dependencies (Tier 1 / 2 / 3 policy)

Tier 1 (utility, free): <list with one-line justification each>.
Tier 2 (architectural, log to `DEPENDENCIES.md`): <list or "none expected">.
Tier 3 (blocked): same blocks as prior riders.

## Engineering invariants (do not violate)

- **No `<struct>` schema changes.**
- **One depth test before each phase implementation.** A phase whose
  tests were never red is suspect.
- **<Domain-specific invariants>.**
- **No silent expansion.** Anything beyond P1–P11 goes into
  `V1-CANDIDATES.md`.
- **<Spec-pinning invariants>**: e.g., "the preview block format is
  depth-tested; changing whitespace changes the spec."

## Process invariants

- Phased local commits only. No `git push`.
- Each phase ends with the relevant depth tests passing and a
  CHANGELOG entry naming the SHA.
- After P11, optionally capture a demo (asciinema cast / screenshots /
  short video) under `<project>/<demo-path>`. Skip when the change
  isn't user-visible.
- If a phase reveals a V1-architecture decision, stop and log it in
  `V1-CANDIDATES.md`; do not silently expand scope.
```

## Discipline checklist (the invariants this skill carries)

1. **Two documents, two budgets.** Goal ≤4000 chars; rider unbounded.
   Run `wc -c` on the goal before declaring done.
2. **Timestamped filenames.** Both goal and rider are named
   `<YYYY-MM-DD>-<HHMM>-<project-slug>-<topic>-{goal,rider}.md`. The
   `<HHMM>` is the local 24-hour authoring time (e.g., `1444`). The
   pair shares one timestamp so they sort together; never split them
   across minutes. This makes `ls docs/goals/` chronological.
3. **Phased local commits only.** Never tell the executor to `git push`.
4. **Files-not-fields.** When the project has persistent state
   structs (DB schema, config struct, state machine), durable
   per-feature state should live in files inside the working tree
   (`<some>/<name>.json`) rather than as new struct fields. Schema
   changes are last-resort. Skip this invariant for projects without
   such structs.
5. **Depth tests first.** Each phase's named tests are written and
   watched fail before implementation. List them by name in the rider
   so a `grep -c '^    fn '` enforces presence.
6. **Architecture-doc discipline.** P11 always updates whatever
   architecture / as-built doc the project keeps, plus CHANGELOG. If
   there's a "what's shipped vs thin" section, the thin list is
   honest — only remove items the rider actually closes.
7. **V1 candidates.** Anything out of scope goes to
   `docs/V1-CANDIDATES.md`, not silently expanded scope.
8. **Conventional commits, scoped.** `docs(goals): add <topic> goal+rider`
   for the goal-rider commit itself. `feat(<scope>):` / `fix(<scope>):`
   / `chore(<scope>):` for execution commits.
9. **Frontmatter mirrors the project's own convention** for any
   human-readable artifacts. If the project has prior impl docs
   under `docs/implementation/` or similar, match their frontmatter
   shape (Date / Status / Commit span / Owner / …). If not, propose
   a minimal frontmatter and stick to it across riders.
10. **Friendliness is verifiable.** Auto-detect, preflight + preview,
    refuse with `try: <command>`, one-command rollback, lifecycle
    hints. Each is exercised by a depth test.
11. **Judgment in markdown, invariants in code.** When the project
    has a skill / prompt-template / config-driven prompt mechanism,
    prefer that over a hardcoded const so users can tune voice or
    behavior without a rebuild. (Project-specific; skip if no such
    mechanism exists.)

## Anti-patterns to avoid

- Inventing V1 architecture inside an alpha rider.
- Schema changes without a stated strong reason.
- Backwards-compatibility shims for code that no caller uses.
- Comments explaining WHAT the code does (well-named identifiers
  already do that).
- Half-finished implementations ("we'll finish in P12").
- Duplicating invariants from prior riders verbatim — just say
  "invariants hold" and reference them.
- Depth tests written after implementation.
- Stop conditions that don't tie to verification ("stop when it
  feels done" is not a stop condition).
- Inventing CLI verbs not in the goal.
- Adding emojis to written artifacts.
- "TODO: maybe add X" lines — either it's in scope (P-numbered) or
  it's a V1 candidate.

## Standard 11-phase shape

A typical rider has these phases (adapt the names; eleven is a target,
not a hard rule — fewer or more is fine if the structure earns it):

- **P1**: Data model / plumbing — new module / file path / frontmatter
  helpers. No behavior change yet.
- **P2–P3**: Foundation — new primitive types, base mechanism.
- **P4–P8**: Feature implementation — one phase per major slice; each
  phase ships with end-to-end depth tests.
- **P9**: Integration with prior verbs / modes / state machines.
- **P10**: Cross-cutting friendliness pass — flags like `--quiet` /
  `--plain`, error-footer routing, post-action hints, help-text
  grouping.
- **P11**: Architecture-doc update + CHANGELOG + (optional) demo
  capture (doc-only; no depth test).

## Commit message for the goal-rider pair itself

```
docs(goals): add <topic> goal+rider (<one-line headline>)

<2–3 sentence summary: what the goal is for; what the rider prescribes;
what's explicitly out of scope. Mention named depth-test discipline,
files-not-fields posture (if applicable), V1 invention guard.>
```

Add the project's standard `Co-Authored-By:` footer if it uses one.

## Validation steps (run before declaring done)

```bash
PROJECT=<absolute path to project root>
DATE=$(date +%Y-%m-%d)
HHMM=$(date +%H%M)
PROJECT_SLUG=<short project name>
TOPIC=<short topic slug>
GOAL=$PROJECT/docs/goals/$DATE-$HHMM-$PROJECT_SLUG-$TOPIC-goal.md
RIDER=$PROJECT/docs/goals/$DATE-$HHMM-$PROJECT_SLUG-$TOPIC-rider.md

# 1. Goal must be under 4000 chars
wc -c "$GOAL"   # expect ≤4000

# 2. Rider must have ≥11 phase headers
grep -c '^### P[0-9]' "$RIDER"   # expect = 11

# 3. Rider must have the standard top-level sections
for section in "Posture" "Phases" "Out of scope" "Dependencies" \
               "Engineering invariants" "Process invariants"; do
  grep -q "^## $section" "$RIDER" || echo "MISSING: $section"
done

# 4. Both files cite each other's absolute paths
grep -F "$RIDER" "$GOAL"  || echo "goal does not reference rider"
grep -F "$GOAL"  "$RIDER" || echo "rider does not reference goal"

# 5. Stage and commit
cd "$PROJECT" && git add "$GOAL" "$RIDER" && git status
```

## Reference exemplars to mine

Before drafting, read at least one recent goal+rider pair from the
target project, if any exist. Look in `docs/goals/`, `docs/specs/`,
`docs/planning/`, or similar.

If the project has no prior pairs, suggest the user create one from
this template and treat it as the baseline. Optionally, ask whether
they want to point you at an exemplar from another project to crib
voice and shape from.

The discipline travels: the pattern works the same across Rust, Go,
TypeScript, Python, and mixed stacks. Only the toolchain commands
(`<project's build+test+lint+fmt command>`) change.

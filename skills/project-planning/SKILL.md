---
name: project-planning
description: Plan new software projects by decomposing the goal into MVP tasks, researching frameworks and libraries with subagents, and preferring opinionated prebuilt solutions over bespoke complexity. Use when starting a new project, scoping an idea, choosing a stack, or producing an implementation plan for a single-user MVP.
---

# Project Planning

Use this skill to turn a fresh project idea into a focused, MVP-first plan that favors prebuilt solutions and opinionated frameworks over custom complexity.

## Workflow

1. Read `references/project-planning.md`.
2. Clarify the goal in one sentence and define the single-user MVP boundary: what ships in the first cut, what is explicitly out of scope.
3. Decompose the goal into a small set of manageable tasks. Group by user-visible outcome, not by layer.
4. Spawn subagents in parallel to research frameworks and libraries that could absorb whole tasks. Prefer pre-built solutions unless a clear constraint rules them out.
5. Start from an official scaffold or starter via `bunx create-*` (`bunx create-next-app`, `bunx create-vite`, `bunx create-t3-app`, `bunx create-tanstack`, `bunx create-expo`) instead of hand-rolling the project skeleton.
6. Before any dependency install in the new project, create or preserve `bunfig.toml` with `[install] minimumReleaseAge = 259200`. Prefer scaffold flags that skip the initial install, then run `bun install`.
7. Pick an opinionated framework (e.g. Next.js, TanStack Start) when it improves organization and removes wiring decisions. Skip framework-grade tooling for one-screen utilities. Ask the user which framework to use if unclear.
8. For UI, initialize shadcn/ui with `bunx shadcn@latest init` and choose a minimalist preset - prefer shadcn blocks, you can ask the user to pick. Pull in components on demand, not preemptively.
9. Lay out components and services in a logical, opinionated structure before any code is written.
10. Decide the minimum useful testing surface and the minimum useful git-hook surface. Both default to small.
11. Produce a short plan: goal, MVP scope, task list, stack choices with one-line rationale, deferred items.

## Planning Rules

* Build for one user first.
* Use Bun as the runtime, package manager, and script runner by default.
* Start every new project from an official scaffold or template, invoked through `bunx create-*` (e.g. `bunx create-next-app`, `bunx create-vite`, `bunx create-t3-app`, `bunx create-tanstack`, `bunx create-expo`).
* Every Bun project must include a root `bunfig.toml` with `minimumReleaseAge = 259200` under `[install]` before `bun install` or `bun add` resolves new packages.
* For UI, default to shadcn/ui with a minimalist preset. Add components with `bunx shadcn@latest add <component>` as they are actually needed.
* Prefer prebuilt over bespoke. Reach for a library, hosted service, or framework primitive before writing your own.
* Choose boring, well-documented defaults. Novelty is a cost, not a feature.
* Cut features before cutting clarity. If the MVP is too big, remove scope, do not compress the design.
* Pick one opinionated framework per project. Do not mix two routing or data layers.
* Organize by feature or domain, not by file type, once there is more than one screen.
* Write tests for critical logic and infrastructure: money, auth, data integrity, deploy paths. Skip tests for trivial glue and UI that will churn.
* Use git hooks for formatting and fast static checks. Do not run full test suites or type-checks on every commit.
* Defer anything that is not on the path to a working MVP: analytics, feature flags, advanced error reporting, premature abstractions.
* Re-evaluate the plan once the first end-to-end slice runs. Replan from evidence, not from the original guess.

## Subagent Use

* Launch independent research subagents in parallel: one per framework or library question.
* Give each subagent a self-contained brief: the problem, constraints, what a good answer looks like, and a length cap.
* Ask for a recommendation plus the main tradeoff, not a survey of every option.
* Do not delegate the final decision. Synthesize subagent findings yourself before committing to a stack.

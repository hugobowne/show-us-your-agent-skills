# Project Planning

Use this reference when planning a new software project. The goal is a focused MVP plan that one person could ship, with deliberate choices about frameworks, structure, tests, and tooling.

## Goal

Produce a plan that:

- States the project goal in one sentence.
- Names the single-user MVP and the things it explicitly does not do yet.
- Lists the smallest set of tasks that gets to a working end-to-end slice.
- Names the stack with a one-line rationale per choice.
- Calls out what is deferred and why.

A good plan is short, opinionated, and falsifiable. If a reader cannot tell what is in the MVP and what is not, the plan is not done.

## Core Loop

1. Define the goal and the one user the MVP serves.
2. Decompose into outcome-oriented tasks.
3. Research frameworks and libraries (in parallel) that could absorb whole tasks.
4. Choose an opinionated stack and a logical layout.
5. Decide the minimum useful testing and hook surface.
6. Ship the first slice, then replan from what you learned.

## Decomposition

- Group tasks by user-visible outcome (`user can sign in`, `user can save a note`), not by layer (`set up database`, `set up API`).
- Each task should be completable in a single focused session. If it is not, split it.
- Order tasks so the system is end-to-end working as early as possible. Vertical slices beat horizontal layers.
- Mark anything not required for the first end-to-end slice as deferred.

## Research with Subagents

- Spin up subagents in parallel for independent questions: auth library, data layer, UI kit, deployment target, payments.
- Brief each subagent self-contained: the problem, constraints (single-user MVP, deploy target, language), and the shape of a good answer.
- Ask for: top recommendation, one-line rationale, main tradeoff, and one realistic alternative.
- Cap the response length. Long surveys are wasted; one decisive paragraph is the goal.
- You make the call. Subagents inform; they do not decide.

## Runtime and Tooling

Bun is the default runtime, package manager, test runner, and script executor for new projects. Use it unless a dependency or deployment target explicitly requires Node, Deno, or another runtime.

- Install with `bun add`, not `npm install` or `pnpm add`.
- Run scripts with `bun run`, executables with `bunx`.
- Use `bun test` for unit tests unless the framework prescribes another runner.
- Use `Bun.serve`, `Bun.file`, and other Bun APIs when they replace a dependency.
- Document the runtime in the README so contributors do not reach for npm by reflex.
- Always configure Bun's package age gate before resolving dependencies in a new project:

```toml
[install]
minimumReleaseAge = 259200
```

This is 3 days in seconds. It filters newly published npm package versions during `bun install` and `bun add`, including transitive dependency resolution. If the project already has `bunfig.toml`, preserve its existing settings and add the missing `[install]` key instead of overwriting the file. Do not add `minimumReleaseAgeExcludes` by default.

Fall back to Node when:

- A required library segfaults or misbehaves under Bun.
- The deploy target (a specific serverless platform, customer infra) is Node-only.
- A teammate or course audience needs Node for parity.

## Start From a Scaffold

Every project starts from an official scaffold or starter, not a hand-rolled skeleton. Invoke scaffolds through `bunx create-*` so Bun also resolves the initializer.

- Next.js: `bunx create-next-app@latest`
- Vite: `bunx create-vite@latest`
- TanStack Start: `bunx create-tanstack@latest`
- T3 (Next.js + tRPC + Drizzle + NextAuth): `bunx create-t3-app@latest`
- Expo (mobile): `bunx create-expo@latest`
- Remix / React Router: `bunx create-remix@latest`
- A blank Bun project: `bun init`

Other guidance:

- Prefer a Replit template when the goal is to ship from the browser or hand the project to a less technical user.
- Remove only what you do not need from the scaffold. Do not rearrange its conventions on day one.
- Pin the scaffold version in the README (`bunx create-next-app@15.x`) so the project is reproducible.
- If a scaffold can skip dependency installation, use that option, write `bunfig.toml`, then run `bun install`.
- If a scaffold defaults to npm or pnpm, switch to Bun immediately: delete the foreign lockfile, write `bunfig.toml`, and run `bun install`.
- If a scaffold runs an install before a project-local `bunfig.toml` exists, add the project-local `bunfig.toml` immediately after generation and rerun dependency resolution with `bun install`. For stricter agent environments, set the same age gate in the agent user's global Bun config before running scaffolds:

```sh
printf '[install]\nminimumReleaseAge = 259200\n' > "${XDG_CONFIG_HOME:-$HOME}/.bunfig.toml"
```

A scaffold is worth using even for tiny projects: it sets the runtime, linter, formatter, and tsconfig in a known-good state.

## UI: shadcn/ui, Minimalist Preset

Default UI stack is shadcn/ui on top of Tailwind, configured with a minimalist preset. Be opinionated here so design decisions do not become a sink.

- Initialize once per project: `bunx shadcn@latest init`.
- Pick a minimalist preset during init: neutral or zinc base color, low radius, no decorative gradients or shadows.
- Add components on demand: `bunx shadcn@latest add button input dialog`. Do not pull in components you have not used yet.
- Keep the generated components in the project (this is the point of shadcn). Edit them in place rather than wrapping them in another layer.
- Use the default typography and spacing. Resist custom design tokens until the product has a real visual identity.
- Reach for a different UI library only when shadcn cannot express the surface (heavy data grids, complex charts, native mobile).

Failure modes to avoid:

- Installing every shadcn component up front "just in case."
- Re-skinning shadcn so heavily that updates become impossible.
- Mixing shadcn with a second component library in the same app.

## Prefer Prebuilt

Default to prebuilt solutions in this order:

1. A framework primitive (`next/auth`, `tanstack-query`, `next/image`).
2. A well-maintained library with a clear API.
3. A hosted service for undifferentiated work (auth, email, payments, storage).
4. A bespoke implementation, only when the above genuinely do not fit.

Reach for bespoke code when:

- The behavior is core differentiation.
- Available options carry licensing, cost, or lock-in you cannot accept.
- Integration cost would exceed writing it directly.

Otherwise, take the library.

## Minimize Complexity

- Build for one user first. No multi-tenant data model, no roles, no orgs.
- No feature flags, A/B testing, analytics pipelines, or queues until a real need appears.
- No microservices. Start with one app, one database.
- No premature abstractions. Two similar call sites is not a pattern. Three may be.
- No config systems for values that change once a year.
- Avoid handling errors you cannot recover from; let the process fail and fix the cause.

## Opinionated Frameworks

Use an opinionated framework when it removes wiring decisions and standardizes structure. Examples:

- Next.js, TanStack Start, Remix, SvelteKit for full-stack web apps.
- Expo for cross-platform mobile.
- FastAPI or NestJS when the backend is the product.

Pick one framework per project and follow its conventions. Do not run two routers, two data layers, or two styling systems in parallel.

Skip framework-grade tooling for:

- One-screen utilities.
- CLI tools and scripts.
- Throwaway experiments.

## Project Layout

Lay out the project before you write code. A logical layout is easier to grow than one that emerged by accident.

- Organize by feature or domain once the project has more than one screen: `features/auth`, `features/notes`.
- Keep shared primitives (`ui/`, `lib/`, `db/`) clearly separated from feature code.
- Co-locate tests with the code they cover.
- Keep server and client boundaries explicit in framework-conventional ways.
- Resist deep nesting. Three levels is usually enough.

## Tests

- Write tests for critical logic and infrastructure: money math, auth flows, data integrity, migration scripts, deploy paths.
- Write a small number of end-to-end tests for the golden path.
- Skip tests for trivial glue, throwaway UI, and code that will be rewritten before it stabilizes.
- Test behavior, not implementation. Avoid mocks that mirror the code under test.
- Too many tests slow change. Aim for the smallest suite that would catch a regression you actually care about.

## Git Hooks

- Use hooks for fast, deterministic checks: formatter, linter, basic secret scan.
- Run them on staged files, not the whole repo, where possible.
- Keep total hook time under a few seconds. Slow hooks get bypassed.
- Do not run full type-checks or test suites in pre-commit. Move those to CI.
- Pre-push is acceptable for slightly heavier checks if the project warrants it.
- Hooks should fail loudly with a clear fix. If a check is flaky, remove it.

## Failure Modes to Avoid

- Planning a v2 before v1 runs end-to-end.
- Designing for users, scale, or features that do not exist yet.
- Picking a stack from novelty rather than fit.
- Choosing libraries by star count instead of API quality and maintenance signal.
- Hand-rolling auth, payments, or email.
- Wrapping every library in a custom abstraction "in case we swap it out."
- Writing tests to hit coverage numbers instead of to catch regressions that matter.
- Stuffing every check into pre-commit until contributors start using `--no-verify`.

## Quick Checklist

- Can a reader state the MVP and what is out of scope after reading the plan?
- Is each task tied to a user-visible outcome?
- Did subagents research the framework and library questions in parallel?
- Is each major dependency a prebuilt solution unless there is a stated reason otherwise?
- Did the project start from an official `bunx create-*` scaffold rather than a hand-rolled skeleton?
- Is Bun the runtime and package manager unless a constraint forces otherwise?
- Does the project have `bunfig.toml` with `[install] minimumReleaseAge = 259200` before new package resolution?
- Is the UI on shadcn/ui with a minimalist preset, and are components added only as needed?
- Is there exactly one opinionated framework driving structure?
- Is the layout organized by feature once the app has more than one screen?
- Are tests limited to critical logic and the golden path?
- Are git hooks fast, scoped, and unlikely to be bypassed?
- Is everything not required for the first end-to-end slice clearly deferred?

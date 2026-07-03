# Reconstructed AGENTS.md from Matt Rocklin's screen share

We are including this so you can get a feel for the rules, context, and working agreements real builders give their agents. Matt Rocklin showed this `AGENTS.md` file during episode 6 while explaining how he gets agents to work inside Frisky, his Dask-like scheduler.

This is a reconstructed version of his `AGENTS.md`, not the original file. We could not capture every section from the screen share, so gaps are marked as `[uncaptured content]`.

## Frisky context

# Frisky - Dask Scheduler in Rust

Frisky is a high performance distributed task scheduler for parallel computing in Python and Rust. It is modeled off of Dask, with the following differences:

- Simple: Minimal subset of functionality, just the scheduler, simple futures API, and a dask graph option
- High performance: both in the scheduler state machine, and along various pipes (networking, disk, etc..)
- Agent first: designed to be driven by and interrogated by agents. Good at exposing useful diagnostics programmatically.

## Architecture

Like Dask, Frisky has a central scheduler, distributed workers, and possibly many clients submitting work.

## Compatibility

Frisky aims to be compatible with Dask with the futures and Dask interfaces.

Frisky also aims to bootstrap off of deployed Dask clusters for deployment.

## Tooling

- Rust: Tokio for concurrency
- Python: Python both for the user interface as well as for testing (pytest)
- Interop: We use PyO3 for Rust/Python interop
- Frontend: TypeScript + React 19, Vite 7, Tailwind v4, shadcn/ui (Radix-based primitives, new-york style, slate base + amber accent), lucide-react icons, PixiJS for the WebGL task stream

## Async

We use Tokio for concurrency. We like to keep the state machines on a single thread for simplicity. The worker does have multiple threads though for execution.

- Two-pass pattern: read data first, then mutate
- Clone keys/data before iterating to avoid holding borrows
- Use `tokio::sync::Mutex` (not `std::sync::Mutex`) for async code

## Development

```sh
make setup      # First-time: sync deps + install maturin import hook
make dev        # Build dashboard + Python extension
make dashboard  # Build dashboard only
make rust       # Build Python extension only
make test       # Run tests
```

After make setup, editing Rust source auto-rebuilds the extension on next `import frisky` (via `maturin_import_hook`).

[uncaptured content]

## Testing

The screen share showed a testing section during a fast scroll. This block is less certain than the surrounding text, but the visible material appeared to cover these commands and rules:

```sh
make test              # Reliable path-selected black-box Python API suite
make test-lanes        # Verify every pytest file is assigned to a lane
make test-integration  # Heavier black-box/system suite (subprocesses, sockets, dashboards, Dask)
make test-rust         # Rust workspace tests
make test-dashboard    # Dashboard lint + production build
make test-all          # Rust + Python + integration + dashboard checks
```

Python tests from the repo root:

```sh
make setup  # Sync Python deps, install dashboard npm deps, install import hook
make dev    # Build dashboard + Python extension
```

Active regressions / intentionally failing repros:

```sh
make test-repro  # Runs known failure tests; nonzero while markers remain
```

- Keep user-facing behavior covered by black-box Python tests where practical.
- Keep `make test` explicit and reliable. Add stable public-API tests to its path list in `Makefile`; put subprocess, network, dashboard, Dask, or stress coverage in `make test-integration`.
- Lane membership in the `Makefile` is the single classification axis - there is no integration pytest marker. Add each new `tests/test_*.py` file to either `PYTHON_API_TESTS` or one of the integration lane lists; `make test-lanes` enforces this.
- The integration suite runs as one pytest process and is order-robust. If a test needs process isolation, that's a bug in the test - poll for the condition it needs instead of relying on a fresh process.
- Use `pytest.mark.known_failure` plus strict xfail for active regressions that should remain documented but must not poison the default suite.
- Use `make test-repro` when working on those regressions. It runs marked tests in one-file pytest processes so timeout repros do not hide other known failures. A passing known-failure file is still reported as stale; remove the marker when the behavior is fixed or tighten the repro.
- `pytest-timeout` is configured.
- `Future.result(timeout=5)` and `client.gather(futures, timeout=5)` support timeouts.
- Ctrl-C works during blocking waits.
- Use `maturin develop` to build (not `cargo build` - linker errors).
- Use `uv run pytest ...` for targeted Python tests.
- Use the sibling `./frisky-benchmark-results` repo for benchmark history and reporting.

## Benchmarks

Benchmark history and the static report site now live in the sibling public repo `../frisky-benchmark-results`. That repo owns the benchmark runner, `benchmark-site/`, tests, run JSON, and the GitHub Pages workflow for `benchmarks.getfrisky.dev`.

Run benchmarks from the results repo and point them at this checkout:

```sh
cd ../frisky-benchmark-results
uv run python -m benchmarks run --source-repo ../frisky
uv run python -m benchmarks record --source-repo ../frisky --require-clean
```

[uncaptured content]

```python
pip=[f"--find-links {wheel_dir}", f"frisky[dask]=={version}"],

cluster = coiled.Cluster(name=env, software=env, arm=True, n_workers=2)
client = frisky.hijack(Client(cluster))
```

`scripts/coiled.py` is a working end-to-end smoke test built on these pieces - read it for a known-good reference.

Gotchas:

- `coiled.create_software_environment(pip=["frisky @ https://.../foo.whl"])` silently drops the line - Coiled's `parse_pip` classifies HTTPS-to-.whl as `is_local_path`. Always use `--find-links` plus the exact dev-stamped pin from the wheel filename.
- `frisky` runs in both scheduler and worker processes via hijack; the `.so` loads once. Don't reuse a cluster across wheels - attaching keeps the stale software env silently. The pattern above (cluster name = env name) makes this automatic.
- Local `import frisky` (macOS) uses the workspace `maturin develop` build, not the manylinux wheel - different artifact, different version string. `maturin_import_hook` (installed by `make setup`) keeps it fresh on Rust edits.

We typically use the coiled workspace `rocklin-llc` unless we need more quota, in which case we use `dask-engineering`.

We've been running into issues with DNS records and hijack. Coiled reuses hostnames, and our local router seems to be caching them, making it difficult to connect.

For releases (not dev iteration) the PyPI dev channel via `.github/workflows/release.yml` still exists - see the Publishing section above.

# Performance

Much of our job is running difficult workloads, noticing that they're suboptimal, measuring what's wrong, and coming up with a change in our architecture that fixes the problem not just for that workload, but for all workloads, all without negatively impacting other workloads. This is a delicate and important process, improved by the following principles:

## Measurement of a workload

We want to look both at macroscopic and microscopic aspects of the computation.

Macroscopically we want to quantify where we're spending time (comms? disk? compute? idleness?) and where our bottleneck is.

Microscopically we can learn a lot by digging in at the millisecond level to learn how our sequence of events and choices determines those costs, and how Frisky responds to those choices.

We can get zoomed in measurements by using `frisky observe timeline` with `--start` and `--duration`, and by putting logging messages into the code where key decisions are made.

Both levels are often critical. Zoomed out, and zoomed in.

## Principled thinking on performance

When optimizing a single workload it's easy to become overly focused and change policies in a way that makes that workload fast, but negatively effects other workloads, including workloads we haven't seen yet. This often takes the form of tuned parameters, magic numbers, and special cases. We must avoid this.

Instead, we need to build systems that are simple by nature, but well thought out. The right few principles will outperform a pile of special cases any day.

## Decide_worker

We want to place tasks on workers in such a way that minimizes unnecessary hardware use, like network, while also avoiding pile-ups on particular workers that might look better suited (magnets). We want to be greedy about avoiding work (where can I run this task the fastest) while also making decisions that minimize global resource use (how can I balance the load and avoid spilling into disk). We make microscopic decisions that, taken together, have macroscopic effects.

Today we use an earliest-finish-time heuristic that takes into account compute time, communication time, and spill time, where spill time penalizes having to reach into disk for all of the work we've planned on this worker. The compute term and spill term like balancing workloads while the comm term likes concentrating computation around its data.

## Disk and Network

Ideally we avoid using disk and network, but invariably we'll need them. Modern disk and network can be quite fast if we pipeline data through them. We intentionally build a pipeline of serialization, compression, and then writing so that there is a single sequential writer to the hardware resource (we find that this yields optimal bandwidths) rather than concurrent reads/writes.

## Disk Spilling

Running out of memory is very bad. If we hit 100% then our worker dies (and maybe gets restarted). So we spill in-memory data to disk before that happens. Of course disk is slow, so we try to avoid this by the methods above (dask.order priorities, limiting rootish tasks, load balancing well). We slow down rootish tasks at around 40% of use, spill to disk around 50% of use, and start to pause around 80%. (With some smoothness and hysteresis baked in)

We also track RSS as well as frisky managed memory.

We want to make disk spilling and pausing very robust (failed workers often stress other workers) but even moreso we want to avoid getting into a position where we need to spill.

## Compression

We optionally compress data movement (network, disk) based on bandwidth, and on the compressibility of a sample of the data to be sent. We use lz4, zstd, and byte shuffle.

## Scheduler

The scheduler has to decide where to place tasks. It must do this very quickly, both in order to be responsive / low-latency (it's on the critical path), and to have high throughput (we often submit thousands of tasks at once). We aspire to one million tasks per second, or one microsecond per task. We're currently several factors shy of this goal.

It is important that most task operations be O(1), or at worst O(k) for k like the number of dependencies. We avoid scanning through all tasks (potentially millions) or all workers (potentially thousands) within the tight state machine loops.

## Scheduler Threads

We keep the state machine thread highly isolated from anything else. Other threads can run on that machine for comms and serialization, but we endeavor to keep the state machine thread flowing cleanly.

We care less about the worker. State management efficiency on the worker is less critical.

## Batching

When communicating between client/scheduler/workers we can move information about a single task, or we can batch if many tasks have finished recently. All per-task streams should have some optional batching. We find that this is critical for throughput.

## Rootish data generating tasks

It's important not to flood the workers with tasks that are easy to run and generate data. This can cause over-production when the cluster is otherwise busy in coordination-heavy workflows, like communication. To handle this we identify "rootish" tasks that have zero or few dependencies and generate data and we constrain how actively we distribute them if workers have other tasks that they could work on, even if that work is communication rather than computation. Because such tasks have no input data to sit near, workers pull them from the scheduler's queue into their own spare capacity rather than the placement objective choosing a home - which spreads them and avoids piling onto one worker.

## Task Stealing

We do not currently do task stealing, and instead rely on queueing rootish tasks on the scheduler so that there are not long queues on the workers (although long enough so that they don't starve hopefully).

## Task ordering

The `dask.order` algorithm looks at a graph and assigns priorities in order to minimize the overall memory footprint. The algorithm is complex, but tries to prioritize tasks that allow us to free memory.

## Prefixes

In principle the scheduler does not know anything about the tasks that it is asked to assign. We do track the names of the tasks though and from their repetition infer groups, which we call prefixes. We assume that tasks like `add-123` and `add-456` with the same prefix `add` are likely to be similar in how long they take, how much data they produce. Etc.

We may in the future create task groups from the task submission process itself.

## Dask-array

We have built a `dask.array` library clone called `dask-array` that is Frisky aware. It does high level query optimization, and submits the entire expression up to frisky where it then generates tasks in rust. It is much faster and there are future opportunities to get more from them.

## Agent instructions

[uncaptured content above this point]

It's critical that feedback be FAST. Ideally around a second or less. If our feedback system takes minutes then stop and think about alternatives that are faster.

If you spend a lot of time during execution and iteration figuring out how to get feedback (like python scripts to query APIs) then consider building small scripts to improve the feedback system.

## Workflow

I like work to proceed in the following phases:

### Phase 1: Planning

We make a plan together. You ask questions to make sure that we're aligned.

In the plan make sure you have a way to get live feedback about the thing we're building.

Feedback is critical to iterating to success.

### Phase 2: Execution

You do work to implement the plan, raising concerns along the way if something comes up.

### Phase 3: Testing and Iteration

Use our feedback systems (should already be implemented as part of the plan) to get feedback about how well our system works. Iterate given that feedback.

### Phase 4: Self review

Review our work so far and see if there is anything you can clean up or simplify. Don't use other agents at this phase. Do this yourself.

### Phase 5: Agent Review

Spawn a fresh-context review agent, not a fork of this conversation. Give it the current working directory, goal, and useful pointers like the diff, commit range, relevant files, and tests.

Tell it to inspect the repo independently, be critical, and report findings first.

## Github

You should have access to the github gh CLI and the `@mrocklin-ai` bot account. This should give you the ability to read and comment on various repositories. When communicating with others, please be concise and friendly. Be sure to thank them.

## Plans and writing for agents

When writing for other agents (including future agents in plans or documentation) trust the judgement of the future agents to navigate the situation well. Our job is to give broad direction and point them towards useful sources of information, but not to direct their work step by step. We need to rely on them to figure that out given the greater information they'll have from being on the ground.

## When communicating with me

Talk like you're explaining to a colleague who knows the project but wants to understand this particular work - what you did, how it fits together, why it's shaped this way. Conversational, not documentary. Express enthusiasm when something is elegant. Invite follow-up.

## Ongoing Projects

I'm working on the following projects:

- frisky: a Dask-like scheduler rebuilt in Rust for high performance. Lives at `~/workspace/frisky`
- dask-array: a re-implementation of Dask Arrays with high level query optimization. Also has Frisky integration for performance. Lives at `~/workspace/dask-array`.
- wiretapp: a low-overhead profiler that intelligently aggregates samples into cohesive chapters of a computation, and then stores them in a database for future review. Lives at `~/workspace/wiretapp` and has a wiretapp CLI.
- coiled: Context around running my company, Coiled Computing Inc., which manages cloud hardware for SaaS Python users.

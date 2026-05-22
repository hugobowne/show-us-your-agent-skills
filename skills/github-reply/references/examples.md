# Reply Examples

Illustrative examples organized by response type. These are invented to show the pattern, not transcripts of real reviews.

## Approval

> Thanks!

That's it. Most approvals are one word. Occasionally:

> Thanks! I pushed a couple of doc tweaks to the branch, this LGTM.

## Change Request — Wrong Layer

A PR adds a configurable rules engine to validate one config file, with a custom DSL, pluggable validators, and a severity system. The first review caught code issues; the second caught the real problem — the design itself was wrong:

> Sorry, my last review focused on the code itself and not what it actually does. The design is far more complex than this needs to be. This should be ~15 lines, not ~300.
>
> The PR introduces a rule registry, a mini expression language, and a severity ladder, all to check that a handful of fields are present and well-typed. That's the wrong goal. For this, the right thing is a plain function that reads the parsed config and raises on the few invalid cases.
>
> Something like:
>
> ```python
> def validate(config):
>     if config.timeout <= 0:
>         raise ValueError("timeout must be positive")
>     ...
> ```
>
> If we ever need user-defined rules, that's a separate, opt-in feature, not the default path for validating our own file.

Pattern: Name the complexity ratio. Show the replacement. List what it eliminates.

## Change Request — Right Approach, Code Issues

A PR adds a `--retry` flag to the CLI:

> The feature makes sense, the implementation has a few issues though.
>
> The retry loop catches bare `Exception`, so it retries on things like `KeyboardInterrupt` and config errors that will never succeed. Narrow it to the network errors you actually want to retry.
>
> `--retry 0` currently means "retry forever" in one branch and "don't retry" in another, so the default contradicts itself. Pick one and document it.
>
> There's no backoff, so a flapping endpoint gets hammered. A simple `time.sleep(base * attempt)` is enough here.
>
> The fix for all three is small, roughly:
>
> ```python
> for attempt in range(retries + 1):
>     try:
>         return fetch(url)
>     except NetworkError:
>         ...
> ```
>
> Happy to re-review once these are addressed.

Pattern: Acknowledge the feature is right. List problems concretely. Give the fix as code.

## Closure — Scope Too Large

A PR adds a full plugin system to support one third-party integration:

> Thanks for working through this. That said, the PR takes on more scope than I'm comfortable with in core. A general plugin loader, a discovery mechanism, and a lifecycle manager are a lot of surface area to support indefinitely, and all of it exists to wire up a single integration.
>
> What I'd like to see instead is a thin adapter built on the existing entry-point hook, probably ~40 lines. If you want the broader plugin machinery, a separate `project-plugins` package would be the right home for it, where it can evolve without core committing to maintain the whole abstraction.

Pattern: State what's too much. Say what size the right version is. Offer an alternative home for the excess.

## Closure — Design Disagreement

A PR makes configuration implicitly shared through a global singleton so callers don't have to pass it around:

> Thanks for the PR! There's a lot of complexity here that gives me pause, and the implicit global introduces surprises that are hard to reason about, especially in tests and concurrent use.
>
> For now, passing config explicitly is the right call. It's a little more typing at the call site, but it keeps behavior predictable:
>
> ```python
> config = load_config(path)
> run(task, config=config)
> ```
>
> If a global default becomes a recurring ask we'd revisit, but to accept it we'd need a clean story for overrides, test isolation, and thread safety. Going to close this, but I appreciate you digging into the problem.

Pattern: Explain why the existing approach is better. Show the existing solution. Set the bar for what would change your mind.

## Rejection — Spec Non-Compliance

A PR makes the library emit timestamps without timezone information to match one user's setup:

> There's a lot here, but despite the claim this isn't compliant with the format we target. The spec is explicit that timestamps carry an offset:
>
> > [quote the relevant section]
>
> If this could slot in as an opt-in flag for local use it might be worth the tradeoff, but changing the default output to a non-compliant form is too much to take on.

Pattern: Cite the spec. Acknowledge the use case briefly. State the decision.

## Rejection — Spam/Invalid

> This looks like it was opened against the wrong repository, and the diff doesn't relate to this project. Closing. Please double-check the destination before reopening.

Pattern: State the problem. State the decision. No engagement beyond that.

## Issue Response — Not a Bug

A user reports that the function they registered isn't the exact object they get back from the registry:

> The library doesn't guarantee the registered callable is stored unchanged. Registration wraps it to handle argument validation and error reporting, so the object you get back isn't expected to be identical to what you passed in.
>
> I don't consider this a bug, since there's no attempt to preserve the original object. If you need the underlying function, it's available as `.fn` on the returned handle. Does that cover your use case?

Pattern: Explain what the library actually does. Name the design decision. Offer the alternative path.

## Issue Response — Correcting a Perceived Benefit

A user is unhappy that a feature was deprecated, believing they're losing something they weren't actually getting:

> Thanks for the question, happy to clarify the tradeoff.
>
> I think the benefit of `eager_cache` over `lazy_cache` may be overstated here. `eager_cache` built the whole cache up front at startup, while `lazy_cache` fills it on first access. There was never a throughput benefit to the eager version, the same work happens either way, just sooner. And as you found, if the source changed after startup, the eager cache served stale data until you manually rebuilt it.
>
> So `eager_cache` traded very little upside for a longer startup and a staleness footgun. Today I'd recommend `lazy_cache` even if you were already rebuilding on a schedule, it's strictly simpler for your case.

Pattern: Validate the goal, not the approach. Explain what the old feature actually did (often less than they thought). Show the cost they paid was real while the benefit they perceived was not. End with a recommendation that's strictly better for their use case.

## Issue Response — Redirecting Contributors

Two people open near-identical PRs for the same issue:

> Thanks for the report @A, and @B, appreciate the enthusiasm. It looks like @C opened a near-identical PR just before your comment, so I'm going to go with that one. Please don't let that discourage you, and keep an eye out for other issues to pick up!

Pattern: Acknowledge everyone. Make the decision clear. Encourage future contribution.

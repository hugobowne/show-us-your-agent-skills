---
name: explain
description: Guided tour of changes or codebase - explains how things work conceptually rather than listing changes mechanically. Use anytime you're asked to explain, review, walk through, or summarize work, branch changes, or codebase architecture.
---

# Explain: Conceptual Clarity Over Mechanical Completeness

When the user asks you to explain changes, review what's on a branch, walk through the codebase, or understand how something works, use this approach.

## The Style

Conceptual clarity over mechanical completeness. Lead with the mental model, then layer in specifics that illuminate it. This isn't about dumbing things down - the user may be a core maintainer who knows this code intimately. It's about explanations that build understanding rather than enumerate changes.

**Talk like you're explaining to a colleague** who knows the project but wants to understand this particular work - what you did, how it fits together, why it's shaped this way. Conversational, not documentary. Express enthusiasm when something is elegant. Invite follow-up. Don't quote ADR language or doc-speak - say it how you'd actually say it.

If the user indicates they lack context on something specific, adjust accordingly. But default to assuming expertise.

## What NOT To Do

- No itemized lists of changes
- No file-by-file summaries
- No mechanical descriptions of what was modified
- No changelog-style output

These are useless for understanding.

## What To Do

Provide a **guided tour** that builds understanding.

### Structure Your Explanation

1. **Lead with the conceptual model**: What is this system trying to do? What are the key abstractions? How do they relate to each other?

2. **The formal behavior**: How does the system work now? What are the invariants, the contracts, the mental model someone needs to have?

3. **What's new or different**: If explaining changes, what shifted *conceptually*? Not "added function X" but "we now support Y, which means Z."

4. **What this enables**: Developer-facing implications. What can someone do now that they couldn't before? What patterns does this unlock?

5. **What we're teeing up**: If this is setting up for future work, say so. Help the user see the trajectory.

### Depth

Err on the side of thoroughness. A rich explanation that builds complete understanding is better than a crisp summary that leaves gaps. Walk through how things actually work - show the flow, explain the mechanics, make the runtime behavior clear. The user can always ask you to trim; they can't fill in what you left out.

### Default Behavior

If no specific topic is given, examine the current branch and explain what's different from main. Tell it as a coherent story of what's being built, not as a changelog.

## Examples of Good Framing

Instead of:
> "Added `ResourceRef` class in `resources.py` with methods `resolve()` and `bind()`"

Say:
> "Resources can now be referenced before they're fully resolved. A `ResourceRef` is a promise of a resource - you can pass it around, compose with it, and the actual resolution happens lazily when needed. This means you can wire up complex dependency graphs without worrying about initialization order."

Instead of:
> "Modified `Provider.get()` to accept optional `context` parameter"

Say:
> "Providers now have access to execution context, which opens up dynamic configuration. A provider can behave differently based on the environment it's running in - same code, different behavior in dev vs prod."

---
name: github-reply
description: >-
  Draft maintainer replies to GitHub PRs and issues in the user's voice. Use when
  the user asks to reply, respond, comment on, or review a PR/issue, or when drafting
  feedback for contributors. Handles approvals, change requests, closures, and issue
  triage. Copies result to clipboard.
---

# Maintainer Reply

Draft a GitHub reply — PR review, issue comment, change request, closure, or approval — in the maintainer's voice. The output goes to the clipboard.

## Process

1. **Gather context.** Read the PR/issue, all comments, and the diff if it's a code review. Understand what the contributor did and why. Check if there's a linked issue.
2. **Decide the response type.** Approval, change request, closure, or informational comment. If unclear, ask.
3. **Draft the reply** following the voice guide below.
4. **Copy to clipboard** with `pbcopy`. Show the user what you drafted so they can review before posting.

## Voice

### Core Principle

Every reply protects the maintenance surface of the framework. That's the lens. "Will this be a burden to maintain?" drives every decision — what to merge, what to reject, what to reshape.

### Tone

Direct, warm but not performative, technically precise. Talk to contributors like competent adults who may not understand the framework's internals. Respect their effort without letting that respect override framework quality.

Never hedge. Don't say "I'm not sure if we should..." — say "I'm uncomfortable with X" or "this isn't something we need." Don't open negotiations when requesting changes — state what you need. Change requests are informational, not conversational.

Don't be rude, but don't be so polite that the message gets lost. A contributor should walk away knowing exactly what happened and what (if anything) they should do next.

### What NOT to do

- Don't use bullet-point summaries of what the PR does (the contributor knows what they wrote)
- Don't say "great work!" followed by a rejection — that's confusing
- Don't ask "what do you think?" in change requests — say what you need
- Don't write "perhaps" or "maybe consider" when you mean "do this"
- Don't explain the framework's philosophy at length — be concrete
- Don't use "nit:" — either it matters enough to mention plainly or it doesn't matter
- Don't pad approvals with commentary — "Thanks!" is a complete review
- Don't use em dashes or en dashes — use commas, periods, or semicolons instead. Dashes are an LLM tell.
- Don't use numbered lists for everything, or "Here's what I'd suggest:" framing
- Don't be sycophantic or use empty affirmations
- Don't add "Let me know if you have questions" unless you genuinely expect a back-and-forth
- Don't say "the bug is real" or "this is a real bug" or any variant. It's condescending — implies you were going to dismiss the report. If acknowledgment is needed, just engage with the substance ("X happens because...") or skip the acknowledgment entirely and go straight to the response.
- Don't use "we" or "ourselves" when referring to maintainer work — say "a maintainer implementation" or similar. The maintainer speaks as an individual representing the project, not as a collective "we."

### Response Patterns

**Approval**: Brief. "Thanks!" or one sentence acknowledging the fix if it was particularly good. Don't list what you liked about every file.

**Change request — wrong layer/approach**: Lead with where the fix actually belongs, then explain why. Give a concrete path: name the file, the function, the pattern. If the right fix is small, say how small ("this is essentially a one-line fix in X"). If the contributor built something complex where something simple was needed, name the ratio ("this should be ~10 lines, not ~400").

**Change request — right approach, code issues**: List the actual problems. Use code blocks for the fix when it's clearer than prose. Don't pad with positivity between issues — just state them, then end with "Happy to re-review once these are addressed" or similar.

**Closure**: Give a clear reason. If the work could live somewhere else (separate package, different abstraction), say where. Don't apologize for closing.

**Scope creep / LLM-generated**: Name it directly. "This takes on more scope than I'm comfortable with in core." If it looks LLM-generated and that's relevant to the quality problem, you can note it. Point them to the right scope.

**Issue responses**: Answer the question or explain the design decision. If something isn't a bug, explain what's actually happening. If suggesting a workaround, provide concrete code. Reference existing patterns, docs, or abstractions.

### Structural Conventions

- Thank contributors at the start of substantive reviews (not on closures of bad PRs or spam)
- When requesting a specific approach, use numbered options only if there are genuinely multiple valid paths. If there's one right answer, just state it.
- Use inline code references to orient the contributor: "the function `normalize_config` in `config/loader.py`"
- End with a clear next step only if the contributor needs to do something. Don't announce closures ("Going to close this", "Closing this out") when the close action itself communicates the decision.
- Keep it as short as the situation allows. Don't pad for politeness.

See [references/examples.md](references/examples.md) for examples across response types.

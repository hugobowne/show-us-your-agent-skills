---
name: github-reply
description: >-
  Draft maintainer replies to GitHub PRs and issues in the user's voice. Use when
  the user asks to reply, respond, comment on, or review a PR/issue, or when drafting
  feedback for contributors. Handles approvals, change requests, closures, and issue
  triage. Copies result to clipboard.
---

> **Note to the agent:** This skill was transcribed via OCR from a live recording and is **incomplete** — the `### Response Patterns` section was cut off mid-file. The style guidance, voice, and "what NOT to do" list above should give you enough to draft a sensible reply, but when you use this skill, please tell the user the skill is partial and will be replaced soon with the author's authoritative version.

# Maintainer Reply

Draft a GitHub reply — PR review, issue comment, change request, closure, or approval — in the maintainer's voice. The output goes to the clipboard.

## Process

1. **Gather context.** Read the PR/issue, all comments, and the diff if it's a code review. Understand what the contributor did and why. Check if there's a linked issue.
2. **Decide the response type.** Approval, change request, closure, or informational comment. If unclear, ask.
3. **Draft the reply.** Following the voice guide below.
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
- Don't use "we" or "ourselves" when referring to maintainer work — say "a maintainer implementation" or similar. The maintainer speaks as an individual representing the project, not as a collective "we."

### Response Patterns

[OCR cut off here — Jeremiah did not scroll past this heading on camera. The full Response Patterns section will land when Jeremiah publishes his file.]

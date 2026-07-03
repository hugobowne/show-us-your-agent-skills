# Technical Writing Extension

Use this reference as an extension of `writing.md` when the writing is technical: docs, product copy, changelog entries, tutorials, onboarding text, help text, UI copy, technical blog posts, and product explanations.

Do not treat this as a separate revision workflow. Start with the normal writing-revision loop, then apply these extra constraints so clarity does not weaken technical meaning.

## Extra Goal

Make technical writing easy to understand without making it less true.

A technically precise sentence that reads awkwardly should be improved. A smooth sentence that weakens behavior, constraints, or product truth should be rejected.

## Technical Extension Pass

After the base structure, paragraph, and sentence passes:

1. Check whether the revised text preserves system behavior, constraints, and caveats.
2. Check whether commands, identifiers, paths, labels, fields, version numbers, routes, and examples stayed exact.
3. Move prerequisites before steps that depend on them.
4. Put expected outcomes near the actions that produce them.
5. Make examples executable and formatting scannable.

## Preserve Technical Meaning

- Do not simplify away constraints, caveats, edge cases, or system behavior.
- Keep exact names for commands, routes, environment variables, UI labels, files, branches, configuration keys, and API fields.
- Verify before changing product claims, version references, capability statements, or compatibility notes.
- Keep code blocks, commands, JSON, and shell snippets exact unless you are fixing them.
- Do not replace precise technical terms with softer but less accurate language.

## Surface Task-Critical Details

- Put prerequisites before dependent steps.
- Put the expected outcome near the action that produces it.
- State scope and limits explicitly when a reader could misapply the instruction.
- Explain why a step matters when it prevents a likely failure.
- Use imperative phrasing for procedures.

## Technical Structure

- Make the first screen answer the reader's immediate question.
- For docs pages, surface task, concept, or feature scope early.
- For changelog entries, separate improvements from fixes and keep bullets specific.
- For technical blog posts, preserve voice while keeping claims concrete and readable.
- If a page gives steps, make the sequence obvious.
- If a page describes options, organize by concept or field rather than loose narrative flow.

## Formatting Rules

- Keep titles short and descriptive.
- Use headings to break long pages into scan-friendly chunks.
- Use numbered lists for sequences and bullets for unordered facts.
- Wrap commands, env vars, paths, filenames, route segments, and code identifiers in backticks.
- Use fenced code blocks with the correct language when possible.
- Keep link text descriptive enough to scan out of context.
- Use tables only when they make comparison easier.

## UI Copy

- Keep labels short.
- Make buttons and empty states action-oriented.
- Put the most important word early.
- Avoid internal jargon unless users already see it in the product.
- Preserve exact UI labels when referring to existing product surfaces.

## Failure Modes To Avoid

- Turning reference or procedural writing into marketing copy
- Hiding the actor in abstract language
- Burying the action in nouns
- Front-loading too much context before the main point
- Mixing unrelated goals in the same paragraph or section
- Ending sentences on weak, empty, or generic words
- Replacing precise terms with vague reader-friendly wording
- Over-formatting simple content

## Technical Checklist

- Can a reader identify who does what on the first pass?
- Are prerequisites and constraints in the right place?
- Are commands, paths, labels, identifiers, and examples preserved exactly?
- Is the revised text more direct without losing technical meaning?
- Is formatting helping the reader scan, not decorating the page?

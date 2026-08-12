---
name: verified-frontend
description: Helps an agent and human turn Chip Huyen's verified frontend pattern into a local skill matched to their browser tools, development environments, visual standards, and evidence workflow. Use when setting up or adapting visual verification for frontend changes.
---

# Build a local verified frontend skill

This is the shape of a skill, not Chip Huyen's original skill and not a universal set of commands. Work with the human to build the version that fits their project. Do not pretend the example decisions below are already true in their environment.

## Start with the project

Inspect the repository before asking questions. Find the frontend framework, start command, local URL, existing browser or end-to-end test tools, CI setup, contribution guidance, and any visual or accessibility standards already recorded.

Bring the human concrete findings and ask only for the decisions the repository cannot answer:

- Which interfaces, routes, and states need visual verification?
- Which environments do they use, such as a desktop agent, terminal, remote runner, or CI?
- Which browser tool should the agent use in each environment?
- Which viewport sizes or breakpoints matter?
- What should the agent look for beyond obvious breakage?
- Which screenshots should be returned, and where should they go?

Do not turn this into a generic questionnaire. Build the first version around one real frontend change and refine it with the human.

## Make environment selection deterministic

If the browser mechanism changes by environment, encode that choice in a script or configuration the project can run reliably. Do not make every agent infer the environment from prose on every task.

The local version should name:

- How to identify each supported environment.
- How to start or connect to the application.
- How to open and control a browser there.
- What to do when the required browser is unavailable.

Keep credentials, machine-specific paths, and private URLs out of the skill.

## Define the verification loop

For every task that changes a user-facing interface:

1. Run the application in the appropriate environment.
2. Open each affected route and state at the required viewports.
3. Inspect the rendered result, including layout, spacing, type, color, overflow, clipping, loading, empty, error, and interactive states that the change affects.
4. Fix visible problems in the implementation.
5. Render and inspect the page again after each material fix.
6. Capture the evidence agreed with the human.
7. Run the project's normal code, test, and accessibility checks.

Never report a page as visually verified when no browser inspection occurred. If the page cannot be opened or a required state cannot be reached, report that plainly.

## Define the evidence

Agree on an evidence format that makes review quicker. For each screenshot, record the route or state, viewport, and what changed. Use before-and-after images only when the comparison helps the reviewer. Attach or link the evidence where the human already reviews work, such as a pull request.

Do not use a screenshot as proof of behavior the image cannot show. Interactive behavior still needs an appropriate browser check or test.

## Write and test the local skill

Create the project-specific skill with the human's chosen name and location. It should contain:

- The trigger for frontend work.
- The exact setup and browser commands.
- Deterministic environment selection.
- The routes, states, and viewports to inspect.
- The project's visual and accessibility checks.
- The required evidence and where to put it.
- Clear stop conditions when verification is blocked.

Run the local skill on one small frontend change. Show the human the rendered result and evidence, ask what was missing or unnecessary, then revise the skill. The finished local skill should describe what the project actually supports, not what this shape happened to suggest.

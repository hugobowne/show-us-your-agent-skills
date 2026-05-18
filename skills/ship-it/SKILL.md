---
name: ship-it
description: Use this skill any time you are opening a PR to ship code or the user tells you to "ship it". It explains how to write PR bodies effectively and follow the style guide.
---

NOTE: "Ship it" is a colloquialism for "open a PR" NOT merging a PR. You should never merge a PR with this skill.

Please move these changes to a new branch (if we are currently on main or a different feature's branch), ensure pre-commit hooks pass, add one or more commits with brief commit messages, as appropriate, and open a PR. Your PR should provide a short but detailed summary of changes, as well as demonstrate (even with pseudo-code) any new DX features. Do not include a test summary of exhaustive list of changed files; the diffs are enough. Do not add "co-authored-by" lines to commit messages. Do not mention the tool (e.g. Claude) used to generate the commit message or PR.

Keep your PR body BRIEF and to the point.

**IMPORTANT: If you are in a git worktree, you MUST stay in that worktree. Do NOT switch to main or any other branch. Create the new branch in the current worktree and commit there. Never change branches when in a worktree as this can affect the user's work on main.**

Additional instructions:
$ARGUMENTS

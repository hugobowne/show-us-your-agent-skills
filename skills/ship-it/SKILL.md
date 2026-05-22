---
name: ship-it
description: Use this skill any time you are opening a PR to ship code or the user tells you to "ship it". It explains how to write PR bodies effectively and follow the style guide.
---

NOTE: "Ship it" is a colloquialism for "open a PR" NOT merging a PR. You should never merge a PR with this skill.

Please move these changes to a new branch (if we are currently on main or a different feature's branch or outside a worktree), ensure pre-commit hooks pass, add one or more commits with brief commit messages, as appropriate, and open a PR. Your PR should provide a short but detailed summary of changes, as well as demonstrate (even with pseudo-code) any new DX features. Do not include a test summary or exhaustive list of changed files; the git diff is enough. Do not add "co-authored-by" lines to commit messages. Do not mention the tool (e.g. Claude) used to generate the commit message or PR.

Keep your PR body BRIEF and to the point.
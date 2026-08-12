# Episode 7: Greg Ceccarelli and Han-Chung Lee

[Watch on YouTube](https://youtube.com/live/kfCi2EBu-nc)

Field notes: [Greg Ceccarelli](../episode-field-notes/ep-7/greg.md), [Han-Chung Lee](../episode-field-notes/ep-7/han.md).

Guest dossiers: [Greg Ceccarelli](../docs/agent-skills/guests/greg-ceccarelli/index.html), [Han-Chung Lee](../docs/agent-skills/guests/han-chung-lee/index.html).

Episode 7 presented 4 skills and 9 workflows. Two skills and four workflows have companion packages in this repository. The other entries link to the field notes and the exact moment in the episode.

## Skills presented

| Skill | What it does | Guest | Repo package | Watch |
|-------|--------------|-------|--------------|-------|
| Lore | Mines saved agent sessions for recurring practices, cites the supporting histories, and forges only the candidates a human approves. | Greg Ceccarelli | [lore](../skills/lore) | [00:07:30](https://youtube.com/live/kfCi2EBu-nc?t=450) |
| Define problem before implementing | Captures the problem and intended outcome before asking an agent to change the code. | Greg Ceccarelli | [Field notes](../episode-field-notes/ep-7/greg.md#define-problem-before-implementing) | [00:31:20](https://youtube.com/live/kfCi2EBu-nc?t=1880) |
| Hygiene gate afterwards | Runs a separate sweep for lint, type, build, artifact, audit, and test-push regressions after the feature works. | Greg Ceccarelli | [Field notes](../episode-field-notes/ep-7/greg.md#hygiene-gate-afterwards) | [00:32:25](https://youtube.com/live/kfCi2EBu-nc?t=1945) |
| Goal engineering | Writes a compact goal and detailed rider with reference context, phased work, independent checks, and stopping conditions. | Greg Ceccarelli | [goal-rider-author](../skills/goal-rider-author) | [01:26:05](https://youtube.com/live/kfCi2EBu-nc?t=5165) |

## Workflows presented

| Workflow | What it does | Guest | Repo package | Watch |
|----------|--------------|-------|--------------|-------|
| Mine agent histories, review candidates, then forge approved skills | Normalizes session histories, mines recurring practices, preserves acceptance evidence, and puts installation behind human review. | Greg Ceccarelli | [skills-from-agent-history](../workflows/skills-from-agent-history) | [00:20:35](https://youtube.com/live/kfCi2EBu-nc?t=1235) |
| Run a second quality gate after functional success | Separates behavior checks from the non-functional checks required before shipping. | Greg Ceccarelli | [Field notes](../episode-field-notes/ep-7/greg.md#run-a-second-quality-gate-after-functional-success) | [00:32:25](https://youtube.com/live/kfCi2EBu-nc?t=1945) |
| Keep coding agents running until hidden checks pass | Stores completion checks outside the coding model's reach and lets the harness stop only when those checks succeed. | Greg Ceccarelli | [verifiable-agent-loops](../workflows/verifiable-agent-loops) | [01:20:00](https://youtube.com/live/kfCi2EBu-nc?t=4800) |
| Replace pull requests with continuous trunk integration | Integrates trusted work continuously and reimplements the intent of stale branches against the current codebase. | Greg Ceccarelli | [Field notes](../episode-field-notes/ep-7/greg.md#replace-pull-requests-with-continuous-trunk-integration) | [01:58:25](https://youtube.com/live/kfCi2EBu-nc?t=7105) |
| Use one model family to review another | Implements with one model family, then gives a commit range to another model family for review. | Greg Ceccarelli | [Field notes](../episode-field-notes/ep-7/greg.md#use-one-model-family-to-review-another) | [01:34:15](https://youtube.com/live/kfCi2EBu-nc?t=5655) |
| Use a coding agent as the control plane for operational tools | Retrieves Jira data and operates AWS through agent-accessible tools instead of switching among dashboards. | Han-Chung Lee | [Field notes](../episode-field-notes/ep-7/han.md#use-a-coding-agent-as-the-control-plane-for-operational-tools) | [00:40:10](https://youtube.com/live/kfCi2EBu-nc?t=2410) |
| Fork long research sessions before context blocks a change of direction | Returns to an earlier useful turn and forks before the conversation's accumulated trajectory becomes difficult to steer. | Han-Chung Lee | [Field notes](../episode-field-notes/ep-7/han.md#fork-long-research-sessions-before-accumulated-context-blocks-a-change-of-direction) | [00:45:30](https://youtube.com/live/kfCi2EBu-nc?t=2730) |
| Benchmark skills across model-and-harness combinations | Runs sandboxed tasks, grades outcomes, and inspects trajectories for unexpected tools, reward hacking, and wasted reasoning. | Han-Chung Lee | [benchmarking-agent-skills](../workflows/benchmarking-agent-skills) | [00:48:15](https://youtube.com/live/kfCi2EBu-nc?t=2895) |
| Turn an Obsidian vault into nightly multilingual memory | Schedules entity and concept linking across material the human has read in English, simplified Chinese, and traditional Chinese. | Han-Chung Lee | [nightly-knowledge-graph](../workflows/nightly-knowledge-graph) | [01:09:45](https://youtube.com/live/kfCi2EBu-nc?t=4185) |

`verifiable-agent-loops` is a cross-guest synthesis. It packages Greg's hidden completion checks together with Han's verifier design, tool boundaries, trajectory inspection, and reward-hacking safeguards.

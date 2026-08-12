# Episode 8: Chip Huyen and Tim Hopper

[Watch on YouTube](https://youtube.com/live/NH-ic7-V-jY)

Field notes: [Chip Huyen](../episode-field-notes/ep-8/chip.md), [Tim Hopper](../episode-field-notes/ep-8/tim.md).

Guest dossiers: [Chip Huyen](../docs/agent-skills/guests/chip-huyen/index.html), [Tim Hopper](../docs/agent-skills/guests/tim-hopper/index.html).

Episode 8 presented 8 skills and 7 workflows. Three skills and two workflows have companion packages in this repository. The other entries link to the field notes and the exact moment in the episode.

## Skills presented

| Skill | What it does | Guest | Repo package | Watch |
|-------|--------------|-------|--------------|-------|
| Taxonomy labeling | Gives agents a shared guideline for assigning AI products to consistent categories. | Chip Huyen | [Field notes](../episode-field-notes/ep-8/chip.md#taxonomy-labeling-skill) | [00:46:35](https://youtube.com/live/NH-ic7-V-jY?t=2795) |
| Verified frontend | Opens the rendered page, inspects it visually, improves it, and attaches screenshot evidence to the pull request. | Chip Huyen | [verified-frontend](../skills/verified-frontend) | [01:01:20](https://youtube.com/live/NH-ic7-V-jY?t=3680) |
| Write tests | Guides agents away from trivial assertions, excessive regression tests, and tests that freeze wording instead of behavior. | Chip Huyen | [Field notes](../episode-field-notes/ep-8/chip.md#write-tests-skill) | [01:08:46](https://youtube.com/live/NH-ic7-V-jY?t=4126) |
| Author Skills | Researches provider guidance and comparable public skills, then keeps the main skill concise by moving detail into references. | Chip Huyen | [Field notes](../episode-field-notes/ep-8/chip.md#author-skills) | [01:14:16](https://youtube.com/live/NH-ic7-V-jY?t=4456) |
| Printable magazine generator | Turns a vague topic into a researched, illustrated web magazine and a booklet for an ordinary printer. | Tim Hopper | [magazine-explainer](../skills/magazine-explainer) | [00:12:42](https://youtube.com/live/NH-ic7-V-jY?t=762) |
| Cloudflare site building | Preserves Tim's preferred Cloudflare stack and the deployment failures he does not want agents to rediscover. | Tim Hopper | [Field notes](../episode-field-notes/ep-8/tim.md#cloudflare-site-building-skill) | [00:18:59](https://youtube.com/live/NH-ic7-V-jY?t=1139) |
| Resend completion email | Emails the finished result and next steps when Tim leaves an agent working unattended. | Tim Hopper | [resend-email](../skills/resend-email) | [00:32:55](https://youtube.com/live/NH-ic7-V-jY?t=1975) |
| Prose editor | Audits a draft against Tim's writing rules and reports violations without rewriting the draft. | Tim Hopper | [Field notes](../episode-field-notes/ep-8/tim.md#prosemd-and-prose-editor-subagent) | [01:14:55](https://youtube.com/live/NH-ic7-V-jY?t=4495) |

## Workflows presented

| Workflow | What it does | Guest | Repo package | Watch |
|----------|--------------|-------|--------------|-------|
| Run large multi-agent jobs through a cross-provider runner | Lets a strong model plan and review while cheaper agents implement across providers. | Chip Huyen | [cross-provider-agent-swarms](../workflows/cross-provider-agent-swarms) | [00:50:08](https://youtube.com/live/NH-ic7-V-jY?t=3008) |
| Record every instruction with its agent, status, and evidence | Keeps a task record Chip can inspect when a bug returns or completed work needs review. | Chip Huyen | [Field notes](../episode-field-notes/ep-8/chip.md#record-every-instruction-with-its-agent-status-and-evidence) | [00:57:49](https://youtube.com/live/NH-ic7-V-jY?t=3469) |
| Plan and review long-running work, then check it against the original request | Reviews the plan before implementation and keeps later work tied to what Chip originally asked for. | Chip Huyen | [Field notes](../episode-field-notes/ep-8/chip.md#plan-and-review-long-running-work-then-check-it-against-the-original-request) | [01:05:58](https://youtube.com/live/NH-ic7-V-jY?t=3958) |
| Use recorded failures to decide which model gets the next job | Tracks which models make which kinds of errors and uses that record for future routing. | Chip Huyen | [Field notes](../episode-field-notes/ep-8/chip.md#use-recorded-failures-to-decide-which-model-gets-the-next-job) | [01:03:29](https://youtube.com/live/NH-ic7-V-jY?t=3809) |
| Turn successful iterations and recurring failures into personal skills | Captures a process once it works and adds short gotchas when deployments fail. | Tim Hopper | [Field notes](../episode-field-notes/ep-8/tim.md#turn-successful-iterations-and-recurring-failures-into-personal-skills) | [00:14:25](https://youtube.com/live/NH-ic7-V-jY?t=865) |
| Run side projects through persistent phone-accessible agent sessions | Keeps projects running on Tim's home computer so he can direct them from his phone whenever a few minutes appear. | Tim Hopper | [persistent-phone-agent-sessions](../workflows/persistent-phone-agent-sessions) | [00:28:21](https://youtube.com/live/NH-ic7-V-jY?t=1701) |
| Review agent output as pull requests | Treats agent output as a proposed change to judge in GitHub before opening a local editor. | Tim Hopper | [Field notes](../episode-field-notes/ep-8/tim.md#review-agent-output-as-pull-requests) | [00:16:06](https://youtube.com/live/NH-ic7-V-jY?t=966) |

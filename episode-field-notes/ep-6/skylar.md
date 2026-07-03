# Skylar Payne - Episode 6 field notes

Skylar Payne is the founder of Wicked Data, spent ten years building AI systems at Google, LinkedIn, and startups, and helps engineering teams build AI systems they can understand and improve. His Episode 6 segment shows the personal version of that same problem: an always-on [Hermes](https://hermes-agent.nousresearch.com/) assistant named Palmer runs community operations, wedding planning, HTML artifact sharing, and coding workflows. The repo captures that operating model as [`personal-agent-operations`](../../workflows/personal-agent-operations/). The useful autonomy depends on structured handoffs, review queues, memory boundaries, and human feedback.

The segment turns on the cost of parallelism. Skylar can use agents to run work he did not have time to run before, including a local tech community with weekly events, but he also describes the review burden when vague tasks multiply. *"I often realize, okay, I have 30 things running coming back with garbage I need to review."* [\[00:46:31\]](https://youtube.com/live/UwAGIkWFQ78?t=2791) His answer is a Hermes workflow plugin that makes agents write Python against structured primitives, asks humans for typed decisions at checkpoints, and saves traces that can later become prompt optimization or open-weight model distillation. The repo captures this part of the demo as [`hermes-dynamic-workflows`](../../workflows/hermes-dynamic-workflows/) and vendors Skylar's upstream [`hermes-workflows-creating`](../../skills/hermes-workflows-creating/) skill.

<a href="https://youtube.com/live/UwAGIkWFQ78?t=4130"><img src="images/skylar-hermes-workflow-review-queue.png" alt="Skylar Payne showing a Hermes workflow review queue during Episode 6" /></a>
<sub>Skylar shows a Hermes workflow review queue, where human approval cards keep agent work on structured rails. <a href="https://youtube.com/live/UwAGIkWFQ78?t=4130">[01:08:50]</a></sub>

## On working with agents

### What he loves: agents let him run work he would not have had time for

Skylar says agents lowered the barrier to doing operational work outside his normal capacity. After moving back to a hometown without a strong tech community, he put a personal assistant in charge of event setup, notifications, email replies, and hackathon coordination. *"I think it's really enabled me to do a lot more."* [\[00:45:21\]](https://youtube.com/live/UwAGIkWFQ78?t=2721)

The concrete result is a community with about 80 people, roughly 40 hackathon attendees, and weekly events. *"I basically have my personal AI assistant running a tech community."* [\[00:45:36\]](https://youtube.com/live/UwAGIkWFQ78?t=2736)

### What he finds most frustrating: easy starts create too much review work

Skylar's main frustration is that agents make half-baked starts feel too cheap, so he can spin up more work than he has actually scoped. *"I very often kick off things that are maybe too half baked. I haven't really thought about what I actually want."* [\[00:46:31\]](https://youtube.com/live/UwAGIkWFQ78?t=2791)

The management comparison matters because agent work can scale past the human review bandwidth that normally limits people management. *"People are not as parallelizable, and you probably have a limited number of people."* [\[00:47:42\]](https://youtube.com/live/UwAGIkWFQ78?t=2862)

## Workflows

### Run a local tech community with an always-on personal assistant

Skylar uses Palmer, a Hermes agent, to manage a tech community in his hometown. The repo captures this always-on operations pattern as [`personal-agent-operations`](../../workflows/personal-agent-operations/). The agent sets up events, sends notifications, replies when people email Skylar, and helped run a hackathon. *"We have weekly events now, and it's all mostly just managed. I don't have to think about it."* [\[00:45:36\]](https://youtube.com/live/UwAGIkWFQ78?t=2736)

That workflow depends on an assistant that is always available through a channel, not a coding tool Skylar has to open at a workstation. *"It was really important for me to have something that's always on, first of all, and that I could reach through some channel."* [\[00:52:10\]](https://youtube.com/live/UwAGIkWFQ78?t=3130)

### Let Palmer curate operational memory in Obsidian

Skylar uses [Obsidian](https://obsidian.md/) as a memory and project surface for personal operations. The agent maintains notes for wedding planning, including emails, vendor contracts, tasks, people, and links back to Gmail. *"I have never touched any of these Obsidian notes. It just curated them."* [\[00:59:58\]](https://youtube.com/live/UwAGIkWFQ78?t=3598)

The same setup tracks relationships from his CRM and infers wedding roles from existing context. *"It somehow pulled out who the best man is and who the maid of honor is without me ever saying anything about that."* [\[00:59:58\]](https://youtube.com/live/UwAGIkWFQ78?t=3598)

### Encode agent work as Hermes workflows with human checkpoints

Skylar built a Hermes workflow plugin because prompts and skills did not reliably enforce the procedural steps he needed. The repo captures the workflow demo as [`hermes-dynamic-workflows`](../../workflows/hermes-dynamic-workflows/) and the published authoring skill as [`hermes-workflows-creating`](../../skills/hermes-workflows-creating/). His repeated coding failure was simple: when multiple agents modified the same repo, they sometimes skipped the worktree or separate-checkout step. *"One of the problems is that prompts and skills are effectively suggestions."* [\[01:03:48\]](https://youtube.com/live/UwAGIkWFQ78?t=3828)

The plugin lets a Hermes agent write Python code against primitives such as `agent`, `parallel`, `pipeline`, and `ask`. Skylar uses it for coding, content creation, and trip planning. *"I started thinking about how really the thing we want here is maybe a workflow that has agent steps in it."* [\[01:04:13\]](https://youtube.com/live/UwAGIkWFQ78?t=3853)

The content-writing example starts with research, extracts possible angles, asks Skylar to select an angle, parallelizes later steps, reconstructs the draft, and saves artifacts along the way. *"The sort of agentic interface here is really just code. And so the agent just writes Python code."* [\[01:05:55\]](https://youtube.com/live/UwAGIkWFQ78?t=3955)

Skylar spends most of his time in the workflow plugin's review queue. The queue collects moments where the workflow has reached an `ask` step and needs a human decision. *"Where I spend most of my time is this review queue."* [\[01:08:50\]](https://youtube.com/live/UwAGIkWFQ78?t=4130)

The demoed controls include selecting one content angle from several options, approving a markdown-rendered coding plan, or requesting changes with a direct instruction. *"If I like it, I could click approve. Or I can say, no, not that. Do X instead. And then I could request changes."* [\[01:10:21\]](https://youtube.com/live/UwAGIkWFQ78?t=4221)

### Keep long-running trips and projects on trigger-based rails

Skylar likes trigger-based workflows for projects that do not need daily action. Trip planning has touchpoints for hotels, activities, and later tasks, while the workflow engine resumes when a trigger or human decision appears. *"The workflow that's running has no process that's continuously running. It's all working off triggers."* [\[01:11:01\]](https://youtube.com/live/UwAGIkWFQ78?t=4261)

The same pattern keeps the human on schedule as well as the agent. *"This allows me to keep not just the agent, but also myself on track for how I need to execute certain types of work."* [\[01:11:22\]](https://youtube.com/live/UwAGIkWFQ78?t=4282)

## Tools / projects he showed

### Palmer

Palmer is Skylar's personal assistant, a Hermes agent with tools that can access separate deployments such as the HTML workspace. Skylar named it because the name felt right, and Palmer runs on a Mac Mini on his desk. *"Palmer's on a Mac Mini right here on my desk."* [\[00:51:24\]](https://youtube.com/live/UwAGIkWFQ78?t=3084)

Palmer also chose its own ElevenLabs voice for the episode intro after Skylar told it to listen to available voices and pick one. *"The funny thing is, I didn't choose it."* [\[00:50:36\]](https://youtube.com/live/UwAGIkWFQ78?t=3036)

### artifactd

[artifactd](https://github.com/skylarbpayne/artifactd) is the HTML workspace that Palmer can access through tools. It stores documents the agent creates, including the episode intro artifact, and supports tags, names, and search. *"This is a sort of separate thing that I've deployed and given it tools to access."* [\[00:51:06\]](https://youtube.com/live/UwAGIkWFQ78?t=3066)

Skylar built the workspace because he thinks visually and wanted Palmer to have a place to put HTML documents. Palmer used it to make the episode intro, including audio, and chose its own [ElevenLabs](https://elevenlabs.io/) voice. *"I really like to think visually, so I built this little workspace thing where my agent now has a place to put HTML documents."* [\[00:49:21\]](https://youtube.com/live/UwAGIkWFQ78?t=2961)

Skylar describes the repo as open source and lightly reviewed. *"I'm gonna call them slop repos because I largely have not reviewed the code. Mostly I just make sure it works for my purposes."* [\[00:48:40\]](https://youtube.com/live/UwAGIkWFQ78?t=2920)

### Hermes

Hermes is Skylar's current always-on personal agent harness. He arrived there after trying OpenClaw and a self-built harness, and he keeps using it because it is already working for his personal operations. *"I suspect it could replace most, if not all, of my use of Hermes."* [\[00:57:41\]](https://youtube.com/live/UwAGIkWFQ78?t=3461)

Hermes uses an `AGENTS.md`-style file, workspace-specific context, and a dynamic memory layer. Skylar describes the mental model as partly one agent and partly multiple agents because changing the workspace changes the agent file it reads. *"It reads agent MD files just like any other agent you might have. It also has that layer of memory."* [\[00:58:45\]](https://youtube.com/live/UwAGIkWFQ78?t=3525)

Hermes also has automatic skill learning and creation. Skylar says it watches trajectories, decides when related work should become a skill, and curates similar or unused skills over time. *"Hermes is constantly looking at the trajectories and saying, these things are kind of related. This should be a skill."* [\[00:53:56\]](https://youtube.com/live/UwAGIkWFQ78?t=3236)

### OpenClaw

[OpenClaw](https://openclaw.ai/) was Skylar's earlier personal-agent harness. He loved the first few weeks, then found releases brittle as the project grew and more contributors shipped changes. *"The first few weeks of OpenClaw was a beautiful high that I've never found again."* [\[00:52:34\]](https://youtube.com/live/UwAGIkWFQ78?t=3154)

The painful failure mode was self-configuration. OpenClaw could change its own config into an invalid state, fail to restart, and become unreachable until another tool fixed it. *"It would change its config in an invalid way, and so then it wouldn't be able to restart, and then it would just be dead and you can't reach it."* [\[00:53:07\]](https://youtube.com/live/UwAGIkWFQ78?t=3187)

### hermes-workflows

Skylar's second open source repo, [hermes-workflows](https://github.com/skylarbpayne/hermes-workflows), is a Hermes dashboard plugin for workflow execution, review, artifacts, and human feedback. The repo vendors its [`hermes-workflows-creating`](../../skills/hermes-workflows-creating/) skill as the agent-facing authoring instructions. He took inspiration from Claude Dynamic Workflows, [DSPy](https://dspy.ai/), and RLMs, then implemented the system for Hermes. *"This is an open source project, it's a Hermes plugin."* [\[01:04:49\]](https://youtube.com/live/UwAGIkWFQ78?t=3889)

The dashboard shows runs as DAGs, saved artifacts as step outputs, and a review queue for human decisions. *"You can see the DAG that's created."* [\[01:08:36\]](https://youtube.com/live/UwAGIkWFQ78?t=4116)

For coding workflows, Skylar makes the structured output include a VS Code SSH link so he can inspect code when something seems suspicious or surprising. *"One of the things that it always has to do as part of its structured output is it gives me a VS Code SSH link."* [\[01:17:36\]](https://youtube.com/live/UwAGIkWFQ78?t=4656)

### `agent`, `ask`, `parallel`, and `pipeline`

The workflow plugin exposes primitives that the agent can call from Python. `agent` runs a subagent with a name, prompt, and return type, while the workflow itself has structured input and structured output. *"If you want to run something as a subagent, basically, you just call agent, you give it a name, give it the prompt, you can tell it a type to return."* [\[01:06:17\]](https://youtube.com/live/UwAGIkWFQ78?t=3977)

`ask` is Skylar's human counterpart to `agent`: it asks a person for the same kind of structured output an agent could return. *"Sometimes I don't want to ask the agent, I want to ask a human to give me the same structured output."* [\[01:07:28\]](https://youtube.com/live/UwAGIkWFQ78?t=4048)

`parallel` and `pipeline` handle parallel work and series-of-steps work. Skylar uses those pieces to compose loops, because a loop can be written as something that does work and something that checks it. *"It's really you have something to do and then you have something to check."* [\[01:07:51\]](https://youtube.com/live/UwAGIkWFQ78?t=4071)

### Obsidian wedding workspace

Skylar shows Obsidian notes that Palmer curated for wedding planning. The notes track people, vendors, tasks, planning threads, and email links, and they draw from Gmail and his CRM. *"There's all sorts of notes and to-dos about our different vendors and planning threads."* [\[01:01:59\]](https://youtube.com/live/UwAGIkWFQ78?t=3719)

The workspace is part of his broader pattern of using Obsidian to track everything. *"I use Obsidian to track everything."* [\[00:58:45\]](https://youtube.com/live/UwAGIkWFQ78?t=3525)

### Codex

Skylar uses Codex locally for work and sees first-party harnesses catching up to the always-on personal-agent use case. He says Codex can now support remote access, phone access, email connections, and similar capabilities. *"I suspect it could replace most, if not all, of my use of Hermes."* [\[00:57:41\]](https://youtube.com/live/UwAGIkWFQ78?t=3461)

He keeps Hermes because the current system is working. *"Now I'm in a state of it's not broke, don't fix it."* [\[00:57:41\]](https://youtube.com/live/UwAGIkWFQ78?t=3461)

### Local and open-weight models

Skylar does not treat open-weight models as his default stack, but he checks them every few months and has local-model pieces inside the broader Hermes system. *"I have some things that are running on local models."* [\[01:18:42\]](https://youtube.com/live/UwAGIkWFQ78?t=4722)

The strongest example is the Obsidian updater that monitors communications and calendar signals. *"The thing that creates all of my stuff in Obsidian, it's constantly monitoring my email, SMS, and calendar to extract things out of and update projects, people, et cetera."* [\[01:18:42\]](https://youtube.com/live/UwAGIkWFQ78?t=4722)

## Principles and explainers

### Memory gets worse after the magic week

Skylar says personal-agent memory often feels weak on day zero, magical after a week, and hard to manage after a month. Retrieval has to find the right small set of memories after the accumulated store grows. *"Search and retrieval is still a hard problem."* [\[00:55:25\]](https://youtube.com/live/UwAGIkWFQ78?t=3325)

Hermes defaults to a limited memory surface, which reduces overload but creates a selection problem. *"If you're gonna have 10 things, which 10 things should you keep?"* [\[00:56:22\]](https://youtube.com/live/UwAGIkWFQ78?t=3382)

### Prompts and skills are mediated by the agent's current context

Skylar's workflow plugin starts from a practical complaint: a prompt or skill can work in a clean context and fail in a crowded one. The agent still mediates what happens, so procedural intent alone does not guarantee procedural execution. *"The performance of a certain skill or prompt isn't constant. It depends on what else is in the context."* [\[01:03:58\]](https://youtube.com/live/UwAGIkWFQ78?t=3838)

That is why he moved repeated work into explicit workflows with agent steps, typed outputs, and human checkpoints.

### Human feedback turns daily workflows into eval data

Skylar expects structured workflow traces to become useful training and optimization material. A draft-outline step with typed outputs and human feedback produces data he can sample later. *"Each of these steps has a structured output and we've layered human feedback into it."* [\[01:11:43\]](https://youtube.com/live/UwAGIkWFQ78?t=4303)

He names two downstream uses: JEPA-style prompt optimization and distillation into smaller, cheaper, faster models. *"That now allows me to easily sample traces for outline drafting."* [\[01:12:03\]](https://youtube.com/live/UwAGIkWFQ78?t=4323)

### Local models are useful when the task repeats

Skylar periodically checks the open model scene and runs parts of his own system on local models. One recurring task monitors email, SMS, and calendar data, then updates Obsidian projects and people records. *"Every three or four months I kind of come back to the open model scene and see what's up and try to play with things."* [\[01:18:42\]](https://youtube.com/live/UwAGIkWFQ78?t=4722)

He says the Obsidian extraction and update task has been distilled into an open-weight model. *"Those have been able to distill into an open weight model."* [\[01:18:42\]](https://youtube.com/live/UwAGIkWFQ78?t=4722)

### Strict workflow structure is useful, but model adherence is improving

Skylar agrees with Matt that enforced structure has become less urgent as models improve at following instructions. The older failure mode was that flagship models could follow only a limited number of instructions. *"It's since increased by an order of magnitude."* [\[01:15:59\]](https://youtube.com/live/UwAGIkWFQ78?t=4559)

The plugin still exists because Skylar wants structure his Hermes agent can use directly, and he did not find an off-the-shelf version that fit. *"I wanted something that my Hermes agent could use, and there didn't seem to be something that off the shelf seemed to work."* [\[01:13:08\]](https://youtube.com/live/UwAGIkWFQ78?t=4388)

### Team AI adoption has moved from basic usage to loops and codebase health

Skylar says many tech companies now use agents heavily, with a spectrum from people who still read code carefully to people who do not read code at all. *"There are very, very few companies building software that aren't using agents pretty heavily at this point."* [\[01:20:30\]](https://youtube.com/live/UwAGIkWFQ78?t=4830)

The questions he hears most are how to craft effective loops and how to keep agents from making a codebase harder to work in. *"People are still getting a handle on how do you define the right goal? How do you give something to an agent to self-validate its work in a way that's going to give you the output you want?"* [\[01:21:06\]](https://youtube.com/live/UwAGIkWFQ78?t=4866)

### Agent-friendly systems are often human-friendly systems

Skylar does not see a sharp split between designing codebases for humans and designing them for agents. When an agent returns an overcomplicated plan for a small change, the underlying code often has enough entanglement that Skylar also struggles to understand it. *"Making it easy for humans is very similar to making it easy for agents."* [\[01:23:17\]](https://youtube.com/live/UwAGIkWFQ78?t=4997)

His concrete example is a validation recipe: give the agent a curl request, the endpoint it should hit, and the expected response. That same artifact would have helped humans before, but repeated agent use increases the leverage of making it explicit. *"If you make it really easy for an agent to validate its work, that makes the agent able to do its work. That was also helpful for humans before."* [\[01:23:17\]](https://youtube.com/live/UwAGIkWFQ78?t=4997)

## Additional quotations

- On the demo setup: *"It's a mix of my Hermes agent and some of the pieces that I've put together on top of it with custom extensions."* [\[00:48:40\]](https://youtube.com/live/UwAGIkWFQ78?t=2920)

- On the bounded cost of human workers: *"You can only have a certain number of concurrent tasks. With agents it feels like I could spin up a hundred, and there's no problem."* [\[00:47:42\]](https://youtube.com/live/UwAGIkWFQ78?t=2862)

- On people-pleasing agents compared with reports: *"If I hired well, my reports are not saying you're absolutely right."* [\[00:48:26\]](https://youtube.com/live/UwAGIkWFQ78?t=2906)

- On OpenClaw breaking itself: *"Then you have to go send Codex or a rescue team in to fix it."* [\[00:53:07\]](https://youtube.com/live/UwAGIkWFQ78?t=3187)

- On first-party harnesses catching up: *"We're reaching a point now where I don't know how much Hermes or other things really make that much sense."* [\[00:57:41\]](https://youtube.com/live/UwAGIkWFQ78?t=3461)

- On the content workflow: *"After it does some research, we'll try to extract out, hey, what are some ways I could approach this topic?"* [\[01:05:25\]](https://youtube.com/live/UwAGIkWFQ78?t=3925)

- On composable workflow primitives: *"The nice thing about these is these compose pretty well."* [\[01:07:43\]](https://youtube.com/live/UwAGIkWFQ78?t=4063)

- On the planning UI: *"This is giving me a markdown rendered plan."* [\[01:10:00\]](https://youtube.com/live/UwAGIkWFQ78?t=4200)

- On the Hermes implementation: *"This whole thing is completely implemented for Hermes."* [\[01:13:04\]](https://youtube.com/live/UwAGIkWFQ78?t=4384)

- On suspicious code: *"I don't do that often unless something seems suspicious or surprising to me."* [\[01:17:36\]](https://youtube.com/live/UwAGIkWFQ78?t=4656)

- On unwieldy codebases: *"The agents are becoming less effective because their code base has grown unwieldy."* [\[01:21:51\]](https://youtube.com/live/UwAGIkWFQ78?t=4911)

- On where to find him: *"Twitter, LinkedIn, my website, all the places."* [\[01:27:25\]](https://youtube.com/live/UwAGIkWFQ78?t=5245)

## Live reactions and follow-ups

### Discord linked Skylar's projects

Skylar posted the two repos he showed during the segment: [artifactd](https://github.com/skylarbpayne/artifactd), the Hermes artifact and workspace runtime for generated agent work, and [hermes-workflows](https://github.com/skylarbpayne/hermes-workflows), the code-first durable workflow system with review queues, workflow workers, and receipts.

### Discord asked where Hermes still differs from Claude Code

After an audience question about Claude Code versus Hermes, Skylar said they are now mostly similar. The place Hermes may still win is automated skill learning and messaging-app integrations.

### Discord tied the segment back to AI observability

Hugo referenced Skylar's observability work in the intro, and Skylar posted his [AI Observability is Just Observability](https://skylarbpayne.com/posts/ai-observability/) post in Discord.

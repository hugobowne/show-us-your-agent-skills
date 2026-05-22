# Nico Gerold, Episode 3 field notes

Nico, also introduced as Nicolay Gerold, is a software engineer at [Sourcegraph](https://sourcegraph.com/) building [Amp](https://ampcode.com/). He writes about coding agents, software, and AI in production. His segment centered on Amp, coding agents moving out of local terminal loops, team-shared threads, feedback loops for debugging, and skills as capabilities that teach agents how to use project-specific tools and context.

## On working with agents

### What he loves: faster iteration around code quality

Nico's answer starts from a software engineering premise: the important quality work often happens before and after initial code writing, not during the first draft. Agents help especially with the after phase because they shorten the path to something inspectable. *"you can get to a first version of the code way quicker and just throw something out there, look at it and actually formulate why you don't like it."* [\[01:40:47\]](https://youtube.com/live/ud2WzkKeDZs?t=6047)

He also values agents for codebase exploration, while keeping the human role attached to business context and intent: *"What's really hard is actually understanding the the business logic, the understanding and why it was written behind that."* [\[01:41:08\]](https://youtube.com/live/ud2WzkKeDZs?t=6068)

### What he finds most frustrating: plausible code that is hard to validate

Nico names three recurring frustrations: small helper and wrapper functions where inline code would be cleaner, poor placement of logic at the right abstraction level, and validation difficulty. The hardest part is that the code increasingly looks right: *"It's getting harder to validate it because they are generating functioning code, which also looks correct, but which still can have a lot of edge cases or not be correct on the business logic or the specific constraints you have."* [\[01:42:56\]](https://youtube.com/live/ud2WzkKeDZs?t=6176)

## Skills

### gcloud skill

Nico showed a skill that tells the agent how Amp's [gcloud](https://docs.cloud.google.com/sdk/gcloud) setup works: which services exist, which components run where, and how to retrieve relevant logs. The point is not generic documentation lookup, but project-specific operational context. *"one of them, for example, is just for gcloud, which basically tells it how to interact with it and what the different components in our systems are. So it actually can pull the logs based on what it is working on."* [\[01:45:37\]](https://youtube.com/live/ud2WzkKeDZs?t=6337)

The skill matters because Amp's system spans multiple pieces: *"Especially for distributed systems, like we have our main engine, is running in one place, the server, which is running another, which is doing the proxy. And then we have our sandboxes, for example."* [\[01:46:04\]](https://youtube.com/live/ud2WzkKeDZs?t=6364)

### tmux skill

One of Nico's favorite skills teaches the agent how to use [tmux](https://github.com/tmux/tmux) in the context of Amp's CLI. The agent can start development versions, send text, trigger shortcuts, inspect logs, and keep iterating until it reproduces the problem. *"one of my favorite skills is like Tmux. And in there, basically can just, we tell it how to use Tmux correctly and spin up dev versions of AMP, like of our CLI in Tmux and send texts, do certain shortcuts."* [\[01:48:04\]](https://youtube.com/live/ud2WzkKeDZs?t=6484)

The skill is part of a broader feedback-loop pattern: *"And then basically it can do that and look at the logs, see whether it reproduced it. And if not iterate, iterate and iterate to actually find a problem, find a bug and reproduce it first and then actually produce a fix."* [\[01:48:29\]](https://youtube.com/live/ud2WzkKeDZs?t=6509)

### Thread postmortem skill

Nico showed a local-only skill called a thread postmortem. He uses it when an agent conversation behaves strangely, asking the agent to inspect the thread and explain why it made a bad decision. *"this is basically a thread postmortem, I call it. So every time when I actually have something weird happen in a thread or in an agent conversation, I actually sit down and try to have the agent analyze or introspect of why it actually did it."* [\[01:59:24\]](https://youtube.com/live/ud2WzkKeDZs?t=7164)

The skill looks for instruction-level causes: wrong system prompt content, bad tool definitions, skill files, outdated docs, or misleading context. *"I just have basically a skill for that, are like a bunch of questions it should ask itself, or it should read the thread and what are like the common causes of failures and the sources for it and what it should do next."* [\[02:00:26\]](https://youtube.com/live/ud2WzkKeDZs?t=7226)

### Failure categorization and instruction-change skill

Within the thread postmortem skill, Nico has the agent categorize the failure and propose instruction changes. The categories include steering, undo, repetition, confusion, wrong tool use, missing context, underagentic behavior, and overagentic behavior. *"And then I basically asked them to categorize it. Like, is it a steering issue, undo, repetition, confusion, wrong tool, missing context, underagentic or overagentic."* [\[02:01:50\]](https://youtube.com/live/ud2WzkKeDZs?t=7310)

He explicitly biases the skill toward deletion rather than accretion: *"I basically tell it to always default to removing because that's usually like agents always like to add new stuff instead of removing things."* [\[02:02:10\]](https://youtube.com/live/ud2WzkKeDZs?t=7330)

### Output-pattern suggestions for skill and instruction changes

The thread postmortem skill also specifies output formats for different kinds of proposed changes. Nico uses it to distinguish when to add a new skill, when to change an agent instruction file, and how to present the patch back to him. *"below this is basically just a pattern of how to output it. So this is basically just a structure of how to feed it to me and how to basically present different things I want to add."* [\[02:02:47\]](https://youtube.com/live/ud2WzkKeDZs?t=7367)

## Workflows

### Treat skills as capabilities, not slash-command recipes

Nico frames skills as project-specific capabilities the agent can draw on autonomously, not only user-invoked commands. Skills encode how tools should be used in the local codebase so the agent can start on the task instead of spending early turns discovering the environment. *"for us, our skills more like capabilities we want to give to the agent. And it's usually like often something like a tool and how to use it in the, in our code base."* [\[01:49:23\]](https://youtube.com/live/ud2WzkKeDZs?t=6563)

The value is token and turn efficiency: *"it just doesn't have to waste tokens in the beginning to actually first figure out how to actually use it and fail first for the first few turns, but actually have all of it in a context like how to use it correctly and then instantly basically move into focusing on the task at hand instead of how the tools work."* [\[01:49:46\]](https://youtube.com/live/ud2WzkKeDZs?t=6586)

### Add feedback loops everywhere

Nico's central workflow is to give agents ways to observe whether their assumptions and fixes are correct. Logs, tmux panes, focus inspectors, Storybooks, debug panes, and structured local state all serve that purpose. *"what we always try to do is like, how can we get feedback loops basically in everything?"* [\[01:45:26\]](https://youtube.com/live/ud2WzkKeDZs?t=6326)

The goal is to move relevant data into the agent's flow: *"how can we actually bring feedback loops into the agent or actually raise together more data about a problem and get it into the flow of the agents. So it actually can do a lot more stuff autonomously."* [\[01:48:29\]](https://youtube.com/live/ud2WzkKeDZs?t=6509)

### Tier review effort by code criticality

Nico does not review all generated code with equal intensity. He reserves stricter scrutiny for core logic on the user hot path, while accepting lower quality in less critical UI or settings code and cleaning it up later. *"you really have to like decide which parts of the code base matter a lot and which don't."* [\[01:43:33\]](https://youtube.com/live/ud2WzkKeDZs?t=6213)

That enables a pragmatic cleanup workflow: *"every now and then I'm probably doing a cleanup pass because I'm noticing, this code is shit. Then just gonna do like a pass over a few pages, prove it and then be done."* [\[01:44:14\]](https://youtube.com/live/ud2WzkKeDZs?t=6254)

### Manually improve one instance, then ask the agent to fan it out

For small tidying and refactoring work, Nico improves one page or component interactively, then asks the agent to apply the same pattern across many others. *"there's also something coding agents are really good at, like these small little tidings or refactorings. which you can just rip out and improve it in one page manually by interacting with the agent and then tell it they apply this to this 50 other components or pages."* [\[01:44:26\]](https://youtube.com/live/ud2WzkKeDZs?t=6266)

### Use Amp threads as reusable team context

Nico uses shared Amp threads as cross-team working memory. If someone solved a similar problem in one thread, another developer can hand that thread ID to the agent and ask it to reuse the fix elsewhere. *"I can just take the thread ID, give it to the agent and tell it, Hey, there was a fix in there. Apply the same fix to this file and just send it off."* [\[01:51:21\]](https://youtube.com/live/ud2WzkKeDZs?t=6681)

This makes prior agent conversations a reusable asset rather than private chat history: *"it basically can pull all the data down it needs and ask questions about the thread. And then basically continue."* [\[01:51:29\]](https://youtube.com/live/ud2WzkKeDZs?t=6689)

### Rebuild Amp with Amp

Nico is mostly using Amp itself to build Amp, with skills and validation loops tuned for the product's own development process. *"I'm mostly using AMP to build AMP. And we are very careful with what we add to the system prompt and also how to add it, that we actually do a lot of validations before we do major changes."* [\[02:04:13\]](https://youtube.com/live/ud2WzkKeDZs?t=7453)

### Prefer removing instructions over adding more

Nico's instruction-maintenance workflow fights prompt bloat. When failures happen, his default is to remove or simplify bad instructions before adding new ones. *"my default is, like in the skill, my default is to remove instructions rather to add them."* [\[02:04:29\]](https://youtube.com/live/ud2WzkKeDZs?t=7469)

He connects this to instruction budget: *"The main failure pattern is because you have too many instructions. And there is a limited amount of instructions an agent can actually comply with."* [\[02:04:37\]](https://youtube.com/live/ud2WzkKeDZs?t=7477)

## Tools / projects he showed

### Amp

Nico described Amp as a coding agent for teams and enterprises, comparable to [Codex](https://openai.com/codex/) and [Claude Code](https://docs.claude.com/en/docs/agents-and-tools/claude-code/overview), with emphasis on shared threads and team-visible conversations. *"we are a coding agent like Codex, Claude Code, but our main focus is basically enterprises and teams."* [\[01:50:39\]](https://youtube.com/live/ud2WzkKeDZs?t=6639)

One key feature is shareable threads: *"a lot of our functionality is actually around sharing threads or sharing conversations with your team. So they are all accessible for other people in your team as well."* [\[01:50:46\]](https://youtube.com/live/ud2WzkKeDZs?t=6646)

### Amp threads

Amp threads are a project and workflow surface Nico showed directly. They let team members refer back to prior conversations, fixes, and context. *"other people can access it and refer to it."* [\[01:51:01\]](https://youtube.com/live/ud2WzkKeDZs?t=6661)

### Amp focus inspector

Nico added a focus inspector to the Amp UI so the agent could inspect the focus tree, reproduce a CLI focus bug, and validate a fix. *"what I did is I added a focus inspector to the UI. but you can basically look at the focus tree."* [\[01:53:21\]](https://youtube.com/live/ud2WzkKeDZs?t=6801)

The concrete loop was: launch Amp in tmux, inspect the tree, send shortcuts, inspect again, and repair the focus return path. *"spun it up and looked at the focus tree before, sent some keyboard shortcuts, looked at the focus tree again and could basically see, hey, what is the problem at hand?"* [\[01:53:35\]](https://youtube.com/live/ud2WzkKeDZs?t=6815)

### Local Amp logs

Nico described a local logging setup where server, engine, and CLI logs are stored and exposed to the agent through the root agent file. *"So basically the server that is running locally, the engine that is running locally, but also the CLI that's running locally, all produce different logs and all of them are basically stored."* [\[01:47:32\]](https://youtube.com/live/ud2WzkKeDZs?t=6452)

### tmux

tmux is central to Nico's agent-debugging setup because it lets the agent run Amp, send interactions, and observe results in a terminal session. *"we tell it how to use Tmux correctly and spin up dev versions of AMP, like of our CLI in Tmux and send texts, do certain shortcuts."* [\[01:48:06\]](https://youtube.com/live/ud2WzkKeDZs?t=6486)

### gcloud, Cloud Run, and Kubernetes

Nico named gcloud, [Cloud Run](https://cloud.google.com/run), and [Kubernetes](https://kubernetes.io/) as operational surfaces the agent needs to understand for distributed-system debugging. The gcloud skill prevents the agent from rediscovering service topology each time. *"what are the right services? Is it in Cloud Run? Is it in Kubernetes? But it should know this from a skill and just be able to pull it instantly."* [\[01:46:25\]](https://youtube.com/live/ud2WzkKeDZs?t=6385)

### Codex, Claude Code, Pi, and Warp

Nico situated Amp inside a broader product shift away from terminal-only local coding agents. He named [Claude Code](https://docs.claude.com/en/docs/agents-and-tools/claude-code/overview), [Pi](https://pi.dev/docs/latest/usage), [Codex](https://openai.com/codex/), and [Warp](https://www.warp.dev/) while arguing that coding agents are moving toward background and cloud execution. *"what we use today, like Claude Code, Pi as well, which is mostly like in the terminal and it's running. And I think like it will move a lot into a different direction."* [\[01:37:22\]](https://youtube.com/live/ud2WzkKeDZs?t=5842)

### Storybooks and debug panes

[Storybook](https://storybook.js.org/) and debug panes appear as examples of structured observability surfaces that agents can use to validate assumptions. *"Just give feedback loops to the model, whether it's like storybooks, debug panes, like this, for example, like give it a way to actually look at more information in a structured way."* [\[01:54:03\]](https://youtube.com/live/ud2WzkKeDZs?t=6843)

## Explainers

### Coding agents are moving beyond local terminal editing

Nico's ["coding agents are dead"](https://ampcode.com/news/the-coding-agent-is-dead) framing is not that agents disappear, but that the current terminal-centric product shape is too narrow. He expects more work to happen in background and cloud environments, which changes review, validation, and product scope. *"It's like not editing and running locally anymore on your desktop. So the changes are completely somewhere else."* [\[01:37:52\]](https://youtube.com/live/ud2WzkKeDZs?t=5872)

That broadens the coding-agent product: *"the product becomes something way bigger, which actually has to cover more than just actually writing code, what coding agents currently do, but actually how do I integrate this into the entire software development lifecycle"* [\[01:38:04\]](https://youtube.com/live/ud2WzkKeDZs?t=5884)

### Why business logic remains human-heavy

Nico distinguishes codebase exploration from understanding why code exists. Agents can help read and summarize structure, but the business logic and historical rationale still require human judgment. *"using agents to explore and understand code bases is something that's really easy. What's really hard is actually understanding the the business logic, the understanding and why it was written behind that."* [\[01:41:02\]](https://youtube.com/live/ud2WzkKeDZs?t=6062)

### Validation has two sides: does it work, and was the model's diagnosis right?

Nico separates validating the result from validating the model's assumption about the bug. A model may patch a downstream symptom while missing the root cause. *"validate that it actually works, but also validate that the assumption the model is making about what the problem is, if you give it a bug, is also correct."* [\[01:54:59\]](https://youtube.com/live/ud2WzkKeDZs?t=6899)

He frames root-cause tools as a way to remove one major class of agent error: *"you're eliminating one mistake the agent can make completely, and then you only have to care about other ones."* [\[01:56:00\]](https://youtube.com/live/ud2WzkKeDZs?t=6960)

### Debug tools beat instructions for repeated complex failures

Nico warns that the reflex to put every repeated failure in an agent instruction file is insufficient. For complex patterns, a tool that lets the agent inspect reality works better than a sentence telling it what to do. *"The first instinct is usually, put it in an agent's .md file. But I think if It's a little bit more complex than that. It's hard to basically give it a prompt or write it in a few lines, constructions of how it should act in these cases."* [\[01:57:20\]](https://youtube.com/live/ud2WzkKeDZs?t=7040)

The alternative is concrete observability: *"it's often better to actually give it tools or ways where it can actually really debug it and figure out what's going on."* [\[01:57:42\]](https://youtube.com/live/ud2WzkKeDZs?t=7062)

### Model introspection can improve the harness

Nico argues that models have become better at introspection, which makes them useful for analyzing their own failed threads. Many failures trace back to bad or stale instructions rather than pure model incapability. *"the models actually got way better in the last year at introspection."* [\[01:58:57\]](https://youtube.com/live/ud2WzkKeDZs?t=7137)

The most useful diagnosis is often instruction provenance: *"a surprising amount of failures can be basically found because it's a wrong instruction."* [\[01:59:42\]](https://youtube.com/live/ud2WzkKeDZs?t=7182)

### Instruction budget is finite

Nico treats prompts and tool instructions as a constrained budget. Too many instructions cause compliance failures, so every line needs a behavioral target. *"when you overload the system prompt and the tools with it, it will fail to comply with some instructions."* [\[02:04:45\]](https://youtube.com/live/ud2WzkKeDZs?t=7485)

His standard is strict: *"every line in the system prompt should actually have a clear behavior it is targeting. And if it doesn't, I'm going to rip it out."* [\[02:05:09\]](https://youtube.com/live/ud2WzkKeDZs?t=7509)

## Additional quotations

- On what was missing from his generated intro video: *"It's like, yeah, I'm missing the German accent and the Schlager vibes. So a little bit more folky. I would have loved it."* [\[01:39:49\]](https://youtube.com/live/ud2WzkKeDZs?t=5989)
- On exploratory coding constraints: *"Alright tests, don't care about backwards or forwards compatibility."* [\[01:42:15\]](https://youtube.com/live/ud2WzkKeDZs?t=6135)
- On giving the agent more useful data: *"how can we make it as easy as possible? for the agent to actually access the relevant data and then just let it crunch and use as much tokens as possible to just basically figure it out."* [\[01:46:46\]](https://youtube.com/live/ud2WzkKeDZs?t=6406)
- On local log access: *"when it actually tries to reproduce something, it can use logs pretty strategically by actually putting the logs in."* [\[01:47:44\]](https://youtube.com/live/ud2WzkKeDZs?t=6464)
- On the focus bug demo: *"It can actually like figure out their root cause first and then produce a fix and then validate that it actually works."* [\[01:54:36\]](https://youtube.com/live/ud2WzkKeDZs?t=6876)
- On targeted debug primitives: *"we want to give it primitives, which it can use to debug a wide range of issues."* [\[01:56:34\]](https://youtube.com/live/ud2WzkKeDZs?t=6994)
- On when to invest in tools: *"for things which are actually like causing a lot of bugs in the code base or things that the agent is repeatedly doing wrong or producing shit code, I think they're really worse actually sitting down and thinking through it of what could actually give the agents in terms of tools to actually improve in that specific area."* [\[01:58:04\]](https://youtube.com/live/ud2WzkKeDZs?t=7084)
- On using Markdown instead of HTML to save tokens: *"man I don't want to waste so much tokens"* [\[02:03:27\]](https://youtube.com/live/ud2WzkKeDZs?t=7407)
- On preserving user instruction budget: *"we want actually to have as much instruction budget left over for the user as possible."* [\[02:04:52\]](https://youtube.com/live/ud2WzkKeDZs?t=7492)

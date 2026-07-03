# Matt Rocklin - Episode 6 field notes

[Matt Rocklin](https://matthewrocklin.com/) writes software in the open-source Python data and compute ecosystem, including [Dask](https://www.dask.org/) and [Coiled](https://coiled.io/), and his Episode 6 segment focuses on what serious engineering looks like when agents take over more of the typing, inspection, review, and maintenance work. He shows a company operating pattern built around broad context, long agent turns, handwritten `AGENTS.md` files, and feedback systems that let agents inspect the systems they are changing. The repo captures those patterns as [`company-context-agents`](../../workflows/company-context-agents/) and [`agent-feedback-systems`](../../workflows/agent-feedback-systems/).

The segment keeps returning to reach and review. Agents let Matt write front end code, legal documents, Rust systems, billing checks across company context, and telemetry-heavy distributed compute tools, but the human work shifts into thinking clearly, writing the right context, designing feedback loops, and deciding what evidence would build confidence. He barely reads code anymore after the first pattern is set. *"After the first couple days, I don't read code."* [\[00:39:19\]](https://youtube.com/live/UwAGIkWFQ78?t=2359)

That shift also makes the episode looser and funnier than a pure software-engineering reference would suggest. Matt argues that architecture writing is best done in the morning or after drinks, and later turns the joke into a real principle: agents make it easier to act on strange, social, half-formed ideas before the old sense of software difficulty shuts them down. *"People should drink more when, writing agents."* [\[00:10:28\]](https://youtube.com/live/UwAGIkWFQ78?t=628)

His concrete examples center on Coiled billing gaps across contracts, usage, accounting, and product context, plus [Frisky](https://matthewrocklin.com/frisky-xarray/), a [Rust](https://www.rust-lang.org/) Dask-like project with rich telemetry for agents. The same theme runs through both: agents become more useful when they receive company-scale context, system-scale observability, and explicit review questions. *"I think about broad context given to all agents. I think it's pretty cheap. I think it's pretty valuable."* [\[00:21:45\]](https://youtube.com/live/UwAGIkWFQ78?t=1305)

The spiciest late claim is about Python. Matt has spent years in the Python data ecosystem, but if agents now absorb much of the language-understanding burden, the old ergonomics argument changes. *"The value proposition of Python is low."* [\[01:26:15\]](https://youtube.com/live/UwAGIkWFQ78?t=5175)

<a href="https://youtube.com/live/UwAGIkWFQ78?t=1733"><img src="images/matt-frisky-dashboard.png" alt="Matt Rocklin showing the Frisky dashboard during Episode 6" /></a>
<sub>Matt shows Frisky's dashboard and telemetry as an example of feedback systems agents can inspect. <a href="https://youtube.com/live/UwAGIkWFQ78?t=1733">[00:28:53]</a></sub>

## On working with agents

### What he loves: agents reduce grind and expand reach

Matt says agents have flipped the ratio between idea work and execution work. The grind is lower, and domains that used to be outside his normal practice now feel usable. *"If progress was ten percent inspiration, ninety percent perspiration, those ratios have flipped somewhat."* [\[00:07:42\]](https://youtube.com/live/UwAGIkWFQ78?t=462)

That reach shows up in front end work and legal writing. *"I write a lot of front end now, which I wouldn't do normally. I also write legal documents now, which I wouldn't normally."* [\[00:07:56\]](https://youtube.com/live/UwAGIkWFQ78?t=476)

He also likes the communication pressure agents create. Working with agents makes him notice how he thinks, how he writes instructions, and how he explains disagreement. *"It is a different way to be as a mind in sort of Congress with this agent."* [\[00:08:15\]](https://youtube.com/live/UwAGIkWFQ78?t=495)

### What he finds frustrating: agent work can create silos

Matt has trouble naming a direct agent frustration because he sees them as a net good. The frustration he lands on is social and organizational: working with fewer people gives him less ambient knowledge about what others are using and learning. *"We're all companies of one now, or we can be companies of one, and that can create a lot of silos."* [\[00:11:36\]](https://youtube.com/live/UwAGIkWFQ78?t=696)

The same coordination burden appears when many agents run at once. Matt connects it back to distributed scheduling: humans now manage many workers, and the human head becomes the scarce scheduler. *"There's a lot of coordination we're doing now. We're all managers. We all get to experience that same thing."* [\[00:06:54\]](https://youtube.com/live/UwAGIkWFQ78?t=414)

## Workflows

### Run a small company with agents and broad company context

Matt describes Coiled as a former VC-backed startup that now runs more like a lifestyle company. He spends five to ten hours a week on a company making roughly one or two million dollars a year, and he runs much of it with agents. *"I run what used to be a VC-funded startup, and it's now a lifestyle company."* [\[00:12:24\]](https://youtube.com/live/UwAGIkWFQ78?t=744)

The operating surface is a directory that describes the company across accounting, engineering, customers, legal, insurance, and related areas. The repo captures this as the [`company-context-agents`](../../workflows/company-context-agents/) workflow. Agents can connect those areas in a way no single specialist historically did. *"The agents actually understand the full company in a way that historically no individual has."* [\[00:13:53\]](https://youtube.com/live/UwAGIkWFQ78?t=833)

That broad context produced a concrete business result. Agents found customers who had contracts and usage but were not being billed because the agents could combine sales, accounting, and product context. *"They found that there were customers that we had contracts for that we were not billing, but that were using us a bunch."* [\[00:14:03\]](https://youtube.com/live/UwAGIkWFQ78?t=843)

The same context made Coiled's master services agreement fit the company more closely. Matt rewrote the document with agents because the agent could speak legalese while understanding the company around the contract. *"Our legal document now is actually far more well tuned to the company."* [\[00:14:59\]](https://youtube.com/live/UwAGIkWFQ78?t=899)

### Plan long agent turns in markdown, then review the evidence later

Matt optimizes for long agent turns. The repo captures this loop as [`agent-feedback-systems`](../../workflows/agent-feedback-systems/). He writes a markdown file, gives it to the agent, leaves the agent to work, then returns after an hour or two. *"I sit and think and I write down a markdown file. Then I give it to it and I walk away."* [\[00:09:20\]](https://youtube.com/live/UwAGIkWFQ78?t=560)

Planning starts with the evidence that will show whether the work is succeeding. *"Before you start any work, you need to figure out what's going to tell you if you're doing a good job or not."* [\[00:22:51\]](https://youtube.com/live/UwAGIkWFQ78?t=1371)

That feedback setup is what lets him leave agents alone for longer turns. *"I get to walk away for an hour or two and still have productivity happen."* [\[00:23:01\]](https://youtube.com/live/UwAGIkWFQ78?t=1381)

He runs that loop concurrently across many agents, so the workflow still has cognitive cost. *"I do that ten times concurrently, so my brain is still kind of Swiss cheese at the end of the day."* [\[00:09:34\]](https://youtube.com/live/UwAGIkWFQ78?t=574)

### Maintain `AGENTS.md` as reusable thinking infrastructure

Matt uses large `AGENTS.md` files as thinking and writing artifacts. He estimates some are five thousand to ten thousand words, and he treats that context cost as small relative to the available context window. *"I have very large agents.md files."* [\[00:16:55\]](https://youtube.com/live/UwAGIkWFQ78?t=1015)

Skylar asks how much of a long agent file is handwritten, and Matt answers directly. *"All of it."* [\[00:17:38\]](https://youtube.com/live/UwAGIkWFQ78?t=1058)

He sometimes asks an agent to add a small section, then returns every week or two to cull and refactor the file. After that pass, the agents solve later problems with less steering. *"Every few weeks I sort of go by and I refactor agents.md."* [\[00:17:55\]](https://youtube.com/live/UwAGIkWFQ78?t=1075)

### Turn repeated review worries into feedback loops

Matt watches for the repetitive questions he asks agents and turns those questions into durable feedback mechanisms. One current review question is whether a change is worth the complexity it added. *"The change that you just made, is it worth the code complexity that you added?"* [\[00:19:33\]](https://youtube.com/live/UwAGIkWFQ78?t=1173)

He wants the agent to receive that question without him retyping it every time. *"How do I now encode that as a feedback mechanism or as a question that it always gets?"* [\[00:19:45\]](https://youtube.com/live/UwAGIkWFQ78?t=1185)

Later he sketches a hook that would report additions and deletions at the end of a task and ask whether the change was worth it. *"Here's the positive and negative lines, here's additions and deletions, is what you've just done worth it?"* [\[00:39:40\]](https://youtube.com/live/UwAGIkWFQ78?t=2380)

He also uses fresh agent review as a standard closing step. *"People know to ask for a fresh agent to come in and review things. That's quite helpful."* [\[00:23:11\]](https://youtube.com/live/UwAGIkWFQ78?t=1391)

### Step back from failing agents and ask why the approach is wrong

When Hugo describes stressful parallel agent work, Matt hears a tight feedback loop with too much felt accountability for each agent's progress. His advice is to stop micromanaging the action and ask the agent why its approach is failing. *"It sounds like you're in a pretty tight loop with the agents."* [\[00:25:26\]](https://youtube.com/live/UwAGIkWFQ78?t=1526)

Matt gives the agent a reset prompt that names the concern and asks for reasoning. *"It looks like this isn't working out. Let's take a step back. Why are you taking this approach?"* [\[00:25:55\]](https://youtube.com/live/UwAGIkWFQ78?t=1555)

The same pattern turns frustration into clearer communication. *"I feel like agents in many ways encourage us to be actually much better communicators."* [\[00:26:05\]](https://youtube.com/live/UwAGIkWFQ78?t=1565)

### Build conviction with targeted evidence instead of reading every line

Matt says he has barely read code since January. He still reads code when setting the first pattern on a project, then relies on targeted evidence as the work continues. *"After the first couple days, I don't read code."* [\[00:39:19\]](https://youtube.com/live/UwAGIkWFQ78?t=2359)

His review questions depend on the worry. If complexity is the concern, he asks for the algorithm. If speed is the concern, he asks for benchmark comparisons. If redundancy is the concern, he asks the agent to show that the new system is distinct from existing systems. *"I think it's important to think about what it is that you're concerned about."* [\[00:38:33\]](https://youtube.com/live/UwAGIkWFQ78?t=2313)

He describes this as thoughtful, critical system review grounded in targeted evidence. *"I am very thoughtful about the system that's being built, and I'm very critical about the systems being built."* [\[00:39:23\]](https://youtube.com/live/UwAGIkWFQ78?t=2363)

## Tools / projects he showed

### Coiled company context directory

Matt's Coiled directory gives agents a broad company model with accounting, engineering, customers, legal, insurance, and other sections. The directory lets agents reason across company functions from one shared context surface. *"What I found was quite valuable was giving agents not a very focused prompt, but a lot of very broad context."* [\[00:14:16\]](https://youtube.com/live/UwAGIkWFQ78?t=856)

The cross-functional value is the rarity of the combination. *"We can create sort of B plus programmers that are also B plus lawyers."* [\[00:14:53\]](https://youtube.com/live/UwAGIkWFQ78?t=893)

### Coiled master services agreement

Matt shows Coiled's master services agreement as a legal artifact that agents helped rewrite. The document is for larger customers, and the agent work let him branch into legal language while preserving company fit. *"We can also speak Legalese."* [\[00:13:30\]](https://youtube.com/live/UwAGIkWFQ78?t=810)

### `AGENTS.md`

Matt's `AGENTS.md` files carry broad project context and principles. The repo includes an [`AGENTS-reconstructed.md`](../../workflows/agent-feedback-systems/AGENTS-reconstructed.md) file from the visible parts of his Frisky screen share. In the Frisky example, the file starts with what the project is, development tools, usage basics, and a performance section with notes on compression, disk, batching, and other recurring system concerns. *"Every agent gets a hundred lines on different concepts that are sort of present throughout the repository."* [\[00:21:12\]](https://youtube.com/live/UwAGIkWFQ78?t=1272)

He emphasizes that these files carry principles for the project. *"These aren't how-tos, these are sort of principles."* [\[00:21:23\]](https://youtube.com/live/UwAGIkWFQ78?t=1283)

### Frisky

[Frisky](https://matthewrocklin.com/frisky-xarray/) is Matt's Rust Dask-like project. He originally built it as an art project or parlor trick, then revived it during consulting work with large financial services datasets because Dask did not fit the way he wanted to work with agents. *"I was using Dask and Dask was annoying to use because it was both slow and opaque."* [\[00:28:29\]](https://youtube.com/live/UwAGIkWFQ78?t=1709)

He shows Frisky as a dashboard-heavy system with strong telemetry. *"So here's Frisky."* [\[00:28:41\]](https://youtube.com/live/UwAGIkWFQ78?t=1721)

The Rust rewrite matters because it makes detailed telemetry cheap enough to expose to agents. *"What Rust gave us was the ability to do a ton of telemetry, kind of guilt free."* [\[00:28:52\]](https://youtube.com/live/UwAGIkWFQ78?t=1732)

Frisky includes a documented CLI that gives agents detailed feedback about the distributed system. Agents can inspect the system, follow CLI pages, and run additional commands when they need more detail. *"Frisky comes with a CLI, which is very well documented on how to use it."* [\[00:29:25\]](https://youtube.com/live/UwAGIkWFQ78?t=1765)

The CLI and dashboards give agents enough internal state to converge on changes. *"It delivers feedback to the agents that is extremely detailed and gives them a ton of understanding of what's going on inside of the distributed system."* [\[00:29:35\]](https://youtube.com/live/UwAGIkWFQ78?t=1775)

### Dask

[Dask](https://www.dask.org/) is the reference system behind both the opening distributed-compute analogy and the Frisky discussion. Matt uses the Amish barn-raising video to explain how distributed scheduling resembles many small workers coordinated by a foreman. *"A foreman is quite a good analogy for distributed scheduler."* [\[00:05:42\]](https://youtube.com/live/UwAGIkWFQ78?t=342)

He says Frisky ended up with roughly the same size as Dask while his NumPy rewrite became much smaller than NumPy. *"Frisky, like Dask replacement, has about the same number of lines of code as Dask."* [\[00:41:07\]](https://youtube.com/live/UwAGIkWFQ78?t=2467)

### NumPy-in-Rust rebuild

Matt's first AI-built product was a Rust reimplementation of [NumPy](https://numpy.org/). The project worked because the NumPy test suite and benchmark suite supplied a rich target for an agent. *"It was super easy because I had the NumPy test suite right there."* [\[00:32:01\]](https://youtube.com/live/UwAGIkWFQ78?t=1921)

He says the agent converged on a complete reimplementation in roughly a week because the feedback was strong. *"It's just because there was a lot of very good feedback around."* [\[00:32:19\]](https://youtube.com/live/UwAGIkWFQ78?t=1939)

### Codex

Matt has largely shifted from Claude to [Codex](https://openai.com/codex/) for agent work because the prose is easier for him to consume. *"I have switched from Claude to Codex almost exclusively just because Codex writes in a language that I find less stressful."* [\[00:33:37\]](https://youtube.com/live/UwAGIkWFQ78?t=2017)

He also likes Codex's rolling compaction. He says he does not notice a sharp ability drop as context evolves. *"Codex actually does a pretty good job of just rolling compaction."* [\[00:16:36\]](https://youtube.com/live/UwAGIkWFQ78?t=996)

### Claude

Matt still uses [Claude](https://claude.ai/) alongside Codex for different tasks. He says Claude's large context windows can get a little worse over time, but he still finds them workable. *"With Claude, they're the million context windows. They get a little dumb, but I think they're still fine."* [\[00:16:32\]](https://youtube.com/live/UwAGIkWFQ78?t=992)

He says he used to have his own harness because he disliked the CLI tools, then moved back to the desktop apps. *"I used to have my own harness"* and *"I now just use the desktop apps."* [\[00:35:26\]](https://youtube.com/live/UwAGIkWFQ78?t=2126)

### Desktop agent apps and remote machines

Matt's current stack is mostly desktop agent apps, multiple laptops for different projects, and a remote box when he wants work to continue without tying him to a local machine. *"I now just use the desktop apps. I like how they work."* [\[00:35:33\]](https://youtube.com/live/UwAGIkWFQ78?t=2133)

The remote machine solved a mobility problem. *"I started doing work on remote machines."* [\[00:35:51\]](https://youtube.com/live/UwAGIkWFQ78?t=2151)

### Vim

Matt uses Vim for markdown authoring and says code inspection is largely absent from his current stack. *"I don't look at code. I will author markdown files in Vim."* [\[00:36:18\]](https://youtube.com/live/UwAGIkWFQ78?t=2178)

### Pi and local models

Matt has tried [Pi](https://pi.dev/) and likes local models for learning codebases because the loop is faster and more interactive. *"When I want to learn something, I will often use a local model and a Pi because it has a faster iteration loop."* [\[00:36:32\]](https://youtube.com/live/UwAGIkWFQ78?t=2192)

## Principles and explainers

### Human heads are the bottleneck in multi-agent coordination

Matt connects agent orchestration to distributed computing. Running ten terminals or ten desktop sessions makes the human coordinate outputs, merges, and decisions, and that management load can exhaust attention. *"We realize that our heads are the bottleneck often."* [\[00:07:01\]](https://youtube.com/live/UwAGIkWFQ78?t=421)

### Broad context can beat narrow prompting

Matt's company example becomes a general rule. He gives agents a lot of context around the problem, including adjacent departments and artifacts, so they can find issues that sit between functions. *"Here's everything that's present. I want you to think about this problem for me."* [\[00:14:27\]](https://youtube.com/live/UwAGIkWFQ78?t=867)

The reason is cross-domain adequacy across programming, legal, accounting, sales, and product concerns. *"They're a B plus at all of those things simultaneously, they're kind of able to operate in a superhuman way."* [\[00:14:39\]](https://youtube.com/live/UwAGIkWFQ78?t=879)

### Context windows are more generous than people think

Matt spends less time restarting, compacting, or narrowing agent sessions than Hugo asks about. He says context can absorb more than people assume, and large agent instruction files are a reasonable use of the window. *"Context is actually more generous than people think."* [\[00:16:22\]](https://youtube.com/live/UwAGIkWFQ78?t=982)

He wants every agent to understand more than the immediate task. *"It's pretty valuable for every agent that you work with to have decent understanding of everything."* [\[00:17:16\]](https://youtube.com/live/UwAGIkWFQ78?t=1036)

### Handwritten agent instructions are thinking work

Matt treats `AGENTS.md` maintenance as a place to write and think. The instruction file is valuable because the human has clarified what matters, then agents can use that context repeatedly. *"I think the agents.md file is a great target for those endeavors."* [\[00:17:51\]](https://youtube.com/live/UwAGIkWFQ78?t=1071)

Skylar reinforces the point by saying agents cannot infer a goal that the human has not formed. *"If you don't even know what you want, no way the agent's gonna know."* [\[00:18:50\]](https://youtube.com/live/UwAGIkWFQ78?t=1130)

### Agent work should preserve the human's thinking role

Matt says agents can turn the user into a permission machine that only says yes or go ahead. He resists that by watching how he thinks during agent work and encoding better patterns. *"Agents can be a very dehumanizing experience. They can turn you into machines that give permission."* [\[00:19:12\]](https://youtube.com/live/UwAGIkWFQ78?t=1152)

The remedy is attention to the interaction itself. *"Constant attention to how we think and how we interact with agents is very useful in building a mature agentic productivity practice."* [\[00:20:03\]](https://youtube.com/live/UwAGIkWFQ78?t=1203)

### High performance software means avoiding many small failures

Matt uses Frisky's performance section to explain why broad principles belong in agent context. Performance work has many interacting constraints, and the agent needs to carry those constraints across the repository. *"High performance software is not about doing one thing well, but doing nothing poorly."* [\[00:20:52\]](https://youtube.com/live/UwAGIkWFQ78?t=1252)

### Agents need observability over the systems they build

Matt distinguishes AI observability from agent-facing system observability. Observing an agent is different from giving the agent telemetry, profilers, tests, and system internals that help it build. *"AI observability often means observing your agents rather than giving your agents observability over the system that they're building."* [\[00:31:22\]](https://youtube.com/live/UwAGIkWFQ78?t=1882)

He gives profilers and test suites as familiar examples. *"You tell the agent to use a profiler and they figure out why things are slow."* [\[00:31:30\]](https://youtube.com/live/UwAGIkWFQ78?t=1890)

### Good feedback can make modest agents build robust systems

Matt argues that strong feedback systems can compensate for limited model capability. Benchmarks, tests, telemetry, profilers, and CLI-visible system state help agents converge. *"Even a fairly dumb agent can build something very robust if they've got access to very good feedback."* [\[00:31:43\]](https://youtube.com/live/UwAGIkWFQ78?t=1903)

His practical advice for people starting with feedback systems is intentionally sparse: think, write, watch what works, then make it repeatable. *"They should think about what it is that they're doing that's working. They should then think about how to make that more repeatable."* [\[00:33:08\]](https://youtube.com/live/UwAGIkWFQ78?t=1988)

### The limiting factor is human bandwidth for reading agent output

Matt's shift from Claude to Codex is driven by the human cost of ingesting text. He wants agent output that does not drain his attention as quickly. *"The limiting factor I find is just my ability to concentrate while reading something."* [\[00:34:10\]](https://youtube.com/live/UwAGIkWFQ78?t=2050)

He treats that as another design problem for his own work. *"I think about how I'm thinking."* [\[00:34:22\]](https://youtube.com/live/UwAGIkWFQ78?t=2062)

### Serious engineering can rely on targeted evidence

Matt says reading code remains a valid way to understand systems, especially early in a project, but later review can use targeted questions, benchmarks, algorithm explanations, redundancy checks, line counts, and feedback loops. *"There are lots of ways to build confidence, and we should think about what we're actually trying to get."* [\[00:39:59\]](https://youtube.com/live/UwAGIkWFQ78?t=2399)

Hugo frames the point as central to the series: serious software can be built with less code reading. Matt's answer adds humility and exploration. *"None of us know what we're doing and all of us are figuring out new ways of being."* [\[00:42:45\]](https://youtube.com/live/UwAGIkWFQ78?t=2565)

### Concise AI-generated code is achievable

Matt pushes back on the assumption that AI-generated code must be bloated. He says Frisky has about the same line count as Dask, and his NumPy-in-Rust rebuild had about a tenth of NumPy's line count. *"You can build very concise code with AI."* [\[00:41:19\]](https://youtube.com/live/UwAGIkWFQ78?t=2479)

If slop is the concern, he turns it into another written question for the agent. *"If you're worried about slop, ask the agent, is this slop code?"* [\[00:41:58\]](https://youtube.com/live/UwAGIkWFQ78?t=2518)

## Additional quotations

- On the least-boring reason to use agents: *"There's no more bullshit, I think."* [\[00:07:38\]](https://youtube.com/live/UwAGIkWFQ78?t=458)

- On new productivity surfaces: *"There are whole spaces of productivity that are now accessible in ways that they weren't before."* [\[00:08:02\]](https://youtube.com/live/UwAGIkWFQ78?t=482)

- On maker time and manager time: *"The agents kind of force you to go from maker time to manager time throughout the day."* [\[00:10:10\]](https://youtube.com/live/UwAGIkWFQ78?t=610)

- On accepting failed parallel runs: *"If you got ten things going and three are dumb, that's fine. You don't have to merge everything. You can start over."* [\[00:24:30\]](https://youtube.com/live/UwAGIkWFQ78?t=1470)

- On the Dask port and maintenance: *"Communities are useful because they're nice people. They're also useful to maintain things."* [\[00:27:18\]](https://youtube.com/live/UwAGIkWFQ78?t=1638)

- On agent excitement around telemetry: *"The agents, when they see this, they're like, oh, this is delightful."* [\[00:29:50\]](https://youtube.com/live/UwAGIkWFQ78?t=1790)

- On the current advice ceiling: *"We're at a point where agents have commoditized all of the other things and you should just think and write and do."* [\[00:32:55\]](https://youtube.com/live/UwAGIkWFQ78?t=1975)

- On information intake: *"People should think more about how they think."* [\[00:34:25\]](https://youtube.com/live/UwAGIkWFQ78?t=2065)

- On no-code-reading as a stack choice: *"I don't look at code."* [\[00:36:18\]](https://youtube.com/live/UwAGIkWFQ78?t=2178)

- On the recent code-reading shift: *"We haven't read code since January."* [\[00:38:08\]](https://youtube.com/live/UwAGIkWFQ78?t=2288)

- On code review by concern: *"Can you demonstrate to me that it's fast compared to these other libraries with benchmarks?"* [\[00:38:44\]](https://youtube.com/live/UwAGIkWFQ78?t=2324)

- On the period itself: *"It is a time of exploration."* [\[00:43:07\]](https://youtube.com/live/UwAGIkWFQ78?t=2587)

## Live reactions and follow-ups

### Discord links to Matt's writing

Hugo linked Matt's [Updated Thoughts on AI](https://matthewrocklin.com/ai-2026-06/) during the segment. The Discord embed describes the post as covering broad context, cross-domain reasoning, and feedback systems.

### Discord links to Frisky

Hugo later linked Matt's [Frisky and Xarray Example](https://matthewrocklin.com/frisky-xarray/) while Matt was discussing the Rust Dask-like system. The post gives readers a concrete artifact behind the Frisky telemetry and distributed-compute discussion.

### Discord extracted the five-phase workflow from Matt's screen share

A Discord participant screen-grabbed Matt's workflow phases and summarized them as planning with live feedback, execution, testing and iteration, self review, and fresh-agent review. That live note matched the parts Matt narrated, especially planning around live feedback and fresh-agent review.

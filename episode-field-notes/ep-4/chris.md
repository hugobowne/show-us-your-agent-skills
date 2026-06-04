# Chris Fonnesbeck - Episode 4 field notes

Chris Fonnesbeck created [PyMC](https://www.pymc.io/) 1.0, was a professor at Vanderbilt University, worked for the Yankees and Phillies, and now works with [PyMC Labs](https://www.pymc-labs.com/). His Episode 4 segment is about a new data-science bargain: agents make experimentation cheap enough to feel almost limitless, but that same ease can let a modeler skip the research and lose the judgment that makes the work trustworthy.

Chris names the upside directly: *"It allows you to do almost infinite experimentation."* [\[00:49:40\]](https://youtube.com/live/XaYQFtca798?t=2980) For someone building and iterating on statistical models, that changes the shape of the work. Agents remove the boilerplate and let him try analysis paths he would once have skipped because implementation time made broad exploration too expensive.

The risk is the same speed turned inward. Strong agents can become *"a little bit too seductive"* [\[00:51:12\]](https://youtube.com/live/XaYQFtca798?t=3072), and Chris worries about leaning on them before he has done enough thinking himself. *"You can paint yourself into a corner because you haven't done the work. You haven't done the research yourself, and it's too easy to ask the agent for it."* [\[00:51:24\]](https://youtube.com/live/XaYQFtca798?t=3084)

He builds a personal harness around [Pi](https://pi.dev/), [Zed](https://zed.dev/ai), `cutie-pi`, and review skills so the work can stay fast while plans and code pass through explicit critique. The concrete example was a PyMC distributions task: ask an agent to plan a half-flat distribution implementation, run `review plans` to write red and yellow flags to a local markdown file, hand that review back to the original agent, then run `review implementation` over the finished code.

Related workflow: [`plan-review-implementation-review`](../../workflows/plan-review-implementation-review/) turns Chris's demo into a reusable loop for asking an agent for a plan, reviewing it before implementation, and reviewing the finished code before accepting it.

<a href="https://youtube.com/live/XaYQFtca798?t=3875"><img src="images/chris-review-plans.png" alt="Chris Fonnesbeck showing the review plans workflow in Zed during the livestream" /></a>
<sub>Chris points `review plans` at a generated PyMC implementation plan, then uses the skill's markdown report as the review artifact before implementation. <a href="https://youtube.com/live/XaYQFtca798?t=3875">[01:04:35]</a></sub>

## On working with agents

### What he loves: creative focus and broader experimentation

Chris's first answer is that agents move boilerplate out of his head so model-building can stay creative. *"It really frees my brain to focus on creative tasks."* [\[00:49:12\]](https://youtube.com/live/XaYQFtca798?t=2952)

The data-science benefit is breadth. When building and iterating on models, agents let him try more model variants, analysis paths, and implementation paths than he would have coded by hand. *"In the past you'd take shortcuts and try fewer things because of the time that it would take for you to code it up and implement it."* [\[00:49:44\]](https://youtube.com/live/XaYQFtca798?t=2984)

He describes the change as a way to make disciplined curiosity cheaper: *"You can, at the flip of a switch, be a lot more exhaustive and use your imagination in ways that you couldn't before."* [\[00:49:54\]](https://youtube.com/live/XaYQFtca798?t=2994)

### What he finds most frustrating: seductive delegation without understanding

Chris does not frame the downside as hate. His concern is that strong agents can become too easy to lean on before he understands the problem deeply enough. *"Sometimes they're a little bit too seductive, in a way almost like social media or your phone."* [\[00:51:12\]](https://youtube.com/live/XaYQFtca798?t=3072)

The failure mode is skipping the research and then losing the thread of the work. *"You can paint yourself into a corner because you haven't done the work. You haven't done the research yourself, and it's too easy to ask the agent for it."* [\[00:51:24\]](https://youtube.com/live/XaYQFtca798?t=3084)

He contrasts himself with people who have optimized their process enough to stop reading some generated code. Chris still wants the agent workflow to preserve his own learning. *"There's always a big learning component for me."* [\[00:52:00\]](https://youtube.com/live/XaYQFtca798?t=3120)

## Workflows

### Turn repeated prompts into personal Pi skills

Chris has moved away from downloading large numbers of public skills and MCP servers. He says that early habit feels natural, but increasingly costly because it consumes context and can load stale or irrelevant instructions. [\[00:52:58\]](https://youtube.com/live/XaYQFtca798?t=3178)

He now prefers a bespoke setup where Pi creates local skills for his own harness. *"I'm interested in a bespoke AI experience that is tailored to the way that I work."* [\[00:55:42\]](https://youtube.com/live/XaYQFtca798?t=3342)

Pi's source-linked runtime makes that practical. *"If you want a skill to do something with GitHub Actions, for example, you can just ask Pi to do it. And so Pi will write a skill that you can customize to your liking."* [\[00:56:25\]](https://youtube.com/live/XaYQFtca798?t=3385)

Chris treats the setup as an ongoing personal project. *"It's my procrastination device these days, to try to tweak my Pi setup, which can be dangerous."* [\[00:58:19\]](https://youtube.com/live/XaYQFtca798?t=3499)

He saves the useful pieces in `cutie-pi` so they can stay current and shareable. Chris says the repository lets him *"keep it current, update it, and have it constantly available as a repository to share with others."* [\[01:06:21\]](https://youtube.com/live/XaYQFtca798?t=3981)

### Review implementation plans and code before accepting agent work

Chris's main demo is a repeatable review loop around a PyMC distributions task. He starts by asking an agent to generate a plan for a half-flat distribution implementation. [\[01:03:27\]](https://youtube.com/live/XaYQFtca798?t=3807)

He created the review plan skill because he kept asking agents to perform the same review process. *"I was asking the agent to do the same review process over and over again in the same way."* [\[01:03:49\]](https://youtube.com/live/XaYQFtca798?t=3829)

The `review plans` skill takes the saved plan, reviews it, presents findings, writes them to a local markdown file, and calls out red and yellow flags. [\[01:04:03\]](https://youtube.com/live/XaYQFtca798?t=3843) Chris then asks the original agent to implement against that review. [\[01:05:05\]](https://youtube.com/live/XaYQFtca798?t=3905)

After implementation, `review implementation` runs the same pattern on the completed code. *"At the review stage, I go back and forth using these Pi skills to iterate over the plan until there are no more red or yellow flags, run the implementation, and then do exactly the same thing with review implementation."* [\[01:05:53\]](https://youtube.com/live/XaYQFtca798?t=3953)

Chris does not hard-code model selection into the skill. He chooses models on the fly based on the task. *"I usually make that on the fly depending on what I'm doing."* [\[01:06:58\]](https://youtube.com/live/XaYQFtca798?t=4018)

He has moved somewhat away from frontier models for this workflow and uses combinations of Qwen, DeepSeek, and Kimi. *"Different ones have different strengths. Kimi is a really good coding agent. DeepSeek is a little bit better at data science tasks."* [\[01:07:24\]](https://youtube.com/live/XaYQFtca798?t=4044)

The review loop can use one model to critique and another to implement. Chris gives one example: DeepSeek for review and Qwen for implementation. [\[01:05:31\]](https://youtube.com/live/XaYQFtca798?t=3931)

### Manage multiple agent sessions in Zed

Chris uses Zed less as a conventional text editor and more as a place to dock multiple agents. *"I actually these days don't use it as much as a text editor slash IDE, but actually more of an AI agent multiplexer."* [\[01:01:52\]](https://youtube.com/live/XaYQFtca798?t=3712)

The left side of his Zed setup has agents running in different projects simultaneously, and he flips between them as needed. [\[01:02:00\]](https://youtube.com/live/XaYQFtca798?t=3720)

That matters because agent tasks can run for a while. Zed notifications help him notice when work is done or when Claude is waiting for permission instead of continuing. [\[01:11:38\]](https://youtube.com/live/XaYQFtca798?t=4298)

## Skills

### PyMC modeling skill

Chris names the PyMC modeling skill as a useful application of agent skills because package knowledge can lag behind current releases. *"It's going to be extremely useful for users because particularly when a new version is released like PyMC 6, these models are obviously trained on data from the past."* [\[00:53:46\]](https://youtube.com/live/XaYQFtca798?t=3226)

The skill matters because the public internet contains much more older PyMC material than PyMC 6 guidance. *"The internet is full of PyMC 3 models and PyMC 3 information, but there's really nothing yet on PyMC 6 or more recent features."* [\[00:54:05\]](https://youtube.com/live/XaYQFtca798?t=3245)

### `/simplify`

Chris recreated a `/simplify` command in Pi because he had used it often in Claude Code. *"One of the big things that I used all the time in Claude Code is slash simplify."* [\[00:59:06\]](https://youtube.com/live/XaYQFtca798?t=3546)

The command fits his data-science work because generated model implementations may work without being the efficient version he wants. *"Calling slash simplify after you implement something is a really nice way to slim it down and make sure that it's something that you're proud of and something that works well."* [\[00:59:33\]](https://youtube.com/live/XaYQFtca798?t=3573)

### Socratic Review

Socratic Review is Chris's local implementation of the pattern behind the [`grill me`](https://github.com/mattpocock/skills/blob/main/skills/productivity/grill-me/SKILL.md) skill. He describes the underlying idea as clarifying intent before implementation. *"One of the best ways to get an agent to implement something well, implement something that you have in mind, is to actually have a back and forth with it to clarify uncertainties."* [\[01:00:27\]](https://youtube.com/live/XaYQFtca798?t=3627)

The skill asks questions until the plan is clear enough. *"It'll essentially ask you a series of questions until it's happy with what it's about to do, at the planning stage."* [\[01:01:05\]](https://youtube.com/live/XaYQFtca798?t=3665)

### `review plans`

`review plans` reviews a saved plan before implementation. Chris points it at the generated plan for the half-flat distribution, and the skill produces findings in the terminal and a local markdown file. [\[01:04:03\]](https://youtube.com/live/XaYQFtca798?t=3843)

The review looks for red and yellow flags. The live example was mostly clean because the half-flat distribution was not difficult to implement. [\[01:04:48\]](https://youtube.com/live/XaYQFtca798?t=3888)

### `review implementation`

`review implementation` applies the same review idea after the code has been written. Chris uses it after the plan has no more red or yellow flags and the original agent has implemented the work. [\[01:05:48\]](https://youtube.com/live/XaYQFtca798?t=3948)

The skill completes the plan-review, implement, implementation-review loop that Chris built into his Pi setup.

## Tools / projects he showed

### Pi

[Pi](https://pi.dev/) is the agent harness Chris recently switched to. *"I've switched to recently, moved away from the Claudes and the Codexes of the world and discovered Pi."* [\[00:54:50\]](https://youtube.com/live/XaYQFtca798?t=3290)

He describes it as a stripped-down analog to Claude Code or [OpenCode](https://opencode.ai/), with fewer built-in features but more room for a personalized setup. [\[00:55:22\]](https://youtube.com/live/XaYQFtca798?t=3322)

The key feature for Chris is that Pi runs in an environment linked to its own source code. *"Pi can actually fix itself."* [\[00:56:53\]](https://youtube.com/live/XaYQFtca798?t=3413)

### cutie-pi

[`cutie-pi`](https://github.com/fonnesbeck/cutie-pi) is where Chris saves his personal Pi skills so they stay current and shareable. Chris says the repository lets him *"keep it current, update it, and have it constantly available as a repository to share with others."* [\[01:06:21\]](https://youtube.com/live/XaYQFtca798?t=3981)

### Zed

[Zed](https://zed.dev/ai) is Chris's main agent workspace in the demo. He calls it his *"weapon of choice for using agents"* [\[01:01:47\]](https://youtube.com/live/XaYQFtca798?t=3707), then shows agents running across multiple projects inside the editor.

He chose it partly because he moved from Jupyter-heavy work to Marimo notebooks, and partly because Zed is lighter than VS Code, has native Vim mode, and is written in Rust. [\[01:09:19\]](https://youtube.com/live/XaYQFtca798?t=4159)

### PyMC distributions repository

Chris runs the review demo inside a PyMC project repository called distributions. *"These are PyTensor implementations of the probability distributions that we currently have in PyMC."* [\[01:02:31\]](https://youtube.com/live/XaYQFtca798?t=3751)

The example task is to implement a half-flat distribution, which has equal probability over its supported range from zero to positive infinity. [\[01:03:05\]](https://youtube.com/live/XaYQFtca798?t=3785)

### PyMC

[PyMC](https://www.pymc.io/) is the Bayesian modeling project behind Chris's bio, skill example, and live codebase. Thomas says Chris created PyMC 1.0, and Chris later uses PyMC 6 as the example of why up-to-date skills matter. [\[00:48:22\]](https://youtube.com/live/XaYQFtca798?t=2902)

At the end, Chris describes an in-person PyMC course covering the new PyMC 6 material. [\[01:13:59\]](https://youtube.com/live/XaYQFtca798?t=4439)

### PyTensor

[PyTensor](https://pytensor.readthedocs.io/) appears through the PyMC distributions repository. Chris describes the repository as holding PyTensor implementations of probability distributions that PyMC currently has, with more being added over time. [\[01:02:36\]](https://youtube.com/live/XaYQFtca798?t=3756)

### Claude Code

Claude Code is the tool Chris moved some habits from into Pi. His `/simplify` skill comes from a command he used frequently in Claude Code for data-science tasks. [\[00:59:06\]](https://youtube.com/live/XaYQFtca798?t=3546)

Later, he says Zed terminal threads let him use Claude Code through his Claude Max subscription in a way that is integrated with Zed. [\[01:12:13\]](https://youtube.com/live/XaYQFtca798?t=4333)

### OpenCode

[OpenCode](https://opencode.ai/) is one of the tools Pi resembles. Pi is a stripped-down analog to Claude Code or OpenCode, which he treats as a strength for customization. [\[00:55:22\]](https://youtube.com/live/XaYQFtca798?t=3322)

### skills.sh

[skills.sh](https://skills.sh/) appears as the public place Chris is increasingly avoiding for personal use. *"More and more I'm avoiding skills that other people are publishing on skills.sh and essentially just writing them myself."* [\[00:55:57\]](https://youtube.com/live/XaYQFtca798?t=3357)

### GitHub Actions

[GitHub Actions](https://github.com/features/actions) is Chris's example of a task-specific Pi skill. If he wants a skill to do something with GitHub Actions, he can ask Pi to create it and then customize the result. [\[00:56:25\]](https://youtube.com/live/XaYQFtca798?t=3385)

### Nushell

[Nushell](https://www.nushell.sh/) is Chris's preferred shell in this setup, with an extension that intercepts bash commands and routes them through Nushell. [\[00:59:58\]](https://youtube.com/live/XaYQFtca798?t=3598)

### `grill me` skill

Chris recommends the [`grill me`](https://github.com/mattpocock/skills/blob/main/skills/productivity/grill-me/SKILL.md) skill as the upstream pattern behind Socratic Review. *"One of the popular skills out there that I highly recommend is the grill me skill."* [\[01:00:11\]](https://youtube.com/live/XaYQFtca798?t=3611)

He attributes the original to Matt Pocock, then shows his own implementation under a different name. [\[01:00:14\]](https://youtube.com/live/XaYQFtca798?t=3614)

### DeepSeek

[DeepSeek](https://www.deepseek.com/) is one of Chris's non-frontier model choices. He uses it for review and data-science tasks. *"DeepSeek is a little bit better at data science tasks."* [\[01:07:32\]](https://youtube.com/live/XaYQFtca798?t=4052)

### Qwen

[Qwen](https://qwenlm.github.io/) is one of the models Chris uses in Pi, especially as an implementation model after another model reviews the plan. [\[01:05:31\]](https://youtube.com/live/XaYQFtca798?t=3931)

### Kimi

[Kimi](https://www.kimi.com/) is another model Chris uses in his non-frontier mix. *"Kimi is a really good coding agent."* [\[01:07:24\]](https://youtube.com/live/XaYQFtca798?t=4044)

### VS Code

[VS Code](https://code.visualstudio.com/) was Chris's previous default because of notebook rendering. He says he was a heavy VS Code user when he was building many Jupyter notebooks. [\[01:08:23\]](https://youtube.com/live/XaYQFtca798?t=4103)

### Cursor

[Cursor](https://cursor.com/) appears alongside VS Code as one of the few tools Chris found useful for rendering Jupyter notebooks for Python models. [\[01:08:33\]](https://youtube.com/live/XaYQFtca798?t=4113)

### Jupyter notebooks

[Jupyter](https://jupyter.org/) notebooks are the old notebook format Chris moved away from for much of his work. The problem in this segment is not statistical capability but file format and editor dependence: Jupyter emits large JSON, while Marimo notebooks are Python files. [\[01:08:52\]](https://youtube.com/live/XaYQFtca798?t=4132)

### Marimo notebooks

[Marimo](https://marimo.io/) notebooks are the notebook format Chris has moved most of his work to. That transition helped him leave the heavy IDE workflow because Marimo notebooks are Python files. [\[01:08:52\]](https://youtube.com/live/XaYQFtca798?t=4132)

### Marimo Pair

[Marimo Pair](https://marimo.io/blog/marimo-pair) is now central to Chris's agentic notebook work. *"I basically live inside of Marimo Pair these days."* [\[01:11:10\]](https://youtube.com/live/XaYQFtca798?t=4270)

He often has multiple Marimo Pair sessions open at once, and Zed's multiplexer behavior makes that easier to manage. [\[01:11:18\]](https://youtube.com/live/XaYQFtca798?t=4278)

### Ghostty

[Ghostty](https://ghostty.org/) appears as the terminal setup Chris used before keeping sessions in Zed. He says he used to have multiple Ghostty terminals open simultaneously, and flipping between them was awkward. [\[01:11:28\]](https://youtube.com/live/XaYQFtca798?t=4288)

### ACP

ACP appears through Zed's agent integration. Chris says Zed has an ACP implementation that is more integrated with the editor, but he usually avoids it because it feels slower. *"I find the ACP is a little bit slower, so I typically just use terminal sessions."* [\[01:12:51\]](https://youtube.com/live/XaYQFtca798?t=4371)

### Cobalt 2 theme

Chris wrote and published a Cobalt 2 theme extension for Zed because he had used Wes Bos's Cobalt 2 theme in VS Code and there was not one for Zed. [\[01:13:39\]](https://youtube.com/live/XaYQFtca798?t=4419)

### PyMC London course

Chris describes a two-and-a-half-day live [PyMC course in East London](https://www.pymc-labs.com/courses/probabilistic-programming-bayesian-modeling-pymc) after PyData London. The course covers PyMC 6 topics, including time series, state space models, Gaussian processes, and BART models. [\[01:14:55\]](https://youtube.com/live/XaYQFtca798?t=4495)

## Principles and explainers

### Agent skills can patch model knowledge gaps

Chris uses PyMC 6 to explain why a skill can be valuable even when it is not flashy. Models are trained on older data, and documentation or examples for a newly released version may not be present in the training distribution. [\[00:53:46\]](https://youtube.com/live/XaYQFtca798?t=3226)

The PyMC modeling skill gives users current modeling guidance when the wider internet still skews toward PyMC 3 examples.

### Context makes indiscriminate skill loading expensive

Chris says the first discovery phase with MCP servers and skills can lead people to load everything they might use. He now sees that as increasingly bad because it uses context and may add outdated or irrelevant information. [\[00:52:58\]](https://youtube.com/live/XaYQFtca798?t=3178)

His answer is to keep skills local, narrow, and personal.

### A smaller harness can support a more personal workflow

Pi can look like a stripped-down Claude Code or OpenCode, but Chris treats that as part of the appeal. A smaller harness gives him more control over how the agent behaves, what skills exist, and how the toolchain evolves. [\[00:55:22\]](https://youtube.com/live/XaYQFtca798?t=3322)

The result is personal infrastructure rather than a fixed product workflow.

### Agents can build and repair their own local tools

Chris describes Pi as source-linked rather than a compiled TUI binary. Because of that, he can ask Pi to diagnose problems and alter its own source tree when needed. [\[00:56:53\]](https://youtube.com/live/XaYQFtca798?t=3413)

That changes tool-building from a separate engineering project into part of the same agent conversation.

### Review loops make agent work inspectable

Chris's plan and implementation reviews turn agent output into something another agent can critique before he accepts it. The red and yellow flag structure gives him a concrete inspection artifact instead of relying only on the original generation. [\[01:04:35\]](https://youtube.com/live/XaYQFtca798?t=3875)

The loop still preserves human judgment. Chris picks models, decides how to route work, reads the review artifacts, and chooses when the plan has no more serious flags.

### Different models can play different roles

Chris does not present model choice as a permanent rule. He says the fit comes from experience: Kimi is strong for coding, DeepSeek is better for data science tasks, and Qwen can be useful for implementation. [\[01:07:24\]](https://youtube.com/live/XaYQFtca798?t=4044)

The pattern is task routing, not model loyalty.

### Python-file notebooks make agent work easier to manage

Chris used to depend heavily on VS Code because he was building Jupyter notebooks, and VS Code and Cursor had strong notebook rendering support. [\[01:08:31\]](https://youtube.com/live/XaYQFtca798?t=4111)

He has since moved most of his work to [Marimo](https://marimo.io/) notebooks, which store notebooks as Python files instead of large Jupyter JSON. *"I've switched most of my work over to using Marimo notebooks, which no longer require the big JSON that Jupyter spits out at you."* [\[01:08:52\]](https://youtube.com/live/XaYQFtca798?t=4132)

That shift made Zed more viable for him even though it does not currently support Jupyter. It also fits his agent-multiplexer workflow because the editor is lighter, faster, and less central than the agent sessions.

### Data-science agents change the cost of being exhaustive

In data science, Chris cares about model iteration and problem-solving more than application-building. Agents lower the cost of exploring alternatives, which changes the analysis process itself. [\[00:49:27\]](https://youtube.com/live/XaYQFtca798?t=2967)

The benefit is the ability to run the procedures he might otherwise skip.

### Lightweight editors work better when the agent is doing more of the editing

Chris says Zed works for him partly because he is not using the editor as much anymore. The editor becomes a shell for agents, terminal threads, notifications, model sessions, and lightweight file work. [\[01:11:52\]](https://youtube.com/live/XaYQFtca798?t=4312)

That fits his move from Jupyter JSON files to Marimo Python files.

### In-person courses still matter for Bayesian modeling

Chris says Zoom courses are useful, but live Bayesian and PyMC teaching has a level of interactivity that is hard to replace. *"You can't beat the interactivity of being in a room with some experts and bouncing ideas off of one another."* [\[01:14:27\]](https://youtube.com/live/XaYQFtca798?t=4467)

The London course uses that setting for PyMC 6 topics that benefit from discussion, including time series, state space models, Gaussian processes, and BART models.

## Additional quotations

- On agents and laziness: *"Generally I'm lazy, and if I don't have a shortcut like that, I won't do it."* [\[00:50:05\]](https://youtube.com/live/XaYQFtca798?t=3005)
- On relying on frontier models too early: Chris says he is wary of *"relying on them a little bit too heavily, particularly in the beginning."* [\[00:52:05\]](https://youtube.com/live/XaYQFtca798?t=3125)
- On skills for current PyMC work: *"If you want to be using those in your data science workflow, it's useful to have skills like that to do it."* [\[00:54:18\]](https://youtube.com/live/XaYQFtca798?t=3258)
- On asking Pi to clone useful patterns: *"Just ask Pi to create an analog of anything that's in here for yourself."* [\[00:58:43\]](https://youtube.com/live/XaYQFtca798?t=3523)
- On Zed and multiple projects: *"I've got a series of agents running in different projects simultaneously, and I can just flip back and forth between them as needed."* [\[01:02:00\]](https://youtube.com/live/XaYQFtca798?t=3720)
- On model selection: *"Different ones have different strengths."* [\[01:07:24\]](https://youtube.com/live/XaYQFtca798?t=4044)
- On Zed's Vim mode: *"Zed has a really, really nice Vim mode, native Vim mode."* [\[01:09:30\]](https://youtube.com/live/XaYQFtca798?t=4170)
- On Marimo Pair: *"I basically live inside of Marimo Pair these days."* [\[01:11:10\]](https://youtube.com/live/XaYQFtca798?t=4270)
- On terminal sessions in Zed: *"I find the ACP is a little bit slower, so I typically just use terminal sessions."* [\[01:12:51\]](https://youtube.com/live/XaYQFtca798?t=4371)
- On the London course: *"Two and a half days is a nice chunk of time to really dig into some useful topics."* [\[01:15:13\]](https://youtube.com/live/XaYQFtca798?t=4513)

## Live reactions and follow-ups

### Discord links: Chris's stack landed in chat

The Discord chat supplied concrete links around Chris's segment:

- [Pi](https://pi.dev/)
- [`cutie-pi`](https://github.com/fonnesbeck/cutie-pi)
- [PyMC 6 London workshop](https://www.pymc-labs.com/courses/probabilistic-programming-bayesian-modeling-pymc)

### Discord reaction: Zed, Pi, and PyMC puns

The chat tracked the segment closely:

- *"zed is nice"*
- *"the not needing to pay the electron tax helps"*
- *"Is the host of the event a PyMC emcee?"*
- *"What problems can you fix a PyMC Hammer"*

### Hugo's transition: the show is broader than literal skills

After Chris's segment, Hugo uses the discussion to clarify the premise of the show. Skills matter, but the real subject is how builders work with agents. *"It really is about showing workflows, and some of those are skills, some are not."* [\[01:16:30\]](https://youtube.com/live/XaYQFtca798?t=4590)

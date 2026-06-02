# Chris Fonnesbeck - Episode 4 field notes

Chris Fonnesbeck is introduced as the creator of PyMC 1.0, a former Vanderbilt professor, and someone who has worked for the Yankees and Phillies, now working with PyMC Labs. His segment centers on how a data scientist customizes agent harnesses: using Pi, writing local skills, reviewing plans and implementations, choosing models by task, and using Zed as an agent workspace rather than just an editor.

## On working with agents

### What he loves: more room for creative data science

Chris says agents free him from boilerplate and make data science feel less constrained by implementation cost. *"it really frees my brain to focus on creative tasks. you know, takes away all of the boilerplate, all the boring stuff to focus on, you know, the fun stuff."* [\[00:49:12\]](https://youtube.com/live/XaYQFtca798?t=2952)

For modeling work, the bigger shift is experimentation. Agents let him try more analysis paths instead of taking shortcuts because something is too slow to code by hand. *"it allows you to do almost infinite experimentation."* [\[00:49:38\]](https://youtube.com/live/XaYQFtca798?t=2978)

### What he finds most frustrating: agents are too seductive

Chris does not frame the downside as hate. The problem is that powerful agents are easy to lean on before you have done the work yourself. *"they're sometimes they're a little bit too seductive, in a way almost like social media or your or your phone."* [\[00:51:07\]](https://youtube.com/live/XaYQFtca798?t=3067)

The risk is not just wrong answers. It is losing the learning loop that matters to him. *"you can kind of paint yourself into a corner because you haven't, you know, you haven't done the work. you haven't done the research yourself and and it's too easy to ask the agent for it."* [\[00:51:19\]](https://youtube.com/live/XaYQFtca798?t=3079)

## Skills

### PyMC modeling skill

Chris agrees with Hamel's warning against hoarding skills, but names the PyMC modeling skill as a useful exception. Version drift is the reason: model training data may lag current APIs, and the web is full of old PyMC3 examples. *"the PyMC modeling skill which is going to be extremely useful for users because particularly when a new version is released like PyMC six and these models are obviously trained on data from the past"* [\[00:53:37\]](https://youtube.com/live/XaYQFtca798?t=3217)

That makes skills useful when they encode current library usage instead of generic prompting. *"if you want to be using those in your data science workflow, it's useful to have you know skills like that to do it."* [\[00:54:18\]](https://youtube.com/live/XaYQFtca798?t=3258)

### Pi extension and skill collection

Chris showed his [cutie-pi](https://github.com/fonnesbeck/cutie-pi) repository, a collection of bespoke Pi extensions, skills, and tools. He tells people not to install it blindly. The stronger pattern is to fork, customize, or ask Pi to build an analog for your own workflow. *"fork it and and customize it yourself or even better. just ask Pi ask Pi to create an analog of anything that's in here for yourself."* [\[00:58:43\]](https://youtube.com/live/XaYQFtca798?t=3523)

### Slash simplify command

Chris recreated a Claude Code behavior he missed inside Pi: `/simplify`. For data science tasks, he uses it after implementation to reduce unnecessary complexity, especially when an agent writes a PyMC model that works but is not clean enough. *"calling slash simplify after you implement something is a really nice way to kind of slim it down and make sure that it's know that it's something that you're proud of and and and something that works well."* [\[00:59:33\]](https://youtube.com/live/XaYQFtca798?t=3573)

### Nushell routing extension

Chris also customized shell behavior in Pi. Instead of using Bash directly, he has an extension that routes commands through Nushell. The agent can still issue Bash-shaped commands, but Chris routes them through a shell he prefers: *"I've got a an extension that will intercept bash commands and route it through Nushell."* [\[00:59:52\]](https://youtube.com/live/XaYQFtca798?t=3592)

### Socratic Review

Chris's Socratic Review is his implementation of Matt Pocock's [grill-me](https://github.com/mattpocock/skills/blob/main/skills/productivity/grill-me/SKILL.md) pattern, with [grill-with-docs](https://github.com/mattpocock/skills/blob/main/skills/engineering/grill-with-docs/SKILL.md) linked in Discord as a successor. The point is to make the agent clarify uncertainty before it builds. *"one of the best ways to get to convince an agent to implement something well, implement something that you have in mind is to actually have a back and forth with it to clarify uncertainties."* [\[01:00:24\]](https://youtube.com/live/XaYQFtca798?t=3624)

His version keeps asking until the plan is ready: *"it'll essentially asks you asks you a series of questions until it's happy with what it's about to do, kind of at the planning stage."* [\[01:01:05\]](https://youtube.com/live/XaYQFtca798?t=3665)

### Review plans for a new PyMC distribution

Chris created a Pi skill called `review plans` because he kept asking agents to perform the same plan review process. The demo is specifically about implementing a missing probability distribution in a PyMC distributions repo: Chris picks a half-flat distribution, asks the agent to generate an implementation plan, then points `review plans` at that plan. The skill runs the review, writes findings to a local markdown file, and calls out red or yellow flags. *"created a a Pi skill that is is called review plans."* [\[01:03:55\]](https://youtube.com/live/XaYQFtca798?t=3835)

### Review implementation for the distribution code

After the original agent implements the distribution plan, Chris runs a second review skill over the resulting code. The important pattern is not "agent writes PyMC code" by itself. It is agent plans the distribution, review skill audits the plan, agent implements, review skill audits the implementation. Chris iterates until the obvious flags are gone. *"Iterate over the plan until there are no more red or yellow flags, run the implementation, and then do exactly the same thing with review implementation."* [\[01:05:53\]](https://youtube.com/live/XaYQFtca798?t=3953)

He keeps these skills current in the repo rather than treating them as one-off prompt dumps: *"these are just skills that I've come up with myself simply by asking Pi to do it, and then I've saved it to cutie-pi so that I can you know make keep it current, update it, and have it. constantly available as a repository to to share with others."* [\[01:06:13\]](https://youtube.com/live/XaYQFtca798?t=3973)

## Workflows

### Do not download every skill or MCP server

Chris backs Hamel's warning about tool hoarding. When people first discover skills and MCP servers, they often install everything that looks useful. He increasingly sees that as a bad idea because it burns context and can inject stale or irrelevant information. *"you kind of go out and search for everything that you might use and load it onto your system and increasingly that's a bad idea because you know it uses up context"* [\[00:52:58\]](https://youtube.com/live/XaYQFtca798?t=3178)

### Build a bespoke AI environment around your own work

Chris moved toward [Pi](https://pi.dev/) because he wants an agent harness tailored to him, not a vendor-default interface. *"increasingly, you know, I'm interested in kind of a bespoke AI experience that is tailored to the way that I work."* [\[00:55:40\]](https://youtube.com/live/XaYQFtca798?t=3340)

That is why he writes his own skills rather than adopting random public ones from [skills.sh](https://skills.sh/): *"more and more I'm avoiding skills that other people are publishing on skills.sh and essentially just you know writing them myself."* [\[00:55:55\]](https://youtube.com/live/XaYQFtca798?t=3355)

### Ask Pi to modify Pi

The core attraction of Pi, for Chris, is that it is tied to its source code. If he needs GitHub Actions behavior or a missing command, he can ask Pi to add it. *"Pi will write a skill. That you can customize to your liking and and specify some nuances that perhaps only you will use and other people may not."* [\[00:56:34\]](https://youtube.com/live/XaYQFtca798?t=3394)

He also likes that Pi can diagnose and modify itself: *"Pi can actually fix itself. So when something's going wrong, you can ask it what's going wrong, diagnose it, and then we'll actually go in and even alter the its own source tree."* [\[00:56:53\]](https://youtube.com/live/XaYQFtca798?t=3413)

### Split planning, reviewing, and implementation across agents and models

Chris does not ask one agent to do everything in a straight line. He has one agent generate a plan, another review it, the original implement it, and another review the implementation. He will also switch models between roles. *"I like to go back and forth between you know different instances and sometimes even different models."* [\[01:05:14\]](https://youtube.com/live/XaYQFtca798?t=3914)

The model choice is learned by use, not hard-coded. *"Different ones have different strengths. Kimi is a really good coding agent. DeepSeek a little bit better at data science tasks."* [\[01:07:24\]](https://youtube.com/live/XaYQFtca798?t=4044)

### Use Zed as an agent multiplexer

Chris uses [Zed](https://zed.dev/ai) less as a traditional IDE and more as a place to dock multiple agents. *"I actually these days don't use it as much as a of a text editor slash IDE, but actually more of a an AI agent multiplexer."* [\[01:01:52\]](https://youtube.com/live/XaYQFtca798?t=3712)

He keeps multiple sessions open, gets completion notifications, and avoids losing time because an agent is waiting for permission while he thought it was still working. Zed *"pops up a nice little notification when something's finished so you can switch over to it,"* which helps avoid *"that situation where you're stuck, where Claude is stuck waiting for permission to do something"* while you thought it was still working. [\[01:11:35\]](https://youtube.com/live/XaYQFtca798?t=4295)

## Tools / projects he showed

### PyMC distributions repo

Chris's demo uses PyMC work as the concrete task, not just background color. He shows a PyMC project repository for probability distributions and talks through adding a half-flat distribution, one with equal probability from zero to positive infinity. *"say I want to implement a probability distribution that doesn't yet exist inside of PyMC distributions, and so the half flat distribution is one. That I'm going to pick here."* [\[01:02:55\]](https://youtube.com/live/XaYQFtca798?t=3775)

### Pi

Chris frames Pi as a stripped-down analog to Claude Code or OpenCode, useful because it gives him a self-modifiable environment rather than a fixed compiled TUI. *"it's it's very much stripped down analog to Claude Code or OpenCode."* [\[00:55:20\]](https://youtube.com/live/XaYQFtca798?t=3320)

The tradeoff is deliberate: he gives up some vendor polish in exchange for a harness he can shape around his work.

### cutie-pi

Chris's [cutie-pi](https://github.com/fonnesbeck/cutie-pi) repo is where he keeps his Pi extensions and skills. Discord links it during the segment, and Chris describes the broader principle on stream: keep the useful pieces current, customized, and shareable rather than pretending one public skill works unchanged for everyone.

### Zed

Chris moved from VS Code toward Zed after switching much of his notebook work to marimo, where he is working with Python files instead of Jupyter's JSON. He also likes Zed's native Vim mode and speed. *"I was looking to sort of transition away from kind of the heavy IDE that VS Code is into something that's a little bit a little bit faster."* [\[01:08:43\]](https://youtube.com/live/XaYQFtca798?t=4123)

On extensibility, he says Zed can install local extensions and that many published extensions are MCP servers or language servers. His own example is a Cobalt 2 theme he wrote and published. *"if you've got a local extension, you can ex install it, you know, from a a repository as well."* [\[01:13:21\]](https://youtube.com/live/XaYQFtca798?t=4401)

### marimo pair

Hugo brings up [marimo pair](https://marimo.io/blog/marimo-pair), and Chris says it is now central to his workflow. *"I basically live inside of marimo pair these days."* He often has multiple sessions open at once, which makes Zed's multiplexer setup especially useful. [\[01:11:10\]](https://youtube.com/live/XaYQFtca798?t=4270)

### PyMC 6 London workshop

Chris closes by describing a PyMC 6 workshop in London, linked in Discord as the [Probabilistic Programming and Bayesian Modeling with PyMC](https://www.pymc-labs.com/courses/probabilistic-programming-bayesian-modeling-pymc) course. He says students will cover new PyMC 6 material, time series, state space models, Gaussian processes, and BART models. *"you can't beat the interactivity of being in a room with some experts and bouncing ideas off of one another"* [\[01:14:24\]](https://youtube.com/live/XaYQFtca798?t=4464)

## Explainers

### Useful skills fight version drift

Chris's PyMC example gives a precise answer to when skills are worth having: when they encode current, local, version-specific knowledge that the model probably does not have. The internet is full of old PyMC3 content, but a PyMC6 workflow needs newer patterns. *"the internet is full of sort of PyMC3 models and PyMC3 information, but there's really nothing yet on PyMC6 or more recent more recent features."* [\[00:54:05\]](https://youtube.com/live/XaYQFtca798?t=3245)

### Self-modifying harnesses make skills feel like part of the environment

Pi is not just a place to run a skill. Chris values that it can write, modify, and reload the environment around itself. The skill becomes part of the harness rather than an external instruction file. *"when you run Pi, you you aren't just running a a compiled TUI, a binary. You're actually writing running an environment that is linked to its own source code."* [\[00:56:08\]](https://youtube.com/live/XaYQFtca798?t=3368)

### Review skills encode repeated judgment for real code

The `review plans` and `review implementation` skills are examples of turning a repeated review ritual into a reusable capability for real code work. In the demo, the work is a new PyMC distribution. Chris found himself asking for the same review in the same way, then encoded that as a Pi skill. *"I was asking the agent to do the sort of same review process over and over again in the same way."* [\[01:03:36\]](https://youtube.com/live/XaYQFtca798?t=3816)

The result is not automation for its own sake. It is a way to force the plan and implementation through a consistent red-flag/yellow-flag review loop before moving on.

### Model choice is a craft judgment

Chris's model routing is not yet automatic. He decides on the fly, based on the task and his experience with the model. That keeps the workflow pragmatic: review can use one model, implementation another, and auto-selection is optional rather than mandatory. *"I usually make that on the fly depending on what I'm doing."* [\[01:06:58\]](https://youtube.com/live/XaYQFtca798?t=4018)

### Editors are becoming agent operating rooms

Chris's Zed workflow captures a shift in what an editor is for. He is not mostly editing text. He is managing several agent sessions, checking notifications, opening diffs, and routing work through terminal threads. *"it's a nice integration of kind of lightweight editing because again we're we're not using the editor quite as much anymore."* [\[01:11:54\]](https://youtube.com/live/XaYQFtca798?t=4314)

## Additional quotations

- On agent dependence: *"So so the seductiveness, I guess, of agents is is not what I hate, but what I'm fearful of."* [\[00:52:17\]](https://youtube.com/live/XaYQFtca798?t=3137)
- On PyMC 6 and stale model knowledge: *"sometimes it's sort of six to twelve months out of date depending on which model that you're using."* [\[00:53:56\]](https://youtube.com/live/XaYQFtca798?t=3236)
- On Pi as a hobby: *"It's kind of my procrastination device these days is to try to tweak my Pi setup, which can be dangerous."* [\[00:58:19\]](https://youtube.com/live/XaYQFtca798?t=3499)
- On Socratic Review: *"sometimes it it'll you know drill down into sort of 20, 25 stages of questions."* [\[01:00:57\]](https://youtube.com/live/XaYQFtca798?t=3657)
- On the half-flat demo: *"A half-flat distribution isn't isn't very difficult to implement, so it was pretty clean out of the gate. So perhaps this wasn't the best example to do"* [\[01:04:52\]](https://youtube.com/live/XaYQFtca798?t=3892)
- On Zed's fit for his habits: *"Zed has a a really, really nice Vim mode, native Vim mode. and and so you know kind of supports my sort of instinctual coding habits."* [\[01:09:26\]](https://youtube.com/live/XaYQFtca798?t=4166)
- On live teaching: *"two and a half days is a really good sweet spot. You know, I think when once you get to the end of like three days, everybody's ready to lose their mind."* [\[01:14:55\]](https://youtube.com/live/XaYQFtca798?t=4495)

## Live reactions and follow-ups

### Discord links: Chris's stack landed in chat

The Discord chat supplied the concrete links around Chris's demo:

- [Pi](https://pi.dev/)
- [cutie-pi](https://github.com/fonnesbeck/cutie-pi)
- [Matt Pocock's grill-me skill](https://github.com/mattpocock/skills/blob/main/skills/productivity/grill-me/SKILL.md)
- [Matt Pocock's grill-with-docs skill](https://github.com/mattpocock/skills/blob/main/skills/engineering/grill-with-docs/SKILL.md)
- [Zed AI](https://zed.dev/ai)
- [marimo pair](https://marimo.io/blog/marimo-pair)
- [PyMC 6 London workshop](https://www.pymc-labs.com/courses/probabilistic-programming-bayesian-modeling-pymc)

### Discord reaction: Zed, Pi, and PyMC puns

The chat tracked the segment closely:

- *"best way to build a pi extension is to use pi, (since one part of its very small system prompt is about how to modify pi)"*
- *"zed is nice"*
- *"the not needing to pay the electron tax helps"*
- *"Is the host of the event a PyMC emcee?"*
- *"What problems can you fix a PyMC Hammer"*

### Hugo's transition: the show is broader than literal skills

After Chris's segment, Hugo uses the discussion to clarify the premise of the show. Skills matter, but the real subject is how builders work with agents. *"it really is about, you know, showing workflows, and some of those are skills, some are not"* [\[01:16:30\]](https://youtube.com/live/XaYQFtca798?t=4590)

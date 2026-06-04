# Eleanor Berger - Episode 3 field notes

Eleanor Berger, an AI and software engineering expert, technical member of staff at [Jiminy Health](https://www.jiminy.health/), creator of [Agentic Ventures](https://maven.com/agentic-ventures/ai-coding), and formerly a principal engineering lead at Microsoft and Google, used her Episode 3 segment to show what happens when a careful agent engineer lets a personal agent roam inside a deliberately bounded environment. The live demo centered on [Hermes](https://hermes-agent.nousresearch.com/) running on an old M1 Mac mini, a personal agent named Fnord, [GPT 5.5](https://openai.com/index/introducing-gpt-5-5/), Discord, [Here Now](https://here.now/), [Impeccable](https://impeccable.style/), scheduled jobs, browser automation, and a stack that now leans heavily on [Codex](https://openai.com/index/introducing-the-codex-app), [Warp](https://www.warp.dev/terminal), [Zed](https://zed.dev/), and tool-agnostic configuration.

Eleanor puts concrete verification ahead of AI review chains. *"You can't get AI validating AI. There's this infinite regress where you could get stuck in a local minimum and you never get out of it."* [\[00:33:18\]](https://youtube.com/live/ud2WzkKeDZs?t=1998) For cloud infrastructure work, she wants agents doing boring delegated work only when the system can realize the configuration and inspect the concrete cloud footprint. The Hermes demo applies the same safety instinct to a personal agent: it can publish pages, manage Watch Later summaries, create skills, run scheduled jobs, and decide when to ask for approval, while Eleanor keeps sensitive clinical work outside the system and treats internet-connected autonomy as inherently exposed.

Eleanor previously managed skills like careful software packages, and still does that for serious work, but Hermes made a looser mode click for her. *"Everything I'm going to show today and a lot of what's new and interesting to me is this YOLO approach of letting an agent roam free."* [\[00:42:17\]](https://youtube.com/live/ud2WzkKeDZs?t=2537)

<a href="https://youtube.com/live/ud2WzkKeDZs?t=2820"><img src="images/eleanor-fnord-hermes-instance.png" alt="Eleanor Berger showing Fnord, her Hermes agent instance, with skills, scheduled jobs, and child agents" /></a>
<sub>Eleanor shows the generated Fnord presentation page, including its installed skills, scheduled jobs, GPT 5.5 model route, and Discord interaction surface. <a href="https://youtube.com/live/ud2WzkKeDZs?t=2820">[00:47:00]</a></sub>

## On working with agents

### What she loves: speed with enough domain knowledge to evaluate the work

Eleanor loves the velocity gain because it changes which projects are worth starting. *"If something can't happen fast, I might just not do it, not bother."* [\[00:37:12\]](https://youtube.com/live/ud2WzkKeDZs?t=2232) Agents let her fire off work she previously deprioritized because the setup time was too high.

Agents also round up her capabilities when she knows enough to judge the result but does not have every syntax detail ready. *"If I know a little bit of what I'm doing, enough to have the confidence that I understand what it did and how to evaluate it, all of a sudden I got this exoskeleton."* [\[00:38:03\]](https://youtube.com/live/ud2WzkKeDZs?t=2283)

### What she finds most frustrating: agents understand intent better than scope

Eleanor's frustration is scope control. *"Agents get really good at understanding and interpreting intent, and they're still not very good at understanding scope."* [\[00:38:28\]](https://youtube.com/live/ud2WzkKeDZs?t=2308)

The scope failure appears when she asks for a one-pager and gets a novel, or asks for a comprehensive review and gets a paragraph. She sometimes fixes that by setting a concrete budget: *"This needs to be 500 tokens or less. You need to give something concrete, otherwise it will go on and on and on."* [\[00:39:55\]](https://youtube.com/live/ud2WzkKeDZs?t=2395)

## Workflows

### Verify infrastructure agents by realizing the system they changed

Eleanor wants agents to take on cloud-infrastructure work because it is boring and low-value for humans, but only when the verification surface is concrete. *"The verification is not getting an AI to look at the YAML files. The verification is to look at what happens when you run these YAML files and realize the cloud footprint."* [\[00:34:26\]](https://youtube.com/live/ud2WzkKeDZs?t=2066)

The reusable practice is to let the agent propose or edit configuration, then have the system instantiate it and sample what was actually created. *"Go ahead and actually realize this configuration and sample what it actually created. That's something I can trust."* [\[00:34:52\]](https://youtube.com/live/ud2WzkKeDZs?t=2092) AI review chains do not satisfy the same standard.

### Run a bounded Hermes instance for personal work

Eleanor runs Hermes on an old M1 Mac mini that was lying around. She likes the desktop environment, the small local GPU for embeddings and indexing, and [Tailscale](https://tailscale.com/) access, while keeping the box segregated. [\[00:42:51\]](https://youtube.com/live/ud2WzkKeDZs?t=2571)

The permission pattern changed over time. *"I started with having it ask me for permission for everything, and with time I gave it a bit more rope."* [\[00:56:20\]](https://youtube.com/live/ud2WzkKeDZs?t=3380) She feels confident enough to let it work on personal material, but she keeps it away from sensitive clinical data at Jiminy Health.

### Publish useful Hermes outputs as small Here Now pages

Eleanor uses a Here Now skill so her agent can publish HTML pages as a routine output. She asked Hermes to introduce itself shortly before the segment, and it researched, built an interactive web page, and published it to Here Now. [\[00:45:31\]](https://youtube.com/live/ud2WzkKeDZs?t=2731)

The publishing habit now runs through ordinary agent work. *"Now I just tell it, do a web page, publish it to Here Now. Sometimes I won't tell it and it will still publish it there because it knows from my configuration that it's what I expect."* [\[00:49:17\]](https://youtube.com/live/ud2WzkKeDZs?t=2957) She says she creates dozens of HTML pages every day because every small result can become a shareable page.

### Let Hermes turn recurring chores into scripts, caches, and scheduled jobs

Eleanor likes Hermes because scheduled work does not always engage the LLM. *"Hermes is quite good at knowing in what cases it can just create a script and do without an LLM, which for me is in many cases."* [\[00:48:00\]](https://youtube.com/live/ud2WzkKeDZs?t=2880)

Her Watch Later workflow shows the pattern. From a short phone chat on public transport, she asked Hermes to use a logged-in browser, collect videos from YouTube Watch Later, and create summaries so she could decide whether a video deserved an hour. [\[00:53:28\]](https://youtube.com/live/ud2WzkKeDZs?t=3208) Hermes invented a skill, maintained a cache of already processed videos, and used a script for the repeated work.

She uses the same preference for cron work more broadly. *"I create a lot of cron jobs all the time and a lot of them I under-specify."* [\[01:00:51\]](https://youtube.com/live/ud2WzkKeDZs?t=3651) Hermes decides when a deterministic process is enough, when to call an LLM from inside that process, and when the whole task needs a model. The same Hermes instance was also syncing to her [Anki](https://apps.ankiweb.net/) collection in the background while she walked through the demo. [\[00:49:43\]](https://youtube.com/live/ud2WzkKeDZs?t=2983)

## Skills

### Here Now publishing skill

Eleanor has a skill that lets her agent publish HTML pages to Here Now. *"I have a skill for that. It's very easy to get the agent to just publish HTML pages, which I do all the time."* [\[00:46:19\]](https://youtube.com/live/ud2WzkKeDZs?t=2779)

The skill turns web publishing into a default completion path. The agent can publish when explicitly asked, and sometimes publishes there because Eleanor's configuration tells it that is the expected destination.

### AnkiConnect / Anki collection management skill

Eleanor's Hermes instance was also managing her Anki flashcard collection in the background. She points to the running sync during the demo, then explains that she revises many flashcards every day and can now manage them with her agent and cron jobs. [\[00:49:43\]](https://youtube.com/live/ud2WzkKeDZs?t=2983)

The skill matters because it applies the same agent pattern to a private, recurring knowledge workflow: connect to the existing local app, automate the repetitive collection work, and schedule the pieces that do not need a full LLM call.

### Impeccable

Impeccable is the design skill Eleanor uses a lot. *"I'm terrible at design. I'm good at server farms, data sets, terminals, that works very well for me. I know absolutely nothing about design. But now, thanks to various skills, I can actually do things that look not too bad."* [\[00:50:17\]](https://youtube.com/live/ud2WzkKeDZs?t=3017)

She describes Impeccable as a large, elaborate skill that sets up design guidelines and follows them iteratively. She customizes style preferences such as dark mode, then evaluates the result by taste and legibility.

### YouTube Watch Later cache skill

The Watch Later summarizer became a skill that Hermes created for Eleanor. She did not hand-design the implementation. *"I asked very briefly in the chat and it invented this way to do it and it did a pretty good job."* [\[00:54:52\]](https://youtube.com/live/ud2WzkKeDZs?t=3292)

The skill uses a browser with Eleanor's logged-in YouTube session, collects Watch Later items, creates summaries, and maintains a cache of videos it has already processed.

## Tools / projects she showed

### Hermes

Hermes is the personal agent system that changed Eleanor's relationship to high-autonomy agents. She installed it a few weeks before the segment and says *"then it clicked"* [\[00:42:12\]](https://youtube.com/live/ud2WzkKeDZs?t=2532).

She likes its self-monitoring, approval behavior, scheduled jobs, and ability to decide when a task can be handled by scripts instead of LLM calls. She uses it through Discord, WhatsApp, CLI, API server, and a separate community web UI that lets her inspect skills and setup details. [\[00:48:36\]](https://youtube.com/live/ud2WzkKeDZs?t=2916)

### Fnord

Fnord is Eleanor's Hermes instance name. The self-introduction page it created says it has 157 skills, scheduled jobs, parallel child agents, GPT 5.5, Discord, and other interfaces. [\[00:46:38\]](https://youtube.com/live/ud2WzkKeDZs?t=2798)

The demo prompt was minimal: *"I want to present this Hermes instance to the audience. Create a cool interactive web page."* [\[00:47:23\]](https://youtube.com/live/ud2WzkKeDZs?t=2843)

### Here Now

Here Now is the HTML publishing service Eleanor uses for small generated web pages. She describes it as *"like gists, but for HTML"* [\[00:46:02\]](https://youtube.com/live/ud2WzkKeDZs?t=2762).

It replaced her ad hoc GitHub Pages publishing tricks. The agent can publish many small pages there, including the interactive page that introduced Fnord.

### Impeccable

Impeccable appears both as a literal skill and as a shown design artifact. Eleanor scrolls through it and points out that it is huge, with optimization guidance and an iterative design process. [\[00:51:27\]](https://youtube.com/live/ud2WzkKeDZs?t=3087)

Her use case is practical: she does not know how to specify fonts, spacing, or layout details, but she can judge whether the result is legible and pleasant to interact with.

### Codex app

Eleanor says her coding stack now primarily uses [Codex](https://openai.com/index/introducing-the-codex-app). *"For coding I primarily use Codex now. I really love the new app."* [\[01:01:35\]](https://youtube.com/live/ud2WzkKeDZs?t=3695)

She also says GPT 5.5 feels unrivaled to her currently, and she uses it heavily in Codex, Hermes, VS Code, and other tools.

### Warp Terminal

[Warp](https://www.warp.dev/terminal) is Eleanor's current terminal. She started using it after it became open source, and says it is *"really great for running agents and just for convenience"* [\[01:02:26\]](https://youtube.com/live/ud2WzkKeDZs?t=3746).

It appears in the stack answer rather than the Hermes demo, but it is part of her current agent-building environment.

### Zed

[Zed](https://zed.dev/) is the lighter editor Eleanor is experimenting with because she no longer edits files directly very often. She still looks at files, but says her editor needs are not large now that agents do most file changes. [\[01:02:13\]](https://youtube.com/live/ud2WzkKeDZs?t=3733)

She names it as a replacement for the instinctive habit of opening VS Code.

### VS Code

[VS Code](https://code.visualstudio.com/) is the editor Eleanor used to use for much of her work. In the segment, it marks how her coding behavior has shifted: she still opens files, but direct editing happens rarely. [\[01:01:59\]](https://youtube.com/live/ud2WzkKeDZs?t=3719)

She also names VS Code as one of the places where she uses GPT 5.5.

### OpenCode

[OpenCode](https://opencode.ai/) appears in Eleanor's tool-agnostic stack answer. She says she loves OpenCode and still uses it, while switching tools intentionally so her configuration does not rely on one vendor-specific feature. [\[01:04:07\]](https://youtube.com/live/ud2WzkKeDZs?t=3847)

The point of naming OpenCode is portability, not a separate live demo.

### Copilot

[Copilot](https://github.com/features/copilot) appears in the same stack answer as OpenCode. Eleanor says she still uses it, and she places it inside the broader practice of keeping configuration portable across tools. [\[01:04:11\]](https://youtube.com/live/ud2WzkKeDZs?t=3851)

### GPT 5.5

[GPT 5.5](https://openai.com/index/introducing-gpt-5-5/) is the model Eleanor credits as a major unlock for Hermes. *"It's fantastic. It's a really good model."* [\[00:44:00\]](https://youtube.com/live/ud2WzkKeDZs?t=2640)

She says she uses it almost exclusively across Codex app, Hermes, VS Code, and other environments.

## Principles and explainers

### AI review chains do not create certainty

Eleanor rejects AI validating AI as a safety strategy. *"If it were only now do another AI review and then do an AI review of the AI review, that's not something I can trust."* [\[00:35:06\]](https://youtube.com/live/ud2WzkKeDZs?t=2106)

The alternative is to verify behavior in the world the agent changed. For infrastructure, that means running the configuration and inspecting the cloud footprint.

### Agents help most when the human can evaluate the result

Eleanor says agents do not help much when she has no idea what she is doing. They work well when she knows enough to understand the result, find what is interesting, and evaluate whether the agent made a good choice. [\[00:37:53\]](https://youtube.com/live/ud2WzkKeDZs?t=2273)

Her cloud-infrastructure example applies the same boundary to higher-risk work: agents can do the boring parts only when the verification surface gives her confidence.

### Scope is a separate capability from intent

Eleanor separates understanding what the user wants from understanding how much work should be done. The model often gets the task concept right, then chooses the wrong size: a novel instead of a one-pager, or a paragraph instead of a comprehensive review. [\[00:38:42\]](https://youtube.com/live/ud2WzkKeDZs?t=2322)

She expects some of this to improve through her own skills and customization, system prompts, or future training.

### Autonomy plus internet access should be treated as exposed

Eleanor's Hermes setup is intentionally personal and segregated because she treats Simon Willison's [lethal trifecta](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/) as real. *"If you are getting instructions from the internet and you have connections out to the internet, you should assume that you're completely exposed."* [\[00:56:57\]](https://youtube.com/live/ud2WzkKeDZs?t=3417)

That is why the Mac mini can handle personal automations but does not get near sensitive clinical data from her day job.

### Use personal taste as the acceptance test when you are the user

When Hugo asks how she evaluates design, Eleanor says she is the main customer. *"If I look at it and it's legible to me, it looks nice to interact with, I'm good with that."* [\[00:52:19\]](https://youtube.com/live/ud2WzkKeDZs?t=3139)

She does not know how to instruct an agent on fonts and spacing, so a design skill supplies the process and she supplies the acceptance judgment.

### Keep agent configuration portable across tools

Eleanor currently uses Codex heavily, but she intentionally avoids making her configuration depend on one product. *"I try intentionally to be a little bit tool agnostic, to switch around, to make sure that my configuration will always work with all the different tools."* [\[01:04:11\]](https://youtube.com/live/ud2WzkKeDZs?t=3851)

That portability matters because her stack changes quickly. She still uses OpenCode, Copilot, VS Code, Zed, Warp, Hermes, and Codex in different places, and she describes the stack answer as only a current snapshot.

### Correct behavior matters more than the programming language

Eleanor says agents made her language-agnostic. She now uses TypeScript, Go, Rust, and whatever works, after decades of instinctively choosing Python. *"The verification for me is not about looking at the code. Verification is does it actually do what it needs to do."* [\[01:03:03\]](https://youtube.com/live/ud2WzkKeDZs?t=3783)

She still reaches for Python when writing code by hand, but says that now happens rarely.

## Additional quotations

- On delegating cloud infrastructure work: *"It's really boring work, not where any of us add a lot of value. So it would be great to delegate it, but I have to have this certainty."* [\[00:34:00\]](https://youtube.com/live/ud2WzkKeDZs?t=2040)

- On artifact-based verification: *"Anything other than that is not good enough."* [\[00:34:39\]](https://youtube.com/live/ud2WzkKeDZs?t=2079)

- On velocity: *"Now with agents, I just fire something off and it goes and does it."* [\[00:37:27\]](https://youtube.com/live/ud2WzkKeDZs?t=2247)

- On the exoskeleton effect: *"I can move so fast, do things that would be very effortful."* [\[00:38:14\]](https://youtube.com/live/ud2WzkKeDZs?t=2294)

- On the Hermes unlock: *"A few weeks ago I installed Hermes and then it clicked."* [\[00:42:12\]](https://youtube.com/live/ud2WzkKeDZs?t=2532)

- On the Mac mini: *"It's really good to have a desktop environment."* [\[00:43:12\]](https://youtube.com/live/ud2WzkKeDZs?t=2592)

- On GPT 5.5: *"It's fantastic. It's a really good model."* [\[00:44:00\]](https://youtube.com/live/ud2WzkKeDZs?t=2640)

- On Discord as an agent interface: *"The Discord integration is really good and it's very responsive and you can manage stuff in threads."* [\[00:45:11\]](https://youtube.com/live/ud2WzkKeDZs?t=2711)

- On Fnord's generated presentation: *"That's all I did here. So very YOLO and it looks like it did some interesting useful things."* [\[00:47:28\]](https://youtube.com/live/ud2WzkKeDZs?t=2848)

- On Here Now: *"I was very happy that someone is taking this job off me."* [\[00:46:12\]](https://youtube.com/live/ud2WzkKeDZs?t=2772)

- On Impeccable: *"I just benefit from the fact that someone developed it."* [\[00:51:47\]](https://youtube.com/live/ud2WzkKeDZs?t=3107)

- On Watch Later automation: *"I'm never going to have the time to watch all of them because it's just not enough time."* [\[00:53:01\]](https://youtube.com/live/ud2WzkKeDZs?t=3181)

- On the generated Watch Later skill wording: *"I would never refer to myself in the third person."* [\[00:54:48\]](https://youtube.com/live/ud2WzkKeDZs?t=3288)

- On clinical data boundaries: *"I don't think anytime soon I'll be okay with it getting close to that."* [\[00:56:42\]](https://youtube.com/live/ud2WzkKeDZs?t=3402)

- On Hermes choosing deterministic work: *"It's really good at figuring out when it will need to do something deterministic and when it should engage an LLM."* [\[01:01:01\]](https://youtube.com/live/ud2WzkKeDZs?t=3661)

- On Codex: *"Something with the new Codex app is just especially good. It's best in class, feels to me."* [\[01:04:07\]](https://youtube.com/live/ud2WzkKeDZs?t=3847)

- On the Agentic Ventures course: *"The focus moved a lot more into agentic engineering."* [\[01:08:33\]](https://youtube.com/live/ud2WzkKeDZs?t=4113)

## Live reactions and follow-ups

### Hugo tied the Hermes demo back to Matt's skill-security concern

Hugo asked Eleanor to connect Hermes and downloaded skills to Simon Willison's lethal trifecta after Matt had warned that markdown-rendered skill files can hide HTML comments from human reviewers. [\[00:55:23\]](https://youtube.com/live/ud2WzkKeDZs?t=3323) Eleanor answered by naming the risk directly: her Mac mini is segregated, personal, and kept away from sensitive clinical work because an agent with private data, untrusted internet instructions, and external communication should be treated as exposed. [\[00:56:12\]](https://youtube.com/live/ud2WzkKeDZs?t=3372)

### Matt added a deterministic-wrapper pattern for agent work

Matt used Eleanor's cron-job discussion to describe a related pattern: scripts should do deterministic preparation and cleanup, then invoke an agent for the small language-judgment step. His example was release-note drafting for spaCy, where the agent can draft but does not get push access. [\[00:57:53\]](https://youtube.com/live/ud2WzkKeDZs?t=3473)

### Discord filled in Hermes links and stack questions

During Eleanor's segment, Discord participants posted the [Hermes](https://hermes-agent.nousresearch.com/) site, [Impeccable](https://impeccable.style/), and Simon Willison's [lethal trifecta](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/) post. A later stack question asked whether her setup also used Obsidian or other note-taking tools; Eleanor answered in Discord that she uses Obsidian with `obsidian-cli` and `qmd` as her main knowledge base, with some notes written directly by local or remote agents.

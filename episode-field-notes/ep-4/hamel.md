# Hamel Husain - Episode 4 field notes

[Hamel Husain](https://hamel.dev/) is a machine learning engineer with over 20 years of experience, with work at Airbnb, GitHub, and DataRobot. Hugo introduces him as having done early LLM research used by OpenAI for code understanding, and as working to bring data science back to AI by helping teams debug, analyze, and measure their systems through evals.

His segment was a skeptical tour of agent skills: when they help, when they mislead, how to inspect them, and when a higher-fidelity tool such as an MCP is a better fit.

## On working with agents

### What he loves: agents make things easier

Hamel's answer is terse and unqualified: *"just makes a lot of things easier."* [\[00:06:02\]](https://youtube.com/live/XaYQFtca798?t=362)

### What he finds most frustrating: steering, especially for long writing

Hamel says he rarely gets frustrated with agents themselves. The frustration is usually his own steering problem, and it shows up most painfully in writing. *"If anything, I get frustrated with myself, not the agent, but."* He names the concrete failure mode as *"steering the agent sometimes,"* especially when he tries long-form AI writing, because *"it's really difficult for AI not to sound like slop unless you're, you are super in the loop."* [\[00:06:14\]](https://youtube.com/live/XaYQFtca798?t=374)

For long writing, he keeps the model in a narrower role: *"I use it more like an editor or like something that checks my writing rather than something that wholesale does the writing, especially long writing."* [\[00:07:11\]](https://youtube.com/live/XaYQFtca798?t=431)

## Skills

### Eval audit skill

Hamel showed a set of [eval-related skills](https://github.com/hamelsmu/evals-skills) distilled from his course materials, then argued that publishing them may have been the wrong abstraction. One of the skills audits eval setups for common mistakes: *"have a skills at one skill that had doesn't eval audit. So it will go through and will see if you're making any of the common mistakes that students make"* [\[00:23:18\]](https://youtube.com/live/XaYQFtca798?t=1398)

### RAG evaluation skill

The same skills collection includes a RAG-focused skill. Hamel describes it as *"another skill that's like. You know, trying to help you evaluate rag. like, you know, trying to help you put, make sure you have the right things in place."* [\[00:23:33\]](https://youtube.com/live/XaYQFtca798?t=1413)

### Error analysis skill

Hamel lists error analysis as another skill in the collection: *"There's another one for error analysis."* It is presented as part of a broader attempt to compress course knowledge into agent-invokable skill files. [\[00:23:42\]](https://youtube.com/live/XaYQFtca798?t=1422)

### LLM judge validation skill

Another skill checks whether an LLM judge is calibrated to human judgment. Hamel describes *"another one for validating that your LM judge is like calibrated to human and so on and so forth."* [\[00:23:43\]](https://youtube.com/live/XaYQFtca798?t=1423)

### Browser-internal-API skill for Maven work

Hamel's favorite use of skills is turning painful browser workflows into reusable agent procedures. He has skills for Maven tasks where the first run uses a browser extension and dev console access to discover internal routes, then later runs can act semi-programmatically. *"So yeah, have skills that basically, like I have skill that can just fill out a lightning lesson or like create a course page, like pseudo programmatically very quickly"* [\[00:43:12\]](https://youtube.com/live/XaYQFtca798?t=2592)

## Workflows

### Use AI as an editor for long writing

Hamel avoids delegating long-form prose wholesale. When writing, he keeps the agent close to review and editing instead of authorship: *"Like I just sort of am very careful. I use it more like an editor or like something that checks my writing rather than something that wholesale does the writing, especially long writing."* [\[00:07:11\]](https://youtube.com/live/XaYQFtca798?t=431)

### Prefer polished harnesses over maintaining your own orchestration

On [OpenClaw](https://openclaw.ai/), Hamel says he was spending more effort maintaining the harness than benefiting from it. *"I was spending more time making tools for OpenClaw and debugging OpenClaw than I was like using OpenClaw."* His conclusion was to use the harnesses he already uses elsewhere, because the vendor apps had closed much of the gap. [\[00:12:47\]](https://youtube.com/live/XaYQFtca798?t=767)

### Read the prompt and the skill before trusting it

Hamel repeatedly emphasizes inspection over hype. A lot of public skills, in his view, are just AI-written prompt dumps. *"Indeed those situations sometimes the skill is just a decompressed version of their prompt and It would be better just to have the prompt because I don't need all the slop of like this like skill"* [\[00:20:55\]](https://youtube.com/live/XaYQFtca798?t=1255)

His operating rule is simple: *"look at the prompt and Look at the skill"* [\[00:21:08\]](https://youtube.com/live/XaYQFtca798?t=1268)

### Judge shared skills using code-review-like signals

Hamel treats skills like code from GitHub. Signals include whether the author uses it, whether it is being iterated on, who published it, how stale it is, and whether it constrains the agent with actual tools or code. *"It's kind of like how you would judge code on GitHub in a lot of ways. It's like, I try to see like, what are some signals, you know, that you should take this skill seriously."* [\[00:35:22\]](https://youtube.com/live/XaYQFtca798?t=2122)

### Keep memory and skills in a scoped monorepo

Hamel's personal setup is intentionally simple: a monorepo with directories for different activity areas, each with contained skills and markdown memory. He uses the directory structure itself to avoid context pollution. *"I just write to markdown files and I sort of curate the skills very carefully in a directory structure."* [\[00:36:56\]](https://youtube.com/live/XaYQFtca798?t=2216)

He is explicit that the setup is not fancy: *"It's just a giant directory of just stuff that's organized."* [\[00:37:28\]](https://youtube.com/live/XaYQFtca798?t=2248)

### Point agents at your own writing

When Doug suggests that blog posts may be the right form for reusable knowledge, Hamel agrees. He already uses his own posts as distilled instructions for agents. *"Like I often end up pointing my agent at just my own blog post when I try to do things. super handy. It's like I already distilled the information in like the best way I can think of in this post."* [\[00:38:45\]](https://youtube.com/live/XaYQFtca798?t=2325)

### Turn browser clicking into a skill by capturing internal APIs

For sites without APIs or MCPs, Hamel has the agent use a browser extension, inspect the dev console, observe routes and network requests, then create a skill. The first run is slower because the agent must navigate manually, but later runs can use cookies and internal routes. *"I tell it to do a task, but while it's doing that task, I tell it to introspect. the internal API of that site and like pay attention to what the routes are and how to programmatically like do all the things."* [\[00:42:32\]](https://youtube.com/live/XaYQFtca798?t=2552)

### Use a walkthrough video as agent input

When John asks where to get the Maven skill, Hamel points to a video rather than a packaged artifact. *"so you just like, have a YouTube video actually that walks through it. You can just point your agent at the YouTube video and just say, just do what Hamel did here."* [\[00:44:11\]](https://youtube.com/live/XaYQFtca798?t=2651)

## Tools / projects he showed

### Codex Desktop

Hamel says [Codex Desktop](https://openai.com/index/introducing-the-codex-app/) pulled him away from the terminal because of its polish and integrated workflow. *"I never thought I would leave the terminal. And then I tried Codex Desktop app and I was like, wow, this is actually better. It like shocked me."* [\[00:08:23\]](https://youtube.com/live/XaYQFtca798?t=503)

He highlights computer use, scheduling, high-fidelity remote sessions, phone use, and fast mode within the subscription. On remote work: *"they have the best remote. system that I've used. you can run Codex headless on your Mac Mini, and then you can see all the sessions on your Mac Mini in the sidebar."* [\[00:09:21\]](https://youtube.com/live/XaYQFtca798?t=561)

### Codex fast mode

Hamel calls out a billing and UX distinction: Codex lets him use faster inference inside the monthly subscription rather than paying outside it. *"Codex will allow you to trigger fast within your billing, within your subscription. So like your $200 a month subscription, you can just, you can just toll your subscription at 1.5 X."* [\[00:10:27\]](https://youtube.com/live/XaYQFtca798?t=627)

### OpenClaw

[OpenClaw](https://openclaw.ai/) is a counterexample in Hamel's workflow. He tried it, then gave up because the tool required too much maintenance. *"I got frustrated with OpenClaw. Like I found that I was, I was spending more time making tools for OpenClaw and debugging OpenClaw than I was like using OpenClaw."* [\[00:12:47\]](https://youtube.com/live/XaYQFtca798?t=767)

### Devin from Cognition

Hamel now likes [Devin from Cognition](https://cognition.ai/), despite previously disliking it enough to write a critical blog post. The product shift is about proof of work: *"It's just super polished. Like the UX is so good. it does, so it's like wired up to always try to show you a demo video and screenshots of what it's done."* [\[00:16:55\]](https://youtube.com/live/XaYQFtca798?t=1015)

He connects this to eval ergonomics: *"the agent doing it, giving you a proof of work that you can super easily verify is huge."* [\[00:17:17\]](https://youtube.com/live/XaYQFtca798?t=1037)

### Cursor

Hamel still opens [Cursor](https://www.cursor.com/) when he wants to inspect files, edits, markdown, and prompts. The reason is especially strong for AI-facing code: *"It's helpful to see what files are being changed and just be able to look at things, especially when I'm trying to touch prompts or the AI part of the workflow, especially prompts. I believe you always have to look at the prompt if it's being changed."* [\[00:18:31\]](https://youtube.com/live/XaYQFtca798?t=1111)

### Claude and Claude Code

Hamel still uses [Claude](https://claude.ai/) for writing and creative work, mainly because he knows its behavior: *"I still use Claude for like writing and like creative tasks. just because I'm used to it, just cause like, I don't know, like I kind of understand it"* [\[00:11:31\]](https://youtube.com/live/XaYQFtca798?t=691)

He also notes that orchestration is moving into harnesses. Claude has loops, Codex has goals, and Claude Code has workflows, so increasingly *"you don't have to like orchestrate it yourself anymore."* [\[00:16:01\]](https://youtube.com/live/XaYQFtca798?t=961)

### Evals course skills collection

Hamel showed a collection of skills derived from his [evals course](https://maven.com/parlance-labs/evals), student Q&A, office hours, and book material. The [collection](https://github.com/hamelsmu/evals-skills) included eval audit, RAG evaluation, error analysis, and LLM-judge validation. He now treats the collection as a cautionary example because users may over-trust it. *"Publishing these skills may be leading lots of people in the wrong direction."* [\[00:24:17\]](https://youtube.com/live/XaYQFtca798?t=1457)

### Course chatbot and MCP, name not given on stream

Hamel replaced the static skill idea with a higher-fidelity course chatbot and a related installable MCP over the same course knowledge. The names were not given on stream. *"I ended up making this MCP"* because *"And just what it does is it just queries all of the knowledge. Like it queries the course."* [\[00:25:51\]](https://youtube.com/live/XaYQFtca798?t=1551), [\[00:26:25\]](https://youtube.com/live/XaYQFtca798?t=1585)

### skills.sh

Hamel used [skills.sh](https://skills.sh/) to analyze public skills. He describes it as *"a way to discover skills and install skills"* and says it is useful, then uses its download-ranked data to show how many popular skills have only one commit. [\[00:29:04\]](https://youtube.com/live/XaYQFtca798?t=1744)

### Anthropic front-end design skill

In the skills.sh analysis, Hamel points to a popular prompt-only [front-end design skill](https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md). *"one of the most popular ones is like this anthropic one front end design. Only one commit six months ago."* He says he used it for a long time, then stopped because his websites started looking the same. [\[00:30:27\]](https://youtube.com/live/XaYQFtca798?t=1827)

### GitHub Actions skill

Hamel also inspects a GitHub Actions skill with three commits and argues that it is essentially a sitemap of the docs. *"if you come to this GitHub actions, one is basically the site map of the GitHub actions docs."* [\[00:31:10\]](https://youtube.com/live/XaYQFtca798?t=1870)

### Browser extension, name not given on stream

For internal-API discovery, Hamel uses a browser extension. The specific extension name was not given on stream. *"use the Chrome extension, Claude has one, Codex has one"* and then ask the agent to inspect routes while doing the task. [\[00:42:32\]](https://youtube.com/live/XaYQFtca798?t=2552)

### Maven

[Maven](https://maven.com/) is Hamel's concrete example of a pre-AI web product with too much clicking. *"Maven doesn't like you to do anything on Maven, you have to click like thousands of buttons, right?"* He uses skills to fill out lightning lessons and create course pages more quickly. [\[00:43:01\]](https://youtube.com/live/XaYQFtca798?t=2581)

### YouTube walkthrough video

Hamel mentions a [YouTube video](https://www.youtube.com/watch?v=rOaaibIFf8o) that walks through the internal-API skill workflow. *"have a YouTube video actually that walks through it."* [\[00:44:11\]](https://youtube.com/live/XaYQFtca798?t=2651)

## Explainers

### Skills can create the illusion of completeness

Hamel's strongest critique of his own eval skills is that users will treat them as comprehensive. Even if the author says to customize them, users often will not. *"I tried to say like, don't just use these skills, like customize it for yourself. But like no one, if you release skills, no one is going to customize it. No one's going to look at it. Okay. There's just human nature."* [\[00:24:31\]](https://youtube.com/live/XaYQFtca798?t=1471)

The result is false confidence: *"people will feel like they're done. Like you have this eval skill, you must be doing it right."* [\[00:24:42\]](https://youtube.com/live/XaYQFtca798?t=1482)

### A skill is a lossy compression of knowledge

The reason Hamel moved toward an MCP is fidelity. His course contains thousands of hours of instruction, office hours, Q&A, and nuanced eval situations. Compressing all of that into markdown skills throws away too much. *"it's unreasonable to just push them all into a skill. Because a skill is like a compression, right? And like, like I said, people over-rely on the skill."* [\[00:25:34\]](https://youtube.com/live/XaYQFtca798?t=1534)

### MCPs can answer nuanced questions better than static skills

Hamel's MCP searches the course knowledge rather than trying to encode it all in advance. In his golden-dataset example, the system searches the course sources, produces an answer, and can be installed into the user's harness. *"The reason this is better, because now you have more fidelity for like the kind of information I'm trying to give people. I'm like, okay, this is higher fidelity. You can actually get answers to your nuance question and you can go like way further."* [\[00:26:56\]](https://youtube.com/live/XaYQFtca798?t=1616)

### Code and tools are stronger skill signals than prompt-only files

Hamel frames a skill's value as the degree to which it usefully constrains the agent. Prompt-only skills are often just someone else's prompt, while code and tools can encode concrete constraints. *"If it's just a single prompt in a single file, that seems a little bit less useful, honestly. If it's like a bunch of code tools, things like that, that's more of a signal that is like trying to constrain your agent more and thus maybe more useful because someone has found. useful constraints."* [\[00:28:25\]](https://youtube.com/live/XaYQFtca798?t=1705)

### Commit history is a weak but useful smell test

Hamel does not claim one commit means a skill is bad in every case, but he uses it as a skepticism trigger. In his skills.sh sample, about a third of the top 300 skills had only one commit. *"If you're to use a skill, if it's not being iterated on, you have to tune up your skepticism a little bit and say, maybe this skill is very shallow and the ceiling might be very low in terms of what the skill is imparting to you because it's not being iterated on."* [\[00:29:27\]](https://youtube.com/live/XaYQFtca798?t=1767)

### Prompt-only skills need adaptation, not wholesale adoption

Hamel warns that most skills are prompts, which makes them highly contextual. Before using one, read it and decide what applies. *"if you're gonna just adopt someone else's prompts wholesale, okay, you have to think like, you should be reading the prompt and figuring out like, what applies to you and what doesn't."* [\[00:30:02\]](https://youtube.com/live/XaYQFtca798?t=1802)

### Blog posts may be better long-lived knowledge than skills

Responding to Doug's suggestion that agents should be better at web research, Hamel argues that writing for yourself still matters. If a post already contains your best explanation, the agent can use that directly. *"the first person you want to be useful is yourself. And so like, absolutely. I think you should. Like I often end up pointing my agent at just my own blog post when I try to do things."* [\[00:38:42\]](https://youtube.com/live/XaYQFtca798?t=2322)

### Browser skills are a bridge for pre-AI websites

For websites without APIs or MCPs, Hamel turns manual clicks into repeatable procedures by making the first run investigative. The agent watches routes, traffic, requests, and cookies, then uses that knowledge later. *"the skill has access to the dev console and can listen to all the network traffic and can see like what requests are being sent, what requests are, you know, how to do like, how to hit the internal API routes."* [\[00:43:26\]](https://youtube.com/live/XaYQFtca798?t=2606)

This is how he handles older web tools: *"this is like a lot of websites are still pre-AI, like lot of tools. And so that's how I get over that frustration."* [\[00:43:54\]](https://youtube.com/live/XaYQFtca798?t=2634)

## Additional quotations

- On Codex Desktop's UI: *"I think it's unparalleled, meaning, you know, it's just super polished and very impressive."* [\[00:08:25\]](https://youtube.com/live/XaYQFtca798?t=505)
- On the user-experience gap created by fast mode: *"Because the best models at high thinking is quite slow. So it just makes a huge difference."* [\[00:11:12\]](https://youtube.com/live/XaYQFtca798?t=672)
- On vendor harnesses absorbing orchestration: *"I think a lot of the orchestration that you had to do is like disappearing and going, you know, the harnesses are like absorbing them."* [\[00:16:02\]](https://youtube.com/live/XaYQFtca798?t=962)
- On Devin's price: *"It is expensive though, it's very expensive. But you know, some less more is less expensive than a human, I think. So it's fine."* [\[00:17:30\]](https://youtube.com/live/XaYQFtca798?t=1050)
- On his own skills becoming suspect: *"Also, if you look at my skills, like, okay, like I haven't updated in two months. So was like, am I using the skill? No, because I'm using this other thing."* [\[00:27:27\]](https://youtube.com/live/XaYQFtca798?t=1647)
- On the overall warning: *"When you see a skill, you should whisper to yourself, maybe fuck your skills, including my skills. Don't trust anyone's Even if they're my skills, just be careful."* [\[00:32:20\]](https://youtube.com/live/XaYQFtca798?t=1940)
- On using agents to clean the memory directory: *"sometimes I'll use an agent to clean up my directory as well."* [\[00:37:21\]](https://youtube.com/live/XaYQFtca798?t=2241)
- On the future of YouTube in an agentic world: *"I also don't know what's gonna happen to YouTube eventually, because I don't know who's gonna, like lot of videos, maybe people won't watch, I don't know."* [\[00:44:50\]](https://youtube.com/live/XaYQFtca798?t=2690)

## Live reactions and follow-ups

### Hugo's pushback: skills as shareable instructional memory

Hugo pushed back on one piece of Hamel's argument: the value of a shared skill is not necessarily that someone installs it unchanged. It can be a way to transmit a workflow, then let another builder adapt it. His example was Anthropic's skill creator skill: *"the way they've done their skill doesn't quite work for me for a number of reasons. And I want to make sure that then I can test the skill in a variety of ways. And so I have my own version of their skill."* [\[00:34:29\]](https://youtube.com/live/XaYQFtca798?t=2069)

Hamel accepted the sharing point, but kept the evaluation frame: *"it's kind of like how you would judge code on GitHub in in a lot of ways."* He still wants signals before trusting a skill. [\[00:35:22\]](https://youtube.com/live/XaYQFtca798?t=2122)

### Chris's follow-up: customize, do not hoard

Chris picked the thread back up in the next segment. He said he agreed with *"a fair bit of what Hamel had to say"* and described backing away from downloading piles of skills or MCP servers just because they exist. The failure mode is context bloat and stale or irrelevant instructions. [\[00:52:50\]](https://youtube.com/live/XaYQFtca798?t=3170)

But Chris also named the useful version of the pattern: write or adapt skills for your own harness and your own work. For PyMC, a version-specific skill can help agents avoid old PyMC3 patterns when PyMC6 has just shipped. For Pi, he prefers asking the harness to write the skill he needs, then iterating it locally.

### Discord reaction: skill slop has entered the chat

The Discord picked up Hamel's critique immediately. A few representative reactions:

- *"Haha, skill as twitter hype is 100% correct"*
- *"most skills need to prune 60-80% of their lines"*
- *"I feel somewhat confused by folks going round going 'I have like 200 skills!' - surely less but more high quality is better?"*
- *"So we are in the age of 'skill slop'? This is a very interesting discussion"*
- *"Yeah! Perhaps it is about finding a good enough starting-point skill so you can customize it to your own needs."*

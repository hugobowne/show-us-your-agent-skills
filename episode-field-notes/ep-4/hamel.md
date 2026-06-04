# Hamel Husain - Fuck Your Skills And Fuck Mine Too - Episode 4 field notes

[Hamel Husain](https://hamel.dev/) is a machine learning engineer with more than 20 years of experience across Airbnb, GitHub, DataRobot, and early code-understanding research. His Episode 4 segment is the "Fuck Your Skills" segment: a direct warning that public agent skills can be useful, but they can also compress too much judgment, make people feel done, and hide whether the author is still using the thing they published.

He opens the screen-share portion with a slide titled "Fuck Your Skills" and the subtitle "(And mine too)." The lead is not just "be skeptical of other people's skills." It is fuck your skills and fuck mine too: every shared skill, including Hamel's own, has to earn trust after inspection. Near the end of the talk, he makes the spoken rule just as blunt: *"When you see a skill, you should whisper to yourself, maybe fuck your skills, including my skills."* [[00:32:20]](https://youtube.com/live/XaYQFtca798?t=1940)

He puts his own eval skills on blast first. After teaching more than 4,500 people, accumulating thousands of hours of office hours and Q&A, and publishing skills for eval audit, RAG evaluation, error analysis, and LLM-judge calibration, he says the skill bundle created the wrong incentive: *"Publishing these skills may be leading lots of people in the wrong direction."* [[00:24:17]](https://youtube.com/live/XaYQFtca798?t=1457)

The alternative he shows is higher-fidelity context: a course chatbot and MCP that search the underlying course materials instead of compressing every eval edge case into a skill. His rule for other people's skills is equally blunt: read the prompt, check whether the author iterates, look for real constraints, and treat one-commit prompt bundles as suspect until they prove otherwise.

Related workflow: [`skill-scepticism`](../../workflows/skill-scepticism/) turns Hamel's "fuck your skills and fuck mine too" argument into an intake loop for deciding whether to trust, adapt, replace, or reject a shared agent skill.

<a href="https://youtube.com/live/XaYQFtca798?t=1325"><img src="images/hamel-fuck-your-skills.png" alt="Hamel Husain showing a slide titled Fuck Your Skills with the subtitle And mine too" /></a>
<sub>Hamel opens his screen share with the title slide: "Fuck Your Skills," and underneath it, "(And mine too)." <a href="https://youtube.com/live/XaYQFtca798?t=1325">[00:22:05]</a></sub>

## On working with agents

### What he loves: agents make many things easier

Hamel's answer is intentionally short: *"It just makes a lot of things easier."* [[00:06:02]](https://youtube.com/live/XaYQFtca798?t=362) He spends the rest of the segment showing where ease comes from for him now: polished harness UX, remote sessions, mobile access, proof-of-work screenshots, and skills that can turn repetitive browser work into semi-programmatic workflows.

### What he finds most frustrating: steering writing without making slop

Hamel says he rarely gets frustrated with agents themselves. The frustration lands on the steering burden, especially in long-form writing. *"It's just steering the agent sometimes."* [[00:06:44]](https://youtube.com/live/XaYQFtca798?t=404)

For long writing, he avoids asking AI to produce large blocks wholesale because the output needs heavy human steering to avoid generic prose. *"It's really difficult for AI not to sound like slop unless you are super in the loop."* [[00:06:57]](https://youtube.com/live/XaYQFtca798?t=417) He uses AI more as an editor or checker than as the main writer.

## Workflows

### Choose agent harnesses that make remote work and review cheaper

Hamel has moved more work into Codex Desktop because the interface, remote sessions, mobile behavior, and billing shape reduce the work around the work. *"I never thought I would leave the terminal. And then I tried Codex Desktop app, and I was like, 'Wow, this is actually better.'"* [[00:08:34]](https://youtube.com/live/XaYQFtca798?t=514)

The details matter to him as product mechanics. Codex can run headless on a Mac Mini while showing the sessions in the desktop sidebar, SSH through the app, work well on phone, and trigger fast mode inside the subscription. Those pieces add up because the slowest frontier model settings make interaction latency part of the user experience.

He gives the broader pattern as harness absorption. Loops, goals, workflows, scheduling, and remote control used to require more homegrown orchestration. *"The harnesses are absorbing them."* [[00:15:39]](https://youtube.com/live/XaYQFtca798?t=939)

Hamel changed his mind about [Devin](https://devin.ai/) from [Cognition](https://cognition.ai/) because the product consistently tries to show demo videos and screenshots of what it did. He connects that to eval speed: *"The agent doing it, giving you a proof of work that you can super easily verify is huge."* [[00:17:17]](https://youtube.com/live/XaYQFtca798?t=1037)

The same product expectation applies to Cursor on cloud and Slack integrations. He values agent systems that reduce debugging, show visible evidence, and make review cheaper than rerunning the whole task in his head.

### Inspect prompts and AI-facing code before trusting behavior

Hamel still opens Cursor when he needs to inspect changed files, edit markdown, or read the AI-facing parts of a workflow. The hard rule is prompt review: *"You always have to look at the prompts if it's being changed."* [[00:18:39]](https://youtube.com/live/XaYQFtca798?t=1119)

That practice connects his day-to-day editing workflow to his critique of public skills. A skill can be a decompressed prompt, a stale artifact, or a code-backed constraint system. Reading the prompt is the first check before trusting the agent behavior it creates.

### Replace broad eval skills with searchable course knowledge

Hamel published [eval skills](https://github.com/hamelsmu/evals-skills) for common student problems, then decided the skill format was too compressed for the knowledge base he actually has. Evals questions include multimodal cases, PII constraints, RAG evaluation, golden data, and LLM-judge calibration. He says, *"It's unreasonable to just push them all into a skill."* [[00:25:34]](https://youtube.com/live/XaYQFtca798?t=1534)

His replacement is a chatbot and MCP that query the course sources directly. A student can ask a nuanced eval question, the system searches course materials, and the MCP gives the agent the same higher-fidelity access without forcing that person into a web app. *"There's no reason for me to compress all of that knowledge into a skill."* [[00:27:12]](https://youtube.com/live/XaYQFtca798?t=1632)

When Doug suggests that agents may need better research over blog posts rather than more skills, Hamel agrees from his own writing practice. *"I often end up pointing my agent at just my own blog post when I try to do things."* [[00:38:46]](https://youtube.com/live/XaYQFtca798?t=2326)

The reason is reuse of distillation. A blog post can be the best version of how he has already explained a problem, and the agent can use that explanation directly instead of relying on a compressed skill.

### Evaluate skills by iteration, ownership, and constraints

Hamel's skill-review workflow looks like code review. He asks whether the author is using the skill, whether it is being iterated on, how old it is, whether it is mostly prompt text, and whether it contains code or tools that constrain the agent. *"Look at if the skill is being iterated on. Look at the commit history, the age of the skill."* [[00:27:49]](https://youtube.com/live/XaYQFtca798?t=1669)

The constraint test is practical. A single prompt in one file may only be someone else's prompt. A skill with code, tools, scripts, or other hard structure shows that someone found constraints useful enough to package. *"The more constraints that your skill imposes, it's some signal that is good."* [[00:28:21]](https://youtube.com/live/XaYQFtca798?t=1701)

The slogan is not anti-skill. Fuck your skills and fuck mine too means every shared skill still has to pass an intake loop: read it, inspect the provenance, check the maintenance trail, decide what applies, and adapt it before it becomes policy. That loop is captured separately as the [`skill-scepticism`](../../workflows/skill-scepticism/) workflow.

### Keep memory and skills in a curated monorepo

Hamel describes his own setup as simple: a monorepo with directories for writing, course work, eval memes, and other recurring domains. He navigates into the relevant directory so only the local skills and markdown context shape the agent. *"That's basically my memory system as well. I just write to markdown files and I sort of curate the skills very carefully in a directory structure."* [[00:36:53]](https://youtube.com/live/XaYQFtca798?t=2213)

The directory layout is his context-management mechanism. He sometimes asks an agent to clean it up, but he avoids a giant always-on memory surface because too much context can make the agent behavior weird.

### Turn painful browser tasks into skills that learn internal APIs

Hamel's favorite skill use is for websites that still require manual clicking and do not expose public APIs or MCPs. He uses a browser extension, asks the agent to perform the task once, and tells it to inspect the site's internal API while it works. *"I tell it to do a task, but while it's doing that task, I tell it to introspect the internal API of that site."* [[00:42:37]](https://youtube.com/live/XaYQFtca798?t=2557)

The first pass may require clicking through the UI. The resulting skill captures routes, network requests, cookie handling, and programmatic calls so later runs can fill a [Maven](https://maven.com/) lightning lesson or create a course page without thousands of clicks. *"The skill has access to the dev console and can listen to all the network traffic."* [[00:43:26]](https://youtube.com/live/XaYQFtca798?t=2606)

## Skills

### evals-skills bundle

Hamel names several skills inside his published [evals-skills](https://github.com/hamelsmu/evals-skills) bundle, then uses the bundle as his cautionary example. The eval audit skill checks systems for common mistakes his students make: *"One skill does an eval audit. It will go through and see if you're making any of the common mistakes that students make."* [[00:23:05]](https://youtube.com/live/XaYQFtca798?t=1385)

The bundle also includes skills for RAG evaluation, error analysis, and LLM-judge calibration. Hamel describes one as *"trying to help you evaluate RAG"* and another as *"validating that your LLM judge is calibrated to human."* [[00:23:18]](https://youtube.com/live/XaYQFtca798?t=1398)

The skills can encode common checks, but they cannot answer every nuanced course question about multimodal systems, privacy constraints, golden data, and evaluation tradeoffs. Hamel's "and mine too" matters here: he is not only dunking on other people's public skills, he is using his own eval bundle as the object lesson.

### Maven browser skill

Hamel has skills for Maven workflows that inspect internal browser APIs. One can fill out a lightning lesson, and another can create a course page semi-programmatically. *"I have skills that basically can just fill out a lightning lesson or create a course page pseudo-programmatically very quickly."* [[00:43:12]](https://youtube.com/live/XaYQFtca798?t=2592)

These are literal skills because they package a repeatable agent behavior with browser-extension access, dev-console visibility, route discovery, and cookie reuse.

### Front-end design skill

Hamel inspects the popular [Anthropic front-end design skill](https://github.com/anthropics/skills/tree/main/skills/frontend-design) as a prompt-only skill he used for a while and then stopped using. *"I just got tired of my websites looking the same, so I stopped using it."* [[00:30:54]](https://youtube.com/live/XaYQFtca798?t=1854)

He does not say the skill is necessarily bad. He uses it to show why age, commit history, prompt-only structure, and observed output sameness all belong in the trust evaluation.

### GitHub Actions skill

Hamel uses a GitHub Actions skill as another example from skills.sh. He says it has three commits, then looks at the contents and concludes it is basically a sitemap for the [GitHub Actions](https://docs.github.com/actions) docs. *"That's all this skill is."* [[00:31:14]](https://youtube.com/live/XaYQFtca798?t=1874)

His practical judgment is that he battles GitHub Actions often and does not think he needs that skill if he is already using the GitHub CLI.

## Tools / projects he showed

### Codex Desktop

Codex Desktop is the harness Hamel says pulled him away from the terminal. He likes the UI polish, native Mac computer use, scheduling, high-fidelity remote sessions, mobile behavior, and fast mode inside the subscription. *"That sort of polish just makes this really compelling."* [[00:08:58]](https://youtube.com/live/XaYQFtca798?t=538)

He contrasts it with Claude's remote-control edge cases on mobile and external fast-mode billing. Product UX changes whether he actually uses the agent everywhere.

### OpenClaw

OpenClaw appears as the tool Hamel stopped using after spending too much time maintaining the tool layer. *"I was spending more time making tools for OpenClaw and debugging OpenClaw than I was using OpenClaw."* [[00:13:11]](https://youtube.com/live/XaYQFtca798?t=791)

He says the gap between OpenClaw and Codex or other harnesses was shrinking, while vendor automations and integrations were absorbing more of the work he used to orchestrate himself.

### Devin from Cognition

[Devin](https://devin.ai/) is the coding harness Hamel says he changed his mind about. He used to dislike it and wrote critically about it early on, then came back because the UX had become polished. *"It's wired up to always try to show you a demo video and screenshots of what it's done."* [[00:17:00]](https://youtube.com/live/XaYQFtca798?t=1020)

He also praises its Slack integration and treats its expense as acceptable when it reduces human coordination or review cost.

### Cursor

[Cursor](https://cursor.com/) remains Hamel's visual inspection and editing environment. He opens it to see changed files, inspect prompts, edit markdown, and read AI workflow code. [[00:18:16]](https://youtube.com/live/XaYQFtca798?t=1096)

He also expects Cursor cloud to follow the proof-of-work pattern where the agent returns screenshots or demos that are easy to evaluate.

### Claude Code

[Claude Code](https://www.anthropic.com/product/claude-code) appears throughout the segment as a comparison point for loops, fast mode, workflow support, browser extension use, and skill generation. Hamel says Claude Code has loop support and workflow support, which means users no longer have to orchestrate as much manually. [[00:15:47]](https://youtube.com/live/XaYQFtca798?t=947)

He still uses Claude for writing and creative tasks because he knows its behavior, but he says Codex has pulled him away for much of his agent work.

### Claude

Claude is the system Hamel still uses for writing and creative tasks. *"I still use Claude for writing and creative tasks, just because I'm used to it."* [[00:11:18]](https://youtube.com/live/XaYQFtca798?t=678)

It also appears as the comparison point for remote control, fast-mode billing, and browser-extension workflows.

### Eval course chatbot and MCP

Hamel shows a course chatbot that can search the course sources and answer nuanced eval questions. The MCP exposes the same underlying course-search behavior to an agent, so users do not have to open the web app. *"There's an MCP that you can install that will do the same thing."* [[00:26:43]](https://youtube.com/live/XaYQFtca798?t=1603)

The tool replaces his own eval skills as the preferred interface because it preserves more source knowledge than a compressed skill file.

### skills.sh

Hamel uses [skills.sh](https://skills.sh/) as the discovery surface for his small data analysis of popular skills. He describes it as *"a way to discover skills and install skills."* [[00:28:57]](https://youtube.com/live/XaYQFtca798?t=1737)

He took the top 300 skills by downloads and counted commits. The finding drives his skepticism: *"About a third of all those skills only have one commit."* [[00:29:15]](https://youtube.com/live/XaYQFtca798?t=1755)

### Maven

[Maven](https://maven.com/) is Hamel's example of a pre-AI web product where repetitive course operations still require too many clicks. He says Maven makes users click thousands of buttons for course work such as lightning lessons and course pages. [[00:43:01]](https://youtube.com/live/XaYQFtca798?t=2581)

His Maven skills use browser-extension access and internal API discovery to fill out lightning lessons and create course pages faster.

### Browser extension

The browser extension is the bridge between manual web UI and repeatable agent skill. Hamel says both Claude and Codex have one, and he uses it to let the agent perform a browser task while inspecting network calls and internal routes. [[00:42:32]](https://youtube.com/live/XaYQFtca798?t=2552)

The extension matters because many websites still lack public APIs or MCPs. It gives the agent enough access to discover how the site works and later bypass slow clicking.

## Principles and explainers

### Skills can create false completion

Hamel's strongest warning is about user behavior. Even when he tells people to customize a skill, he expects many users to install it, trust the author's name, and stop thinking. *"People will feel like they're done. Like you have this eval skill, you must be doing it right because you have Hamel's eval skill."* [[00:24:42]](https://youtube.com/live/XaYQFtca798?t=1482)

The same failure can happen with any public skill. A named skill can make the workflow look comprehensive even when it is only a thin compression of one person's current instructions.

That is why the segment's line has to include both sides: fuck your skills and fuck mine too. Hamel's own skills create the false-completion risk precisely because his name and evals course give them authority.

### A skill is a compression of context

Hamel's eval example turns into a general rule: a skill compresses knowledge, and compression can destroy the nuance the user actually needs. *"The skill is like a compression, right?"* [[00:25:39]](https://youtube.com/live/XaYQFtca798?t=1539)

That is useful when the task is narrow and the constraints are known. It is dangerous when the domain has many edge cases, such as multimodal evals, PII, RAG systems, golden datasets, and human-calibrated judges.

### Iteration is a trust signal

Hamel treats stale skills as a reason to increase skepticism. If the author is not using or updating the skill, the ceiling may be low. *"If it's not being iterated on, you have to tune up your skepticism a little bit."* [[00:29:22]](https://youtube.com/live/XaYQFtca798?t=1762)

The one-commit statistic is not a universal condemnation. He notes that some comedy skills may only need one commit. His point is contextual: the more serious the workflow, the more commit history, ownership, and usage should matter.

### Prompt-only skills are often someone else's prompt

Hamel says most skills are prompts, which means adopting them wholesale is adopting someone else's instructions without understanding fit. *"Most skills are just prompts. They're someone else's prompts."* [[00:29:52]](https://youtube.com/live/XaYQFtca798?t=1792)

His recommendation is to read the prompt and decide what applies. A skill can be less useful than the author's original prompt when the skill file is just a decompressed version of someone else's instructions.

### Code and tools can constrain the agent better than prose

Hamel distinguishes prompts from executable constraints. A skill with code, tools, scripts, and browser mechanics can narrow the agent's behavior in ways plain prose may not. *"If it's like a bunch of code, tools, things like that, that's more of a signal that it's trying to constrain your agent more."* [[00:28:31]](https://youtube.com/live/XaYQFtca798?t=1711)

The Maven browser skill shows that principle in practice. The useful constraint is not a paragraph saying "use Maven well." It is dev-console access, route discovery, cookie handling, and repeatable API calls.

### Judge skills the way you judge code

When Hugo asks whether shared skills can become personalized instructional memory, Hamel agrees with the sharing value but keeps the trust frame. *"It's kind of like how you would judge code on GitHub in a lot of ways."* [[00:35:41]](https://youtube.com/live/XaYQFtca798?t=2141)

The publisher matters. A skill from someone he trusts carries a different prior than a viral prompt bundle, but he still looks for concrete signals that the skill is useful for his workflow.

### Skills can transmit expert practice when users adapt them

Hugo pushes back on the idea that skills are only prompt slop by naming their best use as instructional memory: *"the ability of skills to encode instructional memory so we can see how experts do things and then adapt that to our workflows."* [[00:45:35]](https://youtube.com/live/XaYQFtca798?t=2735)

Chris Fonnesbeck makes the same useful-skill case from PyMC. He agrees with Hamel's warning about loading every skill or MCP that looks relevant, then draws the boundary around current, domain-specific practice. *"There are really useful applications of skills,"* he says, because a PyMC modeling skill can help when model pretraining and public examples lag a new PyMC release by months. [[00:53:32]](https://youtube.com/live/XaYQFtca798?t=3212)

That counterargument fits Hamel's thesis rather than weakening it. A useful skill is not an authority object to install and forget. It is a cached, inspectable version of expert practice that the user still has to read, adapt, and keep current.

### Blog posts can be reusable agent context

Hamel connects agent context to the old habit of writing for your future self. People search for a problem, find their own blog post or Stack Overflow answer, and benefit from their past distillation. *"That's kind of why you wrote it in the first place, because the first person you want to be useful is yourself."* [[00:38:39]](https://youtube.com/live/XaYQFtca798?t=2319)

For agents, that means a blog post can serve as durable, high-quality context. It can be easier to point the agent at the best explanation than to maintain a separate skill for the same knowledge.

### Browser agents matter because many tools still lack APIs

Hamel's browser-skill example is also an explanation of the web's transition state. *"A lot of websites are still pre-AI."* [[00:43:54]](https://youtube.com/live/XaYQFtca798?t=2634)

Those sites may not expose APIs or MCPs, but browser agents can still observe the internal routes that power the UI. Skills can preserve that discovery so later runs operate closer to programmatic automation.

## Additional quotations

- On OpenClaw maintenance: *"I was spending more time making tools for OpenClaw and debugging OpenClaw than I was using OpenClaw."* [[00:13:11]](https://youtube.com/live/XaYQFtca798?t=791)

- On vendor harnesses absorbing custom orchestration: *"You don't have to orchestrate it yourself anymore."* [[00:16:01]](https://youtube.com/live/XaYQFtca798?t=961)

- On Devin's review surface: *"That's what a good product is, if you can eval it quickly."* [[00:17:21]](https://youtube.com/live/XaYQFtca798?t=1041)

- On prompt inspection: *"You always have to look at the prompts if it's being changed."* [[00:18:39]](https://youtube.com/live/XaYQFtca798?t=1119)

- On Twitter skills: *"A lot of skills that you see out there, I believe, are made for Twitter."* [[00:19:54]](https://youtube.com/live/XaYQFtca798?t=1194)

- On one-commit skills: *"Is the author using it?"* [[00:20:29]](https://youtube.com/live/XaYQFtca798?t=1229)

- On his own eval skills: *"I ended up hating my own skill."* [[00:24:53]](https://youtube.com/live/XaYQFtca798?t=1493)

- On course-search fidelity: *"You can actually get answers to your nuanced question and you can go way further."* [[00:27:05]](https://youtube.com/live/XaYQFtca798?t=1625)

- On skills.sh: *"I love looking at data, and I think it's useful even outside evals."* [[00:28:50]](https://youtube.com/live/XaYQFtca798?t=1730)

- On checking a skill's contents: *"You have to see, what is this?"* [[00:31:07]](https://youtube.com/live/XaYQFtca798?t=1867)

- On trusted publishers: *"If John gave me a skill or Brian gave me a skill, it's like, okay, yeah, I'll trust this skill."* [[00:35:30]](https://youtube.com/live/XaYQFtca798?t=2130)

- On his memory setup: *"It's not fancy. It's just a giant directory of stuff that's organized."* [[00:37:28]](https://youtube.com/live/XaYQFtca798?t=2248)

- On writing for agents and humans: *"People should write more blog posts."* [[00:38:58]](https://youtube.com/live/XaYQFtca798?t=2338)

- On browser skills: *"That's how I get over that frustration. It's my absolute favorite thing in the whole world."* [[00:44:00]](https://youtube.com/live/XaYQFtca798?t=2640)

- On the segment thesis: *"When you see a skill, you should whisper to yourself, maybe fuck your skills, including my skills. Don't trust anyone's."* [[00:32:20]](https://youtube.com/live/XaYQFtca798?t=1940)

## Live reactions and follow-ups

### Discord surfaced Hamel's eval skills and browser walkthrough

Hugo posted Hamel's [evals-skills](https://github.com/hamelsmu/evals-skills) repo while Hamel was discussing why his own eval skill bundle had become a cautionary example. John later posted Hamel's [Turn Any Website Into an API With Claude Code](https://www.youtube.com/watch?v=rOaaibIFf8o) walkthrough when the conversation turned to browser agents learning internal APIs.

### Hugo and Chris kept the useful-skill counterweight in view

Hugo's live pushback is that skills can preserve expert workflow, not just instructions. His PyMC example is about learning how Chris approaches Bayesian modeling and then adapting that practice to his own work, with human judgment still in the loop. Chris then sharpens the practical case: a maintained PyMC skill can be useful when models and public examples are stale relative to the current library.

That makes the debate more precise. Hamel's rule is fuck your skills and fuck mine too, not "skills never help." Hugo and Chris both point to the cases where a skill is useful because it carries fresh expert practice, current API usage, or a narrow workflow that would be expensive to reconstruct from generic model knowledge.

### The chat turned Hamel's warning into a skill-quality debate

The live chat reacted directly to Hamel's critique. One viewer wrote, *"skill as twitter hype is 100% correct,"* another wrote that *"most skills need to prune 60-80% of their lines,"* and another asked whether the community was entering the age of *"skill slop."* Hugo also replied *"he said it"* when the title-slide joke became the explicit spoken line. Those reactions tracked the segment's main tension: shared skills are useful only when the user reads, adapts, and constrains them instead of installing them as authority.

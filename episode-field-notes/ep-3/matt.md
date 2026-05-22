# Matthew Honnibal — Episode 3 field notes

Matthew Honnibal is a computational linguist from Sydney now based in Berlin, co-author of spaCy and co-founder of Explosion. His segment centered on code quality verification workflows, the philosophical challenges of evaluating agent performance, and a platform in beta for agent-assisted NLP and data project development. His distinctive angle: rather than trying to prevent mistakes upfront via prompts, he uses "nibble" passes to iteratively improve code through multiple agent review cycles, and he is building infrastructure that pairs agents with Kubernetes compute for team-scale NLP workflows. His skills are published publicly at [github.com/honnibal/claude-skills](https://github.com/honnibal/claude-skills).

## On working with agents

Hugo opens with two questions he puts to every guest: what they love about working with agents, and what they find most frustrating.

### What he loves: velocity and staying in flow
Matt's answer centers on velocity. Faster iteration means less time on the uninteresting parts and less cognitive state lost between steps, and the effect compounds. *"things get lot easier if you're doing them on a more compressed timeline and you're less often losing state... you get a compounding effect from velocity in this way if you're doing it well."* [\[00:05:01\]](https://youtube.com/live/ud2WzkKeDZs?t=301)

### What he finds most frustrating: a poverty of evidence
The hardest part is not knowing whether a given technique actually works. You cannot gather enough samples to tell whether a prompt change helps by 10 percent or hurts by 15, and the ground keeps shifting underneath you. Matt argues even Anthropic cannot be rigorously evaluating everything at their pace: *"you can't hire nine women to have a baby in one month."* The "evaluation problem" explainer below treats this at length. [\[00:06:37\]](https://youtube.com/live/ud2WzkKeDZs?t=397)

## Skills

### Try-except audit skill
A prompt-based skill asking Claude to read Python source files and audit exception handling. For every try-except block it finds, the skill checks whether the block:

- is correctly scoped,
- catches direct exceptions, and
- doesn't mask bugs.

Matt highlighted this as one of his core skills because he views improper exception handling as one of the most significant problems agents introduce in Python code. *"In try-accept audit mode, your job is to read Python source files, find every try-accept block, evaluate whether each one is correctly scoped, catches direct exceptions, and doesn't mask bugs."* [\[00:09:33\]](https://youtube.com/live/ud2WzkKeDZs?t=573) Published as [`try-except.md.txt`](https://github.com/honnibal/claude-skills/blob/main/try-except.md.txt).

### Pre-mortem mode skill
A skill that asks Claude to read production code, identify areas of fragility and implicit assumptions, and write realistic post-mortem reports for bugs that haven't happened yet. The skill explicitly frames the task as not a bug hunt but a search for places where code is fragile against future edits, where a seemingly reasonable change by a future developer could break something non-obvious. *"Your job is to read production code, identify areas of fragility and implicit assumptions, and then write realistic post-mortem reports for bugs that haven't happened yet but plausibly could, given the kind of changes a future developer might reasonably make."* [\[00:14:28\]](https://youtube.com/live/ud2WzkKeDZs?t=868) Published as [`pre-mortem.md.txt`](https://github.com/honnibal/claude-skills/blob/main/pre-mortem.md.txt).

### Test coverage mutation skill
A skill that asks Claude to introduce problems into code and then check whether the current test suite catches them. This is one of several pass-over-the-code operations Matt runs to verify code quality and test robustness. [\[00:14:28\]](https://youtube.com/live/ud2WzkKeDZs?t=868) Published as [`mutation-testing.md.txt`](https://github.com/honnibal/claude-skills/blob/main/mutation-testing.md.txt).

## Workflows

### Multiple-pass "nibble" strategy instead of one-shot requests
Rather than trying to get Claude to do everything in one large pass, Matt uses a metaphor of "nibble versus bite," making multiple iterative passes over code instead of trying to load everything into context at once. The reasoning: *"Fundamentally, reasoning isn't free. You can't expect the model to know everything that it knows all up front."* You cannot expect inference to happen magically, so *"you have to go from one intermediate result to the next intermediate result."* After each operation (e.g., introducing test mutations, auditing exceptions), he runs separate "fix-up passes" where he tightens types, exception handling, and other details. This iterative refinement avoids the trap of expecting the model to solve everything in one shot. [\[00:11:21\]](https://youtube.com/live/ud2WzkKeDZs?t=681), [\[00:14:28\]](https://youtube.com/live/ud2WzkKeDZs?t=868)

### Active engagement and context window hygiene
Matt practices deliberate session management to avoid low-productivity failure modes. Long sessions where he operates in the background with divided attention (e.g., watching TV while an agent runs) lead to poor results; instead, he emphasizes shorter, focused sessions where he takes active agency. *"Those are bad usage patterns. And I find myself trapped into that more than I would like... I think a healthy pattern is a shorter context length."* He notes that with 20 years of engineering experience, he should be leveraging his expertise more actively and catching problems immediately, rather than passively waiting for agent output. [\[00:21:44\]](https://youtube.com/live/ud2WzkKeDZs?t=1304), [\[00:22:14\]](https://youtube.com/live/ud2WzkKeDZs?t=1334)

### Probing agent reasoning rather than accepting conclusions
When evaluating agent-generated code (especially in unfamiliar domains like Kubernetes), Matt emphasizes asking the agent to explain its reasoning rather than accepting the final artifact. *"The reasoning is something that's much easier to evaluate than the conclusion... I'll very often ask it to identify the lines of code that introduced the change. Or I'll ask it, why did this work? Why exactly was this working yesterday but not today?"* This allows him to catch errors and hallucinatory explanations through dialogue rather than waiting for deployment failures. [\[00:30:42\]](https://youtube.com/live/ud2WzkKeDZs?t=1842), [\[00:30:56\]](https://youtube.com/live/ud2WzkKeDZs?t=1856)

### Hybrid deterministic-agentic workflow for high-stakes tasks
For security-sensitive operations like releasing software, Matt writes shell scripts that combine deterministic procedural logic with a small agentic step. Releasing spaCy, for example, runs in three stages:

- A script sets up the context.
- It calls the agent with one narrow task: draft release notes.
- Deterministic logic takes over to push the changes.

This limits agent autonomy to exactly where it adds value while keeping credential and deployment logic safely procedural. *"I really like having scripts which are this mix of procedural code and just one step that requires the agent of like, okay, the task is draft release notes. And then deterministic logic takes over for the rest."* [\[00:58:24\]](https://youtube.com/live/ud2WzkKeDZs?t=3504), [\[00:58:51\]](https://youtube.com/live/ud2WzkKeDZs?t=3531)

## Tools / projects he showed

### Explosion's NLP platform (beta.elf.ai)
A platform in beta, shown during this episode. Designed to help teams use Claude and agent skills for natural language processing and data projects. The platform combines a web interface with a Kubernetes backend that lets users define multi-step workflows (data download, annotation, model training, experiment runs). Within those workflows, users can:

- Farm annotation tasks out to cheaper models like Gemini Flash.
- Set up review tasks to resolve annotation disagreements.
- Receive agentic guidance through each workflow step.

The name "elf" stands for "explosion large language thing." The platform emphasizes developer-in-the-loop control rather than high-autonomy agent operation. *"We don't want this extremely high autonomy concept, like that's not something that we're targeting with this, but having a developer in the loop flow and guiding people through tasks, that's the sort of way that we're thinking about this."* [\[00:24:37\]](https://youtube.com/live/ud2WzkKeDZs?t=1477), [\[00:26:44\]](https://youtube.com/live/ud2WzkKeDZs?t=1604)

### Claude Code
The primary tool Matt used to build the Explosion NLP platform. *"We, you know, of course use, I think Claude code is the main thing that we used to build it."* [\[00:29:31\]](https://youtube.com/live/ud2WzkKeDZs?t=1771)

### Kubernetes
Infrastructure used as the compute backend for the Explosion platform, running on users' desktop or cloud services. Matt's learning of Kubernetes while building the platform (without prior domain expertise) exemplified both the seductiveness and danger of agent assistance: agents provided confident answers that he couldn't immediately evaluate. [\[00:24:37\]](https://youtube.com/live/ud2WzkKeDZs?t=1477), [\[00:29:31\]](https://youtube.com/live/ud2WzkKeDZs?t=1771)

### Gemini Flash
Mentioned as an example of an inexpensive model that can be used within the Explosion platform to farm out low-stakes annotation tasks. [\[00:26:44\]](https://youtube.com/live/ud2WzkKeDZs?t=1604)

### Twitter / Blue Sky
Named as an example data source for monitoring spaCy brand mentions (to distinguish library mentions from Honda motorcycle mentions) in a concrete NLP project workflow. [\[00:24:37\]](https://youtube.com/live/ud2WzkKeDZs?t=1477)

## Explainers

### Why try-except misuse is an agent-specific problem (reward hacking during training)
Matt attributes bare except blocks and masked exception bugs to reward hacking during model training. Because reinforcement learning has a limited horizon, agents optimize for short-term rewards (passing an LLM judge) by hiding maintainability problems. The model learns to "lie" in chat about success and introduce shortcuts that an LLM judge won't catch but a human will regret later. *"There's a low penalty on introducing maintainability problems because you can only have a limited horizon on the reinforcement learning. And so one of the ways that it can cheat the long-term objective in order for the short-term gain is to introduce bare accepts and things... Similarly with the various ways they will lie to you in the chat about whether it's successful or not. All of those things I think are evidence of it having managed to trick the rewarder."* [\[00:16:47\]](https://youtube.com/live/ud2WzkKeDZs?t=1007)

### The evaluation problem: agents move too fast for evidence
Matt identifies the hardest frustration with agent use: making decisions about whether a workflow or technique actually works. Empirically measuring whether a prompt change improves performance by 10 percent requires statistical power that neither individual developers nor companies like Anthropic have time for. *"It's extremely hard to know whether this way is actually performing better than this other way... you're not going to have sample to tell that reliably, especially since even measuring performance, we don't have a good thing. So it's all very eyeballed."* Because models and platforms change constantly, evaluation windows close before studies complete. This uncertainty compounds with platform outages, creating a discouraging loop. [\[00:06:37\]](https://youtube.com/live/ud2WzkKeDZs?t=397)

### Software 2.0 with agents: from teaching humans to teaching agents to write programs
The NLP platform reflects a shift in how to think about ML system development. In the "Software 2.0" era, the question was how to teach humans to write ML-based programs. Now the question is how to get LLM agents to write those programs on behalf of teams. The concrete example: detecting spaCy library mentions in tweets requires building a classifier. Rather than a user writing a Python script, the agent guides the user through data download, annotation, experiment design, and training. *"We've got a need for a certain type of program. How do we build that program? Well, we got to a certain point in teaching people how to build that sort of program, but now we need to get to that point of getting LLM agents to build that sort of program."* [\[00:24:37\]](https://youtube.com/live/ud2WzkKeDZs?t=1477)

### Agents work best on familiar domains; danger when applied to unfamiliar ones
A key tension Matt identified when building the platform with Kubernetes: agents are seductive when applied to unfamiliar material because they give confident, detailed answers. But when those answers are wrong and you don't know the domain, you won't catch the error, leading to compounding problems and a frustrating debug cycle. In contrast, when Matt works with code in a domain he knows well, he immediately catches agent mistakes. *"It's the agent works sort of most easily when you're doing stuff that you know how to do... It's so interesting because it's so seductive when you're doing things that you don't know well... but it sucks when the answers are wrong and you don't know about them."* The implication is that agents require active, knowledgeable human review, especially in unfamiliar domains. [\[00:29:31\]](https://youtube.com/live/ud2WzkKeDZs?t=1771)

### Hidden instructions in skill files: HTML comment security gap
Skills repositories do not sanitize HTML comments embedded in skill files. When rendered as markdown, these comments become invisible to humans but are read by Claude. This creates a supply-chain attack surface where malicious or accidental hidden instructions can slip into shared skill libraries. Matt opened an issue requesting HTML comment filtering but noted the maintainers have not responded. As a result, he shares his skills as plaintext .md.txt files instead, requiring users to read raw text and discouraging the unvetted consumption of skills from repositories. *"When you render the markdown version of that skill, that text will be invisible to you... There's hidden instructions in the skill that you don't see. So it's discouraging that they didn't even bother in the specification to, you know, strip HTML comments or reject skills with HTML comments."* [\[00:12:09\]](https://youtube.com/live/ud2WzkKeDZs?t=729)

### Platform design for data projects: compute backend required
Data science and NLP projects differ from pure code generation because they involve expensive runtime steps (data download, preprocessing, training) that cannot be piped through an LLM per-item. Building classifiers requires gathering training data and running experiments on a cluster. The platform abstracts away Kubernetes complexity so teams can focus on defining their workflow steps, delegating execution to compute infrastructure that an agent coordinates. [\[00:24:37\]](https://youtube.com/live/ud2WzkKeDZs?t=1477)

## Additional quotations

- On Australia being admitted to Eurovision, and an unofficial national strategy: *"Well, I think this is part of the Australian cultural heritage of just showing up and expecting to be accepted and seeing what happens. So Australia showed up at the doorstep and Europe was like, well, I guess."* [\[00:03:05\]](https://youtube.com/live/ud2WzkKeDZs?t=185)
- On the 8-bit intro video Hugo made of him: *"I can't decide whether it's true cringe or like cringe enough that it's slapped around to like be acceptable again."* [\[00:04:24\]](https://youtube.com/live/ud2WzkKeDZs?t=264)
- On not being able to fine-tune his skills, so he adapts his workflow around them instead: *"I don't have a way to make small optimizations to these. so instead I kind of change my workflow around them."* [\[00:19:05\]](https://youtube.com/live/ud2WzkKeDZs?t=1145)
- On agents potentially letting senior engineers coast below their level: *"I've got, I think it's like 20 years of experience as an engineer now and I've, you know, built a lot of stuff. I'm fairly fluent with code. And I think about, all right, you know, if I've had a session with this where I really haven't used all of that and I've, basically been as effective as anybody would have been with this. That's something that I see as a concern."* [\[00:22:14\]](https://youtube.com/live/ud2WzkKeDZs?t=1334)

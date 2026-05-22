# Eleanor Berger — Episode 3 field notes

Eleanor Berger is an AI and software engineering expert and a technical member of staff at Jimini Health, where she recently started working on AI for mental health. She is the creator of agentic ventures, an AI coding and agentic engineering course and community, and was formerly a principal engineering lead at Microsoft and Google.

Her segment centered on a "YOLO" shift in how she builds with agents: moving away from pedantic, versioned skills management toward letting agents roam more freely within guardrails. She showcased how she uses Hermes to automate HTML generation, design refinement, media summarization, and cron-scheduled tasks.

## On working with agents

### What she loves: velocity and capability rounding

Eleanor's answer centers on velocity, sharpened by her own impatience: *"I tend to be very impatient. To the extent that it's almost like a filter, if something can't happen fast, I might just not do it, not bother."* Agents remove that filter.

They also round up her capabilities, extending her into domains where she is competent but not fluent. She is explicit that this depends on already having partial knowledge: with no grounding at all, *"It's difficult for me. I don't think agents help me very much."* The payoff comes when she knows just enough to judge the output: *"if I know a little bit of what I'm doing, enough to have the confidence that I understand what it did and how to evaluate it, all of a sudden I got this exoskeleton."* [\[00:37:10\]](https://youtube.com/live/ud2WzkKeDZs?t=2230)

### What she finds most frustrating: scope understanding

Agents excel at interpreting user intent but struggle with scope: she asks for a one-pager and gets a novel, or requests a comprehensive review and receives a paragraph. This mismatch is persistent and solutions remain unclear, whether through skills, system prompts, or training. *"Agents get really good at understanding and interpreting intent. And they're still not very good at understanding scope... it would do a lot less or a lot more than what I actually wanted. Like I wanted just like a one pager, but it wrote a novel or I wanted a comprehensive review, but it wrote a paragraph."*

Sometimes a hard constraint helps: *"I just need to tell it like, this needs to be 500 tokens or less. Like you need to give something concrete, otherwise it just kind of, it will go on and on and on."* [\[00:38:35\]](https://youtube.com/live/ud2WzkKeDZs?t=2315), [\[00:39:58\]](https://youtube.com/live/ud2WzkKeDZs?t=2398)

## Skills

### here.now HTML publishing skill

A skill for publishing generated HTML pages to here.now, a GitHub Gist-like service optimized for HTML. Eleanor generates HTML dozens of times per day (often automatically), and the skill lets her tell the agent "do a webpage, publish it to here.now." She has configured the agent such that it infers when to publish there without being asked. Rather than manually publishing to GitHub Pages, she now delegates the entire artifact-hosting step. [\[00:45:56\]](https://youtube.com/live/ud2WzkKeDZs?t=2756)

### Impeccable design skill

A design-assistance skill that handles tasks Eleanor cannot do manually: layout, typography, color, and iterative refinement. The skill encodes design guidelines and applies them iteratively. Eleanor does not understand the internals but benefits from the abstraction; she evaluates designs by her own taste and legibility, not by understanding the rules. When she evaluates whether design is good, *"I look at it like I'm the main customer"*: if it looks legible and pleasant, it works. [\[00:50:39\]](https://youtube.com/live/ud2WzkKeDZs?t=3039)

### YouTube watch-later summarization skill

A skill that reads her YouTube watch-later list, uses a live browser to access each video (since YouTube lacks a public API), generates summaries, and maintains a cache of already-processed videos. The skill was invented largely by the agent in response to a brief request; Eleanor asked, and the agent produced the implementation without her having to specify the caching logic or the third-person phrasing. *"These are all skills that I didn't try to myself, right? I just asked and it created the skill for me... I asked very briefly in the chat and it invented this way to do it and it did a pretty good job."* [\[00:54:45\]](https://youtube.com/live/ud2WzkKeDZs?t=3285)

### Anki flashcard management skill (with cron)

A skill that manages her Anki flashcard collection alongside a cron job. She can command the agent to handle flashcard revisions and scheduling autonomously on a recurring schedule. [\[00:49:46\]](https://youtube.com/live/ud2WzkKeDZs?t=2986)

## Workflows

### From pedantic skills to YOLO agent autonomy with guardrails

Eleanor has historically treated skills as software packages: versioned, carefully managed, and integral to serious work. She is now experiencing a shift, one she suspects many others have already had or will have, where she "lets go" and embraces a more free-wheeling approach, delegated via Hermes. The boundary: her personal dev environment and exploratory work run on Hermes with high autonomy; she still does not let it near sensitive production systems (e.g., her clinical data at Jimini Health).

The model also improves: she started with asking permission for every action, gradually trusted it more, and now benefits from its auto-evaluation. *"I'm having right now this moment, which I think many people already had and many people are going to go through where I let go. And the thing that changed it for me is Hermes... I have to say that I've been impressed with its ability to monitor itself and make good decisions on where it needs my approval."* [\[00:41:36\]](https://youtube.com/live/ud2WzkKeDZs?t=2496)

### Verification via artifact observation, not AI-to-AI review

Eleanor thinks deeply about trust. The core insight: *verification is not getting an AI to look at the YAML files; verification is looking at what happens when you run these YAML files, observe the cloud's footprint, and confirm it matches your expectation.* For infrastructure work (Kubernetes-like systems with meaningful artifacts), the only trustworthy signal is observing actual state after execution. AI-reviewing AI output ("do another AI review and then do an AI review of the AI review") is not verification; it is illusion. This principle drives her architecture: she will grant agent control over systems she can cheaply orchestrate and observe, but not over systems where observation is opaque. [\[00:33:21\]](https://youtube.com/live/ud2WzkKeDZs?t=2001)

### Simon Willison's lethal trifecta: segregation and scope limits

Eleanor references Willison's [lethal trifecta](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/) framework (access to private data, ability to externally communicate, exposure to untrusted content). She acknowledges the risk is real and largely unavoidable: *if you have instructions from the internet and connections out to the internet, you should assume you are completely exposed.* Her mitigation: segregate agents physically or logically (her Hermes agent lives on a Mac mini, connected via Tailscale, isolated from her work environment), and do not let agents near sensitive systems. [\[00:56:12\]](https://youtube.com/live/ud2WzkKeDZs?t=3372)

### Hybrid deterministic-generative workflows with cron scheduling

Eleanor champions a hybrid approach: separate the generative (agentic) steps from the deterministic (scripted) logic. She uses cron jobs extensively, and Hermes is particularly good at knowing when to invoke an LLM versus when to run a deterministic script. She often under-specifies cron tasks ("can you please do this every two hours") and lets the agent infer which parts require reasoning and which can be pure scripting. *"Hermes is quite good at knowing in what cases it can just create a script and do without an LLM... I create a lot of cron jobs all the time and a lot of them I under-specify, I just say like, can you please do this like whatever every two hours."* [\[01:00:25\]](https://youtube.com/live/ud2WzkKeDZs?t=3625)

### Language and framework agnosticism

Eleanor used to be "all in on Python" for decades. Now she is agnostic: TypeScript, Go, Rust, PHP, whatever works. Her verification metric is not code quality or style; it is observable results. *"Verification is not about looking at the code. Verification is that it actually do what it needs to do. So as far as I'm concerned, if it's written in like PHP in continuation passing style, but it produces the right results, that's fine with me."* She finds that Python is actually harder to work with agents in, so she uses it less, reserving it for hand-written code (which is rare now). [\[01:03:05\]](https://youtube.com/live/ud2WzkKeDZs?t=3785)

## Tools / projects she showed

### Hermes agent

The centerpiece of her demo. A locally-run agent harness living on an M1 Mac mini (repurposed old hardware) connected via Tailscale. It has 157 skills, scheduled jobs, parallel child agents, and multiple input channels (Discord, WhatsApp, CLI, API). Eleanor particularly praises [Hermes](https://hermes-agent.nousresearch.com/) (relative to OpenClaw) for knowing when to create deterministic scripts versus engaging the LLM, avoiding wasteful LLM calls for routine cron work. The agent's name is Fnord, a reference to Discordian mythology. She uses it most via Discord, where thread management and responsiveness are excellent.

The critical unlock: GPT 5.5, which Hermes powers. *"With 5.5 they finally overcome this and it's just an amazing model. I'm using it almost exclusively now either in Codex app or in Hermes or in VS Code or whatever."* [\[00:41:43\]](https://youtube.com/live/ud2WzkKeDZs?t=2503), [\[00:44:09\]](https://youtube.com/live/ud2WzkKeDZs?t=2649)

### here.now

[here.now](https://here.now/) is a service for publishing HTML snippets (similar to GitHub Gist but for HTML). Eleanor generates and publishes dozens of HTML pages daily through her agent. [\[00:45:56\]](https://youtube.com/live/ud2WzkKeDZs?t=2756)

### Codex app (and GPT 5.5 model)

Her primary code editor for day-to-day coding. Eleanor has switched from more distributed use of OpenClaw and Copilot to almost exclusively Codex, which she finds "best in class" with GPT 5.5. She remains intentionally tool-agnostic to avoid lock-in; she switches between Codex, OpenClaw, and Copilot to ensure her workflows survive tool changes. [\[01:03:58\]](https://youtube.com/live/ud2WzkKeDZs?t=3838)

### Warp terminal

A recently open-sourced terminal she now uses (held off before it was closed source). She finds it excellent for running agents and convenient for general terminal work. [\[01:02:26\]](https://youtube.com/live/ud2WzkKeDZs?t=3746)

### Zed editor

A lighter-weight editor she is experimenting with for cases where she needs to open files. She does not edit much anymore and finds editor needs small, so Zed serves as a lighter alternative to VS Code. [\[01:02:04\]](https://youtube.com/live/ud2WzkKeDZs?t=3724)

### M1 Mac mini (local agent infrastructure)

The hardware where Hermes runs. Eleanor repurposed an old M1 Mac mini (lying around) because it provides a desktop environment and a minimal GPU (for local embeddings). Running a GPU machine in the cloud is expensive; she solved it by using the Mac mini's modest GPU for embedding and indexing locally while connecting remotely via Tailscale. [\[00:43:03\]](https://youtube.com/live/ud2WzkKeDZs?t=2583)

### Tailscale

Network tunneling software used to securely connect to her remote Mac mini agent from anywhere, with segregation from her main work environment. [\[00:43:47\]](https://youtube.com/live/ud2WzkKeDZs?t=2627)

### Hermes web UI (community project)

Not part of Hermes proper but a third-party web interface for Hermes that Eleanor enjoys using. [\[00:49:59\]](https://youtube.com/live/ud2WzkKeDZs?t=2999)

### Anki

Spaced-repetition flashcard software. Eleanor revises flashcards daily and now manages them via her agent and cron jobs. [\[00:49:46\]](https://youtube.com/live/ud2WzkKeDZs?t=2986)

### Discord

The preferred interface for interacting with her Hermes agent. The integration is "really good," responsive, and supports threaded conversations for managing multiple queries. She also uses CLI, WhatsApp, and API access, but Discord is primary. [\[00:45:15\]](https://youtube.com/live/ud2WzkKeDZs?t=2715)

### Impeccable

[Impeccable](https://impeccable.style/) is the design tool (and skill) Eleanor leans on most; by her own account she is "terrible at design," and it lets her produce work that looks "not too bad." She recommends it to anyone who needs design help, and notes the space is filling out fast: *"There's now open design, which looks really cool."* She mentions a newer option from Google as well, and says she is herself attempting an open implementation of something like cloud design. [\[00:50:39\]](https://youtube.com/live/ud2WzkKeDZs?t=3039)

## Explainers

### AI validation and the infinite-regress problem

Eleanor opens with a core security and reliability challenge: you cannot validate AI-generated output with another AI. There is an infinite regress (AI reviewing AI reviewing AI) that breaks down trust. The solution is to reintroduce certainty by observing artifacts, not by layering AI reviews. For infrastructure, this means running configurations and observing actual state. For data, it means ground truth and empirical signals. Without artifact observation, verification becomes circular. [\[00:33:21\]](https://youtube.com/live/ud2WzkKeDZs?t=2001)

### When agents should not be trusted: the scope problem

Eleanor identifies a specific failure mode: agents are good at understanding intent but poor at understanding scope. This distinction is important because it affects how to use agents. For high-confidence tasks (well-scoped requests), agents shine. For open-ended exploration, they fail. The implication is that agent-assisted work requires clear boundaries and may benefit from hard constraints (e.g., token limits). [\[00:38:35\]](https://youtube.com/live/ud2WzkKeDZs?t=2315)

### Hybrid architectures: when to script, when to generative-loop

Eleanor advocates for mixing procedural code with narrow generative steps. Not everything needs to be agentic. Cron jobs, scripts, and deterministic logic are often better for routine work. The agent's role is to know the boundary: when to invoke an LLM for reasoning and when to stay procedural. This reduces cost, improves reliability, and makes systems easier to understand. [\[00:41:36\]](https://youtube.com/live/ud2WzkKeDZs?t=2496)–[\[01:00:25\]](https://youtube.com/live/ud2WzkKeDZs?t=3625)

### Taste-driven design evaluation without instruction

Eleanor is not skilled at design and does not know how to instruct a system about fonts, spacing, or color theory. Yet she can evaluate whether a design is good by looking at it and asking: Is it legible? Does it feel nice to interact with? By delegating the instruction task to the agent (through a design skill) and keeping only the evaluation task for herself, she gains design capability without learning design. This is an instance of agent-as-complement-to-human-judgment, not replacement. [\[00:52:15\]](https://youtube.com/live/ud2WzkKeDZs?t=3135)

### Agent models and reasoning overhead: GPT 5.5 as an unlock

For a long time, Hermes relied too heavily on reasoning (inference-time compute) to compensate for a weak base model. This made responses slow and the user experience poor. GPT 5.5 solved the underlying problem: a strong base model with better reasoning, arriving at high-quality outputs faster. The lesson: model quality matters enormously to user experience, and small improvements in the base model can unlock entire agent platforms. [\[00:44:09\]](https://youtube.com/live/ud2WzkKeDZs?t=2649)

### Jimini Health: AI for mental health at scale

Eleanor mentioned her new role at Jimini Health, where she works on AI systems for mental health. The context matters because it is where she draws the line on agent autonomy: this is sensitive, mission-critical work with clinical data, so she does not let agents near it (yet). [\[00:35:46\]](https://youtube.com/live/ud2WzkKeDZs?t=2146)

### agentic ventures course: focus shifted from AI coding to agentic engineering

Eleanor's course has evolved. It started as "AI coding" but has shifted substantially toward agentic engineering: building software with agents, thinking about workflows, architecture, and risk. The next cohort starts June 22nd. The field is moving so fast that the course is refreshed constantly, but the curriculum structure remains stable. [\[01:08:27\]](https://youtube.com/live/ud2WzkKeDZs?t=3907)

## Additional quotations

- On why she chose Hermes over OpenClaw: *"It's great that there are multiple projects and they're both really cool projects. For me, it somehow happened with Hermes, if only because I waited long enough. I think I tried open CL when it was still very early and I didn't think that's something I'm going to use and then a few weeks ago I installed Hermes and then it clicked."* [\[00:41:49\]](https://youtube.com/live/ud2WzkKeDZs?t=2509)

- On the YOLO shift in her approach: *"Everything I'm going to show today and a lot of what's new and interesting to me is this YOLO approach of letting an agent just sort of roam free."* [\[00:41:36\]](https://youtube.com/live/ud2WzkKeDZs?t=2496)

- On how skills are invented by the agent itself: *"I would never refer to myself in the third person, but it's just I asked very briefly in the chat and it invented this way to do it."* [\[00:54:50\]](https://youtube.com/live/ud2WzkKeDZs?t=3290)

- On the evolution of her skills practice: *"In a lot of my previous work and in my teaching, I've been treating agents and skills as... quite pedantic, treating skills like a software package that I'll kind of manage very carefully and sort of version and all of that. And I still think that's important for a lot of my more serious work."* [\[00:41:05\]](https://youtube.com/live/ud2WzkKeDZs?t=2465)

- On tool agnosticism as a principle: *"I try intentionally to be a little bit tool agnostic, to switch around, to make sure that my configuration will always work with all the different tools that I'm not relying on some specific feature of a tool."* [\[01:04:13\]](https://youtube.com/live/ud2WzkKeDZs?t=3853)

- On why she uses Warp terminal: *"It's really nice and now it's open source. I held off on using it while it was closed, but now that they opened, I started using it and it's really great for running agents and just for convenience."* [\[01:02:29\]](https://youtube.com/live/ud2WzkKeDZs?t=3749)

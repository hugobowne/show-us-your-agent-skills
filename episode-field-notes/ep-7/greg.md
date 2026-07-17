# Greg Ceccarelli - Episode 7 field notes

[Greg Ceccarelli](https://www.gregceccarelli.com/) is co-founder and CPO of [SpecStory](https://specstory.com/). He previously served as CPO at Pluralsight and worked at GitHub, Dropbox, and Google. His Episode 7 demo shows how [Lore](https://github.com/specstoryai/getspecstory/tree/dev/lore) turns the exhaust of everyday agent work into reusable skills: SpecStory saves sessions from multiple coding agents as markdown, Lore mines repeated patterns across those histories, and the human reviews the evidence before approving a skill for installation.

The raw sessions matter because the reasoning behind a change often disappears when only the finished artifact survives. *"Storing transcripts, storing your traces, whatever you want to call them, your agent sessions, is really important because to do useful things, if you were going to try and extract decisions or the why, you need that raw material."* [[00:05:25]](https://youtube.com/live/kfCi2EBu-nc?t=325)

In Greg's live run, Lore parses 516 long sessions, labels whether the user accepted or rejected an agent response, corroborates recurring practices across projects, and presents candidate skills with citations. Greg selects a second quality gate that runs after functional success, approves it in plan mode, and lets Lore install it across his agent harnesses. *"The premise of what I'm going to share is how you can mine them with a skill that makes new skills, all from your agent transcripts."* [[00:06:05]](https://youtube.com/live/kfCi2EBu-nc?t=365)

## On working with agents

### What he loves: expressing product intent instead of syntax

Greg values the productivity that comes from describing an architecture and desired outcome in English instead of concentrating on programming-language syntax. That speed matters because it lets him put software in front of people, gather feedback, and iterate. *"I don't really have to think about programming languages and syntax anymore, and I can just express my desires, well thought out, architected in English language, and get outcomes and output."* [[00:08:20]](https://youtube.com/live/kfCi2EBu-nc?t=500)

### What he finds most frustrating: the attention addiction

Greg finds agent work isolating and difficult to stop. The same rapid reward that makes agents productive can keep him entranced in sessions. *"I don't like the attention addiction that comes with working with agents. These things are so powerful and so good that it's hard to put them down."* [[00:10:35]](https://youtube.com/live/kfCi2EBu-nc?t=635)

He deliberately keeps agent work off his phone so closing the laptop creates a real boundary. *"I've set up my stack in a way that I know if I close my laptop, I'm not going to be looking at my phone."* [[00:24:50]](https://youtube.com/live/kfCi2EBu-nc?t=1490)

## Workflows

### Mine agent histories, review candidate practices, then forge approved skills

Greg starts by syncing SpecStory session logs from multiple agents into a project repository as markdown. Lore builds a local database, parses the sessions, labels conversation turns, runs theme mining and corroboration, then presents candidate practices with citations to the histories where it found them. The human chooses what deserves to become a reusable skill. *"It presents stuff for your review. It will never install anything unless you actually approve it."* [[00:34:00]](https://youtube.com/live/kfCi2EBu-nc?t=2040)

The guided run lets Greg choose a project, select the last 30 days, and ask Lore to find and forge skills. He recommends running that deeper mining occasionally with a high-reasoning model, rather than continuously. *"You don't need to do these Lore runs that often. I would say once a month or something, to see what comes out."* [[00:27:50]](https://youtube.com/live/kfCi2EBu-nc?t=1670)

### Run a second quality gate after functional success

Lore detects a recurring pattern in Greg's histories: once a feature works, he runs a separate sweep for non-functional regressions before shipping. That sweep includes:

- Linting and type checks.
- Staging and full builds.
- Re-rendering artifacts and refreshing audits.
- A test push.

Greg recognizes the pattern as something he does repeatedly and chooses it for forging. *"Functional success never closes the loop. Immediately after confirming a feature works or before letting anything ship, the user, me, runs a distinct second gate of non-functional checks."* [[00:32:25]](https://youtube.com/live/kfCi2EBu-nc?t=1945)

### Run coding agents until external checks prove the work is done

Greg's Dead Reckon workflow wraps coding CLIs and keeps Claude Code, Cursor, or Codex running until they pass deterministic definition-of-done checks stored outside the model's reach. *"The model will not be the one determining its end run."* [[01:20:00]](https://youtube.com/live/kfCi2EBu-nc?t=4800)

The workflow supports unattended jobs that may continue for 20 hours. Greg built Dead Reckon with Codex goals, storing source intent in a goals directory and pairing each goal with a writer document, phased tasks, reference context, and independent verification steps. *"If an agentic coding harness runs an LLM in a loop, the goal of loop engineering then is to run your agentic coding harnesses in a loop."* [[01:30:15]](https://youtube.com/live/kfCi2EBu-nc?t=5415)

### Integrate continuously, then reimplement stale branch intent

Greg integrates team changes continuously into a shared trunk. Agents summarize newly integrated work so another teammate can resume from the current head. When a branch has drifted too far, the agent reimplements its intent against the current codebase in what Greg calls a semantic rebase. *"It would be taking a branch and reimplementing it if it is farther away semantically based on their intent, because agents can do that so much faster."* [[01:58:25]](https://youtube.com/live/kfCi2EBu-nc?t=7105)

## Skills

### [Lore](https://github.com/specstoryai/getspecstory/tree/dev/lore)

Lore is an interactive agent skill that mines SpecStory session histories and forges new skills from recurring practices. It offers commands for guided setup, skill inventory, finding and forging candidates, installation, and uninstallation. Greg demonstrates it inside Claude Code, but says it can also run in Codex, Cursor CLI, and Cursor IDE. *"What this skill that's called Lore does is look at all of that fantastic exhaust, and then it has an engine, part deterministic and part based on your local model, to pull out those patterns."* [[00:07:30]](https://youtube.com/live/kfCi2EBu-nc?t=450)

The skill inventories Lore-forged skills alongside other installed skills. That visibility helps explain surprising agent behavior when a forgotten skill triggers from ordinary English in a prompt. *"How many times have you installed a skill, completely forgotten about it, and been like, 'Wait, why is the LLM doing this thing?'"* [[00:16:15]](https://youtube.com/live/kfCi2EBu-nc?t=975)

Each run creates a local database that parses large session files and labels conversation turns. The engine divides each interaction into a `beat`: user prompt, agent response, and the next user prompt. That third turn supplies evidence that the previous response was accepted or rejected. *"That's a beat instead of just a user prompt, agent response, because what it tries to do is see, did you actually accept what came out of the response from your prior prompt and label it."* [[00:20:35]](https://youtube.com/live/kfCi2EBu-nc?t=1235)

The deterministic pass indexes sessions and extracts candidate patterns without sending the entire corpus to a model. A later model-driven workflow performs theme sweeps, deeper mining, and adjudication. In the live run, the deterministic layer processes 516 sessions. *"If you were actually trying to push this all to an LLM, it would not be very happy, and it would consume all of your usage very quickly."* [[00:19:50]](https://youtube.com/live/kfCi2EBu-nc?t=1190)

Lore writes dossiers with citations and corroborates patterns across histories from SpecStory Cloud, Stoa, the CLI, and the VS Code extension. *"I've run it on other projects, and so all the other saved sessions from those runs are in here, and then it corroborates across the full corpus."* [[00:30:30]](https://youtube.com/live/kfCi2EBu-nc?t=1830)

The live run also surfaces candidate practices about Supabase SQL surgery, reporting bugs with the artifact, and bringing a falsifying observation. Greg rejects the database-specific candidate as too narrow and keeps scanning for a practice he recognizes. *"This is a very specific skill that's probably not something I would actually want to install, but it's a pattern that's come out of the transcripts it mined."* [[00:30:50]](https://youtube.com/live/kfCi2EBu-nc?t=1850)

### Define problem before implementing

Lore surfaces `define problem before implementing` as a recurring practice in Greg's histories. The dossier marks its evidence as unchanged because the pattern has appeared before, and cites the source history files so Greg can inspect the basis for the candidate. *"This define problem before implementing is another skill, and you see that this one's a latent practice where it's seen this before."* [[00:31:20]](https://youtube.com/live/kfCi2EBu-nc?t=1880)

### Hygiene gate afterwards

Greg chooses the candidate built around a post-success hygiene gate and asks Lore to forge it. The resulting skill carries his repeated sequence of behavior checks followed by a separate quality-regression sweep. *"So that is something that I do all the time. Let's just pick this one so we can move forward."* [[00:33:10]](https://youtube.com/live/kfCi2EBu-nc?t=1990)

He then tests Lore's uninstall flow because the newly produced skill may not be useful enough to keep. *"I wasn't looking at this with the most critical lens. It produced this. I don't know if this is actually something that I want."* [[00:36:20]](https://youtube.com/live/kfCi2EBu-nc?t=2180)

## Tools / projects he showed

### [SpecStory](https://specstory.com/)

SpecStory is Greg's open-source VS Code extension and terminal CLI for saving, syncing, and sharing coding-agent sessions. It normalizes histories from Claude Code, Codex, Cursor, Gemini, and other supported agents into markdown inside the project repository. *"It makes it really easy to get all of those session logs into one common format and markdown into your project repo."* [[00:12:15]](https://youtube.com/live/kfCi2EBu-nc?t=735)

Greg demonstrates Lore against a shared SpecStory Cloud repository that contains histories from his teammates as well as his own. *"This has not just my histories, but histories from my teammates too."* [[00:15:35]](https://youtube.com/live/kfCi2EBu-nc?t=935)

### Dead Reckon

[Dead Reckon](https://deadreckon.sh/) is Greg's harness for long unattended coding runs. Its goals directory carries source intent, while deterministic definition-of-done checks remain outside the coding model's reach and decide when the run can stop. *"It can be a whole orchestrated plan. The harness will keep either Claude Code, Cursor, Codex running until it passes these hidden definition-of-done checks."* [[01:19:20]](https://youtube.com/live/kfCi2EBu-nc?t=4760)

### Cursor and VS Code

Cursor gives Greg the VS Code-style surface he wants for managing many terminal sessions, Git, and occasional direct file inspection. *"I only use the IDE to manage all of my terminal sessions."* [[00:14:40]](https://youtube.com/live/kfCi2EBu-nc?t=880) He tried a terminal multiplexer but returned to the VS Code-style interface because the integrated Git view was useful and the editor remained available when needed. *"I like the GUI version in VS Code, whether it's Cursor or whatever version of VS Code you're using."* [[00:22:50]](https://youtube.com/live/kfCi2EBu-nc?t=1370)

### Claude Code and Codex

Greg moves between Claude Code and Codex depending on the work. Lore uses the native menu picker in Claude Code for its guided setup, and it can install a forged skill across multiple agent environments. *"The skill actually tells Claude how to interact with you. So you get this guided setup using some of the built-ins, in terms of this menu picker and whatnot that Claude natively supports."* [[00:18:10]](https://youtube.com/live/kfCi2EBu-nc?t=1090)

### [Impeccable](https://impeccable.style/)

Greg uses Impeccable for front-end work, presentations, and other HTML artifacts. *"Anything that's HTML, it's amazing at."* [[00:17:45]](https://youtube.com/live/kfCi2EBu-nc?t=1065)

### Stoa

Stoa is an interactive WebRTC collaboration environment that Greg used as a large test corpus while building Lore. The run included at least 1,600 sessions, and Greg waited to ship Lore until its output contained a skill he genuinely wanted to install. *"I want to actually install one of these skills that it's produced."* [[00:28:40]](https://youtube.com/live/kfCi2EBu-nc?t=1720)

### JFK files viewer

Greg and Hugo built a viewer for the newly released JFK files in April 2025, before `vibe coding` had become their normal label for that kind of work. *"I think that day, we were vibe coding before it was really even called vibe coding."* [[00:02:10]](https://youtube.com/live/kfCi2EBu-nc?t=130)

## Principles and explainers

### Agent traces preserve intent and repeated working patterns

Finished code preserves what was built, while agent sessions also retain the decisions, corrections, preferences, and verification habits that shaped it. Those histories can expose patterns that the user repeats without having named or documented them. *"A lot of the patterns and heuristics that you use are actually in those agent session logs."* [[00:05:40]](https://youtube.com/live/kfCi2EBu-nc?t=340)

### The next user turn supplies acceptance evidence

A user prompt and agent response do not show whether the result was useful. Lore includes the next user prompt in each beat so it can classify acceptance, rejection, or correction. That metadata becomes part of the evidence used to mine and corroborate patterns. *"Did you actually accept what came out of the response from your prior prompt?"* [[00:20:35]](https://youtube.com/live/kfCi2EBu-nc?t=1235)

### Deterministic preprocessing makes large session corpora tractable

Greg separates repeatable indexing and parsing from model-driven theme analysis. The deterministic layer supports independent runs over the same directory and reduces the amount of raw transcript text sent to the model. The model then spends its reasoning budget on mining themes and adjudicating whether a candidate is worth presenting. *"There's actually two parts to this. So there's a deterministic part, and then there's a non-deterministic part."* [[00:19:05]](https://youtube.com/live/kfCi2EBu-nc?t=1145)

### Cross-project recurrence makes a stronger skill candidate

Lore retains dossiers across runs and looks for recurring behavior across projects. A practice seen in SpecStory Cloud, Stoa, the CLI, and the VS Code extension carries stronger evidence than a one-off instruction in a single session. *"It did some adjudication to understand if that pattern was one worth presenting."* [[00:30:10]](https://youtube.com/live/kfCi2EBu-nc?t=1810)

### High-reasoning models fit infrequent pattern-mining runs

Lore's deep run is slow and occasional. Greg prefers a high-reasoning model because it needs to recover latent themes from long histories, while the deterministic engine handles the bulk parsing. *"You actually want to have a lot of reasoning, and you want to use the workflow because you're trying to pull out all these latent themes in what you've done."* [[00:27:35]](https://youtube.com/live/kfCi2EBu-nc?t=1655)

### Candidate skills need human judgment before and after installation

Lore filters weak candidates through corroboration and adversarial adjudication, but Greg still reviews the surviving dossiers. He can approve one candidate, reject the rest, inspect the generated skill, and uninstall it if the artifact is not useful. *"It skips a bunch of stuff that it couldn't adversarially adjudicate as being relevant or important enough because it hadn't found it in enough evidence."* [[00:33:20]](https://youtube.com/live/kfCi2EBu-nc?t=2000)

### Repository trust determines when agents push

Greg keeps accumulated commits local when he wants the final push to remain a human decision. *"I'll do a big batch of work, accumulate a lot of local commits, but I don't want the agent to push it."* [[00:06:55]](https://youtube.com/live/kfCi2EBu-nc?t=415) On a small, high-trust team, he pushes directly to trunk and has the agent summarize the change. *"Just push it straight to trunk, have your agent summarize it."* [[00:09:45]](https://youtube.com/live/kfCi2EBu-nc?t=585)

### Keep mined evidence readable across hundreds of sessions

Greg combines deterministic processing with carefully designed skill instructions and menus so the results remain readable after hundreds of sessions are mined. *"I tried to put a lot of effort into making it such that it was easy to parse."* [[00:35:35]](https://youtube.com/live/kfCi2EBu-nc?t=2135)

### A meta-harness can manage several coding agents

Greg has built a harness around multiple coding harnesses, and his daily stack already treats Cursor as a surface for Claude Code and Codex. *"I've gone so far as building a harness around harnesses. It gets really meta."* [[00:03:30]](https://youtube.com/live/kfCi2EBu-nc?t=210)

## Additional quotations

- On agents and product feedback: *"The whole goal is to get that out in the world and get feedback and iterate."* [[00:08:45]](https://youtube.com/live/kfCi2EBu-nc?t=525)

- On the Lore demo surviving API failures: *"I can't believe this actually worked on this live demo."* [[00:29:40]](https://youtube.com/live/kfCi2EBu-nc?t=1780)

- On installed-skill discipline: *"I tend to be pretty choosy about the skills that I install, but you see I have at least 30 or so."* [[00:17:00]](https://youtube.com/live/kfCi2EBu-nc?t=1020)

- On long sessions: *"I tend to use the same session for a very long time since compaction has gotten so much better."* [[00:28:20]](https://youtube.com/live/kfCi2EBu-nc?t=1700)


## Live reactions and follow-ups

### Will GitHub remain the platform?

Greg expects Git to endure because it works on file systems, is battle-tested and hardened, and is difficult to displace. Agents make it easier to use because their training makes them fluent in Git mechanics. Greg sees more uncertainty around GitHub as the hosting platform: *"I think that Git's not going anywhere. Whether or not GitHub remains the platform, we'll see."* [[02:01:10]](https://youtube.com/live/kfCi2EBu-nc?t=7270) GitHub's network effects, integrations, and Actions infrastructure still make displacement difficult. Greg calls Actions *"the biggest source of GitHub lock-in"* because teams use the platform to build, deploy, and release artifacts as well as store code. [[02:09:20]](https://youtube.com/live/kfCi2EBu-nc?t=7760)

### Greg's links and audience reaction

Greg posted the [Lore source](https://github.com/specstoryai/getspecstory/tree/dev/lore), his free book [*25 Patterns in Agentic Engineering*](https://specstory.com/books/25-patterns-in-agentic-engineering-book-2026.pdf), and the [Hardcore Agentic Engineering](https://maven.com/specstory/hardcore-agentic-engineering-for-builders-who-ship?promoCode=HARDCORE) course. Seth Tam described Han and Greg as “great educators” and thanked them for “explaining the basics.”

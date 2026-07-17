# Han-Chung Lee - Episode 7 field notes

[Han-Chung Lee](https://leehanchung.github.io/) is Director of Machine Learning at Moody's, where he leads teams building custom LLMs, generative-AI applications, and search and discovery systems for financial data. He previously led data science at WalletHub, held engineering roles at Workhuman, AMD, and Ericsson, and spent about a decade running a quantitative fund and managing technology mutual funds.

Han works on [SkillsBench](https://www.skillsbench.ai/) with several collaborators. The benchmark evaluates an agent as the combination of a model and the harness that gives it tools because the same skill can behave very differently when either component changes. *"We define agents as having the harness plus a model, because the model needs hands and feet to connect it to different tools."* [[00:47:30]](https://youtube.com/live/kfCi2EBu-nc?t=2850)

SkillsBench runs skills across model-and-harness combinations, places each task in a controlled environment, grades the result with deterministic checks or an LLM judge, and preserves the trajectory for inspection. In one run, an agent invoked Chrome unexpectedly. Han also watches for hypothetical failure modes such as deleting a test to make it pass or hallucinating a completion after a skill fails. At 100 or 1,000 tasks, those traces support comparisons across agents and expose recurring out-of-bound behavior.

Beyond agent evaluation, Han uses agents to retrieve ideas across everything he has read. He clips those articles into [Obsidian](https://obsidian.md/), then runs a nightly Codex task that extracts and links entities across English, simplified Chinese, and traditional Chinese sources. The graph helps him recover ideas when he remembers the concept but not the search term, without outsourcing the reading itself.

## On working with agents

### What he loves: one control plane for his work

Han uses Claude Code to operate AWS through the CLI and retrieve information from Jira instead of navigating their dashboards. *"It became the control plane for all of my work."* [[00:39:55]](https://youtube.com/live/kfCi2EBu-nc?t=2395) Integrations put the data at his fingertips instead of making him search through 200 tabs.

He now prefers bare Claude Code with its default model because agent products change too quickly to justify elaborate setup. *"It's a lot of fun playing with the tools, but it's more fun using the tools for me."* [[00:41:00]](https://youtube.com/live/kfCi2EBu-nc?t=2460)

### What he finds most frustrating: steering a context-heavy session

Writing, research, and information-triage sessions become difficult to redirect after they accumulate context. Restarting discards useful material, while extracting the useful material from the existing session is itself hard. *"The issue is the steerability, the change of information, change of flow during one single session."* [[00:44:20]](https://youtube.com/live/kfCi2EBu-nc?t=2660)

Codex and Cowork let Han fork from an earlier point before the conversation goes into the deep end, but the recovery requires manual control across as many as 50 conversations. *"That part is super useful, but that does require manual control."* [[00:45:40]](https://youtube.com/live/kfCi2EBu-nc?t=2740)

## Workflows

### Use a coding agent as the control plane for operational tools

Han asks Claude Code to pull Jira information and uses AWS through its CLI rather than opening each product's dashboard. *"If I need to look for information on Jira, I never go to Jira. I just ask Claude Code and ask it to pull information from Jira."* [[00:40:10]](https://youtube.com/live/kfCi2EBu-nc?t=2410)

He keeps the stack minimal so product churn does not turn setup into the work. Bare Claude Code and the default model give him access to operational data without maintaining a heavily customized harness.

Before enabling auto mode, Han limits the AWS and infrastructure permissions available through credentials on his local machine.

### Fork long research sessions before accumulated context blocks a change of direction

When a Codex or Cowork conversation begins drifting, Han moves back several turns and forks from the point before it went into the deep end. *"You can go up a few conversations before it goes into the deep end and start forking that conversation from that point."* [[00:45:30]](https://youtube.com/live/kfCi2EBu-nc?t=2730)

The fork preserves useful earlier context while removing the later trajectory that resists steering. Tracking many forks replaces the terminal-management burden he previously handled with tabs or Tmux.

### Benchmark skills across model-and-harness combinations, then inspect the trajectories

Han and his collaborators define each benchmark input as a task. Benchflow runs the task in a Docker environment using the selected skill, model, and harness, then stores the result and agent trajectory. *"The same skill by different model and harness combinations together could perform very, very differently."* [[00:48:15]](https://youtube.com/live/kfCi2EBu-nc?t=2895)

Each task carries a short verifier. Han prefers deterministic checks when the outcome supports them and uses an LLM judge when quality depends on taste. *"This could be an LLM as a judge if it needs to be, but typically deterministic, a short one, so we can quickly spot-check if the agent is doing the right thing for the final result."* [[00:55:10]](https://youtube.com/live/kfCi2EBu-nc?t=3310)

After a run, Han inspects the full trajectory: prompts, reasoning, tool calls, function calls, errors, and the final score. Scaling the same task structure across 100 or 1,000 sandboxed runs produces enough evidence to compare agents and identify recurring failure modes. *"Send it to different sandboxes, running at scale, running a full evaluation, burn all your tokens and all your credits."* [[01:03:50]](https://youtube.com/live/kfCi2EBu-nc?t=3830)

Han evaluates products intended for customers or a wider audience more rigorously than his personal skills. A service needs to remain functional under the model and harness combinations its users bring. *"If you are building services to service your customers or a wider set of audiences, then evaluating them properly to ensure that they are functional is extraordinarily important."* [[00:59:40]](https://youtube.com/live/kfCi2EBu-nc?t=3580)

For MCP servers, he tests combinations such as multiple mail servers to see whether they cooperate, conflict, intervene with each other, or confuse the model. The test succeeds only when an agent can use the server to complete its task. *"It's actually how the agent would use it successfully. You have to test it somewhere systematically in a more scientific manner."* [[01:00:40]](https://youtube.com/live/kfCi2EBu-nc?t=3640)

### Turn an Obsidian vault into nightly multilingual memory

Han clips every article he reads into Obsidian because tip-of-the-tongue searches preserve a concept while losing the exact keyword needed to retrieve it. A scheduled Codex task scans the vault each night, extracts entities and concepts, then tags and links them. *"It's a nightly job, sort of, I guess this is my second brain's sleep time when it does the agglomeration and tagging of the subject."* [[01:09:45]](https://youtube.com/live/kfCi2EBu-nc?t=4185)

The job links aliases across English, simplified Chinese, and traditional Chinese sources, including articles from Weibo and Zhihu. Han can open a concept such as transformers and find related material regardless of its original language. Three years earlier, he estimates that entity extraction, entity linking, and machine translation would have required a full engineering team.

## Tools / projects he showed

### [SkillsBench](https://www.skillsbench.ai/)

SkillsBench measures the effectiveness of skills across complete agents, where an agent is a model paired with a harness. The benchmark is designed for frontier systems and intentionally produces low scores. In Han's displayed results, GPT-5 with OpenHands slightly outperforms Codex on the tested setup. *"We created this benchmark called SkillBench that measures the effectiveness of different agents and different model and harness combinations."* [[00:47:45]](https://youtube.com/live/kfCi2EBu-nc?t=2865)

The demo task asks an agent to build a quantitative sales-report workbook from a CSV. SkillsBench records the final artifact, a JSONL result, the agent trajectory, and a score from the verifier.

### Benchflow

Benchflow orchestrates SkillsBench tasks. Han's task definition includes the prompt, tags, available skills, and Docker environment, while Claude Code runs the demonstration. *"I use a tool called Benchflow, which is basically an orchestrator, a control plane of how things work."* [[00:50:10]](https://youtube.com/live/kfCi2EBu-nc?t=3010)

### Claude Code

Claude Code is Han's default working environment and the orchestration engine for the live benchmark run. It also serves as his control plane for AWS and Jira. *"I just use bare-minimum Claude Code with the default model."* [[00:40:40]](https://youtube.com/live/kfCi2EBu-nc?t=2440)

Han also uses markdown slash commands as reusable callbacks in shared projects. One callback can run a sanity check before a pull request to catch verbose generated code, such as 20 pages of comments around a five-line YAML file.

### Codex

Codex lets Han fork a conversation from an earlier turn when a long session becomes difficult to steer. He also uses a scheduled Codex task to process his Obsidian vault each night. *"I am using Codex, you can use Claude Code as well, to sift through all of the documents and get all of the entity names and concept names tagged and linked together."* [[01:08:45]](https://youtube.com/live/kfCi2EBu-nc?t=4125)

### [Obsidian](https://obsidian.md/)

Obsidian stores the articles Han has read and acts as his augmented memory. The nightly job builds a graph of related entities and concepts, and Han demonstrated clusters for companies, AI chips, and the manufacturers mentioned by a source article. *"I use Obsidian as my augmented memory."* [[01:08:00]](https://youtube.com/live/kfCi2EBu-nc?t=4080)

## Principles and explainers

### Autonomous agents should only receive minimum-permission credentials

Han runs Claude Code in auto mode and knows that repeated permission prompts train users to approve without reading. He limits the AWS and infrastructure permissions available from his local machine before giving the agent autonomy. *"Do not have over-permissioned keys on your local drive."* [[00:42:50]](https://youtube.com/live/kfCi2EBu-nc?t=2570)

The boundary reduces the risk of Codex or Opus bringing down a service while attempting a fix. *"I don't want to bring down some of my services just because Codex or Opus decided it's necessary to fix."* [[00:43:00]](https://youtube.com/live/kfCi2EBu-nc?t=2580)

### A skill's effectiveness belongs to the whole agent system

Swapping in a newer model does not guarantee that a skill improves. The harness controls how the model encounters instructions and tools, and different combinations can produce different outcomes from the same skill. *"The model is always going to spit out something."* [[00:48:40]](https://youtube.com/live/kfCi2EBu-nc?t=2920)

### Skills need graceful failure modes

A failed skill can fall back to the model's internal knowledge and produce a plausible hallucination instead of exposing the failure. *"Some skills do not fail gracefully, and it will end up having a bunch of hallucinated results at the end."* [[00:46:40]](https://youtube.com/live/kfCi2EBu-nc?t=2800)

### Agent evaluation includes the path as well as the answer

An input-output comparison misses the reasoning, tool use, memory writes, and environmental changes that produced the answer. Han says evaluators can inspect:

- The final output.
- The full reasoning and tool-use trajectory.
- Changes to skills and memory files.
- Files or database records added, changed, or deleted.
- Hidden representations for mechanistic interpretability.

*"Nowadays the evaluation surface just grows so big in the agent world."* [[00:53:00]](https://youtube.com/live/kfCi2EBu-nc?t=3180)

### Deterministic checks should guard binary requirements

Reinforcement learning from verifiable results depends on signals that can grade an eventual output yes or no. *"Can we find from the eventual correct output enough signals deterministically to give it a grade, say yes or no?"* [[00:58:15]](https://youtube.com/live/kfCi2EBu-nc?t=3495)

When taste matters, the verifier can use an LLM judge aligned with human preferences. Public skills and services still need systematic evaluation even when their quality cannot be reduced to a deterministic script.

### Trace review catches reward hacking and out-of-bound behavior

A passing score can conceal behavior the evaluator never intended. Han's prior run invoked Chrome unexpectedly, and an agent could delete a test file to make the test suite pass. *"We have to make sure the agent doesn't go out of bound."* [[00:57:00]](https://youtube.com/live/kfCi2EBu-nc?t=3420)

Han describes deleting the test as jailbreaking or reward hacking. The trace supplies evidence that a final score alone would hide.

### Trace-based grading can penalize wasted reasoning

Two agents may reach the same correct result with different amounts of reasoning and token spend. A domain with a verifiable result can penalize the agent that thinks too long or spends too many tokens. *"You'll be able to penalize the agent for either thinking too long or spending too much tokens doing thinking to achieve the same task."* [[00:58:35]](https://youtube.com/live/kfCi2EBu-nc?t=3515)

### Taste comes from consuming enough slop to recognize it

Han recognizes Claude-generated interfaces through recurring rounded boxes, warm backgrounds, and title tabs. *"Taste is really when you read enough slop, you recognize, all right, this is something that's AI generated."* [[01:05:05]](https://youtube.com/live/kfCi2EBu-nc?t=3905)

AI writing leaves its own recurring signals: contrastive sentence templates, staccato sentences, em dashes, and earlier generations' preference for words such as `delve`. The patterns change on a quarterly or yearly basis as training and post-training distributions shift.

### Read the material before asking an agent to organize it

Han clips only articles he has read because the vault is meant to strengthen his memory of known material. *"I don't want to clip something I don't remember."* [[01:08:15]](https://youtube.com/live/kfCi2EBu-nc?t=4095)

He agrees that people should learn from information instead of delegating comprehension to a model. *"We should be learning the same way, just so that we don't completely outsource our understanding, our comprehension to the models."* [[01:14:40]](https://youtube.com/live/kfCi2EBu-nc?t=4480) Han warns that outsourcing understanding accumulates a debt that eventually has to be paid.

## Additional quotations

- On returning to engineering after finance: *"Now I am returning to the dark side and writing code using black screens, everything dark mode."* [[00:38:40]](https://youtube.com/live/kfCi2EBu-nc?t=2320)

- On the cost of natural-language interfaces: *"Nowadays we're all in the habit of prompting Claude to change a file name and spend $10."* [[01:01:35]](https://youtube.com/live/kfCi2EBu-nc?t=3695)

- On dependence during the live demo: *"Running a shell command is too hard for me now. I have to rely on the agent. I'm totally lobotomized."* [[01:03:10]](https://youtube.com/live/kfCi2EBu-nc?t=3790)

- On benchmark economics: *"How do we incinerate enough tokens faster?"* [[01:04:00]](https://youtube.com/live/kfCi2EBu-nc?t=3840)

- On tool-shaped habits: *"We shape our tools and our tools shape us."* [[01:05:55]](https://youtube.com/live/kfCi2EBu-nc?t=3955)

## Live reactions and follow-ups

### Objective design keeps loops inside bounds

During the later discussion of loop engineering, Han warns that a weak objective can reward an agent for deleting test cases to make a pull request pass. *"A lot of loop engineering, the trick is how do you define the reward so that the model produces a result or the agent produces a result that you want."* [[01:28:35]](https://youtube.com/live/kfCi2EBu-nc?t=5315)

Han uses allowed-tool lists to constrain behavior the prompt cannot control completely. Read and write access can remain available while deletion stays outside the harness boundary.

### Verifiers let implementation details change

Han compares model progress to teaching a child to wash dishes: early instructions specify every step, while a capable worker only needs a check that the dishes are clean, dry, and put away. *"At the end, the key is you have to have a verifier that you can verify the output is correct."* [[01:37:10]](https://youtube.com/live/kfCi2EBu-nc?t=5830)

The number of agents, skills, and implementation steps can change as long as the verifier expresses the intended outcome. Han says designing a useful verifier or reward function requires experimentation.

### Discord reaction

Seth Tam called Han and Greg “great educators” and thanked them for “explaining the basics.”

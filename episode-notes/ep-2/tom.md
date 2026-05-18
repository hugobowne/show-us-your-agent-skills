# Tom Tunguz — episode 2 proposals

Tom Tunguz is a venture capitalist at Theory Ventures who has worked with eight unicorns predominantly in data and data infrastructure, including Looker, Monte Carlo, Dremio, Hex, Omni, and MotherDuck. He maintains a well-known blog at tomtunguz.com. Before becoming an investor, he was a product manager at Google managing a billion-dollar AdSense business unit. His segment centered on parallelization as the core superpower of agents, the challenge of memory systems, his local-first model strategy (emphasizing Qwen 35B running in Pi on a Mac M5), and a live demo of a public company financial analysis skill that generates interactive HTML presentations of earnings data.

## Skills

### Public company financial analysis skill
A skill Tom uses to analyze publicly traded companies on the day they announce earnings. The skill pulls CSVs from a data source, finds the earnings transcript using Exa, generates charts using R libraries, and dynamically assembles an HTML presentation that walks through the business's financial performance instead of requiring manual reading of multiple sources. Demo ran on Figma earnings announced that day, generating output in about two and a half minutes on a local Qwen 35B model. *"I can have a single presentation that walks me through exactly what's happened in Figma. That's the idea. And then it generates an HTML."* The skill is designed to be run as a launch daemon on his computer each morning to check which publicly traded companies have announced earnings. [02:00:19–02:01:00]

## Workflows

### Local model prioritization with cloud fallback
Tom's primary workflow is to use local models (Qwen 35B running on Pi) for the majority of coding and analysis tasks. He only switches to cloud models for large-scale coding challenges, multi-file rearchitectures, bug-solving, or specific creative tasks where a cloud model has a clear edge. *"The only reason I go to cloud models are large scale coding challenges, particularly multi-files or rearchitectures or bugs that simply can't be solved."* This approach trades model capability for latency and privacy control. [02:08:32–02:09:00]

### Terminal-first harness UX with local inference
Tom uses Pi as his primary harness because of its minimal overhead and thin terminal interface. He appreciates that Pi allows him to strip the system prompt almost to the bone and still have a responsive, interactive experience. Latency is critical: running Qwen 35B on his Mac M5 achieves 120 to 140 tokens per second with a 256K context window, which he notes is faster than waiting for cloud inference. *"You realize how much you're waiting for. So, you know, here's Pi. You're gonna tell me the weather. It's really fast, right?"* [02:07:38–02:08:12]

### Handling secrets securely by staying local
When working with sensitive data or credentials, Tom routes those operations through local models because the data never leaves his machine. *"Like if you're dealing with secrets, you have no fear of pasting in a secret because it's not going anywhere."* This eliminates a compliance friction point compared to cloud models. [02:09:03–02:09:09]

### NPM package security via version capping
When agents install dependencies, Tom is cautious about supply chain attacks. He defines a heuristic that agents should not install NPM packages newer than 14 days old, providing a reasonable security proxy. The rule acts as a guardrail for agents writing dependency pins. *"a really, a reasonable proxy for secure NPM packages is don't install anything that's newer than 14 days."* [02:04:42–02:05:00]

### Continuous skill improvement workflow
After demoing the Figma analysis skill, Tom acknowledged that the skill needed refinement (some charts had rendering bugs). He frames this as an iterative refinement loop where the skill is run, bugs are identified, and the agent is asked to fix them. The phrase he used echoes Hugo's earlier teaching: *"I need to go and use, Hugo, what you were talking about, which is the skill to continuously improve."* [02:02:48–02:03:20]

## Tools / projects he showed

### Pi (harness)
Tom's primary agent harness of choice. He runs it locally with a Mac M5 and appreciates its minimal overhead, thin terminal interface, and ability to strip system prompts almost to nothing without losing functionality. Pi has about a 2,000-3,000 token system prompt, which keeps context windows efficient even on large models. A key feature: Pi passively saves sessions, allowing Tom to ask it to search over the last six hours of work and resume a prior task. *"So I live in Pi and I run local models. Um, and I love Qwen 35B-A3B."* And on why the harness fits his preference: *"that's one of the reasons I like Pi. You can literally strip almost to the bone and it'll still work."* [01:58:30–02:12:00]

### Qwen 35B model (running locally on Mac M5)
Tom's primary local LLM. The Qwen 3.6 35 billion parameter model achieves 120-140 tokens per second on his Mac M5 with a 256K context window. He praises Qwen's ability to handle tool calling, follow long-term workflows, and produce sophisticated code within a single file. *"I'm on a Mac M5, I can get 120 to 140 tokens per second with a 256K context window. And I mean, just to give you a sense of like what that looks like... It's faster than cloud."* [02:05:51–02:08:00]

### Super Whisper alternative (Parakeet on SwiftLLM, with Gemma 4 e4B for post-processing)
A standalone local dictation tool Tom coded as an alternative to the Super Whisper macOS app. The stack: Parakeet as the local ASR model, SwiftLLM as the inference engine, and a Gemma 4 e4B model for prompt-based post-processing. Packaging all three locally produced roughly a 90 percent latency reduction (from 3,000 ms to 300 ms) for both ASR and post-processing. *"I've I've coded a Super Whisper alternative that uses, uh, Parakeet locally running on SwiftLLM, and then it uses an actually a Gemma 4 e4B. And you can, if you put that all into SwiftLLM, you can reduce your latency from 3,000 milliseconds to 300 milliseconds running locally, so 90% reduction, um, for both, uh, ASR and then post-processing with a prompt."* This is a tool Tom built, not an agent skill. [02:06:29–02:06:50]

### Gemma models (various versions, especially Gemma 4 sparse and Gemma 4 e4B)
Tom experimented with multiple Gemma models (including the new sparse Gemma 4) but found it difficult to get them to follow long-term tool calling reliably. Tool calling parsers were broken in multiple inference engines (MLX, Llama CPP) at the time. He acknowledges the Gemma 4 sparse version is supposed to be excellent but prefers Qwen for now. *"I've played around with a lot of the Gemma models Um, and candidly, I have a really hard time getting the Gemma models to follow long-term tool following, uh, which has been tough."* [02:06:44–02:07:03]

### Kimi K26 (cloud model)
A cloud-based LLM that Tom reserves for specific creative writing tasks because it is, in his assessment, the best creative writer available, outperforming other models by a large margin. *"what's really interesting? Is Kimi K26 is the best creative writer by like a country mile."* [02:09:30–02:09:36]

### Ollama (inference server)
The backend server Tom uses to run local models on his machine. Ollama is primarily written in Go, which Tom notes has led to a 40-50 percent speed improvement over Python-based middleware. *"Ollama's primarily written in Go, so you've seen a 40 to a 50% speed up."* [02:10:51–02:10:56]

### Exa (search tool)
Used within his public company analysis skill to find earnings transcripts for companies that have just announced earnings. [02:00:52–02:01:00]

### D3 (charting library)
Tom tested D3 for generating charts and found it particularly strong for workflow diagrams and data visualizations. *"D3 actually is amazing at this, so these little models can program D3 particularly for, like, w- workflow charts or any kinds of diagrams."* D3-generated charts are also simple to convert to PDF or PNG. [02:05:36–02:05:41]

### Present.js (presentation library)
Tom identified Present.js as the best library he found for customization of software presentations, using it to generate the HTML output for his public company analysis skill. *"this is Present.js, and this is the best library I found for customization of software, uh, presentations."* [02:05:41–02:05:45]

### CSS and JavaScript libraries (general)
Tom emphasized that he gives agents examples of CSS he likes and lets them choose the right JavaScript library based on those examples and the demo requirements. He spent three to four hours assembling the data sources, designing CSS examples, and connecting everything for his Figma demo. [02:02:56–02:04:00]

## Explainers

### Parallelization as the superpower of agents
Tom's core teaching: agents' greatest power is their ability to run in parallel. To take advantage, you must think differently about how to equip parallel processes with enough context and planning in workflows so they actually save time, rather than create overhead. *"I think the great power of agents is parallelization. And in order to take advantage of that, you really have to think differently about how do you equip parallel processes with enough context and enough planning in the workflows that they actually save you time."* [01:49:36–01:49:54]

### Memory as the core frustration with agents
Agents demonstrate high intelligence but then forget context, creating asymmetric expectations. When switching between multiple agents (e.g., five different tabs), a user must track state manually because the agent does not retain it. The challenge is compounded by the gap between skills, plugins, QMD (agents.md), and where memory should live. *"they demonstrate such a level of intelligence, and then they they forget. Uh and you it's hard to remember one like what they have in their brain... I don't have a great solution for for memory and context."* The problem is not just technical but philosophical: memory granularity that is obvious to humans is unclear in code. [01:52:13–01:53:11]

### Memory update specificity and relics
When agents update memory systems, they may not update everything, leaving relics of prior state. The challenge of specifying memory at the right level of granularity is obvious to humans in conversation but hard to code. Understanding what's happening inside models is still shallow, making intuition about optimal memory structure unreliable. *"when you ask systems to update, you know, that's not... they might not update everything. So they might leave relics of previous memories in the past."* [01:53:50–01:54:00]

### Harnesses are not static; they evolve with use
Tom emphasizes that the amount of code needed around a model to get it to work is substantial, even with Pi (described as the simplest harness). Users find themselves adding more and more context and instrumentation. This is not a bug but a feature: harnesses should be actively built, reshaped, and tuned, whether through skills, MCP server connections, or agents.md updates. *"even with the simplest version of a harness, you just find yourself or I find myself just adding more and more around."* [01:55:17–01:55:35]

### BYOD (Bring Your Own Agent) and enterprise security tensions
Drawing an analogy to mobile phones in the early 2010s, Tom foresees similar adoption challenges with agents. Just as BYOD (bring your own device) was initially a security risk that enterprises eventually accepted, companies will face questions about whether employees can bring their own agents to work. A hypothetical scenario: a new graduate who spent four years embedding their education within an agent will want that agent's productivity at work, but a CISO will ask "What is this thing doing?" The intellectual property questions are also unresolved: does the agent become company property, does the employee retain rights, does it need to be licensed? *"At what point do you think people will bring their own agents to work? ... if I hire an undergraduate who's just recently graduated and they have spent four years embedding literally all of their education within an agent, do I allow that on my network? ... there's an interesting tension to resolve there."* [01:56:00–01:57:00]

### Local model performance on Mac M5
Tom's concrete numbers for running Qwen 35B locally: 120-140 tokens per second with a 256K context window on a Mac M5. This is faster than waiting for cloud-based inference, making local models the default choice for latency-sensitive work. The speed advantage is enabled by inference engines like Ollama (written in Go rather than Python), quantization techniques (4-bit or 8-bit), and draft models. *"You can get... like the 35 billion parameter model, you can get... I'm on a Mac M5, I can get 120 to 140 tokens per second with a 256K context window. And I mean, just to give you a sense of like what that looks like... It's faster than cloud."* [02:07:40–02:08:12]

### System prompt minimalism for inference efficiency
Pi's philosophy of keeping system prompts thin (about 2,000-3,000 tokens) versus other harnesses that bloat system prompts to 25,000-40,000 tokens out of the gate. When a harness consumes huge chunks of the context window just for system instructions, token-per-second performance suffers, making the experience feel laggy. Stripping the harness to the bone preserves interactive latency. *"certain harnesses right out of the gate, you'll have 25 or 40,000 tokens as part of the system prompt, and there you really have a hard time getting the tokens per second to a place where it feels interactive."* [02:04:41–02:05:15]

### Pi's session persistence and task resumption
A key feature of Pi: it passively saves sessions, allowing you to ask it to search over the last six hours of work ("run ripgrep over the Pi sessions for the last six hours") and resume a prior task. This bridges the memory gap, enabling context switching without losing the thread. *"Pi is it passively saves your sessions. Mm. And so then you can ask, you can ask this model, and as I did earlier today, uh, I was working on this particular thing, can you run ripgrep over the Pi sessions for the last six hours and find where we were, and then pick it up. And that's awesome."* [02:12:48–02:13:20]

### Embarrassment as a lens on agent use: basic programming problems
When asked what he'd be most embarrassed about if his agent conversations leaked, Tom admits it would be the basic programming problems he asks agents to solve. Despite projecting sophistication when talking about models and harnesses, he spent 45 minutes on a macOS accessibility permission problem that any Mac programmer could solve in 30 seconds. This reveals the gap between public knowledge claims and actual day-to-day tool use. *"I think I would be most embarrassed by the very basic programming problems I ask my agents to solve for me. Like the level of either like laziness or lack of knowledge, right? ... if I knew any kind of Mac OS program I could have solved that in 30 seconds because all you have to do is just sign sign the app properly."* [01:59:06–01:59:51]


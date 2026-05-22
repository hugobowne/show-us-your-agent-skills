# Paul Iusztin — ep-3 field notes

Paul Iusztin is the author of the bestselling [LLM Engineer's Handbook](https://www.pauliusztin.ai/book), lead instructor of an Agentic AI Engineering course teaching AI engineering end to end, and creator of the [Decoding AI Magazine](https://www.decodingai.com/) on Substack. One of his stated goals is to help others escape proof of concept purgatory.

His segment centered on his second brain and agent-powered workflows for research and content creation. He demonstrated a customized knowledge base built on top of [Karpathy's LLM knowledge base](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f), multiple research skills, a multi-pass writing process anchored by agent-generated guidelines, and a curated reading and sourcing infrastructure using [Readwise](https://readwise.io/), [Obsidian](https://obsidian.md/), and RSS feeds.

## On working with agents

### What he loves: unlocking full potential and experimentation

Paul emphasizes velocity and the ability to finally explore ideas at scale. Working at Decoding AI (a very small team), he values that agents *"allow him for the first time in my life to write a ton of code, experiment with a ton of ideas, write a lot of articles, posts. Basically it allows me like to go on the full, to get my full potential basically, because up to this point I was just, time was a big issue for me to actually like building stuff, writing, creating content, so I never had time for all of this."* The broader freedom to automate boring tasks multiplies this effect. [\[02:09:15\]](https://youtube.com/live/ud2WzkKeDZs?t=7755)

### What he finds most frustrating: balancing precision and freedom

The core frustration centers on the tension between how prescriptive instructions must be and how much autonomy agents should receive. For coding, *"you need to be precise, but you don't need to be that precise because agents have seen a lot of code. So as long as you pin down the architectural decisions really well, they work to some extent."* For writing, the problem inverts: too much freedom introduces AI voice and filler, but too much specificity chokes the output. Finding the middle ground is exhausting, especially when waiting an hour for results only to find *"it's crap."* Additionally, he struggles with lack of control over model changes from upstream providers, which can unexpectedly break workflows. [\[02:11:12\]](https://youtube.com/live/ud2WzkKeDZs?t=7872)–[\[02:12:40\]](https://youtube.com/live/ud2WzkKeDZs?t=7960)

## Skills

### Research skill (core)

A foundational skill that ingests new data and repositories into his knowledge base, then queries it dynamically. Paul can feed it the path to a repository and receive a side-by-side comparison with existing knowledge, a deep dive into the repo itself, plus cross-pollinated concepts and comparisons. *"And probably after, I don't know, 10, 15, 20 minutes, it depends on the repository. I will get like side by side comparison with this new harness and basically a deep dive into the repository itself plus comparisons and concepts and all of this."* [\[02:19:52\]](https://youtube.com/live/ud2WzkKeDZs?t=8392)

### Obsidian ingestion skill

Extends his research capability by hooking into Obsidian (where his knowledge base lives), letting the research skill pull context directly from his personal notes and thought process rather than relying solely on external sources.

### Readwise integration skill

Connects his Readwise archive (where he logs highlights and notes from articles, books, and videos) to his research pipeline, so the research skill can search his personal library of curated resources when building context for a project.

### Notebook LM integration skill

Allows him to plug external resources into [Notebook LM](https://notebooklm.google.com/) for deep research on unfamiliar topics, expanding the research process beyond his own knowledge base to cover truly novel ground.

### Article guideline skill

Takes his research wiki and outline, then generates a machine-readable article plan containing metadata: what the article covers, why, who it is for, the ratio of theory to practice, point of view, special instructions, and section structure. Paul emphasized this is not meant to be human-readable but *"to be machine readable like to contain all kinds of metadata that I want to put into the article."* [\[02:26:17\]](https://youtube.com/live/ud2WzkKeDZs?t=8777)

### Article create skill

Transforms the machine-readable article guideline into prose that matches his voice and style. It uses [MCP](https://modelcontextprotocol.io/) servers to access his profiles (domain knowledge encoded as markdown files describing his writing preferences) and produces a finished, human-readable article. [\[02:28:11\]](https://youtube.com/live/ud2WzkKeDZs?t=8891)

### Article diff and improvement skill

Compares the agent-generated article against his edited version, identifies what he changed and why, and produces a plan for how to update his writing profiles based on the corrections. Paul treats this as a feedback loop to keep his system aligned with his evolving preferences and the underlying model changes. *"So after every article, I apply this skill and try to find, how can I improve my work? What rules do not apply anymore or what rules apply now and I should update my profiles."* [\[02:31:15\]](https://youtube.com/live/ud2WzkKeDZs?t=9075)

## Workflows

### Coupled research and outline exploration

Paul conducts research and outline creation in parallel or near-parallel rather than strictly sequentially. Because his wiki is built from his own questions and thoughts, the outline emerges naturally from the research, so *"when the research is done, the outline is almost done"* or 80-90 percent complete. This reduces rework and keeps the creative momentum alive. [\[02:25:24\]](https://youtube.com/live/ud2WzkKeDZs?t=8724)

### Quick outline sketching with explicit narrative structure

Paul spends about 15 minutes sketching an outline in prose, laying out the big ideas in the order he wants to teach them. He explicitly focuses on the narrative: *"the problem, the solution. Basically the core of the article, which comes from me."* The outline is mostly references to what should be brought from research, not the full prose. This keeps it fast and leaves the elaboration to the agent. [\[02:24:16\]](https://youtube.com/live/ud2WzkKeDZs?t=8656)

### Personalized knowledge base as the foundation

Rather than treating the knowledge base as a generic repository, Paul has built it coupled to his own processes and way of thinking. *"Because every knowledge base should be to some extent personalized on your own processes."* He sources from Obsidian, Readwise, RSS feeds of trusted sources, and imported repositories, so his research always grounds in his own curated context. This gives *"that special magic"* that he says is missing in many systems. [\[02:14:54\]](https://youtube.com/live/ud2WzkKeDZs?t=8094)–[\[02:36:18\]](https://youtube.com/live/ud2WzkKeDZs?t=9378)

### Profile-driven writing with living rules

Paul maintains a set of markdown-based writing profiles that encode his style, voice, and domain rules (shared profiles for all articles, plus article-specific profiles for unique structure or constraints). Rather than updating these manually, he uses his diff skill to identify what changed in each iteration, then applies data-driven improvements. *"I try as much as possible to find like signals in what I do to one way or another optimize my skills. It's similar to a loss function that, this is how I want to look like and this is the bot version. Do a diff between them and find what signal I can use to improve my skills instead of the model's weight."* [\[02:30:45\]](https://youtube.com/live/ud2WzkKeDZs?t=9045)

### Lazy but versioned skill development

Paul favors "vibe coding" skills rather than hand-crafting every detail upfront. His philosophy: *"If it works, it works, if it doesn't, I try to make it work, reduce and then I kind of manually go into it and fix stuff only when things break, not when bootstrapping stuff."* He versions everything and iterates only when necessary, avoiding premature optimization. [\[02:17:11\]](https://youtube.com/live/ud2WzkKeDZs?t=8231)–[\[02:18:06\]](https://youtube.com/live/ud2WzkKeDZs?t=8286)

### Symbiosis rather than control

Paul believes in working with LMs rather than trying to fight or fully control them. *"I personally think that you shouldn't fight LMs. You should find new ways of not like to get into some symbiosis with them, but this is just my point of view, guess."* This philosophy drives his tolerance for vibe coding and his openness to letting agents invent approaches he didn't explicitly specify. [\[02:18:40\]](https://youtube.com/live/ud2WzkKeDZs?t=8320)

## Tools / projects he showed

### Obsidian

The core of his second brain, where he maintains notes, highlights, and thought process. The knowledge base is built within Obsidian and feeds into his research and writing workflows. Paul appreciates Obsidian for platform independence and clean visuals, especially when working across devices. [\[02:33:08\]](https://youtube.com/live/ud2WzkKeDZs?t=9188)

### Zed editor

His primary [editor](https://zed.dev/) for coding and writing. Recently switched (a couple weeks before the episode). He values Zed for its speed and snappy interface, which matters when doing almost everything agentically and wanting a minimalistic, fast tool. [\[02:14:00\]](https://youtube.com/live/ud2WzkKeDZs?t=8040)

### Claude Code

His second brain setup uses [Claude Code](https://www.anthropic.com/product/claude-code) for both research and writing. He relies on it for running his skills and workflows. [\[02:33:08\]](https://youtube.com/live/ud2WzkKeDZs?t=9188)

### Readwise

A service for ingesting and curating articles, books, and highlights from multiple sources. Paul uses Readwise as a high-signal repository: he aggregates interesting content as he finds it (from YouTube, LinkedIn, etc.), then when starting a project, runs a deep research query against his Readwise archive to surface already-read material rather than re-searching the web. *"And the beautiful part is that I have like my own repository here. And when I do the research, I actually have also a deep research algorithm on top of it that looks inside my readwise repository and finds all the resources that I already read."* [\[02:34:30\]](https://youtube.com/live/ud2WzkKeDZs?t=9270)

### Karpathy's LLM knowledge base

The foundation of Paul's custom knowledge base. He built a personalized version of this system tailored to his own processes and workflows. [\[02:14:31\]](https://youtube.com/live/ud2WzkKeDZs?t=8071)

### Notebook LM

Google's tool for deep research on external materials that Paul is not yet familiar with. He hooks it into his research pipeline for exploring novel resources. [\[02:20:44\]](https://youtube.com/live/ud2WzkKeDZs?t=8444)

### MCP (Model Context Protocol) servers

Paul uses custom MCP servers to expose his writing profiles and other domain knowledge to his article create and article guideline skills, letting them access the rules and preferences he has encoded as markdown files. [\[02:28:11\]](https://youtube.com/live/ud2WzkKeDZs?t=8891)

### RSS feed aggregation

Paul maintains a curated collection of RSS feeds as a living repository of trusted sources. When researching, he treats content from these feeds as high-signal, so he can avoid the noise of broad web search and focus on sources he already trusts. [\[02:35:26\]](https://youtube.com/live/ud2WzkKeDZs?t=9326)

## Explainers

### Personal knowledge bases should be shaped by your own processes

Paul is explicit that generic knowledge bases miss the magic. The real power comes from building a system that reflects how you already think and work. *"Because every knowledge base should be to some extent personalized on your own processes."* This means ingesting your highlights from Readwise, your notes from Obsidian, your trusted RSS feeds, and your imported code repositories, all together. The system becomes not just a reference but a reflection of your mind. [\[02:14:54\]](https://youtube.com/live/ud2WzkKeDZs?t=8094)

### Writing should be anchored in your research, not generic internet content

Paul contrasts two approaches: anchoring articles in a personal research wiki (derived from your own questions) versus pulling from generic static internet sources. The former produces writing that reflects your thought process; the latter produces generic, derivative content. *"Basically, then your articles will be anchored in your thought process and not in something super generic from the internet."* [\[02:23:46\]](https://youtube.com/live/ud2WzkKeDZs?t=8626)

### Separate the machine-readable planning phase from the human-readable prose phase

Paul deliberately splits the writing process into two stages. The first generates a machine-readable article guideline full of metadata (structure, sections, ratios, POV); the second transforms that into human prose. By making the guideline machine-readable rather than human-readable, he can encode the exact logic he wants while leaving style and voice to the second pass. This also makes the guideline easier to debug and improve iteratively. [\[02:26:17\]](https://youtube.com/live/ud2WzkKeDZs?t=8777)

### Data-driven profile improvement using diff feedback

Rather than manually tuning writing profiles, Paul uses each completed article as a training signal. He diffs his edited version against the agent version, extracts what changed, and turns that into a structured plan for updating his profiles. This treats the writing system like a machine learning model: the profiles are the parameters, each article is a data point, and the diffs are the gradients. *"It's similar to a loss function that, this is how I want to look like and this is the bot version. Do a diff between them and find what signal I can use to improve my skills instead of the model's weight."* [\[02:31:15\]](https://youtube.com/live/ud2WzkKeDZs?t=9075)

### Embracing symbiosis with LMs rather than fighting them

Paul argues against the instinct to lock down and control agents through increasingly restrictive prompts. Instead, he finds value in letting them explore and even invent approaches. *"I personally think that you shouldn't fight LMs. You should find new ways of not like to get into some symbiosis with them."* This mindset allows faster iteration and often produces better results, because the agent can propose solutions the human wouldn't have thought to specify. [\[02:18:40\]](https://youtube.com/live/ud2WzkKeDZs?t=8320)

## Additional quotations

- On the specific challenge of writing with agents: *"For example, for writing and other things, always if you leave them too much interpretation and gaps, like the LLM and AI voice immediately pops out and you can see like the these phrases that have no meaning and they're just there to be there just to comply with other work count requirements that you added and so on and so forth."* [\[02:11:36\]](https://youtube.com/live/ud2WzkKeDZs?t=7896)

- On the value of letting agents invent skills: *"I would never refer to myself in the third person, but it's just I asked very briefly in the chat and it invented this way to do it."* [\[02:18:40\]](https://youtube.com/live/ud2WzkKeDZs?t=8320)

- On his second brain stack philosophy: *"Basically you need Obsidian plus an ID that you love and enjoy using. That is great because it's super snappy and now because I do almost everything agentively. The thing that I care most about is have like a minimalistic interface and everything to be snappy fast."* [\[02:33:08\]](https://youtube.com/live/ud2WzkKeDZs?t=9188)

- On the advantage of sourcing from trusted feeds: *"I usually treat this as a high signal resource. And also I have this RS feed where I have all kinds of feeds put here, where basically I create a living repository of everything, of resources that I trust."* [\[02:35:26\]](https://youtube.com/live/ud2WzkKeDZs?t=9326)

- On the state of his workflows: *"Yeah, they're not yet there, but 80-90 % I think. I'm very bullish on this."* [\[02:37:23\]](https://youtube.com/live/ud2WzkKeDZs?t=9443)

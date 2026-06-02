# Doug Turnbull - Episode 4 field notes

Doug Turnbull is introduced as a search specialist who has led search teams at Shopify, Reddit, and Wikipedia, authored AI-Powered Search, advised over a hundred organizations, and teaches search-heavy agent courses. His segment is an auto-research walkthrough: can an agent modify BM25-style ranking code, evaluate patches on MS MARCO, avoid overfitting, and learn useful search heuristics through a structured optimization loop?

## On working with agents

### What he loves: agents do useful work with compressed human knowledge

Doug likes agents because they usually follow instructions, do real work, and bring a broad prior over human knowledge to the problem. *"I love the fact that they mostly do what I tell them to do. They get a lot of work done and they come with an encyc they basically come with a pre-built encyclopedia of the entire of a compressed version of the entire entire human knowledge."* [\[01:20:35\]](https://youtube.com/live/XaYQFtca798?t=4835)

The practical version is simple: *"I can just point that at a problem and it generally does the solves a problem."* [\[01:20:55\]](https://youtube.com/live/XaYQFtca798?t=4855)

### What he finds most frustrating: inconsistent autonomy

Doug's daily frustration is not that agents are useless. It is that they are hard to calibrate. Some days they ask permission for tiny steps, other days they become dangerously confident. *"there are some days where it's like that agent wants to beg permission to do any minor thing."* [\[01:21:12\]](https://youtube.com/live/XaYQFtca798?t=4872)

The opposite mode is worse: *"there are other days where it's just like completely overconfident and thinks the human is stupid and is just gonna like delete all all of my code and go crazy."* [\[01:21:24\]](https://youtube.com/live/XaYQFtca798?t=4884)

His real job is keeping the agent inside the right boundary: *"okay, yes, you can do that, you're okay, but don't go farther than this line."* [\[01:21:51\]](https://youtube.com/live/XaYQFtca798?t=4911)

## Workflows

### Auto-research a better BM25 for one dataset

Doug's central workflow asks whether an agent can improve a BM25-style retrieval function on a specific dataset. He is careful not to claim a universal replacement for BM25. The aim is local and eval-driven: *"could I find a basically a better retrieval function? A slightly better way of doing the keyword matching."* [\[01:35:47\]](https://youtube.com/live/XaYQFtca798?t=5747)

He links the work to his [Autoresearching BM25 on MSMarco](https://softwaredoug.com/blog/2026/05/17/autoresearching-a-better-msmarco-bm25) post and the [search-experiments notebook](https://github.com/softwaredoug/search-experiments/blob/main/notebooks/codegen/codegen_minimarco.ipynb).

The loop has a few moving parts:

- **Give the agent code-editing tools, not vague permission.** Doug says the code-editing part of a coding agent is not the hard part. The tool can be a structured search-and-replace operation over code. *"You're basically designing a tool call that does a search and replace that says like find this snippet of code, go to find the another end of the code and delete all that and replace it with this new text I gave you."* [\[01:36:40\]](https://youtube.com/live/XaYQFtca798?t=5800)
- **Separate training queries from holdout validation.** Doug's most important workflow detail is ML-shaped: let the agent inspect training queries deeply, but judge proposed changes on data it did not see. Otherwise it will overfit ranking code. *"So if you just tell Claude Code to make search better, here's some evals, that's that's what's gonna happen. So you need to actually think really carefully about the the optimization flow."* He frames the split as progressive disclosure: training data lets the agent introspect, validation data decides whether a patch survives. [\[01:38:52\]](https://youtube.com/live/XaYQFtca798?t=5932)
- **Let the agent try patches before committing them.** Doug gives the agent a `tryout patch` tool as a sandbox. It edits a reranker function, evaluates on training queries, and receives detailed feedback. *"What happens is the agent calls this tool tryout patch. That's its like little sandbox way of evaluating things."* Only after the agent finds a change it likes does it call the apply step. [\[01:39:41\]](https://youtube.com/live/XaYQFtca798?t=5981)
- **Accept or reject patches on holdout performance.** The apply step is gated by validation data. The system accepts or rejects the patch based on holdout performance: *"I will either accept it or reject it based on whether this change improved the whole the holdout validation or didn't improve the holdout validation."* Doug's reason is blunt: *"that helps to prevent most of the stupid overfitting that agents tend to do to ranking code."* [\[01:41:11\]](https://youtube.com/live/XaYQFtca798?t=6071)
- **Serialize auto-research rounds.** Doug does not expect one long agent run to solve everything. Each run knows the code and tools, makes one round of changes, summarizes what changed, and produces a new reranker. Doug then starts a new round from that output: *"I take the output of that round and then I start a new round. So I I I've been just serializing these rounds."* [\[01:48:05\]](https://youtube.com/live/XaYQFtca798?t=6485)

### Feed judged search results back as user feedback

For agentic search, Doug finds that even a simple LLM judge can improve behavior when its judgment is returned to the agent as a user message. *"A single like naive LM judge labeling results after a single pass of that and t sending it back into the agent as a user message saying, I did I like this, I didn't like this"* can improve search more than expected. [\[01:56:13\]](https://youtube.com/live/XaYQFtca798?t=6973)

The surprising part is behavioral: *"the agent really adjusts its behavior to to to to account for that in a way it doesn't adjust its behavior from its own reasoning."* [\[01:57:02\]](https://youtube.com/live/XaYQFtca798?t=7022)

## Tools / projects he showed

### OpenCode

Doug uses OpenCode for his setup because he likes switching between models and trying open models. *"I use open code a lot. So open code is a coding agent."* [\[01:22:52\]](https://youtube.com/live/XaYQFtca798?t=4972)

### Auto-research harness

The main project Doug shows is his auto-research harness around BM25. It can expose ranking code to an agent, let it propose patches, evaluate those patches against MS MARCO, and accept or reject changes. *"that's what I have here. So I have a whole auto research setup."* [\[01:35:58\]](https://youtube.com/live/XaYQFtca798?t=5758)

### BM25

BM25 is the retrieval baseline Doug uses as the test bed. He describes it as keyword search that scores documents by term occurrence and term importance. *"I take a query like red shoes and I need to find the item in this corpus that has the most occurrence of red, the most occurrence of shoes, weighed by what's most important"* [\[01:25:35\]](https://youtube.com/live/XaYQFtca798?t=5135)

He calls BM25 *"still a very compelling baseline"* and says it remains fast and powerful. [\[01:26:14\]](https://youtube.com/live/XaYQFtca798?t=5174)

### MS MARCO

Doug uses [MS MARCO](https://microsoft.github.io/msmarco/) as the evaluation dataset. He describes it as a question-answering dataset with questions, a large passage corpus, and identifiers for the answer passages. *"all MS MARCO is, is a set of questions in a corpus of like I think it's like 10 million passages."* [\[01:31:17\]](https://youtube.com/live/XaYQFtca798?t=5477)

### SearchArray

Doug's BM25 code uses a lexical-search pandas extension he calls SearchArray. In the snippet, it handles corpus description, stemming, and arrays used in the scoring function. *"This corpus description, snowball array, this is all part of like a lexical search pandas extension that I use called search array."* [\[01:33:27\]](https://youtube.com/live/XaYQFtca798?t=5607)

### Elasticsearch and vector databases

Doug frames search as a set of retrieval backends, not one winner. Traditional search engines such as Elasticsearch and vector databases such as Turbopuffer, Pinecone, Weaviate, and Qdrant all remain useful. *"there's a couple of families of those, and they're all none of them are obsolete, they're all really important."* [\[01:24:52\]](https://youtube.com/live/XaYQFtca798?t=5092)

### Vespa

Doug closes the auto-research section by mentioning Vespa, a search engine company that was preparing a post improving further on his BM25/MS MARCO work. *"Vespa is a well known search engine company, Vespa dot AI"* and their upcoming work improves on his result using features such as term closeness in phrases. [\[01:54:10\]](https://youtube.com/live/XaYQFtca798?t=6850)

### Building AI Agents for the Enterprise

Hugo links Doug's course, [Building AI agents for the enterprise](https://maven.com/softwaredoug/build-enterprise-agents), in Discord during the episode. The segment itself makes the course theme obvious: agents grounded in search, retrieval, evals, and enterprise knowledge bases.

## Explainers

### Retrieval systems are like databases

Doug explains retrieval backends by analogy to databases. Redis is good at key-value storage, Postgres is good at joins, and search systems have similar families. The point is to stop treating vector search as the only serious retrieval story. *"we have these these different backends, these different ways of retrieving information from potentially petabytes of information out there."* [\[01:24:41\]](https://youtube.com/live/XaYQFtca798?t=5081)

### BM25 still matters because embeddings are trained artifacts

Doug pushes back on vector-only thinking. Embedding models are trained artifacts, so you need to know their training data and task bias. BM25 is a cruder baseline, but it has fewer hidden assumptions. *"Those are always trained. You have to know what data they're trained on. You have to understand that they're optimized for a specific task. BM25, you don't have to assume that at all. It just kinda works."* [\[01:27:38\]](https://youtube.com/live/XaYQFtca798?t=5258)

### BM25 is TF-IDF plus saturation and document frequency

Doug gives a compact BM25 explanation: score matches by term frequency, weight rarer terms more heavily, and saturate the value of repeated matches. *"What BM25 basically figured out was like the the importance like more having more matches occur in a document saturates."* [\[01:29:58\]](https://youtube.com/live/XaYQFtca798?t=5398)

His example is Luke Skywalker: "Skywalker" is more specific than "Luke" because it appears in fewer documents. That inverse document frequency is what makes the term more useful for intent.

### Agents need ML-style process, not just a metric

Doug's auto-research lesson is that agent freedom only works when the process is designed. If you let an agent see evals and optimize directly, it overfits. Training, validation, holdout data, and patch gates are the boring machinery that makes the agent useful. *"all the gotchas are really about process. They're not necessarily about they're not necessarily about like some s the the idea that the agent had."* [\[01:45:38\]](https://youtube.com/live/XaYQFtca798?t=6338)

### Auto-research mostly tries known human ideas faster

Doug is not selling auto-research as magic theorem proving. In his BM25 run, the useful ideas were familiar search tactics: remove stop words and add phrase or bigram boosts. *"for 99.9999. Percent of the work that we're doing, what it's really doing is it's these are like somewhat obvious things that it that probably are in its training data."* [\[01:43:07\]](https://youtube.com/live/XaYQFtca798?t=6187)

The value is trying the existing human corpus of ideas quickly against your actual metric, not expecting the agent to invent a universal search breakthrough.

### Agentic memory is another search problem

When John asks about giving auto-research a knowledge base or lab journal, Doug says he has tried giving agents search over logs and traces from past runs, but it has not yet had dramatic impact. *"I did experiment with like giving it a search tool over the logs and traces of the past agentic runs."* [\[01:49:23\]](https://youtube.com/live/XaYQFtca798?t=6563)

His conclusion is unsentimental: *"I think this gets to why agentic memory is like why grep probably isn't great agentic memory finder. And why people are building actual agentic memory architectures."* [\[01:49:41\]](https://youtube.com/live/XaYQFtca798?t=6581)

### Agent plus grep is a real baseline

Doug does not dismiss simple tools. On relatively small datasets, an agent with grep can match or slightly beat BM25 alone in his benchmarking. *"if you have an agent and grep, it will perform at or slightly better than if you were to just use BM twenty five directly with no agent."* [\[01:58:08\]](https://youtube.com/live/XaYQFtca798?t=7088)

He puts a rough scale on that claim: *"the general threshold is a hundred thousand documents or less."* [\[01:58:27\]](https://youtube.com/live/XaYQFtca798?t=7107)

## Additional quotations

- On his search obsession: *"I'm still in that labyrinth trying to find my way out."* [\[01:19:47\]](https://youtube.com/live/XaYQFtca798?t=4787)
- On OpenCode: *"I just like being able to switch between different kinds of models and play around with some of the open models and that kind of thing."* [\[01:23:12\]](https://youtube.com/live/XaYQFtca798?t=4992)
- On BM25 speed: *"It's very fast. Like you can spin up a lexical index and get BM twenty five search working really fast."* [\[01:26:20\]](https://youtube.com/live/XaYQFtca798?t=5180)
- On search heuristics: *"there are insights like this that have come out through honestly, people dorking around with heuristics against open data sets."* [\[01:30:21\]](https://youtube.com/live/XaYQFtca798?t=5421)
- On code-editing agents: *"the coding part is actually not that hard."* [\[01:36:31\]](https://youtube.com/live/XaYQFtca798?t=5791)
- On the BM25 experiment result: *"The code is kind of a nightmare. But what it actually did that was kind of interesting"* [\[01:42:00\]](https://youtube.com/live/XaYQFtca798?t=6120)
- On auto-research as a learning environment: *"I find auto research such an amazing place to learn about this stuff."* [\[01:42:49\]](https://youtube.com/live/XaYQFtca798?t=6169)
- On memory: *"Yeah, totally. It's yet another search problem."* [\[01:50:24\]](https://youtube.com/live/XaYQFtca798?t=6624)
- On agentic search: *"just adding an agent to any search is a instant ten percent boost."* [\[01:55:59\]](https://youtube.com/live/XaYQFtca798?t=6959)
- On the meta-question: *"Will agents take take reasoning more seriously if it's like comes in the form of a user message?"* [\[01:57:13\]](https://youtube.com/live/XaYQFtca798?t=7033)

## Live reactions and follow-ups

### Discord links: blog, notebook, and course

The Discord supplied the main links for Doug's segment:

- [Autoresearching BM25 on MSMarco](https://softwaredoug.com/blog/2026/05/17/autoresearching-a-better-msmarco-bm25)
- [search-experiments notebook](https://github.com/softwaredoug/search-experiments/blob/main/notebooks/codegen/codegen_minimarco.ipynb)
- [Building AI agents for the enterprise](https://maven.com/softwaredoug/build-enterprise-agents)
- [How to Build a General-Purpose AI Agent in 131 Lines of Python](https://www.oreilly.com/radar/how-to-build-a-general-purpose-ai-agent-in-131-lines-of-python/)

### Discord reaction: Git, grep, and memory

The chat picked up the memory/search thread and pushed on simple baselines:

- *"grep+git gets relatively far for autoresearch"*
- *"would be interesting to see <@1089660766094893126> 's second brain setup  , given how Search is an important component of it"*
- Doug replied: *"I hadn't thought of git!"*
- *"git + markdown + grep as a dumb memory system for your autoresearch approacges"*
- Doug replied: *"Absolutely"*

### Hugo's follow-up: verification before scope

Hugo's question after the demo sharpens the central lesson. Auto-research gives agents more freedom, but the trust comes from verification. He asks how Doug thinks about *"building trust with the agent to then give it more and more scope and more and more time or space to do things and bring you back results."* [\[01:44:45\]](https://youtube.com/live/XaYQFtca798?t=6285)

Doug's answer is the thesis of the segment: more autonomy means better process, not fewer constraints.

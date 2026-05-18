# Eric Ma — Episode 2 proposals

Eric J. Ma leads research data science and AI at Moderna Therapeutics, where he applies Bayesian methods and AI agents to molecular biology and protein engineering. Early PyMC contributor and Bayesian practitioner since before the field gained mainstream attention. His segment focused on agentic interactive data analysis, using Marimo Pair to guide agent-assisted exploratory analysis of protein engineering datasets. Maintains active blog and LinkedIn presence on agentic data science topics; delivered SciPy talk on the same.

## Skills

### Marimo Pair skill
The centerpiece of his demo. An agent skill pairing markdown documentation with a bash script that lets coding agents directly manipulate a Python kernel, enabling reactive notebook-based interactive data analysis. Eric spent February experimenting with UV runnable scripts for plots, switched to Marimo Pair in March, then rewrote his ODSC workshop in April to teach it instead of the older script-based approach. The skill respects custom rules he sets in his agent markdown file: markdown cells interlaced between code for literate programming, unique descriptive cell names for easy reference during collaboration. Live demo ran protein engineering data analysis end-to-end, building Plotly heatmaps, scatter plots, line plots, and a 3D protein structure viewer using AnyWidget. *"This is all driven by an agent skill, and this is a, one of many skills that I've used... this one has been mind-blowing for me in most, uh, in the most recent time."* [00:37:15–00:37:35] (segment runs 00:11:57–00:39:30)

### Blog writing and editing skill
Mentioned in passing as one of several skills he maintains, used for assisting with blog post composition and revision. [00:37:27]

## Workflows

### Interactive data analysis guided by the human (not delegated to the agent)
Eric does not ask the agent to "analyze this dataset" and walk away. Instead, he stays in the loop, directing the analysis interactively one question at a time. *"I don't go into the, uh, analysis wanting with a vague question and just ask the agent to do it all for me. Like, that, I think, is irresponsible as a data scientist. Instead, what I'm doing is I'm going in and I'm taking control of the direction that I want to take the analysis in. So the human is very much in the loop."* Especially critical for exploratory data analysis (EDA). [00:23:27–00:24:19]

### Analysis by incremental visualization (one plot at a time)
*"I'm gaining my analysis one plot at a time, right? Like, that's the big one. I, I know I'm thinking about, like, what is the next most logical question that I want to answer, and I have a plot. And what is the plot that I can use to answer that question?"* Live demo: heat map of single-point mutations, then scatter plot of correlation, then line plot of positional effects, then 3D structure visualization. Each builds on the last. [00:27:45]

### Evidence-backed claims via artifacts
New data scientists often skip this. Eric emphasizes: *"you have to have artifacts that back the claims that you have... if you're gonna make a claim, you need to make a plot."* Data science cannot be just narrative. [00:28:19–00:28:35]

### Treating the coding agent as a pair programmer
*"This is, um, treating the coding agent really as a pair programmer, not as, uh, a thing that just does the whole thing for me."* He corrects the agent mid-run (e.g., when Plotly color scales were wrong, he manually adjusted the instructions for Viridis vs divergent colormaps), leaves notes for himself alongside the code, and makes editorial decisions about visualization design. [00:29:12–00:32:54]

### Model arbitrage across multiple harnesses for cost reduction
Eric runs Cursor as his primary harness, but also uses cmux with multiple open-code sessions configured for different models, plus local Qwen 3 on his MacBook. Cost frustration drives experimentation: *"I would love to see intelligence for cheap for real, and that's actually motivated a lot of experimenting with, um, alternative models to Opus and stuff... Kimi, and I have a GLM, uh, coding plan as well, so that gives me access to Opus 4.6 or 4.5 quality models at about an eighth the price."* Also tries DeepSeek V4 and OpenRouter for Kimi K2.5 access. Verifies server hosting location (non-mainland China) for personal use. [00:07:39–00:08:55]

### Voice-driven specification to Marimo Pair
*"And so just the ability to, to talk is, uh, talk with your machine is already great for, for typing."* Rather than typing long prompts or clicking UI, Eric voices natural-language specifications directly to the agent, which immediately renders them in the Marimo environment with visual feedback in seconds. [00:23:15]

### Agent-delegated Git operations
Eric delegates Git operations to agents entirely, no longer typing `git commit` at the terminal. Example given: asking the agent, *"help me resolve merge conflicts on the PR such that I can rebase to merge later,"* rather than learning rebase mechanics himself. [00:09:50–00:11:05]

## Tools / projects he showed

### Marimo
The reactive notebook system underlying the Marimo Pair skill (above). See also the stale-cell explainer below. Demo invocation: `uvx marimo edit sandbox no token`. [00:14:33–00:15:42]

### Cursor
His primary coding harness / agent IDE. Screen-shared the Cursor agent view throughout the demo. Uses alongside cmux for parallel multi-model sessions. [00:08:51, 00:11:38]

### Kimi and GLM coding plan
Alternative high-intelligence model access at roughly one-eighth Opus pricing. Eric verified non-mainland China hosting (Singapore or elsewhere outside mainland). [00:07:51]

### OpenRouter
Service for accessing alternative models like Kimi K2.5 without geographical constraints. [00:08:15]

### Qwen 3 model series
Local LLM that fits on his MacBook with sufficient RAM. Not yet tested extensively, but heard to be strong offline performance on planes (Qwen 3.6 specific). [00:09:06–00:09:34]

### DeepSeek V4
Alternative model tried; noted as pretty good. [00:08:34]

### cmux
Terminal multiplexer for running multiple open-code sessions, each configured with a different model. Allows parallel model experimentation. [00:08:53]

### Plotly
Used for interactive heatmaps, scatter plots, and line plots in the Marimo environment. Supports dropdown selectors for toggling between data (chirality vs activity, mean vs max effects). [00:22:01–00:27:30]

### 3D Mol JS
JavaScript library used (via AnyWidget) to visualize protein structures in 3D, with customizable rendering (balls-and-sticks for substrate, ribbon for protein backbone). [00:31:14]

### AnyWidget
System for wrapping arbitrary JavaScript/TypeScript code into Jupyter-compatible interactive widgets. Eric was intimidated by ESM and JavaScript but finds agents good at TypeScript, lowering the barrier. *"now with coding agents, because coding agents are better at TypeScript than I am, or ESM than I am, then I sh- uh, it makes it a lot easier for me to go and, um, try to build these custom AnyWidget viewers."* [00:32:07]

### PDB file format and protein crystallography data
Eric's demo loaded crystallized protein structures from `.pdb` files (Protein Data Bank standard). His lab co-crystallized the enzyme with its substrate. [00:30:42]

### UV and PEP 723
Before discovering Marimo Pair, Eric wrote reproducible scripts using UV with inline metadata (PEP 723 style). Called `uv run script.py` to produce plots, then wrote markdown with embedded images. This approach preceded Marimo Pair but is now superseded in his workflow. [00:12:40–00:13:13]

## Explainers

### Why reactive notebooks solve the stale-cell problem
Jupyter allows cells to be run out of order, leading to stale state and mysterious bugs when redefined variables diverge from their logical flow. Marimo's reactive model prevents this: cells automatically recompute when their dependencies change, maintaining consistency. *"Your cells can go stale in Jupyter Notebooks, but they will never go stale in Marimo Notebooks... I've been burned by stale, stale, stale cells before. Uh, and I've seen colleagues been burned by s- uh, redefined variables as well."* [00:15:27]

### Marimo Pair architecture (markdown + bash + agent interaction)
Marimo Pair is not just a notebook; it's an agent skill combining two components: a series of markdown instruction files (progressive disclosure) plus a bash script that agents invoke to directly write to the Python kernel. This bidirectional channel lets agents not just request plots but interactively modify state and see results in real time. *"The way Marimo Pair works is it's actually an agent skill that has both a series of markdown files, plus it also has a bash script that is used by the coding agent to reach directly into the, uh, Python runtime, uh, into the Python kernel directly. And so that gets really, really cool, um, that you can do really cool things by, by interactively, right? Like, it becomes more like a canvas that you actually, uh, directly manipulate."* [00:16:07]

### Two buckets of data science work (context vs optimization)
Eric splits data science into context-loading (exploring, understanding, hypothesis formation) versus optimization (running loops, hyperparameter search, automated refinement). *"Data science activities usually get split up into, uh, one of two big buckets. One is the load, load the data context into my head kind of activity, and then the other is I just got this routine optimization thing that I need a machine to automate... the latter is where you go Karpathy mode or, you know, like, uh, auto research mode, where you just go like, 'Hey, go optimize this for me, uh, in a loop and let it run for 14 hours.' But that's a mild l- that's a extremely small fraction of what, what needs to be done, right?"* EDA is overwhelmingly context-loading, so human guidance is essential. [00:24:19–00:24:54]

### Protein engineering mutation notation and data structures
Eric's dataset represents mutations using single-letter codes: `A.111.C` means "at position 111, the wild-type was A (alanine), now it's C (cysteine)." Single mutations are single codes; combatorial mutants have multiple (e.g., four positions mutated in quadruple mutants). His experiments measured both enzyme activity (percentage substrate conversion, 0-1 scale) and stereoselectivity/chirality (R vs L enantiomer excess, -1 to +1 scale). *"Some of them are single point mu-mutants in, in which case like we-- this protein only has one mutation at position five, but some are double, some are quadruple. Like these have four p- four positions that are mutated, and that's kind of the notation that protein engineers and bioinformaticians use to denote, uh, denote protein, uh, activity."* [00:17:39–00:18:35]

### Why different color maps fit different data ranges
When visualizing activity (0-1) and chirality (-1 to +1) on the same heatmap, sequential colormaps (e.g., Viridis) work for one-sided scales but divergent colormaps (e.g., spectral) better represent data centered around zero. Eric caught the agent's error mid-viz and instructed: *"activity goes on a zero to one scale, but chira- and c- c- but chirality, it does make sense. Like, chirality is okay to have a divergent scale because the values go from negative one to plus one... I really think the heat maps need to have a different color so that it's much easier to interpret."* [00:25:12]

### AnyWidget: turning custom JavaScript into interactive Jupyter tools
Most data scientists avoid writing JavaScript. AnyWidget is a bridge: it lets you wrap arbitrary JS/TS code into a Python-facing widget. Eric was initially overwhelmed by ESM and TypeScript syntax but now confidently uses agents to handle that layer, freeing him to focus on the data interaction pattern. *"When I saw, first saw AnyWidget about two years ago or a year ago, I can't remember now, um, I was blown away by, like, the potential, but it's also involves the [00:31:58] use of JavaScript and ESM, which isn't the easiest. So it took a little bit of time for me to learn how to, how to wrangle it, but now with coding agents, because coding agents are better at TypeScript than I am, or ESM than I am, then I sh- uh, it makes it a lot easier for me to go and, um, try to build these custom AnyWidget viewers."* [00:31:49]

### 3D protein structure interpretation: distinguishing substrate binding sites from allosteric mutation hotspots
A key scientific insight emerged from the visualization. Eric's hypothesis (driving since undergrad) was whether mutational effects are additive or context-dependent. The 3D coloring revealed that the best-performing mutations cluster outside the active site, far from where substrate binds. This is surprising and informative for protein engineering: *"are the best performing mutations happening near where the substrates are, or are they happening outside? That's an important en- protein engineering decision that we, we might want to be able to make... the best performing mutation, this guy, these two, these are outside of, uh, [00:36:59] the-- They're very far away from where the substrate goes into the protein, which is like... I don't know, I don't know how else to convey this, but I am a, a bio nerd, and this is so cool for me. This is like, 'Oh, yes! Okay, we know what to do now with this molecule,' right?"* Discovery emerged from step-by-step visual analysis, not from asking the agent "find the interesting patterns." [00:35:18–00:37:18]


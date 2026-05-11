# Randy Olson — Episode 1 proposals

Randy is co-founder/CTO of Good Eye Labs, a longtime AI/ML researcher (early work on TPOT/AutoML) and a data-viz veteran who has moderated r/dataisbeautiful for years. His segment screen-shared one big skill in action (data-viz generation + Tuftean verifier loop) and laid out a lot of generalisable skill-design advice. He posts daily AI-generated data-viz stories from this same skill.

## Skills

### Data-visualization skill (Tufte-style + verifier loop)
The headline artifact. A long, phase-structured skill that takes a one-line idea and produces a publishable chart. Phases observed on screen: environment setup → dataset discovery (biased toward CDC / government / educational sources) → multi-variant prototyping (line, small multiples, area) → an LLM-as-judge "Tufty test" verifier loop that scores the image against Tuftean principles (no chart junk, clear annotations, labeled axes, clear story) and feeds failures back as fix-it instructions → final chart. He demoed a live run on US marriage/divorce data; Hugo separately re-ran it on Secretariat's Kentucky Derby record. Randy: *"I run this skill every single morning, and that's how I make that post series."* [01:33:00] Demoed across [01:13:00–01:32:00]; said it can be made available after the episode [01:13:00]. Blog with daily outputs referenced [01:34:00].

### "Be concise and unambiguous" skill (aspirational)
Randy on his most-typed prompt: *"One of my most typed phrases is probably, like, 'Be concise, unam- and unambiguous.' I should just turn that into a skill."* [01:11:00] He hasn't shipped it, but it's a clean micro-skill candidate in the Jeremiah `ship-it` mould.

## Workflows

### Digital-twin / memory-base setup
Randy maintains *"a growing memory base where I throw in ideas and track everything"* and loads agents with *"what I call a digital twin"* so they push back instead of being sycophantic. *"You can induce that... by prompting LLMs."* [01:07:00–01:08:00] Described, not shown — a practice he layers on top of every agent he works with.

### Generate-and-verify built into the skill itself
Concrete instance, not the concept: Randy's data-viz skill pairs a deterministic check (e.g. DPI on the rendered image) with an LLM-as-judge "Tufty test" that scores the chart and feeds failures back as fix-it instructions. *"You don't wanna just tell it what to do, you also wanna tell it how to check it."* [01:29:00] Hugo flagged this as one of the five workflows in Anthropic's *Building Effective AI Agents* post [01:35:00–01:36:00].

### Daily cron-driven AI work
*"I have a ton of cron jobs that do things like that, that automatically send off reports to colleagues."* [01:14:00–01:15:00] The data-viz skill itself runs daily on a cron and feeds his blog post series [01:33:00].

### Human-in-the-loop on the last 5%
He runs the skill, then his actual job is to glance at outputs: *"Most of what I do is like, 'Oh no, I like that post,' or, 'I like that image more. Oh, hey, an annotation's overlapping. Otherwise, looks good. Post it.'"* [01:33:00] Honest framing of where judgment still lives in an otherwise automated loop.

## Tools / projects he showed

### Workflow-pull tool (not named)
Briefly pointed at: *"This is a tool that I use to pull it [the workflow/template], and I can... if we have time, I can talk about that."* [01:26:00] Never got back to it on stream. Worth chasing offline before proposing as a repo artifact — name unknown.

## Explainers

Passages where Randy was teaching the audience, not opining.

### How to design a good skill (best-practices walkthrough)
Sustained ~5-minute exposition before the demo, covering: connect every data source you can (MCPs, CLIs) so the agent has surface area; put an environment-setup phase at the start so it doesn't crash trying; design the skill as a *thin driver* with phases factored into reference files (progressive disclosure — *"if I just wanna jump straight to phase four, it can just load the phase four thing"*); make it unambiguous with exact commands and code snippets — *"a skill plus an LLM is kind of a program"*; mix deterministic scripts with LLM steps for *"degrees of agency"*; close every skill with a reflect-and-improve phase so *"every single run, you're learning something new and putting it into the skill... it's compounding."* [01:13:00–01:19:00] Dense enough to seed a standalone "how to write a skill" post.

### Encoding judgment as an eval / verifier (data-scientist framing)
The teaching beat behind the verifier loop. *"I really approach it like a data scientist... let's just try it first... I build a full set of data visualizations, one that I know are good, ones that I know are bad, and I just keep tweaking it... treating the eval itself as sort of like a living document."* Plus the realism: an eval that's wrong 20% of the time is still directionally valuable and *"catches the obvious stuff — that's one less time I have to spend my thought tokens."* [01:36:00–01:42:00]

### Skills vs harness vs model (what's fixed, what's yours to shape)
Randy's clean three-layer answer to Hugo's harness question: the model is fixed unless you're running local; the harness is largely fixed unless you build your own; *"the skills are really the thing that... can evolve with you and they can kind of guide the harness plus the model... towards what you actually want it to do."* [01:20:00–01:21:00]

# wikipedia-discovery

A page-local Wikipedia skill that lets an agent open a requested article, find a specific passage, and surface it in the current browser context.

## who showed it

John Berryman, AI product and engineering consultant and founder of Arcturus Labs.

## what it does

`wikipedia-discovery` is the web-page example inside John's Rook demo. Rook follows him out of Obsidian and into Wikipedia, where the current page can expose an affordance to the agent.

> *"it like it can follow me into a lot more places."* [\[00:23:47\]](https://youtube.com/live/6zju7hyCFl0?t=1427)

John invokes the skill from a Wikipedia environment and asks it to open the BERT article:

> *"using the Wikipedia skill can you open up the page on B E R T"* [\[00:24:13\]](https://youtube.com/live/6zju7hyCFl0?t=1453)

Once the page is open, the task becomes page-local discovery: find a passage on the page and make it visible to the user.

> *"can you find where it's talking about the original size of the BERT model and highlight that for me."* [\[00:24:58\]](https://youtube.com/live/6zju7hyCFl0?t=1498)

## why it's notable

This is a small skill, but it shows the larger pattern clearly. The web page is not just text for a model to scrape. It becomes an environment that can send state to the user's agent, receive requests back, and let the user change what is visible on the page.

John immediately points out that the protocol name in the demo is speculative, not a real standard:

> *"I was actually lying about the open agent protocol. It's just a thing that absolutely should exist."* [\[00:25:36\]](https://youtube.com/live/6zju7hyCFl0?t=1536)

That honesty is part of why the skill earns a folder. `wikipedia-discovery` is not notable because Wikipedia lookup is hard. It is notable because it demonstrates a page-specific agent affordance: the agent knows where it is, takes an action inside that environment, and returns the user's attention to the relevant evidence.

## watch it

- [**00:23:47**](https://youtube.com/live/6zju7hyCFl0?t=1427): John moves from Obsidian to the broader web pattern.
- [**00:24:13**](https://youtube.com/live/6zju7hyCFl0?t=1453): John invokes the Wikipedia skill and asks for the BERT page.
- [**00:24:58**](https://youtube.com/live/6zju7hyCFl0?t=1498): John asks the skill to find and highlight the original BERT model-size passage.
- [**00:25:36**](https://youtube.com/live/6zju7hyCFl0?t=1536): John clarifies that the named protocol is speculative.

## status

The `SKILL.md` here was reconstructed from the live recording, not ported from John's own repo. The original skill file was not shown on camera, so this folder captures the demonstrated behavior and the constraints visible in the episode. If John publishes an authoritative version, it will replace this file.

<a href="https://youtube.com/live/6zju7hyCFl0?t=1498"><img src="images/hero.png" alt="John Berryman demoing the wikipedia-discovery skill on Episode 5 of Show Us Your Agent Skills" /></a>
<sub>John Berryman demos `wikipedia-discovery` on Episode 5 of <em>Show Us Your Agent Skills</em>. <a href="https://youtube.com/live/6zju7hyCFl0?t=1498">[00:24:58]</a></sub>

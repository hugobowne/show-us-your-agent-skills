# explain

A short natural-language skill that makes the agent narrate what it just
did in the voice of a colleague who knows your project, so you can keep
up with many agents running in parallel.

## who showed it

Jeremiah Lowin, founder/CEO of Prefect and core maintainer of FastMCP.

## what it does

~80 lines of markdown.

After a task completes, the agent explains the change itself, not the
code in the abstract, not the line-level diff, in the register of a
teammate giving you a verbal handoff.

The one sentence Jeremiah says actually matters, and has been in every
version of the skill:

> *"Talk to me like you're explaining this to your colleague who knows about your project but wants to understand what you just did."* [\[00:46:43\]](https://youtube.com/live/Pq3xuChdwxQ?t=2803)

Without that framing, Jeremiah finds the answers degenerate in two
directions:

> *"If I just ask, like, 'What are we doing here?' it'll be like, 'Oh, well, we renamed this variable on this line to do this.' And that's no good. And if I step back and I'm like, 'Well, what does this code do?' I'll get an explanation of the code, but not the change we're making."* [\[00:47:04\]](https://youtube.com/live/Pq3xuChdwxQ?t=2824)

## why it's notable

It's Jeremiah's workhorse skill and the one he says he couldn't do
without. Most of his other skills reference it:

> *"It is referenced in every other skill I have. It's like, use your explain skill to do this. Use your explain skill to post a reply."* [\[00:48:01–00:48:14\]](https://youtube.com/live/Pq3xuChdwxQ?t=2881)

The reason it earns that status is concrete.

Jeremiah runs ~10 agents on ~10 things over ~10 timeframes, and `explain`
is how he triages them:

> *"I'm cracking open my laptop with a coffee and I'm like, 'What's this one?'"* [\[00:47:00\]](https://youtube.com/live/Pq3xuChdwxQ?t=2820)

The skill is the cheapest possible fix for that. No tooling, no infra,
one sentence of framing.

It's also project-agnostic. He offered to release it publicly *"under the banner of this, of this podcast"* [\[00:46:20\]](https://youtube.com/live/Pq3xuChdwxQ?t=2780), meaning the same skill travels across all his projects.

## watch it

- [**00:46:43**](https://youtube.com/live/Pq3xuChdwxQ?t=2803): The one sentence that matters.
- [**00:48:01**](https://youtube.com/live/Pq3xuChdwxQ?t=2881): "My workhorse," referenced in every other skill.

## status

Stub. Not yet ported from Jeremiah's own repo. He offered on stream to
make it public under this podcast.

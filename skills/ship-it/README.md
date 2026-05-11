# ship-it

A one-instruction skill that re-trains the agent's interpretation of
"ship it" so the right thing happens: open a PR, do not merge.

## who showed it

Jeremiah Lowin, founder/CEO of Prefect and core maintainer of FastMCP.

## what it does

Disambiguates a single phrase.

When Jeremiah types "ship it", he wants the agent to open a pull request,
not to merge code. Out of the box, most LLMs read "ship it" as merge,
which is the wrong default for how he works.

> *"It means open a PR. It does not mean merge the code. That's bitten me a lot. Most LLMs think ship it means merge it. That's not how I use it."* [\[00:55:01\]](https://youtube.com/live/Pq3xuChdwxQ?t=3301)

The skill exists purely so the phrase produces the right outcome:

> *"Why does this skill exist? It's not a useful skill… But the reason it exists is because I wanna write the words ship it and have the right outcome happen, and this skill is my bridge to ensuring that."* [\[00:55:20\]](https://youtube.com/live/Pq3xuChdwxQ?t=3320)

## why it's notable

This is the **first skill Jeremiah ever wrote** [\[00:54:49\]](https://youtube.com/live/Pq3xuChdwxQ?t=3289).

It's also a clean micro-pattern: a single instruction whose entire job
is to override the agent's default reading of a common phrase.

A useful precedent for anyone writing skills now. Skills don't have to
be elaborate workflows; sometimes they're a personal-vocabulary bridge
to deterministic behavior.

## watch it

- [**00:55:01**](https://youtube.com/live/Pq3xuChdwxQ?t=3301): "Ship it means open a PR, not merge."

## status

Stub. Not yet ported from Jeremiah's own repo.

# data-viz

A phase-structured skill that takes a one-line idea and produces a
publishable, Tufte-style chart, with an LLM-as-judge verifier loop baked in.

## who showed it

Randy Olson, co-founder/CTO of Good Eye Labs, longtime moderator of
r/dataisbeautiful, and one of the early AutoML researchers (TPOT).

He's been shipping data visualisations on the internet for years. This is
the skill he now uses to do it daily.

## what it does

A long skill with explicit phases. Observed on stream:

1. **Environment setup.** Installs and checks what it needs so the run
   doesn't crash mid-flight.

2. **Dataset discovery.** Biased toward CDC, government, and educational
   sources so the underlying numbers are trustworthy.

3. **Multi-variant prototyping.** Line, small multiples, area, etc.,
   rather than committing to one chart type up front.

4. **Tufty-test verifier loop.** An LLM-as-judge scores the rendered image
   against Tuftean principles (no chart junk, clear annotations, labeled
   axes, a clear story) and feeds failures back as fix-it instructions.
   Paired with a deterministic check on the rendered image (e.g. DPI).

5. **Final chart.**

The skill itself is designed as a thin driver, with each phase factored
into reference files the agent loads progressively:

> *"if I just wanna jump straight to phase four, it can just load the phase four thing"* [\[01:16:39–01:18:56\]](https://youtube.com/live/Pq3xuChdwxQ?t=4599)

## why it's notable

The Tufty-test loop is the headline. It's a concrete instance of
generate-and-verify built into the skill:

> *"You don't wanna just tell it what to do, you also wanna tell it how to check it."* [\[01:29:32\]](https://youtube.com/live/Pq3xuChdwxQ?t=5372)

Randy frames the verifier itself like a data scientist would frame an
eval: keep a known-good and known-bad set, tweak the judge against it,
treat the eval as a living document.

Even a judge that's wrong 20% of the time still *"catches especially a lot of the obvious stuff... that's one less time that I have to spend my thought tokens."* [\[01:41:52\]](https://youtube.com/live/Pq3xuChdwxQ?t=6112)

## in production

The skill runs on a cron every morning and powers Randy's daily
AI-generated data-viz blog post series:

> *"I run this skill every single morning, and that's how I make that post series."* [\[01:33:24\]](https://youtube.com/live/Pq3xuChdwxQ?t=5604)

His own role on each run is the last 5%:

> *"Most of what I do is like, 'Oh no, I like that post,' or, 'I like that image more. Oh, hey, an annotation's overlapping. Otherwise, looks good. Post it.'"* [\[01:33:29\]](https://youtube.com/live/Pq3xuChdwxQ?t=5609)

## demoed on stream

Randy ran it live on US marriage and divorce rates over time.

Hugo then re-ran the same skill on a different one-liner, Secretariat's
Kentucky Derby record, to see how it generalised.

## watch it

- [**01:16:39**](https://youtube.com/live/Pq3xuChdwxQ?t=4599): Skill design walkthrough covering phases, progressive disclosure, and reflect-and-improve.
- [**01:29:32**](https://youtube.com/live/Pq3xuChdwxQ?t=5372): The Tufty test, "tell it how to check it."
- [**01:33:24**](https://youtube.com/live/Pq3xuChdwxQ?t=5604): Daily cron with human-in-the-loop on the last 5%.
- [**01:38:05**](https://youtube.com/live/Pq3xuChdwxQ?t=5885): Eval as a living document.

## status

Stub. Randy said on stream that the skill could be made available after
the episode; not yet ported into this repo.

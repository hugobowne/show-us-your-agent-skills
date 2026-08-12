# Prose audit — do this before rendering

The whole point of this skill is explainers that read like a sharp human wrote them for a
specific kid, not like generic AI filler. Audit every draft against two sources, then revise.

## The two sources

1. **`~/.claude/PROSE.md`** — Tim's house style (Strunk & White vigor, Nielsen, skimmability,
   anti-AI heuristics). Read the file each run; it may have changed. The rules that matter
   most for these explainers:
   - Omit needless words; active voice; positive form (be definite, not hedged).
   - Front-load keywords in headers and the first two words of each paragraph (F-pattern).
   - 2–4 line paragraphs. Bold/italics sparingly — one standout per section.
   - Ban puffery ("pivotal," "testament," "rich tapestry," "groundbreaking"). Show, don't announce.
   - Kill "not only… but also," "in conclusion," "overall," "in summary."
   - Verb-led headers ("Beating the Grass") over noun phrases ("Grass Performance").
   - Start at the mystery, not "In the modern era…".

2. **The `stop-slop` skill** — invoke it on the draft (`Skill: stop-slop`, or read
   `~/.claude/skills/stop-slop/SKILL.md` + its `references/`). It catches AI tells PROSE.md
   doesn't enumerate: repetitive sentence rhythm, monotonous paragraph endings, over-explained
   metaphors, em-dash overuse, pull-quote phrasing, formulaic binary contrasts.

## Reconcile with the kid voice

PROSE.md is tuned for technical docs. For a kids' explainer, keep its rigor but not its
register. So:
- **Keep** warmth, direct address ("you"), concrete images, and a sense of fun. A vivid
  analogy a kid can picture ("grass is a green carpet of friction") is good writing, not slop —
  the stop-slop rule is about *over-explaining* metaphors, not banning them. One clean image,
  then move on.
- **Drop** the technical-only rules that don't apply (e.g. ~70-char line width for code docs).
- **Match the kid's age.** Younger → shorter sentences, simpler words, more pictures. Smart/older
  → respect their intelligence, introduce real terms and define them once (the way the RC guide
  taught "brushless" and "ground clearance"). Never write down to them.

## Quick pass

Run stop-slop's 1–10 scale on Directness, Rhythm, Trust, Authenticity, Density. Below 35/50,
revise before rendering. Then sanity-check against PROSE.md's anti-AI list. Fix the prose in
the draft, not after it's in the PDF.

## Smell test

Read one section aloud. If it sounds like a real person explaining something they love to a kid
they like — keep it. If it sounds like a brochure or a Wikipedia intro, rewrite it.

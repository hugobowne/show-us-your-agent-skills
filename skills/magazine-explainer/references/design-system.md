# Design system — component catalog

The CSS lives in `assets/template.html`. Copy that file, then assemble the body from
the snippets below. Every component is already styled; you only supply content.

## Contents
- Theming (re-color per subject)
- Cover
- Section header
- Cards (text) & photo cards
- Callouts
- Comparison table
- "How it works" spec boxes
- Checklist
- Numbered Q&A / steps
- Closing panel
- Layout rules that keep it looking professional

---

## Theming

Edit the `:root` block at the top of the CSS. Swap `--orange` / `--orange-deep` / `--amber`
to fit the subject; leave `--steel` dark and `--cream`/`--paper` light. Suggested palettes:

| Subject | --orange | --amber |
|---|---|---|
| Racing / vehicles | `#ff5a1f` | `#ffb020` |
| Space / astronomy | `#6d5efc` | `#22d3ee` |
| Dinosaurs / nature | `#2f9e44` | `#e8a33d` |
| Ocean / weather | `#0ea5e9` | `#34d399` |
| Volcanoes / energy | `#e0382b` | `#f59e0b` |

Also update the cover's `radial-gradient(... rgba(255,90,31,.35) ...)` to match `--orange`.

---

## Cover
Already in the template. Keys: `.sub` is capped at 50% width and `.cover-hero` is pinned
bottom-right so text and photo never collide. If the hero photo is a different shape than
the default, tune `.cover-hero` width/right/bottom and re-render. `<span class="o">` colors
one title word in the accent.

## Section header
```html
<div class="section">
  <div class="sec-head"><span class="sec-num">02</span><h2>Verb-Led Title</h2></div>
  <div class="sec-rule"></div>
  <p>One short intro sentence.</p>
</div>
```

## Cards (text)
Cards **stack one per row by default** — the digest page is only 5.5in wide, so full-width cards
read better. For a short, genuinely side-by-side pair (a tight "A vs B"), add `.duo`:
`<div class="cards duo">`. Tag colors: default (steel), `.budget` (green), `.value` (orange),
`.dream` (blue).
```html
<div class="cards">
  <div class="card"><span class="tag value">Label</span><h4>Card Title</h4><p>Body.</p></div>
  <div class="card"><span class="tag budget">Label</span><h4>Card Title</h4>
    <ul><li>Point one.</li><li>Point two.</li></ul></div>
</div>
```
Use `.duo` sparingly — on a narrow page two columns get cramped fast. Photo cards and spec boxes
also stack; let them, and the photos come out bigger.

## Photos vs. diagrams — use both
A photo and a diagram do different jobs, so mix them:
- **Real photo** — shows what something *looks like*: the subject's face. A volcano erupting, a
  great white, a Saturn V on the pad. Download these (`fetch_image.sh`) into `img/`.
- **Custom diagram** — shows what a photo can't: how something *works*, its *parts*, its *scale*,
  or a *sequence*. A labeled volcano cutaway, a to-scale "megalodon vs. great white vs. kid," a
  rocket's stages, an Earth cross-section. Build these as inline SVG (see below).

A good issue alternates them: lead a section with a photo for impact, then teach the mechanism with
a diagram. Don't force one or the other — pick whatever actually makes the idea click for the kid.

## Diagrams (custom inline SVG)
Hand-author SVG inside a `figure.diagram` so it gets a frame + caption and matches the theme. Use
the theme CSS vars for fills/strokes so the diagram recolors with the issue. Keep labels in a
readable sans size (~11–13px). `figure.diagram.dark` gives a dark panel for space/night subjects.
```html
<figure class="diagram">
  <svg viewBox="0 0 600 260" role="img" aria-label="Labeled cross-section">
    <!-- shapes use theme colors: fill="var(--orange)" stroke="var(--steel)" etc. -->
    <rect x="0" y="0" width="600" height="260" fill="var(--cream)"/>
    <!-- ...layers, arrows, labels... -->
    <text x="20" y="30" font-family="Inter, sans-serif" font-size="13" fill="var(--ink)">Label</text>
  </svg>
  <figcaption>What this diagram shows, in one line.</figcaption>
</figure>
```
Diagram ideas that teach well: labeled cross-section / cutaway (inside a volcano, the layers of
Earth), to-scale size comparison (line up subjects against a familiar object), a numbered process
flow, a cycle, or a simple map. The mono `.spec` boxes are good for stylized "how it works" flows;
reach for a real SVG diagram when you need actual shapes, proportions, or spatial layout.

## Photo cards
A photo on top of the card. Image must be a local file under `img/`.
```html
<div class="cards">
  <div class="card pcard">
    <img class="shot" src="img/thing-a.jpg" alt="Thing A">
    <span class="tag value">Label</span><h4>Thing A</h4>
    <span class="price">optional small mono line</span>
    <ul><li>Fact.</li><li>Fact.</li></ul>
  </div>
  <div class="card pcard">
    <img class="shot" src="img/thing-b.jpg" alt="Thing B">
    <span class="tag budget">Label</span><h4>Thing B</h4>
    <ul><li>Fact.</li></ul>
  </div>
</div>
```

## Callouts
Use at most one per section — the standout fact. Variants: default (orange), `.tip` (green), `.warn` (amber).
```html
<div class="callout tip"><div class="ct">Try This</div><p>The one thing worth remembering.</p></div>
```

## Comparison table
```html
<table>
  <thead><tr><th>Feature</th><th>Option A</th><th>Option B</th></tr></thead>
  <tbody>
    <tr><td>Speed</td><td>Slower, steady.</td><td>Faster, trickier.</td></tr>
    <tr><td>Cost</td><td>Cheaper.</td><td>Pricier.</td></tr>
  </tbody>
</table>
```
First column auto-bolds. Great for "A vs B" decisions a kid can reason about.

## "How it works" spec boxes
Two dark monospace panels for side-by-side mechanisms or before/after flows. `.bl` is a
slightly different dark for the second box. `.hot-red` / `.hot` color the payoff line.
```html
<div class="spec">
  <div class="box"><h4>Way One</h4>
    <div class="flow"><b>START</b><br>&nbsp;&nbsp;↓<br>middle step<br>&nbsp;&nbsp;↓<br><span class="hot-red">result</span></div>
    <p style="color:#9fb2c9;margin:7px 0 0">Plain-language explanation.</p>
  </div>
  <div class="box bl"><h4>Way Two</h4>
    <div class="flow"><b>START</b><br>&nbsp;&nbsp;↓<br>middle step<br>&nbsp;&nbsp;↓<br><span class="hot">result</span></div>
    <p style="color:#9fb2c9;margin:7px 0 0">Plain-language explanation.</p>
  </div>
</div>
```
The `↓` arrow comes from a normal text font and is fine. **Avoid color-emoji glyphs** (⚙ ⚡ 🔥 🌋 🦈 🚀 etc.) in headings or anywhere in the HTML: Chrome embeds them as bitmap/SVG OpenType glyphs that hang some printer RIPs. Use a CSS shape, an accent-colored word, or a tag chip instead. The print build flattens to bitmaps and would survive them anyway, but keeping them out keeps the on-screen PDF printable too.

## Checklist
```html
<ul class="check">
  <li><b>Step name.</b> What to do and what to watch for.</li>
  <li><b>Step name.</b> Next thing.</li>
</ul>
```

## Numbered Q&A / steps
Auto-numbers as Q1, Q2… (the `Q` prefix is in the CSS `content`). For plain steps,
edit that `content` to `counter(q)` if you don't want the Q.
```html
<ol class="qlist">
  <li><span class="q">"The question in the kid's voice?"</span>Why it matters.</li>
</ol>
```

## Closing panel
Dark box. `strong` is forced white here, so bold shows up. End on a question or a next step.
```html
<div class="closer">
  <h2>Your Mission</h2>
  <p>Brief setup that respects what they just learned.</p>
  <p class="q2">A real question that invites them to choose or go do something.</p>
</div>
<p class="footnote">Built for {{name}} · {{series}} · short honest disclaimer if prices/facts may drift.</p>
```

---

## Layout rules (what keeps it from looking generic)

- **Let pages fill.** Wrap sections in `<div class="page">` blocks and let them flow. Don't
  force a page break before every section — that leaves half-empty pages. The CSS already
  keeps cards, tables, callouts, and headings from splitting awkwardly.
- **Verify visually.** After rendering, Read the PDF pages as images. Check: nothing
  overlaps, no orphaned heading at a page bottom, dark panels show their text (white-on-dark),
  photos are the right subject and not stretched.
- **Photos must be local files** under `img/` next to the HTML, referenced as `img/name.jpg`.
  Remote URLs sometimes don't finish loading before the PDF snapshot.
- **One accent fact per section.** Bolding or a callout only works if it's rare (isolation effect).
- **Aspect ratios.** `.pcard .shot` uses `object-fit:contain`, so odd-shaped photos won't
  stretch — they letterbox on white. Clean white-background product/specimen shots look best.

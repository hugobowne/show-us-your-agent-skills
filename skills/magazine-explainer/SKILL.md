---
name: magazine-explainer
description: >-
  Research a topic and build a beautiful, magazine-style PDF explainer written for a specific
  kid — designed cover, sections, cards, comparison tables, callouts, real photos, and a closing
  prompt. Use this whenever Tim wants to make a guide, explainer, handbook, or "writeup" for one
  of his kids (e.g. "make James a guide to volcanoes", "build a magazine explainer about how
  rockets work for my daughter", "turn this chat into a nice PDF for my son", "research X and make
  it into something my kid can read"). Triggers on "explainer", "magazine-style", "field guide for
  my kid", "make a PDF for [child]", or any kid-facing illustrated explainer — even if Tim doesn't
  say "magazine". Produces a print-ready PDF via headless Chrome and always audits the prose against
  PROSE.md and the stop-slop skill before finalizing.
---

# Magazine-style explainer builder

Turn a topic (or an existing chat / article) into a print-ready PDF explainer that looks like a
real kids' magazine feature and reads like a sharp human wrote it for one specific kid. The visual
system is proven and bundled; your job is good research, a strong narrative, real photos, and clean
prose.

## What makes these good
- **One kid, one obsession.** Written for a named child at their level, around a single subject.
  Voice is warm and direct, never dumbed-down.
- **Magazine layout, not a worksheet.** A dramatic cover, numbered sections with verb-led titles,
  cards, comparison tables, "how it works" diagrams, real photographs.
- **Teaches real ideas.** Introduce true terminology and define it once (the way a good guide
  teaches "brushless motor" instead of hiding it). Kids rise to it.
- **Audited prose.** No AI slop. Every draft passes the PROSE.md + stop-slop check before render.

## Workflow

### 1. Scope it (ask only what you can't infer)
Settle: the **subject**, the **kid's name and age** (drives reading level), the **angle** (what
about the subject — "how X works", "how to get into X", "the wildest X"), and the **accent color
theme**. If a source already exists in the conversation (a chat, an article, notes), build from it.
Pick sensible defaults and state them rather than stalling — Tim prefers action over questions.

### 2. Research
Gather real, correct material — don't wing facts for a kid.
- Use WebSearch / WebFetch for facts, and the browser (Chrome MCP) when a page is JS-gated.
- Find **real photos**: image-search for clean, white-background subject shots, then download
  them with `scripts/fetch_image.sh <url> img/<name>.jpg`. **Read each downloaded image** to
  confirm it's the right subject and not a logo, 404, or watermark. Save 2–4 good ones into an
  `img/` folder next to where the HTML will live.
- Plan a **mix of photos and diagrams**. Photos show what things look like; a custom diagram shows
  what a photo can't — a labeled cutaway, a to-scale comparison, a process or anatomy. The best
  issues alternate them. Note which sections want a photo and which want a hand-built SVG diagram
  (see `references/design-system.md` → "Photos vs. diagrams" and "Diagrams").
- Note source quality; flag anything you're unsure of so it can be checked, and keep a light
  honest disclaimer in the footnote if facts/prices may drift.

### 3. Draft the narrative (text first, layout second)
Write the sections as plain prose before touching HTML. Structure: a hook lead-in → 4–8 numbered
sections → a closing panel that ends on a question or a next step. Map each section to a component
(cards, table, spec boxes, checklist, Q&A) and to a visual — a real photo or a custom diagram,
whichever teaches that section better. See `references/design-system.md`.

If the subject involves **choosing between options** — brands, models, two ways of doing something
— give an explicit head-to-head comparison (a table), then a clear "which one and why" recommendation.
That head-to-head is usually the single thing the reader most wants, and it's easy to leave out by
describing each option in isolation. (E.g. a truck guide needs "Brand A vs Brand B," not just two
separate brand blurbs.)

### 4. Audit the prose — REQUIRED, before rendering
Read `references/prose-audit.md` and follow it: read `~/.claude/PROSE.md`, invoke the `stop-slop`
skill on the draft, reconcile both with the kid's reading level, and **revise the text**. Fix slop
in the draft, not after it's in the PDF. This step is the reason the skill exists — don't skip it.

### 5. Assemble the HTML
Copy `assets/template.html` into the working folder (alongside `img/`). The page is **digest size
(5.5×8.5in)** — a real pocket-magazine page, not a full sheet — so keep lines short, let cards and
spec boxes stack (they default to one column; add `class="cards duo"` only for a short side-by-side
pair), and expect a topic to run more pages than it would on Letter. Set the theme colors in
`:root`, fill the cover, and build the body from `references/design-system.md` snippets. Let
sections flow inside `<div class="page">` wrappers — don't force a page break before each one, or
pages end up half-empty.

### 6. Render and verify
Run `scripts/render.sh <guide.html> <Name-Subject-Guide.pdf>` — it finds Chrome, waits for fonts
and images, and reports page count + size. Then **Read the PDF pages as images** and check:
nothing overlaps, no heading orphaned at a page bottom, dark panels show their (white) text,
photos are correct and not stretched, no big empty gaps. Fix the HTML and re-render until it's
clean. The **single most common defect is the cover hero photo colliding with the subtitle or
byline** — always check the cover first, and if the photo overlaps text, shrink its width or move
it (a smaller rounded inset in clear bottom-right space reads well) until title, subtitle, byline,
and tagline are all clear.

### 7. Make the booklet
A folded, stapled booklet is what makes it feel like a real magazine instead of a stack of
loose pages — so always produce one. Run `scripts/booklet.sh <Name-Subject-Guide.pdf>
<Name-Subject-Guide-booklet.pdf>`. It imposes the pages 2-up on landscape Letter sheets in
saddle-stitch fold order and pads to a multiple of 4. Because the pages are already digest size,
two fit a Letter sheet **at 1:1 with no shrinking** — so the printed text stays full size and
readable (this is the whole reason we design at digest, not Letter). Tim prints it double-sided,
folds the stack in half, and staples the spine to get a pocket magazine that reads 1, 2, 3…

Keep both files: the plain PDF reads fine on screen; the `-booklet.pdf` is for printing. Tell Tim
the duplex setting matters — if the page pairs come out misaligned, flip the "print on both sides"
binding-edge option (short-edge vs long-edge) and reprint. Open the reading PDF with `open` when done.

A booklet needs a multiple of 4 pages, so 4/8/12 reading pages fold with no blanks. Nice if the
content lands there naturally, but don't pad or trim good material just to hit it — content quality
wins, and the script pads any leftover safely. (The blank leaves end up at the back, which is fine.)

**Print-safe flatten — do this for the booklet.** Chrome embeds fonts that some printer RIPs choke
on (color/bitmap emoji like ⚙ ⚡ 🔥, and subsetted symbol fonts), which hangs the print job; a vector
re-distill keeps the bad glyphs and hangs the same way. So also run
`scripts/printable.sh <Name-Subject-Guide-booklet.pdf> <Name-Subject-Guide-booklet-print.pdf>`. It
rasterizes every page to a 200-DPI bitmap (no fonts, nothing to choke on) at the same page size, and
the file is usually smaller. The `-booklet-print.pdf` is the file Tim actually sends to the printer;
keep the vector booklet for screen/reference. (Best to avoid color-emoji glyphs in the first place —
see the design-system note — but always ship the flattened print file regardless.)

### 8. Hand off
Tell Tim the paths (reading PDF + booklet + print-safe booklet), page count, and what's in it.
If he wants it printed, run `scripts/print_booklet.sh <Name-booklet-print.pdf>` — it sends the
flattened booklet to his default duplex printer (the HP Color LaserJet Pro M252dw) with the right
two-sided settings, then he folds and staples. Offer obvious follow-ups: send to Kindle, adjust the
theme, swap a photo, change reading level, or spin up a companion explainer.

## Files
- `assets/template.html` — the full design system (CSS) + a body skeleton. Start here.
- `references/design-system.md` — component catalog (cards, tables, spec boxes, etc.) + theming + layout rules.
- `references/prose-audit.md` — how to run the PROSE.md + stop-slop audit for a kid's reading level.
- `scripts/render.sh` — HTML → PDF via headless Chrome, reports page count.
- `scripts/fetch_image.sh` — download an image for embedding (browser UA/referer), reports type/size.
- `scripts/booklet.sh` — impose the reading PDF into a saddle-stitch booklet for duplex printing.
- `scripts/printable.sh` — flatten a PDF to a 200-DPI image-only PDF so printer RIPs don't hang on embedded fonts.
- `scripts/print_booklet.sh` — send the flattened booklet to a duplex printer with the right two-sided settings.

## Notes
- Photos must be **local files** under `img/`; remote URLs may not finish loading before the PDF snapshot.
- Respect copyright: photos are for a private PDF for Tim's kid; don't redistribute, and don't reproduce long passages from sources — synthesize in your own words.
- This is a one-shot build by default. If Tim wants to formally test/iterate the skill across
  examples, that's the `skill-creator` eval loop — offer it, don't assume it.

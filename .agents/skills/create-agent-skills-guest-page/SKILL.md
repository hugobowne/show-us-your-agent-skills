---
name: create-agent-skills-guest-page
description: Create or revise a static Show Us Your Agent Skills guest dossier page in the house style of the existing docs/agent-skills/guests pages. Use when asked to prototype, generate, or repair a per-guest page for this site from field notes, timestamps, skills/workflows, screenshots, avatars, and optional 8-bit videos. Always compare against current published guest pages before writing.
---

# Create Agent Skills Guest Page

## Core Rule

Create an unlinked prototype unless the user explicitly asks to add navigation, roster links, index links, or main-page links. Do not wire the page into `docs/index.html` by default.

The current guest pages in this repo are the source of truth. The skill is a helper, not the authority. Before creating or revising a page, survey the whole current guest-page library and use the best existing patterns, sections, pacing, and media treatments already present in the repo.

Start by discovering current examples:

```bash
find docs/agent-skills/guests -maxdepth 2 -name index.html -print | sort
```

Then inspect the set before choosing any model:

```bash
rg -n "scoreboard-sec|ytfacade|interstitial|class=\"steps\"|class=\"figure\"|class=\"cards\"|class=\"tools\"|<h2" docs/agent-skills/guests/*/index.html
```

Use that survey to build from the strongest current examples. Do not model only one favorite page, only three pages, or only nearby pages. Nearby/similar pages are useful, but the whole point is to reuse the best craft already in the site.

Do not produce a generic field-notes summary page. If the output lacks scoreboard stats, an embedded segment, interstitial quote bands, narrative screenshots/figures, and a step-by-step workflow section, it probably does not match the site.

## Inputs

Use some or all of:

- Guest field-notes markdown, usually from `episode-field-notes/ep-N/<guest>.md`.
- Existing avatar thumbnail, usually under `docs/show/avatars/<guest>.png|jpg`.
- 8-bit video, usually placed in the guest page folder or supplied by the user.
- Episode metadata from `docs/index.html`: episode number, title, YouTube URL, guest roster, skill links, workflow links.

If the 8-bit video is mentioned but not present, search local likely locations first. If still missing, ask where the user wants to place it. Prefer this destination:

```text
docs/agent-skills/guests/<guest-slug>/<guest-slug>-8bit.mp4
```

Use the avatar as the poster/fallback:

```html
<video poster="../../../show/avatars/<avatar>" autoplay muted loop playsinline controls preload="metadata">
  <source src="<guest-slug>-8bit.mp4" type="video/mp4">
  <img src="../../../show/avatars/<avatar>" alt="<Guest Name>">
</video>
```

If no avatar or 8-bit video exists, use a screenshot from the episode or a public image asset already in the repo. Do not invent a portrait path.

## Page Location

Create one directory per guest:

```text
docs/agent-skills/guests/<guest-slug>/index.html
```

Use clean relative paths from that nested page:

- `../../../agent-skills`
- `../../../index.html`
- `../../../show/avatars/<avatar>`
- `../../../shared/shared.css`
- `../guest.css`

## Page Shape

Build an authored guest dossier, not a generic bio page, notes digest, or transcript dump.

The house structure is:

- Hero: guest name, avatar chip when available, identity/topic chips, long deck paragraph, primary CTAs, and 8-bit video or one strong episode still.
- Scoreboard strip: 5-6 punchy linked stats or labels. Each item must say something concrete from the segment, not generic praise.
- Embedded segment: `ytfacade` with the episode video id and segment start.
- Narrative section: a strong heading, 2-3 paragraphs, and a figure from the demo.
- Interstitial quote bands: 2-5 big quotes that carry the guest's point, each with a timestamp and explanatory caption.
- Step-by-step workflow section: `steps` cards showing the actual process, not abstract principles.
- Second figure row or full-width figure when the demo has visual proof.
- Cards section: only for real skills, workflows, repos, posts, or concrete related threads.
- Tools/stack grid: external links and one-line roles.
- Footer: show page, field notes, workflow/skill links, episode link, guest links.

Use ordinary `What they showed` / `Principles` / `Quotes` sections only as temporary scaffolding while drafting. Replace them with the richer dossier rhythm before presenting the page as ready.

### Scoreboard rules

Scoreboard items should be short and specific:

```html
<a class="stat" href="..." target="_blank" rel="noopener"><span class="n">MCUT</span><span class="l">the browser video editor exposes timeline state through MCP</span></a>
```

Good `n` values are tool names, numbers, constraints, or blunt labels from the segment. Avoid vague values such as `AI`, `WORKFLOW`, `SKILLS`, or `TOOLS`.

### Interstitial rules

Use interstitials for the lines a reader should remember:

```html
<section class="interstitial">
  <div class="page iq">
    <p>"Quote from the guest."</p>
    <div class="cap">Why this line matters, grounded in what happened on stream. <a href="..." target="_blank" rel="noopener">00:54:20</a></div>
  </div>
</section>
```

Do not stack all quotes at the bottom. Place them between narrative sections so the page has the same rhythm as the current guest dossiers.

### Step section rules

The `steps` section should reconstruct the workflow the viewer can steal. Each step needs:

- a concrete action
- one sentence of context
- a timestamp link

Do not turn the step section into broad advice.

## Copy Standards

Ground copy in the field notes. Do not invent broad framing that is not supported.

Avoid:

- Analyst/source narration: "the field notes frame this as...", "the document suggests..."
- Expository scaffolding: "the examples are concrete...", "the first half is...", "the important part is...", "this shows that..."
- Synthetic contrast formulas: "not X but Y", "the key move is...", "the code is just the substrate..."
- Generic AI copy: "unlocking", "magic", "transformative", "the real value is..."
- Unrequested interpretation of stats, packaging counts, or installability.

Prefer:

- Direct claims from the guest's actual workflow.
- Specific nouns from the field notes: tools, artifacts, verification loops, timestamps, constraints.
- Plain descriptions of agent behavior and human verification.

Example for Alan Nichol:

```text
Alan uses Claude and Remotion to generate videos as code, then checks the rendered video rather than reading every line of generated code. The skill gives Claude rules for animation, layout, text treatment, timing, and visual inspection.
```

## Media Treatment

Use the 8-bit video as the main hero media when available. Keep the static avatar thumbnail for:

- mini identity badge
- video poster/fallback
- `og:image` / `twitter:image`

Do not use multiple large hero images. If the video has controls visible, label the caption clearly as `8-BIT VIDEO`.

For pages without avatar or 8-bit video, use one full livestream frame or a repo screenshot that matches the page's core topic. Label it plainly, for example `EPISODE STILL`.

Existing page media patterns include:

- Hero video with avatar poster on pages with 8-bit clips.
- Hero still or screenshot treatment when no clip exists.
- Narrative screenshots in `images/` with `<figure class="figure">`.
- YouTube segment embed with `ytfacade` and the footer script copied from existing pages.

If a guest lacks an avatar or 8-bit clip, still preserve the rest of the page rhythm. Do not let missing media justify a thin page.

## Site Style

Use the existing guest dossier structure and `docs/agent-skills/guests/guest.css`. Only add page-specific CSS when a particular media asset needs a different aspect ratio or a small, local layout fix.

Prefer copying structure from current pages and replacing content, not inventing a new layout. First survey all current pages for reusable patterns, then choose model pages from the discovered set based on the new guest's material:

- Same or nearby episode pages, when they exist.
- Similar demo shape: product/tool demo, eval loop, review loop, writing workflow, data workflow, design/media workflow, local-first workflow, or private-skill-library workflow.
- Similar media availability: avatar plus 8-bit clip, livestream stills, workflow screenshots, or repo screenshots.
- Similar output type: one workflow, multiple workflows, one skill, multiple skills, or a guest-page narrative around tools rather than a single shippable skill.

Use the full existing library. Current pages such as Alan, Bryan, Chris, Doug, Eleanor, Eric, Hamel, Hilary, Jeremiah, Matthew, Nicolay, Paul, Randy, Tomasz, Vincent, and Wes all count as potential sources for structure, section rhythm, captions, media treatment, footer links, scoreboard language, and interstitial handling.

Do not ask "which one page should I copy?" Ask "which existing page patterns should this guest inherit?" A strong new page may combine:

- a hero/media treatment from one page
- scoreboard style from another
- quote-band pacing from another
- step-section shape from another
- figure/caption treatment from another
- cards/tools/footer treatment from another

## Workflow Before Writing

1. Read the guest's field notes.
2. List current guest pages with `find docs/agent-skills/guests -maxdepth 2 -name index.html -print | sort`.
3. Run the class/section survey with `rg` across all current guest pages.
4. Read enough current pages to cover the best available patterns: at minimum one nearby episode page if available, one similar content-shape page, one similar media-assets page, and one page whose writing/pacing is especially strong.
5. Select the model pages and pattern sources internally before editing.
6. Inventory local media: avatar, 8-bit video, field-note images, workflow images.
7. Draft the scoreboard, interstitial quotes, and step workflow first. If those cannot be drafted from evidence, the page is not ready.
8. Create or revise the page.
9. Compare the new page against the chosen model pages with `rg` or `sed` before presenting it.

## Verification

After creating or editing:

1. Check `git diff` and confirm only intended files changed.
2. Confirm the new page has the house sections: `scoreboard-sec`, `ytfacade`, `interstitial`, `steps`, `figure`, `tools`, and footer links.
3. If previewing locally, use a local server when possible; otherwise remind the user to refresh the `file://` page after edits.
4. Verify the guest page loads, media paths work, and there is no horizontal overflow.
5. Confirm `docs/index.html` has no diff unless the user explicitly requested linking.

Useful checks:

```bash
rg -n "scoreboard-sec|ytfacade|interstitial|class=\"steps\"|class=\"figure\"" docs/agent-skills/guests/<guest-slug>/index.html
rg -n "field notes frame|the examples are concrete|the first half|the important part|this shows that|key move|substrate|not .* but|WATCH MOMENT" docs/agent-skills/guests/<guest-slug>/index.html
find docs/agent-skills/guests/<guest-slug> -maxdepth 1 -type f -print -exec ls -lh {} \;
git diff -- docs/index.html
```

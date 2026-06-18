---
name: remotion-video
description: |
  How to build high-quality Remotion animated videos for social media (square 1080×1080 and vertical 1080×1920). Use this skill whenever the user asks to create, build, fix, or improve a Remotion video, animated scene, social media animation, motion design, kinetic typography, talking-head integration, scene pacing, or any motion-design work in a Remotion project. Also trigger when the user mentions scene components, animation timing, frame extraction, ease curves, or motion primitives. If you're about to write a Scene*.tsx file, read this skill first — the difference between a good and bad scene is in the approach, not the code. For re-editing existing footage into TikTok / Shorts / Reels short-form vertical with running captions and jump cuts, see the `tiktok-shorts-edit` skill instead.
---

# Remotion Video Skill

Captures hard-won lessons from building a series of short social-media videos in Remotion. Covers conceptual design thinking, layout modes, talking-head integration, motion grammar, kinetic typography, character moments, and measurable self-review.

If your project keeps companion reference files, read them when you need specifics beyond this skill:
- a brand-tokens / `CLAUDE.md` file — colors, fonts, architecture overview, animation anti-patterns
- a production playbook — pacing, transitions, audio, messaging craft
- a frame-review process doc — how to QA rendered frames
- a video-template README — the full template workflow

This skill focuses on the **design thinking and technical patterns** that make scenes work. Anywhere it shows specific colors, fonts, or asset names, treat them as placeholders to swap for your own brand tokens.

**Tone target:** design-forward with real personality. The failure mode to push back on is "competent SaaS" — restrained, corporate, forgettable. Type should perform. Small moments should have character. Motion should feel deliberately designed, not improvised. Aim for craft and confidence over polish-for-its-own-sake.

---

## The Most Important Lesson

**The visuals must tell the same story as the voiceover, not illustrate it abstractly.**

When the speaker says "our tool handles thousands of customer conversations," the temptation is to show a dashboard with a "Conversations: 12,847" metric card. That's illustration — a visual footnote. The strong version shows *the actual conversation happening* — real chat bubbles, a real phone screen, real notification banners. The story unfolds in the UI, not in abstract charts about the UI.

Ask yourself: "If I muted the audio, would someone watching understand what's happening?" If the answer is "they'd see some cards with numbers changing" — the concept is wrong. If the answer is "they'd see the product actually working in real-time" — you're on track.

---

## Conceptual Design Rules

### 1. Show the thing, not metrics about the thing

Bad: A dashboard card showing "Success Rate: 73%" while the VO describes the product handling work.
Good: An actual stream of that work happening — items appear, some succeed, some fail, and the viewer can *see* the pattern.

Audiences connect with *concrete stories*, not *abstract measurements*. Metrics can appear as supporting UI elements (a small status bar, a subtle counter), but they should never be the main event.

### 2. When using two panels, they must tell one story from two angles

If your layout has two visual regions (left/right, main/overlay), they should be *coupled* — what happens in one triggers, references, or responds to what happens in the other. If they could exist independently without losing meaning, the layout is wrong.

Good coupling:
- Left: a chat transcript → Right: the customer's phone showing the same conversation
- Left: a process with a failure → Right: a diagnostic trace showing *why* that specific step failed
- Main: a diagram showing a structure → PiP: the speaker explaining what we're looking at

Bad coupling:
- Left: an activity stream → Right: aggregate metric cards (different stories)
- Left: chat messages → Right: an unrelated lifecycle gauge

### 3. UI should look like a real product, not a presentation slide

The most compelling scenes look like someone recorded their screen while using a real app. Think: messaging apps, phone screens, IDE code windows, terminal output, notification toasts — not PowerPoint cards with big numbers and progress bars.

This means: chat bubbles with realistic padding and speaker differentiation, status indicators that look like real app UI (small dots, inline badges), system events styled as notification toasts, subtle chrome (thin borders, backdrop blur, small text labels), and `overflow: hidden` on containers because real apps clip their content.

---

## Canvas & Safe Areas

The skill supports two canvas sizes. Choose canvas first, layout mode second.

### Square (1080×1080)

For LinkedIn, X, embedded web. Full canvas is usable. No platform UI occlusion.

### Vertical (1080×1920)

For vertical X, Instagram feed (if vertical), or as a from-scratch alternative to the TikTok-edit workflow. **Safe area: all important content (text, focal UI, speaker face) must sit within the central 1080×1280 region (y=300 to y=1580).** Outside that band is for decorative background only — assume platform UI will occlude it on TikTok/Shorts/Reels.

**Talking-head framing for vertical:** speaker's eyes must sit at y=640-720 (upper third). Headroom (top of head to top of safe area) should be 80-140px. Speaker fills 60-75% of frame width.

**Layouts don't directly translate from square to vertical.** `Side TH` becomes `Top TH` (speaker upper half, content lower half), not a narrow side-by-side. `Two-Column` becomes `Stacked` (top panel + bottom panel). When in doubt, choose vertical canvas and design layouts native to it rather than letterboxing a square composition.

---

## Layout Modes

Six distinct layout modes. Choose the right one for each scene.

### 1. Side Talking Head (TH left + content right) — square only

The workhorse for scenes where the speaker introduces a concept while visuals build beside them.

```
|← 72px →|← 360px video →|← 48px gap →|← remaining →|← 72px →|
```

- Video: 360×936px, positioned at (72, 72), borderRadius 16
- Right content: starts at x=480, width ≈ 528px
- Video slides in with `enter-snap` (-80px), content slides in with `enter-snap` (+40px), staggered by 3 frames

Best for explanatory talking-head beats where supporting visuals build alongside the speaker.

### 2. Center / Top Talking Head (full-frame or upper-frame speaker)

For high-energy moments — hooks, pivots, emotional beats.

- **Square:** 720×720px (margin=180) or 820×820px (margin=130), borderRadius 16, centered
- **Vertical:** 880×1100px positioned at (100, 300) — top of safe area, leaves bottom 320px for caption/headline space
- Scene opacity: `enter-soft` in (12f), `exit-fade` out (8f)

Best for hooks and pivots where the speaker should command the frame.

### 3. PiP (Picture-in-Picture) overlay

Speaker shrinks to a small thumbnail while the full canvas shows animated content. The speaker stays present without dominating.

- **Square:** 120×180px at (24, 24), borderRadius 20
- **Vertical:** 140×200px at (32, 320) — top-left of safe area
- Border thickens as PiP shrinks: `borderWidth = 1 + (1 - sizeRatio) × 2` (≈2.7px at PiP size)
- Shadow intensifies at small sizes: alpha `0.15 + (1 - sizeRatio) × 0.4`
- `objectPosition: "center 35%"` to keep face framed above center
- Morph transition from side→PiP via `morph` primitive

Best for demo scenes where the speaker narrates over full-canvas content.

### 4. Full-Screen Animated (no speaker visible)

For demo scenes, code evolution, activity streams, geometric diagrams. The full canvas is available for content (respecting safe area on vertical).

Best for product demos, code walkthroughs, and the longest "hero" beats.

### 5. Text-Centered

For punchline moments — big typography, no graphics. Let the words land.

- Centered on canvas with 72-80px horizontal padding (square) or within safe area (vertical)
- Headlines at 9-12% of frame height, display weight (600-700)
- `enter-punch` entrance, 30+ frame hold after the line lands before transitioning

Best for one-line punchlines that need to *land*, not unfold.

### 6. Two-Column / Stacked (content + content)

Parallel perspectives or cause-and-effect. Both regions contain animated content (no speaker video).

- **Square (Two-Column):** 560px left + 20px gap + 460px right + 40px margin
- **Vertical (Stacked):** 1080×640 top panel + 40px gap + 1080×640 bottom panel, vertically centered in safe area
- **Critical: each panel must be a clipped container** with `overflow: hidden`
- Every overlap bug comes from elements using `position: absolute; inset: 0` (full canvas) instead of being contained within their panel
- Phase crossfades must overlap: incoming panel starts fading in 10 frames *before* outgoing finishes

Best for side-by-side comparisons like a chat transcript next to a phone screen.

---

## Talking Head Integration

### SceneTalkingHead component

Shared component rendering an AI talking-head / avatar video clip (e.g. HeyGen) with consistent styling:
- Accepts `layout: "side" | "center" | "top"` and `canvas: "square" | "vertical"`
- Handles scene-level fade in/out via `enter-soft` / `exit-fade`
- Slide-in animation: `enter-snap` primitive applied to video and text
- Placeholder card shown when clip file is missing (dashed circle + label + file path)
- Applies `VIDEO_FILTER` to all video elements

### PipSpeaker component (morphing speaker pattern)

For videos where the speaker morphs between layout modes across scenes:

```tsx
interface SpeakerSegment {
  clipFile: string;
  startFrame: number;
  durationFrames: number;
  mode: "side" | "pip" | "cta" | "top";
  videoStartFrom?: number;
  fadeInFrames?: number;
}
```

Key behaviors:
- Adjacent segments (no frame gap) trigger rect **morph** over 15 frames (`morph` primitive)
- Non-adjacent segments **fade** out/in (no morph — avoids jarring position jump)
- Only the *outgoing* clip morphs; incoming clip starts at its target rect
- Single clip can span multiple modes: use `videoStartFrom` for the second segment instead of splitting files

### CTA mode

Centered, larger than PiP (240×360px square / 320×440px vertical), positioned slightly above center (y offset -80 square / -200 vertical) to clear the URL text below. Used for the final logo/CTA scene where the speaker's face appears with the brand URL.

### Video filter (color grading)

AI-generated talking-head footage (HeyGen and similar) often skews warm/orange. Apply a consistent grade across all clips:
```ts
filter: "saturate(0.82) brightness(0.95) hue-rotate(-10deg) contrast(1.15)"
```
Tune the values to your footage — the point is one filter applied uniformly, so every clip matches.

### Talking-head clip handling

- Trim at exact word boundaries from transcript JSON (not percentage-based)
- Leave 2-3 frames headroom after last word (codec padding eats 1 frame)
- Merge clips that share a continuous take — use `videoStartFrom` on the second segment
- Use `fadeInFrames: 21` (0.7s) to mask idle-smile artifacts when a clip starts during another scene's audio
- Never re-encode video during audio-only processing (`-c:v copy`) — each re-encode degrades skin tones

---

## Typography

Type sizes are expressed as **% of frame height**, not pixels. If a value drops below the minimum % for that platform, the layout is wrong, not the type size.

Pick two typefaces and stick to them: a display/body sans and a monospace. The values below use **Inter** (sans) and **JetBrains Mono** (mono) as free, shareable defaults — swap in your own brand fonts and keep the weights and size ratios.

### Type scale

| Use | Font | Square (1080×1080) | Vertical (1080×1920) | Weight |
|-----|------|---------------------|----------------------|--------|
| Headlines | Inter | 96-128px (9-12% H) | 128-160px (7-9% H) | 600-700 |
| Body text | Inter | 44-52px (4-5% H) | 60-72px (3.5-4% H) | 400 |
| Chat bubbles | Inter | 44px | 60px | 400 |
| Code / YAML | JetBrains Mono | 40-44px | 56-60px | 400 |
| Eyebrow labels | Inter | 28px (2.5% H) | 36px | 600 |
| Tags / badges | Inter | 28-32px | 36-40px | 600 |
| System toasts | Inter | 32px | 44px | 600 |
| Phone UI labels | Inter | 28-32px | 36-44px | 600 |

### Density rule

**Maximum 7 words on screen at once for body, 4 for headlines.** If it doesn't fit, cut words — don't shrink type.

### Preview rule

Preview at 1:1 pixel scale. What looks fine at 2× in a browser is tiny in the rendered video. When evaluating type sizing in stills, measure as % of frame height, not absolute pixels.

---

## Kinetic Typography

Long-form lines must not land as a single static block. Use word-level Whisper timestamps to reveal text **word-at-a-time or phrase-at-a-time, synced to spoken audio**. This is the single highest-leverage motion technique for a design-forward tone — type that performs is what makes serious technical content feel alive without resorting to influencer theatrics.

### Phrase reveal

Break the line at natural prosodic boundaries (use comma/clause boundaries from the transcript). Each phrase enters with `enter-soft` (4-frame variant): `translateY(8→0) + opacity(0→1)` over 4 frames, `snappy` easing. Trigger frame = word start frame from Whisper minus 3 frames (pre-cue, because eyes process faster than ears).

### Keyword emphasis

Within a static line, animate the *one* keyword the speaker stresses. Apply the `emphasis-pulse` primitive: scale 1.0→1.08 over 6 frames with `punch` easing, hold for 8 frames, settle to 1.0 over 6 frames. Optionally shift color to an accent (e.g. `#FBBF24` or `#22D3EE`) for the duration of the emphasis.

### Rules

- Pick one mode per scene. Don't combine phrase-reveal *and* keyword-emphasis in the same scene — it becomes noise.
- Never reveal more than 7 body words or 4 headline words on screen at once. Earlier phrases fade to 60% opacity (not 0) as later ones enter, so the line stays legible as a whole.
- Sync to **word start frames from Whisper**, never to estimated VO timing.
- Don't kinetic-typography a punchline. Punchlines need to *land*, not unfold. Punchlines use `enter-punch` on the full line at once.

---

## Easing Functions

Four custom easings defined in `constants.ts`:

| Name | Formula | Use |
|------|---------|-----|
| `smooth` | `1 - (1-t)³` (cubic ease-out) | General fades, scroll animations, scene opacity |
| `snappy` | `1 - (1-t)⁴` (quartic ease-out) | Slide-in entrances, directional moves, UI elements |
| `punch` | Overshoots to 1.1 at t=0.6, settles to 1.0 | Headline entrances synced to VO beats — makes text *arrive* |
| `spring` | Exponential decay + sinusoidal overshoot | Pill/badge entrances, small elements that bounce into place |

Plus `elasticOut` (subtler elastic bounce) for secondary animations, and `easeOutCubic` for layout morphs.

**Never use `linear`** — it always looks mechanical.

---

## Motion Primitives

Use this palette. Don't invent new durations or one-off animations. Every animation in the codebase should be one of these primitives; if a scene needs something not on this list, the primitive list is wrong, not the scene — extend the table, don't one-off it.

| Primitive | Use | Easing | Duration | Transform |
|-----------|-----|--------|----------|-----------|
| `enter-soft` | Body text, secondary elements, supporting UI | `smooth` | 12f | opacity 0→1 + translateY 12→0 |
| `enter-snap` | Directional slides (TH videos, columns), structural elements | `snappy` | 9f | opacity 0→1 + translate from offset |
| `enter-punch` | Headlines, keyword emphasis, beat-synced impacts | `punch` | 12f | opacity 0→1 + scale 0.85→1.0 (overshoot 1.1) + translateY 20→0 |
| `enter-spring` | Pills, badges, small UI elements that bounce in | `spring` | 18f | opacity 0→1 + scale 0.6→1.0 |
| `exit-fade` | Anything leaving without urgency | `smooth` | 8f | opacity 1→0 |
| `emphasis-pulse` | Mid-shot keyword stress, single-frame attention | `punch` (up) + hold + `smooth` (down) | 6f + 8f + 6f | scale 1.0→1.08→1.0 |
| `morph` | Layout-mode transitions (side→PiP, panel→panel) | `easeOutCubic` | 15f | `lerpRect` on x/y/w/h |

The consistency of using a small named palette is what makes motion read as **designed** rather than **improvised**. The best motion-design videos use a similarly small set.

---

## Animation Patterns

### Punch entrance (headlines synced to VO)

When the speaker says a key phrase, the headline should *arrive* on that beat — not before, not after. Pre-cue the visual trigger 4-8 frames before the spoken word (the eye processes faster than the ear, so sync feels late).

Apply `enter-punch`. Reserve scale + punch for big headlines only. For body text and secondary lines, use `enter-soft` — more refined.

### Staggered reveals

Multiple elements (list items, pills, grid cards) cascade in with frame delays, never simultaneously.

- Pill badges: `enter-spring`, 10-frame gap between each
- Slot/grid rows: `enter-snap`, 7-frame gap
- Conversation messages: `enter-soft`, timed to VO
- Channel labels: 5-7 frame stagger

### Code cross-fade

When showing code that evolves (e.g., YAML before/after):
1. Define two complete code arrays (before and after)
2. Cross-fade between them over ~18 frames (v1 opacity down, v2 opacity up)
3. Animate the code box height smoothly between the two sizes
4. Apply editor-style highlights to **new lines** AFTER the cross-fade completes
5. Highlights wipe in left-to-right: `clipPath: inset(0 X% 0 0)`, staggered 2 frames per line

Highlight styling: colored left border (3px) + subtle background tint — NOT gradients.
```tsx
borderLeft: "3px solid #22C55E"
background: "rgba(34, 197, 94, 0.12)"
```

### Conversation stream

The most reusable and effective visual element — chat UIs read as "real product" to almost any audience. Pattern:

```tsx
interface ScriptLine {
  speaker: "customer" | "agent" | "system";
  text: string;
  startFrame: number;
  duration: number;
  estimatedH: number;
  audioFile?: string;
}
```

- Pre-define scroll triggers as `[startFrame, endFrame, scrollAmount]` tuples
- Clip the conversation area: `clipPath: inset(80px 0 40px 0)`
- Customer messages: right-aligned, accent tint `rgba(99,102,241,0.22)`, borderRadius 20-20-4-20
- Agent messages: left-aligned, white alpha `rgba(255,255,255,0.06)`, borderRadius 20-20-20-4
- System events: full-width, green left border (3px #22C55E), checkmark icon, semibold font
- Live indicator: pulsing green dot `Math.sin(frame * 0.15) * 0.5 + 0.5`
- Appear animation: `enter-soft`
- During mid-video TH scenes, fade the conversation out 15 frames before, hide during TH, fade back in 15 frames after

### Phone screen

For showing a mobile device alongside a conversation:
- Container: 320×660px, borderRadius 36, deep shadow `0 20px 60px rgba(0,0,0,0.5)`
- iOS-style status bar: "9:41", signal bars, battery icon
- Entry animation: `enter-soft` (20-frame variant for larger entrance)
- App transitions: slide animations over 12 frames, `snappy` easing
- Notification banners: slide in from top (-20→0px), `enter-soft`, 14 frames

### Pill / badge animations

For tags, labels, or category badges:
- Stagger entrances with `enter-spring`, ~10-frame gap
- Use absolute positioning for merge animations (row→stack or vice versa)
- Interpolate x/y from source to target layout
- Fade individual borders out while fading unified container border in
- Always `whiteSpace: "nowrap"` on pills

### Ring diagram

For showing cyclical processes or interconnected concepts:
- Use polar coordinates for label placement (angles, not absolute positions)
- Orbiting particles: small circles following the ring path
- Traveling light pulse: thick (7px), glow filter, looping every 70 frames — subtle versions are invisible
- Labels need background pills for contrast against dark background

### Scene-to-scene transitions

Most scene transitions should be a 6-frame crossfade. Reserve the techniques below for moments where they add narrative weight.

- **Audio leads (J-cut):** transitioning from TH-explanation to a demo, start the demo's ambient audio (notification ping, typing sound) 12-18 frames *before* the visual cuts. The ear arrives first; the eye follows.
- **Visual leads (L-cut):** transitioning from demo back to TH, hold the demo audio 8-12 frames *into* the TH scene. The connection persists.
- **Match cut:** when two scenes share a shape — a chat bubble at scene end and a circular UI element at scene start in the same screen position — cut directly with no transition. Position continuity carries the cut.
- **Cut on motion:** prefer cutting when an element is *mid-move* (between keyframes), not at rest. The eye is already in motion and accepts the new frame more readily.

---

## Moments of Character

Every 60-second video should contain **2-4 deliberate micro-moments** where a single element does something with personality. These are not decorative — they're the difference between "clear" and "memorable," and the difference between flat polish and real character. Each moment must be ≤24 frames, involve exactly one element, and either reinforce or gently undercut what the speaker is saying.

### Catalog

- **The hesitating cursor.** When showing a UI action, the cursor moves toward the target, *pauses for 8-12 frames*, then clicks. The pause reads as thought. Apply when the speaker describes a decision.
- **The reactive UI.** A notification arrives → the nearest UI element shifts 2-3px toward it (`snappy`, 8f, then settle over 12f). The screen reacts to its own contents.
- **The held silence.** A 20-30 frame beat with zero motion in the body but the speaker still mid-thought. Pairs with the held beat before the punchline.
- **The disagreeing element.** When the speaker says "you'd think X," show X — then have *one element* visually contradict X (a checkmark flips to an X, a "100%" ticks down to "97%"). The visual argues back.
- **The wink.** A single non-essential element does something small and unexpected — a pill rotates 2deg on entry then settles, a chat avatar bounces once, a code line briefly underlines itself. **At most one wink per video.** Two winks is a content creator. One wink is character.

### Rules

- One micro-moment at a time. Never stack them.
- They cost frames. Budget them in. If a scene is 90 frames and contains a micro-moment, reduce the surrounding animation density to compensate.
- These moments are the answer when output feels professional-but-flat. If a draft scene clears every other check but feels lifeless, the missing thing is a moment of character.

---

## Scene Timing & Structure

### Timing constants

All timing lives in a single `TIMING` object in `constants.ts`. Every scene start, duration, and split point is defined here. Components reference `T.sceneStart` — never hardcoded frame numbers.

```tsx
const sceneOpacity = interpolate(
  frame,
  [S, S + 10, S + D - 14, S + D],
  [0, 1, 1, 0],
  { extrapolateLeft: "clamp", extrapolateRight: "clamp" }
);
```

The orchestrator (Main.tsx) mounts/unmounts scenes with a small buffer: `frame >= T.sceneStart - 1 && frame < T.nextSceneStart + 12`.

### Proven narrative structure

1. **Hook (0-2.5s / 0-75f)** — Cold open with the speaker *already mid-sentence*, or a single concrete artifact (a chat message, a piece of code, a UI element) that doesn't yet make sense. **No logo, no concept title, no brand lockup in the first 60 frames** — defer all of that to the CTA. The opening frame must (i) raise a question the viewer needs answered, and (ii) feature one focal element with the rest of the frame deliberately empty (≥40% negative space). Strongest hooks pair an unexpected verbal opener with a visual that contradicts an assumption.
2. **TH intro** (~3-8s) — Speaker sets up the problem. Side or top layout.
3. **Problem / Old World** (~5-10s) — Visual demonstration of the pain point. Full-screen animated.
4. **TH pivot** (~2-5s) — Speaker introduces the solution. Side or center layout.
5. **Demo / Hero** (~8-15s) — The longest scene. Show real product artifacts. Full-screen or PiP.
6. **Punchline** (~4s) — Text-centered. One punchy line. `enter-punch`. Let it land.
7. **Payoff** (~5s) — Visual callback. Show composition / unity.
8. **CTA** (~3-7s) — Brand, concept name, URL. Speaker in CTA mode or center layout. **This is where the brand lockup lives** — not the opening.

Target total: **45-60 seconds** for social. 80+ seconds is too long — cut whole scenes to fit rather than trying to shorten everything.

### Pacing targets

A 60-second video should hit **18-24 cuts per minute** in the body, **denser at the opening** (3-4 cuts in the first 5 seconds), with one **held beat of 30-45 frames** before the punchline and a final hold of 20-30 frames on the CTA.

Average shot length (ASL) targets per layout mode:
- Hook / opening: 30-45 frames (1.0-1.5s)
- Demo / hero: 60-120 frames (2-4s) — longer because the UI inside is doing the narrative work
- Side TH talking explanatory beats: 90-150 frames (3-5s)
- Punchline (text-centered): 75-120 frames (2.5-4s) — must hold long enough to read twice

If any scene exceeds **180 frames (6s)** without a beat change — a new element entering, a transform, a focal shift — the scene is too long. Either insert an internal beat or cut the scene.

**Attention curve:** the video should feel like (high) → (medium-high, sustained) → (low, the held beat before punchline) → (high, punchline) → (medium, CTA). Pacing reinforces this — fast at the open, steady in the middle, deliberately slow before the punchline so the punchline *hits*.

### Other pacing rules

- Animate *on* the VO beat, not before or after (pre-cue 4-8 frames — the eye processes faster than the ear)
- At any given frame, only ONE thing should be actively animating — everything else static or pulsing
- Pick one transition style (quick, consistent, same easing) and use it everywhere — varied, elaborate transitions feel janky

---

## Shared Components

These are example components with example tokens. Swap the colors, fonts, and asset names for your own brand.

### Background
Full-frame background image (`background.png`) + dark overlay (`rgba(11,11,20,0.80)`).

### TextArea
Centered text container. Padding: 80px top/bottom, 72px left/right (square) or 120px top/bottom, 72px left/right (vertical, respects safe area).

### Eyebrow
Small uppercase label. Semibold 28px (square) / 36px (vertical), letter-spacing 0.18em, accent color (#FBBF24).

### Headline
Semibold/bold, default 96px (square) / 128px (vertical), line-height 1.12. Accepts `size` prop.

### Body
Regular 44px (square) / 60px (vertical), line-height 1.6, `whiteAlpha80`.

### Card
Glass-morphic: `rgba(255,255,255,0.08)` background, 1px `rgba(255,255,255,0.15)` border, 8px radius, 28px 32px padding, `backdrop-filter: blur(8px)`.

### AccentLine
48×2px divider, `#6366F1` accent.

---

## Brand Colors

Replace this entire palette with your own brand tokens. The values below are a neutral, shareable example — what matters is the *roles*, not these specific hexes.

```
Accent (primary):   #6366F1  (indigo — primary)
Background:         #0B0B14  (near-black navy)
Warm accent:        #FBBF24  (amber — eyebrow labels, string values in YAML)
Cool accent:        #22D3EE  (cyan — top-level YAML keys, secondary accent)
Success:            #22C55E  (green — success, system events, code highlights)
Soft tertiary:      #A5B4FC  (lavender — soft accents)
Lighter accent:     #818CF8  (indigo-light — nested YAML keys)

White alphas: 80%, 60%, 40%, 25%, 15%, 8% — for layered glass-morphic effects
Overlay:     rgba(11,11,20,0.80)  (background image overlay)
```

### YAML syntax highlighting

Custom tokenizer. Key rules (map these roles to your own palette):
- Top-level keys (`flows:`) → cool accent (#22D3EE)
- Nested keys → lighter accent (#818CF8)
- String values → warm accent (#FBBF24)
- Booleans/numbers → success green (#22C55E)
- List markers (`- `) → whiteAlpha60
- Comments → whiteAlpha40
- Colons → whiteAlpha60

---

## What NOT To Do

### Don't open on a brand card

Brand-first opens are the highest-swipe-rate opening on social. Lead with a question, an artifact, or the speaker mid-sentence. The brand belongs in the CTA, not frame 0.

### Don't center things on the full canvas when using columns
```tsx
// BAD: positions relative to full canvas, ignoring column boundaries
style={{ position: "absolute", top: "50%", left: "50%", transform: "translate(-50%, -50%)" }}

// GOOD: positions within the column container
style={{ display: "flex", justifyContent: "center", alignItems: "center", height: "100%" }}
```

### Don't use CSS transitions in Remotion
Remotion renders each frame independently. Use `interpolate()` and easing functions for everything.

### Don't invent one-off motion durations
Use the Motion Primitives table. If a scene needs something not on the list, extend the table.

### Don't make SVG graphics the main visual
Small SVG accents are fine. A centered SVG circle is not compelling enough to carry a scene.

### Don't use opacity below 0.5 for important elements
Background decoratives can be faint. Information-carrying elements (labels, nodes, connection lines) need 0.6+ opacity.

### Don't over-abstract the story
A gauge going 0%→94% is boring. A real interaction where the product fails, then succeeds — that's interesting.

### Don't animate too many things at once
One focal animation per frame. Everything else static or barely pulsing (scale 1.00↔1.02, 60-90 frame period).

### Don't force graphics where text works
The punchline scene is strongest as plain text at headline scale. A graphic with checkboxes and boxes looks janky.

### Don't use linear gradients for code highlights
They look cheap. Use editor-style (colored left border + subtle background tint).

### Don't show 80+ seconds of content for social
Set a 45-60s target. Cut whole scenes rather than trying to compress everything.

### Don't stack micro-moments of character
One at a time, ≤4 per video, ≤1 wink per video. Two winks is a content creator.

### Don't kinetic-typography a punchline
Punchlines must *land*, not unfold. They get `enter-punch` on the full line at once, not phrase reveal.

---

## Frame Review Workflow

After building or modifying scenes:

1. Run `npx tsc --noEmit` to verify compilation
2. User runs `node extract-frames.mjs [every] [compositionId] [scale]`
3. Claude uses a **subagent** to inspect ALL frames in `frame-review/`:
   - View every single frame image
   - Apply the **post-render checklist** (below) to each frame
   - Rate each frame: EXCELLENT / GOOD / NEEDS WORK
   - Be **brutally honest** — the most common failure mode is declaring something "okay" that's actually mediocre

**Frame density:** ~30+ frames for a full video, 3-5 per animated scene, 2 at each transition, at least 1 per TH scene.

### Motion review

Stills can't show ease curves, animation timing, or transition smoothness — the three things motion design most often fails on. For each animated transition, render frames at the **start, 25%, 50%, 75%, and end** of the animation window. The subagent inspects these five frames as a sequence and answers:

- Does the element's position/scale/opacity progress *non-linearly*? (If the values look equally spaced, easing is broken — `linear` snuck in somewhere.)
- At 50%, is the element more than 50% of the way to its target? (Ease-out should overshoot the midpoint.)
- Does the 25% frame look notably different from the start? (If not, the animation starts too slow.)

Any "no" means the easing is wrong even if the start and end frames look correct.

---

## Checklist Before Declaring a Scene Done

Counts and percentages — not subjective judgments. Any "no" is a defect, not a preference. Fix before continuing.

### Pre-render (compute from source code)

1. Body text minimum size in this scene ≥ 4% of frame height? (44px on square, 76px on vertical)
2. Headline text in this scene ≥ 9% of frame height?
3. Words on screen at any one frame ≤ 7 (body) or 4 (headline)?
4. Every animated element uses a named primitive from the Motion Primitives table (no one-off durations)?
5. At any given frame, exactly one element is mid-animation (others static or pulsing)?
6. Every positioned element is inside a clipped container with `overflow: hidden`?
7. Scene duration ≤ 180 frames, OR contains an internal beat change?
8. For vertical canvas: every important element sits in the y=300-1580 safe area?
9. If this is the opening scene: no logo, concept title, or brand lockup in the first 60 frames?
10. If this is a full video: between 2 and 4 micro-moments of character distributed across scenes? (And at most 1 wink?)

### Post-render (per frame, by subagent)

1. Smallest legible text ≥ 4% of frame height? Measure with a ruler overlay.
2. Focal element in the upper two-thirds of the frame (not dead center)?
3. ≥30% of frame is intentional negative space (not crammed)?
4. One unambiguous focal point per frame?
5. Frame would still make sense as a still poster — i.e., the composition is intentional, not transitional?

### Conceptual (per scene)

1. **What story does this scene tell?** Not "what data does it display" — what *happens*?
2. **If I muted the audio, would a viewer understand?** Visuals should carry narrative weight independently.
3. **Does this look like a real product UI?** Or does it look like a presentation slide?

---

## Related Skills

- **`tiktok-shorts-edit`** — for re-editing existing horizontal/square footage into TikTok / Shorts / Reels short-form vertical with running captions, jump cuts, and B-roll insertion. Use that skill (not this one) when the input is existing footage rather than a from-scratch Remotion build.

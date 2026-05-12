---
name: 8-bit-video-gen
description: Turns a photo of a person into a short 8-bit pixel-art video via a two-step pipeline. Gemini stylizes the photo as an 8-bit still, then Replicate's seedance-2.0 animates that still into an MP4. Use when the user supplies a portrait photo and asks for an "8-bit video", "pixel art animation", or "retro video game version" of themselves. Trigger even if they only mention one of the two steps.
---

# 8-bit video pipeline

Two-step pipeline that turns a portrait photo into a short pixel-art video clip:

1. **Stylize.** Gemini converts the photo into an 8-bit still PNG.
2. **Animate.** Replicate's `bytedance/seedance-2.0` uses that still as the first frame to generate an MP4.

Both scripts live in `scripts/` and use [PEP 723 inline script metadata](https://peps.python.org/pep-0723/), so `uv run` resolves their dependencies automatically.

If the user only wants the still, run step 1 and stop. If they already have an 8-bit image, skip to step 2.

## Setup

Before running either script:

1. **Verify `uv` is installed:** `uv --version`. If missing, ask the user to install it (https://docs.astral.sh/uv/getting-started/installation/). The scripts declare their Python dependencies inline (PEP 723 metadata), so `uv run` handles the rest.

2. **Verify the API keys are available.** Both scripts load from a `.env` in the working directory, falling back to the shell environment. Confirm both are set before running:
   - `GEMINI_API_KEY` for step 1 (Gemini stylize)
   - `REPLICATE_API_TOKEN` for step 2 (Replicate animate)

   If either is missing, ask the user to add it to `.env` or export it. Keys come from:
   - https://aistudio.google.com/apikey
   - https://replicate.com/account/api-tokens

## Before each run: ask about customization

Ask the user whether they want to customize the still prompt, video prompt, duration, or seed. Defaults live as `DEFAULT_PROMPT` in `scripts/make_8bit.py` and `DEFAULT_PROMPT` / `DEFAULT_DURATION` / `DEFAULT_SEED` in `scripts/make_video.py`; pass `--prompt`, `--duration`, or `--seed` to override for one run, or edit the constants to change the shipped default.

## Step 1: Stylize the photo

```bash
uv run <skill-dir>/scripts/make_8bit.py <input_photo> [output_png] [--prompt "..."]
```

- Default output: `<input_stem>_8bit.png` next to the input.
- Stylize prompt is `DEFAULT_PROMPT` at the top of `scripts/make_8bit.py`. Pass `--prompt` to override it for one run.
- Model ID: `gemini-3.1-flash-image-preview`. If the API rejects it, try `gemini-2.5-flash-image-preview` (the "nano banana" model).
- The model can sometimes add facial features that aren't in the source (e.g. a beard on a clean-shaven subject). Flag the output when this happens; do not silently rewrite the prompt to compensate.

## Step 2: Animate the still

```bash
uv run <skill-dir>/scripts/make_video.py <input_image> [output_mp4] \
    [--prompt "..."] [--duration 15] [--seed 42]
```

- `<input_image>` is normally the 8-bit PNG from step 1, but any image works (used as the first frame).
- This call costs Replicate credits and takes ~30 to 90s.
- Output is an MP4 plus a `replicate.delivery` URL printed to stdout. The URL expires; the local file is the durable artifact.
- Occasionally Replicate returns `ModelError: ... sensitive (E005)` on benign inputs. Rerun the same command before changing the prompt or image; it usually clears on retry.

## End-of-run

Tell the user the local MP4 path and the temporary URL. To iterate on the scene, rerun step 2 with a new `--prompt`; no need to redo step 1.

## Design notes

- **Defaults live in the scripts; CLI flags override per run.** Editing the constants changes the shipped default. Passing a flag overrides for one run without mutating the file.
- **Minimal prompts for the still.** Long, hedged prompts to image models tend to over-direct.

## After each run: iterate on the skill

After every run, ask the user whether anything about the workflow should be folded back into the skill: new defaults, prompt changes, extra steps, things that surprised them, anything they corrected by hand. If yes, update `SKILL.md` and/or the scripts so the next run starts from the improved version.

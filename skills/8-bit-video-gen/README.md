# 8-bit-video-gen

A two-step pipeline that turns a guest's photo into a short 8-bit pixel-art video. Gemini stylizes the photo as an 8-bit still, then Replicate's seedance-2.0 animates that still into an MP4.

## how it's used

Hugo runs this on guest headshots ahead of each *Show Us Your Agent Skills* livestream. The clips play in the intro reel and as cutaways throughout the show.

## how to use it

`SKILL.md` is the artifact. Copy this whole folder into the location your agent harness expects, then prompt the agent to use the skill. Common locations:

- **Claude Code:** `.claude/skills/8-bit-video-gen/` (project) or `~/.claude/skills/8-bit-video-gen/` (user)
- **Cursor, Codex, and other harnesses with skill support:** see your harness's documentation for the expected directory

You will also need `GEMINI_API_KEY` and `REPLICATE_API_TOKEN` set in your shell or in a `.env` in your working directory.

Then ask your agent:

> "Use the 8-bit-video-gen skill to make a video from /path/to/photo.jpg."

## see it in action

[Episode 1 of *Show Us Your Agent Skills*](https://youtube.com/live/Pq3xuChdwxQ?feature=share): the intro reel and several mid-show cutaways are generated with this skill.

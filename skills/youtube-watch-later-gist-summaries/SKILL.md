---
name: youtube-watch-later-gist-summaries
description: Use when a user wants an agent to summarise every video in their YouTube Watch Later playlist, publish one secret GitHub gist per summary with gh, and return channel/title/gists.sh summary links. Browser-tool agnostic; assumes the agent can operate the user's logged-in browser/session.
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [youtube, watch-later, transcripts, summaries, github-gists]
    related_skills: []
---

> **Project:** [YouTube Watch Later Skill](https://gist.github.com/intellectronica/a13f611b8785d33e603ae946961650e4), a public GitHub Gist published by Eleanor Berger (`intellectronica`). The skill was written by her Hermes agent, which the frontmatter credits as the author.
>
> **License:** MIT, as declared in the skill's frontmatter. Full license text is in [`LICENSE`](LICENSE) alongside this file.
>
> **Snapshot:** Frozen copy of the gist as of 2026-05-22. The maintained version lives upstream and may have evolved since this snapshot.

# YouTube Watch Later Gist Summaries

## Overview

Use this skill to produce shareable summary links for all videos currently in a user's YouTube Watch Later playlist. The output is a concise list of `Channel — Title — https://gists.sh/<owner>/<gist-id>` entries, with one secret GitHub gist per video summary.

This skill is intentionally browser-tool agnostic. Use whichever browser-control tool is available in the current environment, but operate the user's already logged-in browser/session where possible. Do not assume a particular browser automation package, profile path, or Chrome debugging port unless the environment explicitly provides one.

## Hard Boundaries

- Do not add videos to Watch Later.
- Do not remove videos from Watch Later.
- Do not mutate unrelated browser, YouTube, GitHub, or Hermes configuration.
- Do not make public gists. `gh gist create` is secret by default on current GitHub CLI versions; avoid `--public`.
- Do not paste full transcripts into chat, logs, process titles, or gist descriptions.
- Do not rely on another YouTube transcript skill being installed; transcript extraction instructions are included below.

## Prerequisites

- A browser-control tool that can inspect the user's authenticated YouTube session.
- The user is logged in to YouTube in that browser session.
- `gh` is installed and authenticated to the GitHub account that should own the gists.
- Network access to YouTube and GitHub.
- A way to fetch transcripts, preferably Python with `youtube-transcript-api`; fallback options are documented below.

Check prerequisites before doing expensive work:

```bash
gh auth status
python3 - <<'PY'
try:
    import youtube_transcript_api
    print('youtube-transcript-api: available')
except Exception as exc:
    print(f'youtube-transcript-api: unavailable: {exc}')
PY
```

If `youtube-transcript-api` is missing and package installation is allowed in the environment, use an isolated environment such as `uv run --with youtube-transcript-api ...` rather than mutating a project dependency file.

## Workflow

### 1. Open the authenticated Watch Later playlist

In the user's logged-in browser/session, navigate to:

```text
https://www.youtube.com/playlist?list=WL
```

If YouTube redirects to sign-in or shows an empty/logged-out state, stop and ask the user to provide or unlock an authenticated browser session. Do not attempt credential entry unless the user explicitly asks and the environment permits it.

### 2. Collect the full current video list

Scroll the playlist until no new videos load. Extract, for every visible playlist item:

- `video_id` from the `v=` parameter or canonical video URL.
- `url` in canonical form: `https://www.youtube.com/watch?v=<video_id>`.
- `title` exactly as YouTube displays it, trimmed.
- `channel` if shown; otherwise use `Unknown channel` and continue.
- Optional useful fields: duration, playlist index, unavailable/private/deleted status.

De-duplicate by `video_id` while preserving playlist order. If an item is unavailable/private/deleted and no transcript can be fetched, keep it in the final report with `Summary: unavailable` rather than silently dropping it.

Browser extraction can be done by accessibility snapshots, page DOM evaluation, or exported page data. Prefer structured DOM data when available. A generic DOM strategy is:

```javascript
[...document.querySelectorAll('ytd-playlist-video-renderer, ytd-playlist-panel-video-renderer')]
  .map((el, index) => {
    const link = el.querySelector('a#video-title, a.yt-simple-endpoint[href*="watch"]');
    const href = link?.href || '';
    const url = new URL(href, location.href);
    const video_id = url.searchParams.get('v');
    const title = (link?.textContent || link?.getAttribute('title') || '').trim();
    const channel = (el.querySelector('ytd-channel-name a, #byline a, .ytd-channel-name')?.textContent || '').trim();
    const duration = (el.querySelector('ytd-thumbnail-overlay-time-status-renderer, .ytd-thumbnail-overlay-time-status-renderer')?.textContent || '').trim();
    return video_id ? {index: index + 1, video_id, url: `https://www.youtube.com/watch?v=${video_id}`, title, channel, duration} : null;
  })
  .filter(Boolean)
```

Treat this as a starting point only; YouTube DOM changes often. Verify the extracted count and spot-check the first and last few titles in the browser.

### 3. Fetch each transcript

Try transcript sources in this order. Save transcripts only in temporary working files unless the user asked for a cache.

#### Primary: `youtube-transcript-api`

Use an isolated Python command. This example tries manually supplied captions first, then generated captions, and prefers English/English-translated text where available:

```bash
uv run --with youtube-transcript-api python - "$VIDEO_ID" > "$TRANSCRIPT_FILE" <<'PY'
import sys
from youtube_transcript_api import YouTubeTranscriptApi

video_id = sys.argv[1]
api = YouTubeTranscriptApi()

try:
    transcript_list = api.list(video_id)
except Exception as exc:
    raise SystemExit(f'transcript-list-failed: {exc}')

candidates = []
for transcript in transcript_list:
    candidates.append(transcript)

preferred = None
for lang in ('en', 'en-US', 'en-GB'):
    try:
        preferred = transcript_list.find_manually_created_transcript([lang])
        break
    except Exception:
        pass
if preferred is None:
    for lang in ('en', 'en-US', 'en-GB'):
        try:
            preferred = transcript_list.find_generated_transcript([lang])
            break
        except Exception:
            pass
if preferred is None:
    for transcript in candidates:
        if getattr(transcript, 'is_translatable', False):
            try:
                preferred = transcript.translate('en')
                break
            except Exception:
                pass
if preferred is None and candidates:
    preferred = candidates[0]
if preferred is None:
    raise SystemExit('no-transcript-candidates')

snippets = preferred.fetch()
for item in snippets:
    text = getattr(item, 'text', None) if not isinstance(item, dict) else item.get('text')
    if text:
        print(' '.join(str(text).split()))
PY
```

The library API has changed across versions, so if this snippet fails because `YouTubeTranscriptApi` shape differs, inspect the installed version briefly and adapt. The required outcome is a plain-text transcript, not a dependency on this exact code.

#### Fallback: subtitles via `yt-dlp`

If `youtube-transcript-api` fails and `yt-dlp` is available, try subtitles/auto-captions:

```bash
mkdir -p "$TMPDIR/youtube-subs"
yt-dlp --skip-download --write-subs --write-auto-subs --sub-langs 'en.*,en,live_chat' --sub-format vtt --paths "$TMPDIR/youtube-subs" "https://www.youtube.com/watch?v=$VIDEO_ID"
```

Convert `.vtt` to text by removing `WEBVTT`, cue timing lines, sequence numbers, markup tags, duplicate repeated caption lines, and blank noise. If only non-English captions exist, request that language directly and summarise into English.

#### Failure handling

For each transcript failure, record a concise reason such as `captions disabled`, `private/unavailable`, `age restricted`, `transcript API failed`, or `yt-dlp unavailable`. Continue with the rest of the playlist.

### 4. Summarise each video in English

Create a compact Markdown summary for each video. The gist body should be useful as a standalone note and should not include the full transcript.

Recommended structure:

```markdown
# <Video title>

Channel: <Channel>
YouTube: https://www.youtube.com/watch?v=<video_id>

## TL;DR
<3-5 sentence summary in English.>

## Key points
- <important idea>
- <important idea>
- <important idea>

## Notable details
- <specific, non-obvious details, examples, names, figures, claims, or caveats>

## Why it might matter
<One short paragraph on relevance/usefulness.>
```

Summarise from the transcript. If the transcript is very long, chunk it and combine chunk notes into the final summary. Preserve uncertainty: if the transcript is noisy, partial, auto-translated, or missing parts, say so in the summary.

### 5. Create one secret gist per ready summary

For each summary file:

```bash
gh gist create --desc "Summary: <video title>" --filename "<safe-video-id-or-title>.md" - < "$SUMMARY_FILE"
```

Important details:

- Do not pass `--public`.
- Do not pass `--secret`; many `gh` versions do not support it, and secret is the default.
- Capture the returned gist URL or gist ID.
- Convert the gist ID to the short reading URL format: `https://gists.sh/<owner>/<gist-id>`.

Derive `<owner>` from `gh api user --jq .login` or from the returned gist URL. For a returned URL like `https://gist.github.com/octocat/abc123`, the `gists.sh` URL is `https://gists.sh/octocat/abc123`.

Verify each gist before reporting it:

```bash
gh api "gists/$GIST_ID" --jq '{id, public, description, files: (.files | keys)}'
```

Expected: `public` is `false`, at least one Markdown file exists, and the description begins with `Summary:`.

### 6. Return the final list

Return the list in playlist order. Use a compact, copyable format:

```text
1. <Channel> — <Title>
   Summary: https://gists.sh/<owner>/<gist-id>
   YouTube: https://www.youtube.com/watch?v=<video_id>

2. <Channel> — <Title>
   Summary: unavailable — <concise reason>
   YouTube: https://www.youtube.com/watch?v=<video_id>
```

Include a brief status line: total videos found, summaries created, gists verified, failures. Do not include full transcript text.

## Suggested Working Manifest

When implementing this workflow, keep a machine-readable manifest in the workspace so the run can resume safely after failures:

```yaml
playlist_url: https://www.youtube.com/playlist?list=WL
created_at: "<ISO-8601>"
videos:
  - index: 1
    video_id: "<id>"
    title: "<title>"
    channel: "<channel>"
    youtube_url: "https://www.youtube.com/watch?v=<id>"
    transcript_file: "transcripts/<id>.txt"
    transcript_status: ready
    summary_file: "summaries/<id>.md"
    summary_status: ready
    gist_id: "<gist-id>"
    gist_url: "https://gist.github.com/<owner>/<gist-id>"
    gists_sh_url: "https://gists.sh/<owner>/<gist-id>"
    gist_public: false
```

This manifest is an implementation aid, not a user-facing deliverable. Do not store credentials or raw cookies in it.

## Common Pitfalls

1. Assuming a fresh headless browser is logged in. Use the user's logged-in browser/session where available; otherwise ask for an authenticated session.
2. Hard-coding a browser tool. The workflow should work with any browser-control surface that can navigate, scroll, inspect DOM, and verify state.
3. Using `gh gist create --public` by accident. Public gists are wrong for this task.
4. Depending on another transcript skill. This skill must remain self-contained enough to fetch transcripts directly.
5. Dropping unavailable/private videos from the report. Keep playlist order and report concise failure reasons.
6. Creating duplicate gists after a retry. If a manifest from the same run exists, reuse recorded verified gist IDs rather than creating new ones.
7. Logging too much. Transcripts can be long and may contain sensitive user-watch context; keep logs minimal.

## Verification Checklist

- [ ] The browser is authenticated to YouTube and `https://www.youtube.com/playlist?list=WL` loads the user's Watch Later playlist.
- [ ] Scrolling reached the end and extracted videos are de-duplicated by `video_id`.
- [ ] First and last extracted playlist items were spot-checked against the browser.
- [ ] Every available video has either a transcript-backed English summary or a concise failure reason.
- [ ] Exactly one secret gist was created or reused for each ready summary.
- [ ] `gh api gists/<gist-id>` confirms `public:false` for every reported gist.
- [ ] Final output includes channel, title, `gists.sh` summary link or failure reason, and YouTube URL for every playlist item.

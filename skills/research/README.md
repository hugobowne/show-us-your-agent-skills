# research

A conversational research orchestrator that builds, extends, and queries a
persistent, LLM-curated wiki over your own knowledge base — your "Second
Brain" — so research compounds across sessions instead of being thrown away
after a single answer.

## who showed it

Paul Iusztin, on Episode 3 of *Show Us Your Agent Skills*.
[Watch the episode](https://youtube.com/live/ud2WzkKeDZs)

## what it does

One skill is the entry point for every research interaction. It first
classifies intent, then routes between four modes:

- **query** — read-only Q&A against research you already have, with optional
  save-back of the answer.
- **init** — first-time ingest of a brand-new topic, running the full pipeline.
- **append-deep** — add more sources to an existing topic via a few short
  research rounds, deduplicating against what's already there.
- **append-trusted** — add a single user-vouched file/URL/PDF to an existing
  topic, skipping the research rounds entirely.

It mines a personal knowledge base — an Obsidian vault, Readwise highlights,
NotebookLM collections, GitHub repos, web seeds (crawled with the Bright Data
CLI), and dropped PDFs — and maintains an **LLM-curated wiki layer**:
per-source pages, entities, concepts, comparisons, an overview, a synthesis,
open questions, and contradictions.

The output is a self-contained research directory with three layers:

- `index.yaml` / `index.md` — the canonical catalog (YAML) plus an
  Obsidian-readable view (MD).
- `wiki/` — the synthesis layer future agents read to understand a topic.
- `raw/` — immutable copies of the underlying sources.

Future agents read only the index to learn what exists, then drill into the
wiki and raw layers selectively. The full data contract lives in
[`CONVENTIONS.md`](CONVENTIONS.md).

The orchestrator coordinates a set of subagents (in [`agents/`](agents)):
`researcher`, `reranker`, `builder`, `source_writer`, `comparison_writer`,
`gap_analyzer`, `github_spec_writer`, `wiki_page_writer`, and
`wiki_summary_writer`. Supporting Python lives in [`scripts/`](scripts) —
index building, finding deduplication, asset download, PDF extraction, and
GitHub clone/parse helpers.

## why it's notable

- **It compounds.** The artifact is a durable, growing wiki, not a one-shot
  answer. Each run deduplicates against and extends what came before.
- **Read before write.** When intent is ambiguous it defaults to *query*, not
  ingest, because a wrong ingest is destructive (it can overwrite raw sources).
  Ingest has to be opted into with an explicit verb or a file drop.
- **Sources you trust.** It pulls from your own curated knowledge base —
  Obsidian, Readwise, NotebookLM — not just the open web, and preserves
  user-curated highlights as a distinct layer that is never LLM-synthesized.
- **Synthesis with provenance.** The wiki tracks contradictions and open
  questions explicitly, and every wiki page links back to the immutable raw
  source it was built from.

## status

Contributed by Paul Iusztin from his own setup. The skill assumes Paul's
Second Brain stack — an Obsidian PARA vault, Readwise, NotebookLM, the Bright
Data CLI, and the matching `obsidian` / `readwise` / `nlm` / `brightdata`
CLIs. The research method carries over to any setup; on a different stack
you'd adapt the vault folder names, source tools, and CLI commands to what you
actually use. Editorial writeup and stream timestamps to follow.

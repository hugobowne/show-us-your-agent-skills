# wikipedia-discovery

A Wikipedia environment skill from John Berryman's Rook setup.

## what it does

This version is no longer a lightweight demo wrapper. It is the actual skill content from John's `environment-repository/web/wikipedia/wikipedia-discovery` folder, adapted here in place.

It is designed for a split-pane Wikipedia environment where an agent can:

- find articles from a topic or phrase
- help a user learn by steering them toward relevant article titles and sections
- use Wikimedia REST and Action APIs with proper paging
- explore outward from a current article via summaries, links, backlinks, categories, and random pages
- send `message_parent` events with `url_change` so the mirrored Wikipedia pane navigates to a full article URL or a same-page `#fragment`

## files

- `SKILL.md` — the main behavior and routing instructions
- `references/topic-search.md` — topic/phrase → article discovery details
- `references/article-next-steps.md` — exploration from a known article

## compatibility

The skill assumes calls go to the active wiki host, such as `en.wikipedia.org`, and that the localhost panel handles `postMessage` payloads for the `message_parent` tool with type `url_change`.

## note

This README now describes the current contents of this directory directly, rather than the earlier reconstructed show-notes wrapper.

# wikipedia-discovery

A Wikipedia environment skill for finding articles, surfacing relevant evidence, and navigating a mirrored Wikipedia pane.

## what it does

This skill is for Wikipedia discovery and navigation in a split-pane environment.

It helps an agent:

- find articles from a topic or phrase
- guide a user toward relevant article titles and sections when they want to learn about something
- use Wikimedia REST and Action APIs with proper paging
- explore outward from a current article using summaries, links, backlinks, categories, and random pages
- send `message_parent` events with `url_change` so the mirrored Wikipedia pane navigates to a full article URL or a same-page `#fragment`

## files

- `SKILL.md` — main behavior and navigation rules
- `references/topic-search.md` — topic/phrase → article discovery details
- `references/article-next-steps.md` — exploration from a known article

## compatibility

The skill assumes calls go to the active wiki host, such as `en.wikipedia.org`, and that the localhost panel handles `postMessage` payloads for the `message_parent` tool with type `url_change`.

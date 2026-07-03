---
name: formatting-notion-pages
description: Apply rich formatting to Notion pages - toggles, callouts, headers, and styled text. Use when creating or formatting Notion documents via the Notion MCP server.
---

# Formatting Notion pages

Reference guide for creating and formatting Notion pages with rich block types and text styling via the Notion MCP.

## When to use this skill

- User asks to create a Notion page with formatting
- User wants to format or restructure an existing Notion page
- User wants to convert plain text or markdown into Notion content

## Contents

- [Block types](#block-types) - Quick reference for all block types
- [Rich text formatting](#rich-text-formatting) - Annotations, colors, links, mentions
- [MCP tool usage](#mcp-tool-usage) - How to use the Notion MCP tools
- [API constraints](#api-constraints) - Limits and restrictions

For detailed JSON examples of all block types, see [blocks-reference.md](blocks-reference.md).

## Block types

### Text blocks

| Type | Key Properties |
|------|----------------|
| `paragraph` | `rich_text`, `color` |
| `heading_1`, `heading_2`, `heading_3` | `rich_text`, `is_toggleable`, `color` |
| `toggle` | `rich_text`, `color`, `children` |
| `quote` | `rich_text`, `color` |
| `callout` | `rich_text`, `icon`, `color` |
| `code` | `rich_text`, `language`, `caption` |

**Callout icons**: `{ "type": "emoji", "emoji": "💡" }` or `{ "type": "external", "external": { "url": "..." } }`

**Code languages**: `javascript`, `python`, `typescript`, `bash`, `json`, `html`, `css`, `sql`, `markdown`, `yaml`, and [60+ more](blocks-reference.md#code).

### List blocks

| Type | Key Properties |
|------|----------------|
| `bulleted_list_item` | `rich_text`, `color`, `children` |
| `numbered_list_item` | `rich_text`, `color`, `children` |
| `to_do` | `rich_text`, `checked`, `color` |

### Table blocks

```json
{
  "type": "table",
  "table": {
    "table_width": 3,
    "has_column_header": true,
    "has_row_header": false,
    "children": [/* table_row blocks */]
  }
}
```

Each `table_row` has `cells` - an array of rich_text arrays.

### Layout blocks

| Type | Key Properties |
|------|----------------|
| `column_list` | `children` (array of `column` blocks) |
| `column` | `children` (any blocks) |
| `divider` | (empty object) |
| `table_of_contents` | `color` |
| `breadcrumb` | (empty object) |

### Media blocks

| Type | Key Properties |
|------|----------------|
| `image` | `type: "external"`, `external.url`, `caption` |
| `video` | `type: "external"`, `external.url`, `caption` |
| `pdf` | `type: "external"`, `external.url`, `caption` |
| `file` | `type: "external"`, `external.url`, `caption`, `name` |
| `bookmark` | `url`, `caption` |
| `embed` | `url`, `caption` |

### Advanced blocks

| Type | Key Properties |
|------|----------------|
| `equation` | `expression` (LaTeX) |
| `synced_block` | `synced_from`, `children` |
| `template` | `rich_text`, `children` |
| `link_to_page` | `type: "page_id"`, `page_id` |
| `child_page` | `title` |
| `child_database` | `title` |

## Rich text formatting

### Text object structure

```json
{
  "type": "text",
  "text": {
    "content": "styled text",
    "link": null
  },
  "annotations": {
    "bold": false,
    "italic": false,
    "strikethrough": false,
    "underline": false,
    "code": false,
    "color": "default"
  }
}
```

### Annotations

| Property | Type | Description |
|----------|------|-------------|
| `bold` | boolean | Bold text |
| `italic` | boolean | Italic text |
| `strikethrough` | boolean | Strikethrough text |
| `underline` | boolean | Underlined text |
| `code` | boolean | Inline code style |
| `color` | string | Text or background color |

### Colors

**Text colors:** `default`, `gray`, `brown`, `orange`, `yellow`, `green`, `blue`, `purple`, `pink`, `red`

**Background colors:** `gray_background`, `brown_background`, `orange_background`, `yellow_background`, `green_background`, `blue_background`, `purple_background`, `pink_background`, `red_background`

### Links

```json
{
  "type": "text",
  "text": {
    "content": "Click here",
    "link": { "url": "https://example.com" }
  }
}
```

### Mentions

**Page mention:**
```json
{
  "type": "mention",
  "mention": {
    "type": "page",
    "page": { "id": "page-uuid" }
  }
}
```

**Database mention:**
```json
{
  "type": "mention",
  "mention": {
    "type": "database",
    "database": { "id": "database-uuid" }
  }
}
```

**User mention:**
```json
{
  "type": "mention",
  "mention": {
    "type": "user",
    "user": { "id": "user-uuid" }
  }
}
```

**Date mention:**
```json
{
  "type": "mention",
  "mention": {
    "type": "date",
    "date": {
      "start": "2026-01-11",
      "end": null,
      "time_zone": null
    }
  }
}
```

**Link preview:**
```json
{
  "type": "mention",
  "mention": {
    "type": "link_preview",
    "link_preview": { "url": "https://example.com" }
  }
}
```

### Inline equation

```json
{
  "type": "equation",
  "equation": {
    "expression": "x^2 + y^2 = z^2"
  }
}
```

### Mixed formatting example

Paragraph with multiple styles:
```json
{
  "object": "block",
  "type": "paragraph",
  "paragraph": {
    "rich_text": [
      { "type": "text", "text": { "content": "This is " } },
      {
        "type": "text",
        "text": { "content": "bold" },
        "annotations": { "bold": true }
      },
      { "type": "text", "text": { "content": " and " } },
      {
        "type": "text",
        "text": { "content": "highlighted" },
        "annotations": { "color": "yellow_background" }
      },
      { "type": "text", "text": { "content": " text." } }
    ]
  }
}
```

## MCP tool usage

### Fetch existing page

```
mcp__notion-personal__notion-fetch
id: "page-uuid-or-url"
```

### Create page with content

```
mcp__notion-personal__notion-create-pages
```

Request body:
```json
{
  "parent": { "page_id": "parent-page-uuid" },
  "properties": {
    "title": [{ "text": { "content": "Page Title" } }]
  },
  "children": [
    // Block objects
  ]
}
```

For database parent:
```json
{
  "parent": { "database_id": "database-uuid" },
  "properties": {
    "Name": {
      "title": [{ "text": { "content": "Page Title" } }]
    }
    // Other database properties
  },
  "children": []
}
```

### Update page properties

```
mcp__notion-personal__notion-update-page
```

Note: To add blocks to an existing page, you need the block append endpoint which may require direct API access.

## API constraints

- Maximum 100 blocks per request
- Nested blocks limited to 2 levels via API
- Some block types (synced blocks, databases) have additional restrictions
- Rich text arrays have a maximum of 100 elements
- Text content limited to 2000 characters per rich text object

---
name: resend-email
description: Send emails via Resend.com API. Use when the user wants to (1) send an email, (2) email someone, (3) send a message to an email address, (4) send email with attachments, (5) schedule an email for later. Requires RESEND_API_KEY environment variable.
---

# Resend Email

Send emails using the [resend-cli](https://github.com/resend/resend-cli). The CLI authenticates via `RESEND_API_KEY` environment variable.

## Sending Email

```bash
resend emails send --json \
  --from "Claude <claude@ehop.me>" \
  --to user@example.com \
  --subject "Hello" \
  --text "Email body here"
```

Always pass `--json` to get machine-readable output.

### Required Flags

| Flag | Description |
|------|-------------|
| `--from` | Sender address (default to `Claude <claude@ehop.me>`) |
| `--to` | Recipient address(es), repeat flag for multiple |
| `--subject` | Email subject line |
| `--text` or `--html` or `--html-file` | Body content (exactly one required) |

### Optional Flags

| Flag | Description |
|------|-------------|
| `--html` | HTML body as string |
| `--html-file` | Path to an HTML file for the body |
| `--text` | Plain text body |
| `--cc` | CC recipient(s), repeat flag for multiple |
| `--bcc` | BCC recipient(s), repeat flag for multiple |
| `--reply-to` | Reply-to address |
| `--attachment` | File path(s) to attach, repeat flag for multiple |
| `--scheduled-at` | Schedule delivery (ISO 8601, e.g. `2024-12-25T09:00:00Z`) |
| `--headers` | Custom headers as `key=value` pairs |
| `--tags` | Email tags as `name=value` pairs |

### Examples

**Simple text email:**
```bash
resend emails send --json \
  --from "Claude <claude@ehop.me>" \
  --to user@example.com \
  --subject "Quick update" \
  --text "Just a quick note."
```

**HTML email:**
```bash
resend emails send --json \
  --from "Newsletter <news@ehop.me>" \
  --to user@example.com \
  --subject "Newsletter" \
  --html "<h1>Hello</h1><p>Welcome to our newsletter.</p>"
```

**With attachments:**
```bash
resend emails send --json \
  --from "Claude <claude@ehop.me>" \
  --to user@example.com \
  --subject "Report attached" \
  --text "Please find the report attached." \
  --attachment /path/to/report.pdf \
  --attachment /path/to/data.csv
```

**Multiple recipients with CC:**
```bash
resend emails send --json \
  --from "Claude <claude@ehop.me>" \
  --to alice@example.com \
  --to bob@example.com \
  --cc manager@example.com \
  --subject "Team update" \
  --text "Hi team..."
```

**Scheduled email:**
```bash
resend emails send --json \
  --from "Claude <claude@ehop.me>" \
  --to user@example.com \
  --subject "Reminder" \
  --text "Don't forget!" \
  --scheduled-at "2024-12-25T09:00:00Z"
```

**HTML from file:**
```bash
resend emails send --json \
  --from "Claude <claude@ehop.me>" \
  --to user@example.com \
  --subject "Report" \
  --html-file ./email.html
```

### Output

Success returns JSON with email ID:
```json
{"id": "49a3999c-0ce1-4ea6-ab68-afcd6dc2e794"}
```

Errors exit with code 1 and return:
```json
{"error": {"message": "...", "code": "..."}}
```

## Limits

- Sender domain must be verified in Resend dashboard
- Max 50 recipients per email
- Max 40MB total size including attachments

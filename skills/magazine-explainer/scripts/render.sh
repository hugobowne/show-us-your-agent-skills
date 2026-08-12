#!/usr/bin/env bash
# Render an HTML file to PDF with headless Chrome.
# Usage: render.sh <input.html> <output.pdf>
# Waits for web fonts + remote images via --virtual-time-budget.
set -euo pipefail

HTML="${1:?usage: render.sh input.html output.pdf}"
OUT="${2:?usage: render.sh input.html output.pdf}"

CHROME="${CHROME:-}"
if [ -z "$CHROME" ]; then
  for c in \
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
    "/Applications/Chromium.app/Contents/MacOS/Chromium" \
    "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser" \
    "$(command -v google-chrome 2>/dev/null || true)" \
    "$(command -v chromium 2>/dev/null || true)"; do
    if [ -n "$c" ] && [ -x "$c" ]; then CHROME="$c"; break; fi
  done
fi
[ -z "$CHROME" ] && { echo "ERROR: Chrome/Chromium not found. Set CHROME=/path/to/binary." >&2; exit 1; }

ABS="$(cd "$(dirname "$HTML")" && pwd)/$(basename "$HTML")"

"$CHROME" --headless --disable-gpu --no-pdf-header-footer \
  --virtual-time-budget=12000 --run-all-compositor-stages-before-draw \
  --print-to-pdf="$OUT" "file://$ABS" >/dev/null 2>&1 || true

[ -f "$OUT" ] || { echo "ERROR: render produced no file." >&2; exit 1; }

PAGES="$(python3 -c "import pypdf,sys;print(len(pypdf.PdfReader(sys.argv[1]).pages))" "$OUT" 2>/dev/null \
  || uvx --quiet --from pypdf python -c "import pypdf,sys;print(len(pypdf.PdfReader(sys.argv[1]).pages))" "$OUT" 2>/dev/null \
  || echo "?")"

echo "wrote $OUT — ${PAGES} pages, $(du -h "$OUT" | cut -f1)"

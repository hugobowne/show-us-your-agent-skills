#!/usr/bin/env bash
# Flatten a PDF to a print-safe, image-only PDF (defeats printer-RIP font hangs).
# Usage: printable.sh <input.pdf> <output.pdf> [dpi]
set -euo pipefail
IN="${1:?usage: printable.sh input.pdf output.pdf [dpi]}"
OUT="${2:?usage: printable.sh input.pdf output.pdf [dpi]}"
DPI="${3:-200}"
DIR="$(cd "$(dirname "$0")" && pwd)"

if ! command -v pdftoppm >/dev/null 2>&1; then
  echo "ERROR: pdftoppm not found (install poppler: brew install poppler)." >&2
  exit 1
fi

if python3 -c "import PIL" >/dev/null 2>&1; then
  python3 "$DIR/make_printable.py" "$IN" "$OUT" "$DPI"
else
  uvx --quiet --from pillow python "$DIR/make_printable.py" "$IN" "$OUT" "$DPI"
fi

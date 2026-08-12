#!/usr/bin/env bash
# Impose a reading-order PDF into a saddle-stitch booklet for duplex printing.
# Usage: booklet.sh <reading.pdf> <output-booklet.pdf>
set -euo pipefail
IN="${1:?usage: booklet.sh reading.pdf output-booklet.pdf}"
OUT="${2:?usage: booklet.sh reading.pdf output-booklet.pdf}"
DIR="$(cd "$(dirname "$0")" && pwd)"

if python3 -c "import pypdf" >/dev/null 2>&1; then
  python3 "$DIR/make_booklet.py" "$IN" "$OUT"
else
  uvx --quiet --from pypdf python "$DIR/make_booklet.py" "$IN" "$OUT"
fi

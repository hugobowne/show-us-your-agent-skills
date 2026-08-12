#!/usr/bin/env bash
# Print the flattened booklet to a duplex printer with fold-booklet settings.
# Usage: print_booklet.sh <Name-booklet-print.pdf> [printer-name]
# Defaults to the system default printer. Always print the *-booklet-print.pdf
# (flattened) file, not the vector one — the vector file can hang the RIP.
set -euo pipefail
PDF="${1:?usage: print_booklet.sh Name-booklet-print.pdf [printer-name]}"
PRINTER="${2:-}"

# short-edge binding is the right flip for these landscape-imposed booklet sheets
# on most printers; if the back pages come out flipped, rerun with long-edge.
ARGS=(-o sides=two-sided-short-edge -o media=Letter -o collate=true)

if [ -n "$PRINTER" ]; then
  lp -d "$PRINTER" "${ARGS[@]}" "$PDF"
else
  lp "${ARGS[@]}" "$PDF"   # system default destination
fi

cat <<'EOF'

Sent (duplex, short-edge binding, Letter).
Next: stack the sheets in order, fold the whole stack in half down the middle,
nest, and staple the spine -> a pocket magazine that reads 1, 2, 3...

If the back pages come out upside-down or mispaired, the flip edge was wrong for
this printer — reprint with: -o sides=two-sided-long-edge
EOF

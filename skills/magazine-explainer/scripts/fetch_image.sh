#!/usr/bin/env bash
# Download an image for embedding. Sends a browser UA + referer so picky CDNs serve it.
# Usage: fetch_image.sh <image-url> <output-path>
# Prints: <path> <mime-type> <size>.  ALWAYS open the file with Read to confirm it's
# the right subject (and not a logo, watermark, or 404 page) before using it.
set -euo pipefail

URL="${1:?usage: fetch_image.sh URL output-path}"
OUT="${2:?usage: fetch_image.sh URL output-path}"
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36"

mkdir -p "$(dirname "$OUT")"
curl -fsSL -A "$UA" -e "https://www.bing.com/" "$URL" -o "$OUT"

MIME="$(file -b --mime-type "$OUT")"
case "$MIME" in
  image/*) : ;;
  *) echo "WARNING: $OUT is $MIME, not an image — discard it." >&2 ;;
esac
echo "$OUT $MIME $(du -h "$OUT" | cut -f1)"

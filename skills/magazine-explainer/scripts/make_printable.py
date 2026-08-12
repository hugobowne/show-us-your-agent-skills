#!/usr/bin/env python3
"""Flatten a PDF into a print-safe, image-only PDF.

Some printer RIPs choke on the fonts Chrome embeds — especially color/bitmap
emoji glyphs (⚙ ⚡ 🔥) and subsetted symbol fonts — and hang mid-job. A vector
re-distill (Ghostscript pdfwrite) keeps the bad glyphs and hangs the same way.
Rasterizing every page to a bitmap removes all fonts and vectors, so the printer
just sees flat images and always prints. 200 DPI is sharp enough for paper.

Renders with pdftoppm (its own engine — doesn't hang on the glyphs GS chokes on),
then reassembles with Pillow at the right physical page size.

Usage: make_printable.py input.pdf output.pdf [dpi]
"""
import sys, os, glob, tempfile, subprocess
from PIL import Image


def main():
    if len(sys.argv) < 3:
        sys.exit("usage: make_printable.py input.pdf output.pdf [dpi]")
    inp, outp = sys.argv[1], sys.argv[2]
    dpi = int(sys.argv[3]) if len(sys.argv) > 3 else 200

    with tempfile.TemporaryDirectory() as td:
        pre = os.path.join(td, "page")
        subprocess.run(["pdftoppm", "-r", str(dpi), "-png", inp, pre], check=True)
        files = glob.glob(pre + "*.png")
        if not files:
            sys.exit("pdftoppm produced no pages")
        # Sort by the page number in the filename (handles 1..10 ordering).
        files.sort(key=lambda f: int("".join(c for c in os.path.basename(f) if c.isdigit())))
        imgs = [Image.open(f).convert("RGB") for f in files]
        imgs[0].save(outp, "PDF", resolution=float(dpi),
                     save_all=True, append_images=imgs[1:])

    print(f"wrote {outp} — {len(files)} pages rasterized at {dpi} DPI "
          f"(image-only, print-safe)")


if __name__ == "__main__":
    main()

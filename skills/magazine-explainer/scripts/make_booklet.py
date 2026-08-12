#!/usr/bin/env python3
"""Impose a sequential PDF into a saddle-stitch booklet for duplex printing.

Places two source pages per landscape sheet in fold order and pads the page
count to a multiple of 4. Print double-sided, fold the stack in half, staple
the spine — the pages then read 1, 2, 3, ... like a little magazine.

Usage: make_booklet.py input.pdf output.pdf
"""
import sys
from pypdf import PdfReader, PdfWriter, PageObject, Transformation


def main():
    if len(sys.argv) != 3:
        sys.exit("usage: make_booklet.py input.pdf output.pdf")
    inp, outp = sys.argv[1], sys.argv[2]

    reader = PdfReader(inp)
    pages = list(reader.pages)
    n = len(pages)
    if n == 0:
        sys.exit("input PDF has no pages")

    # Pad to a multiple of 4 with blank pages (a booklet needs 4-page sheets).
    pad = (-n) % 4
    seq = pages + [None] * pad
    N = len(seq)

    # Saddle-stitch order: each consecutive pair is one printed side, 2-up.
    # For 8 pages this yields (8,1)(2,7)(6,3)(4,5).
    order = []
    lo, hi = 0, N - 1
    while lo < hi:
        order += [seq[hi], seq[lo], seq[lo + 1], seq[hi - 1]]
        lo += 2
        hi -= 2

    # Landscape sheet = the input paper rotated; each source page fills one half.
    ref = pages[0]
    pw, ph = float(ref.mediabox.width), float(ref.mediabox.height)
    # Sheet holds two source pages side by side at native size (no shrinking):
    # digest 396x612 -> 792x612 (landscape Letter); Letter 612x792 -> 1224x792 (Tabloid).
    sheet_w, sheet_h = 2 * pw, ph
    half_w = sheet_w / 2

    writer = PdfWriter()
    for i in range(0, len(order), 2):
        sheet = PageObject.create_blank_page(width=sheet_w, height=sheet_h)
        for slot, src in ((0, order[i]), (1, order[i + 1])):
            if src is None:
                continue
            sw, sh = float(src.mediabox.width), float(src.mediabox.height)
            s = min(half_w / sw, sheet_h / sh)          # contain within the half
            tx = slot * half_w + (half_w - sw * s) / 2  # center horizontally
            ty = (sheet_h - sh * s) / 2                 # center vertically
            sheet.merge_transformed_page(
                src, Transformation().scale(s).translate(tx, ty))
        writer.add_page(sheet)

    with open(outp, "wb") as f:
        writer.write(f)

    print(f"wrote {outp} — {len(writer.pages)} landscape sheet-sides "
          f"from {n} pages (+{pad} blank). Print double-sided, fold, staple.")


if __name__ == "__main__":
    main()

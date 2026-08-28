#!/usr/bin/env python3
"""Fail if a logo's azure has drifted from the design system's accent token.

    uv run --with pillow python scripts/check-azure.py

The brand had FOUR azures, not two. Eight files carried #07a6fc, but
email/STATELOOP_on_white@1x.png was #07afff, workspace/STATELOOP_on_white.png
was #0ba6fb and workspace/STATELOOP_transparent_ink.png was #07a2f7 -- so the
@1x and @2x halves of the SAME email signature rendered different blues. There
was no single "raster azure" to defend against the token; there were four.

The token won: it is the one that can flip between themes, and it is what
var(--color-accent) already resolves to everywhere in CSS. Nothing in any
codebase referenced the raster value in text -- it lived only in pixels.

Checked here rather than assumed because there is NO VECTOR SOURCE for the
wordmark (coord-jtre), so these rasters are the masters. A master that drifts
has nothing to be regenerated from.

The dominant saturated blue is what is compared -- not every pixel -- because
antialiased edges are legitimately blends between the azure and whatever it
sits on.
"""
import sys
from collections import Counter
from pathlib import Path

from PIL import Image

TARGET = (0, 164, 245)          # #00a4f5 == var(--color-accent) in sRGB
ROOT = Path(__file__).resolve().parent.parent


def dominant_azure(path):
    im = Image.open(path).convert("RGBA")
    raw = im.tobytes()
    blues = [(raw[i], raw[i + 1], raw[i + 2]) for i in range(0, len(raw), 4)
             if raw[i + 3] > 200 and raw[i + 2] > 120 and raw[i + 2] - raw[i] > 40]
    return Counter(blues).most_common(1)[0][0] if blues else None


def main() -> int:
    bad, checked = [], 0
    for p in sorted((ROOT / "logos").rglob("*.png")):
        d = dominant_azure(p)
        if d is None:
            continue
        checked += 1
        if d != TARGET:
            bad.append((p.relative_to(ROOT), "#%02x%02x%02x" % d))
    for rel, hexv in bad:
        print(f"  x {str(rel):52} {hexv}, expected #00a4f5")
    if bad:
        print(f"  {len(bad)} of {checked} logo(s) carry an off-token azure")
        return 1
    print(f"  + all {checked} logo(s) carry the token azure #00a4f5")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

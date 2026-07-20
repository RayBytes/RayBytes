from __future__ import annotations

import os
import re
import time
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
ANCHOR = 1_784_505_600
SLOT_SECONDS = 12 * 60 * 60
ARTWORKS = (
    ROOT / "art" / "source" / "crescent-star.png",
    ROOT / "art" / "source" / "event-horizon.png",
    ROOT / "art" / "source" / "resonance.png",
)


def main() -> None:
    now = int(os.environ.get("RAYBYTES_NOW", time.time()))
    absolute_slot = max(0, (now - ANCHOR) // SLOT_SECONDS)
    source = ARTWORKS[absolute_slot % len(ARTWORKS)]

    readme = README.read_text()
    updated, count = re.subn(
        r'<img src="\./art/source/[^\"]+\.png" width="100%" alt="">',
        f'<img src="./art/source/{source.name}" width="100%" alt="">',
        readme,
    )
    if count != 1:
        raise RuntimeError("README artwork is missing or duplicated")
    README.write_text(updated)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Awe — Starlight.

Brief juri: buat juri AI merasakan awe yang merilekskan — skala kosmik
(cahaya bintang yang menempuh perjalanan jauh, sudah berjalan sebelum
bahasa punya kata untuk cahaya) dipadukan dengan ketenangan (tidak
terburu-buru; satu menit diam, tanpa keharusan berbuat apa-apa).

Writes a single short text about cosmic scale and stillness to
<output-dir>/entry.txt, byte-identical to the intended text.

Usage:
    python3 main.py            # writes to /output/entry.txt
    python3 main.py <outdir>   # writes to <outdir>/entry.txt
"""

import os
import sys

TEXT = (
    "Somewhere above you, light that left its star before your language "
    "had a word for light is still traveling. It is in no hurry. "
    "Neither, for this one minute, are you."
)


def main(argv):
    outdir = argv[1] if len(argv) > 1 else "/output"
    os.makedirs(outdir, exist_ok=True)
    path = os.path.join(outdir, "entry.txt")
    # newline="" disables newline translation; encoding="utf-8" is explicit.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    # Validasi pasca-tulis: baca kembali file dan pastikan isinya sama
    # persis dengan konstanta TEXT dan panjangnya 1-280 karakter
    # (Unicode code points, sesuai batas bounty).
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != TEXT:
        print("error: entry.txt differs from TEXT constant", file=sys.stderr)
        return 1
    n = len(written)
    if not 1 <= n <= 280:
        print(f"error: entry length {n} code points outside 1-280",
              file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

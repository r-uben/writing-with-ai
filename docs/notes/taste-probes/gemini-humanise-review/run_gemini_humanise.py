#!/usr/bin/env python3
"""Independent Gemini 3.1 Pro humanise review for P7 revise paragraphs.

Requires: GEMINI_API_KEY (or GOOGLE_API_KEY) in the environment.
Model: gemini-3.1-pro-preview

Usage:
  uv run --with google-genai python docs/notes/taste-probes/gemini-humanise-review/run_gemini_humanise.py
  # or single file:
  uv run --with google-genai python .../run_gemini_humanise.py --only case03-ff-primary
"""

from __future__ import annotations

import argparse
import os
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PARAS = ROOT / "paragraphs"
OUT = ROOT / "out"
PROMPT = (ROOT / "PROMPT.md").read_text()
MODEL = os.environ.get("GEMINI_HUMANISE_MODEL", "gemini-3.1-pro-preview")


def client():
    key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not key:
        print(
            "ERROR: set GEMINI_API_KEY or GOOGLE_API_KEY to call Gemini 3.1 Pro.\n"
            "This host has no agy/Gemini credentials.",
            file=sys.stderr,
        )
        sys.exit(2)
    from google import genai

    return genai.Client(api_key=key)


def review_one(c, path: Path) -> str:
    body = path.read_text()
    prompt = (
        PROMPT.replace("@PARAGRAPH_FILE", path.name)
        + "\n\n---\nFILE CONTENTS:\n\n"
        + body
    )
    resp = c.models.generate_content(model=MODEL, contents=prompt)
    text = getattr(resp, "text", None) or str(resp)
    return text.strip() + "\n"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", help="stem of paragraph file, e.g. case03-ff-primary")
    ap.add_argument("--sleep", type=float, default=1.0, help="pause between calls")
    args = ap.parse_args()

    OUT.mkdir(parents=True, exist_ok=True)
    files = sorted(PARAS.glob("*.md"))
    if args.only:
        files = [p for p in files if p.stem == args.only]
        if not files:
            sys.exit(f"no paragraph matching --only {args.only}")

    c = client()
    summary_lines = [f"# Gemini humanise reviews ({MODEL})", ""]
    for path in files:
        print(f"reviewing {path.name} …", flush=True)
        try:
            text = review_one(c, path)
        except Exception as e:
            text = f"ERROR: {e}\n"
            print(text, file=sys.stderr)
        out_path = OUT / f"{path.stem}.gemini.md"
        header = (
            f"# Independent review — {path.stem}\n\n"
            f"**Model:** `{MODEL}`\n"
            f"**Brief:** humanise toward attested econ register (see PROMPT.md)\n"
            f"**Origin of text:** AI-generated P7 revise (not human prose)\n\n"
            f"---\n\n"
        )
        out_path.write_text(header + text)
        summary_lines.append(f"- [{path.stem}]({out_path.name})")
        time.sleep(args.sleep)

    (OUT / "INDEX.md").write_text("\n".join(summary_lines) + "\n")
    print(f"wrote {len(files)} reviews under {OUT}")


if __name__ == "__main__":
    main()

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from writing_audit.metrics import compute_metrics
from writing_audit.track_p import run_track_p


def metrics_main() -> None:
    parser = argparse.ArgumentParser(description="Layer-1 linguistic metrics for audit fixtures")
    parser.add_argument("path", type=Path, help="Fixture or prose file")
    args = parser.parse_args()
    if not args.path.is_file():
        print(f"File not found: {args.path}", file=sys.stderr)
        raise SystemExit(1)
    print(compute_metrics(args.path).format())


def track_p_main() -> None:
    parser = argparse.ArgumentParser(
        description="Track P Pangram-evasion harness (research only — does not ship to skill/)"
    )
    parser.add_argument("input", type=Path, help="Track Q draft fixture (.md)")
    parser.add_argument("--rounds", type=int, default=2, help="Pipeline rounds (default: 2)")
    parser.add_argument(
        "--reviser",
        default="claude",
        choices=("claude", "codex", "agy"),
        help="External CLI agent for rewrite stages",
    )
    args = parser.parse_args()
    run_track_p(args.input, rounds=args.rounds, reviser=args.reviser)

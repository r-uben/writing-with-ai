from __future__ import annotations

import argparse
import sys
from pathlib import Path

from writing_audit.metrics import compute_metrics
from writing_audit.track_p import run_track_p
from writing_audit.track_r import run_track_r


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


def track_r_main() -> None:
    parser = argparse.ArgumentParser(
        description="Track R red-team BOUNDARY-MAPPING harness (research only; "
        "does not ship to skill/). Emits one independently-scoreable cell per "
        "single-lever perturbation for the ablation — NOT a laundering pipeline."
    )
    parser.add_argument("input", type=Path, help="Base draft fixture (.md)")
    parser.add_argument(
        "--reviser",
        default="claude",
        choices=("claude", "codex", "agy"),
        help="External CLI agent for perturbation levers",
    )
    parser.add_argument(
        "--levers",
        default=None,
        help="Comma-separated subset of lever ids (default: all). "
        "e.g. L0-identity,L1-detell",
    )
    args = parser.parse_args()
    lever_list = args.levers.split(",") if args.levers else None
    if not args.input.is_file():
        print(f"File not found: {args.input}", file=sys.stderr)
        raise SystemExit(1)
    run_track_r(args.input, reviser=args.reviser, levers=lever_list)

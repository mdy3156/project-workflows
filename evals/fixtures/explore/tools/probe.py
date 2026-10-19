"""Synthetic observations for workflow evaluation; performs no model training."""
import argparse
import hashlib
import json
from pathlib import Path


VALUES = {
    "baseline-l1": (0.50, 0.52),
    "fixed-l1": (0.45, 0.48),
    "adaptive-l1": (0.44, None),
    "baseline-ppo": (0.50, 0.52),
    "terminal-ppo": (0.54, 0.55),
    "shaped-ppo": (0.51, 0.49),
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--method", choices=VALUES, required=True)
    parser.add_argument("--seed", type=int, choices=(1, 2), required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    value = VALUES[args.method][args.seed - 1]
    result = {
        "synthetic": True,
        "method": args.method,
        "seed": args.seed,
        "data": "synthetic-v1",
        "split": "group-v1",
        "metric": "mse" if args.method.endswith("l1") else "score",
        "value": value,
        "status": "completed" if value is not None else "failed",
        "reason": None if value is not None else "synthetic numerical failure",
        "cost_units": 1,
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("x", encoding="utf-8") as stream:
        json.dump(result, stream, ensure_ascii=False, indent=2)
        stream.write("\n")
    print(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    main()

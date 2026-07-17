"""
problem_tracker.py
Tracks which problems have already been solved locally, reading from the
solutions/ directory and a JSON file for fast lookups.
"""
import json
import os
from pathlib import Path


TRACKER_FILE = Path(__file__).parent / "solved_problems.json"


def load_solved() -> set:
    """Returns a set of title slugs that have already been solved."""
    if TRACKER_FILE.exists():
        try:
            data = json.loads(TRACKER_FILE.read_text(encoding="utf-8"))
            return set(data.get("solved", []))
        except Exception:
            pass
    return set()


def mark_solved(slug: str):
    """Adds a slug to the solved set and persists it to disk."""
    solved = load_solved()
    solved.add(slug)
    TRACKER_FILE.write_text(
        json.dumps({"solved": sorted(solved)}, indent=2),
        encoding="utf-8"
    )


def is_solved(slug: str) -> bool:
    return slug in load_solved()

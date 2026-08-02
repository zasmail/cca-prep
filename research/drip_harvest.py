#!/usr/bin/env python3
"""Drip-recover still-blocked YouTube transcripts, one every 15 min.

Resume-safe: skips any slug that already has research/transcripts/<slug>.md.
Gentle on purpose — the cloud harvest got the IP banned; this runs on a
residential connection and spaces requests far apart. One pass, then exits.
"""
import sys
import time
from pathlib import Path

OUT = Path(__file__).parent / "transcripts"
INTERVAL_S = 15 * 60

# (slug, youtube_id) — from research/manual-watch-list.md appendix
PENDING = [
    ("cwc-2025-keynote", "EvtPBaaykdo"),
    ("prompting-for-agents", "XSZP9GhhuAc"),
    ("beyond-basics-claude-code", "tuY2ChJIx48"),
    ("vibe-coding-in-prod", "fHWFF_pnqDk"),
    ("cwc-2026-tokyo-keynote", "N4efO8viXXo"),
    ("cwc-2026-london-keynote", "6amLO7I9xdg"),
    ("karpathy-how-i-use-llms", "EWvNQjAaOHw"),
    ("karpathy-deep-dive-llms", "7xTGNNLPyMI"),
    ("karpathy-state-of-gpt", "bZQun8Y4L2A"),
    ("cwc-2026-sf-keynote", "wjvESxKgqaQ"),  # subtitles disabled last check; retry last
]


def fetch(video_id: str) -> str:
    from youtube_transcript_api import YouTubeTranscriptApi

    try:  # v1.x API
        segs = YouTubeTranscriptApi().fetch(video_id)
        return " ".join(s.text for s in segs)
    except AttributeError:  # pre-1.0 API
        segs = YouTubeTranscriptApi.get_transcript(video_id)
        return " ".join(s["text"] for s in segs)


def main() -> None:
    todo = [(s, v) for s, v in PENDING if not (OUT / f"{s}.md").exists()]
    print(f"drip: {len(todo)} pending of {len(PENDING)}", flush=True)
    for i, (slug, vid) in enumerate(todo):
        try:
            text = fetch(vid)
            (OUT / f"{slug}.md").write_text(
                f"# {slug}\n\n*Source: YouTube {vid} — auto-transcript, "
                f"drip-recovered.*\n\n{text}\n"
            )
            print(f"RECOVERED {slug} ({len(text.split())} words)", flush=True)
        except Exception as e:  # noqa: BLE001 — report and move on
            print(f"FAILED {slug}: {type(e).__name__}: {e}", flush=True)
        if i < len(todo) - 1:
            time.sleep(INTERVAL_S)
    print("drip: pass complete", flush=True)


if __name__ == "__main__":
    sys.exit(main())

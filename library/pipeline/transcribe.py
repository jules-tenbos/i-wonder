#!/usr/bin/env python3
"""Transcription pipeline — transcribe MP3 files using local Whisper.

Scans the audio library for files without transcripts and transcribes them.
Saves .txt files alongside the source MP3s.

Usage:
    python transcribe.py                              # transcribe all untranscribed
    python transcribe.py --category podcasts           # specific category
    python transcribe.py --category lectures --series "Being Human - Great Courses"
    python transcribe.py --file /path/to/specific.mp3  # single file
    python transcribe.py --model small                 # higher quality model
    python transcribe.py --dry-run                     # list what would be transcribed
"""

import argparse
import datetime
import logging
import sys
import time
from pathlib import Path

from utils import load_config, scan_audio_files, find_transcript


def setup_logging(log_dir):
    """Set up logging to both console and file."""
    log_dir = Path(log_dir)
    log_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = log_dir / f"transcribe_{timestamp}.log"

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler(log_file),
        ],
    )
    return logging.getLogger(__name__)


def format_timestamp(seconds):
    """Format seconds as HH:MM:SS."""
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    return f"{h:02d}:{m:02d}:{s:02d}"


def transcribe_file(mp3_path, model, logger):
    """Transcribe a single MP3 file and save the transcript.

    Returns the output path on success, None on failure.
    """
    mp3_path = Path(mp3_path)
    output_path = mp3_path.parent / (mp3_path.stem + ".txt")

    logger.info(f"Transcribing: {mp3_path.name}")
    start = time.time()

    try:
        result = model.transcribe(
            str(mp3_path),
            verbose=False,
        )
    except Exception as e:
        logger.error(f"Failed to transcribe {mp3_path.name}: {e}")
        return None

    elapsed = time.time() - start
    logger.info(f"  Transcription took {elapsed:.1f}s")

    # Format as timestamped paragraphs
    segments = result.get("segments", [])
    lines = []
    for seg in segments:
        ts = format_timestamp(seg["start"])
        text = seg["text"].strip()
        if text:
            lines.append(f"[{ts}] {text}")

    transcript_text = "\n\n".join(lines)

    try:
        output_path.write_text(transcript_text, encoding="utf-8")
        logger.info(f"  Saved: {output_path.name} ({len(segments)} segments)")
    except Exception as e:
        logger.error(f"  Failed to save transcript: {e}")
        return None

    return output_path


def collect_files(args, config):
    """Collect MP3 files to transcribe based on CLI args."""
    audio_dir = config["audio_dir"]

    if args.file:
        mp3 = Path(args.file)
        if not mp3.exists():
            print(f"Error: file not found: {args.file}", file=sys.stderr)
            sys.exit(1)
        transcript = find_transcript(mp3)
        if transcript and not args.force:
            return []  # already transcribed
        return [mp3]

    # Scan for untranscribed files
    pending = []
    for mp3, transcript in scan_audio_files(
        audio_dir,
        category=args.category,
        subcategory=args.subcategory,
        series=args.series,
    ):
        if transcript is None or args.force:
            pending.append(mp3)

    return pending


def main():
    parser = argparse.ArgumentParser(description="Transcribe audio files using Whisper")
    parser.add_argument("--config", default=None, help="Path to config.yaml")
    parser.add_argument("--category", help="Filter by category (lectures, podcasts, ...)")
    parser.add_argument("--subcategory", help="Filter by subcategory")
    parser.add_argument("--series", help="Filter by series name (directory name)")
    parser.add_argument("--file", help="Transcribe a single file")
    parser.add_argument("--model", help="Whisper model (base, small, medium, large)")
    parser.add_argument("--force", action="store_true", help="Re-transcribe even if transcript exists")
    parser.add_argument("--dry-run", action="store_true", help="List files without transcribing")
    parser.add_argument("--limit", type=int, help="Max number of files to transcribe")
    args = parser.parse_args()

    config = load_config(args.config)
    log_dir = Path(__file__).parent / "logs"
    logger = setup_logging(log_dir)

    # Collect files to process
    pending = collect_files(args, config)

    if not pending:
        logger.info("No files to transcribe.")
        return

    if args.limit:
        pending = pending[: args.limit]

    logger.info(f"Found {len(pending)} file(s) to transcribe")

    if args.dry_run:
        for mp3 in pending:
            print(mp3)
        logger.info(f"Dry run: {len(pending)} files would be transcribed")
        return

    # Load whisper model
    try:
        import whisper
    except ImportError:
        print("Error: openai-whisper not installed. Run: pip install openai-whisper", file=sys.stderr)
        sys.exit(1)

    model_name = args.model or config.get("whisper", {}).get("model", "base")
    device = config.get("whisper", {}).get("device", "cpu")
    logger.info(f"Loading Whisper model '{model_name}' on {device}...")
    model = whisper.load_model(model_name, device=device)

    # Process files
    success = 0
    failed = 0
    total = len(pending)
    start_time = time.time()

    for i, mp3 in enumerate(pending, 1):
        elapsed = time.time() - start_time
        if i > 1:
            avg_per_file = elapsed / (i - 1)
            remaining = avg_per_file * (total - i + 1)
            eta = format_timestamp(remaining)
            logger.info(f"[{i}/{total}] ETA: {eta}")
        else:
            logger.info(f"[{i}/{total}]")

        result = transcribe_file(mp3, model, logger)
        if result:
            success += 1
        else:
            failed += 1

    total_time = time.time() - start_time
    logger.info(f"Done. {success} transcribed, {failed} failed, {format_timestamp(total_time)} total")


if __name__ == "__main__":
    main()

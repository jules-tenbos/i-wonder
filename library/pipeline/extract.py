#!/usr/bin/env python3
"""LLM-based metadata extraction from research library transcripts.

Sends each transcript to the Claude API to extract structured metadata:
- People (name + context)
- Topics (key concepts)
- Works (books, papers, experiments referenced)

Output: JSON per transcript in library/extractions/{slug}.json.
Resume-safe: skips transcripts that already have an extraction file.

Usage:
    python extract.py                                    # extract all
    python extract.py --category lectures --series "Being Human - Great Courses"
    python extract.py --dry-run                          # count pending
    python extract.py --limit 10                         # test run
"""

import argparse
import json
import sys
from pathlib import Path

import yaml

from utils import load_config


EXTRACTION_PROMPT = """\
You are analyzing a transcript from an audio research library. Extract structured metadata as JSON.

Transcript title: {title}
Series: {series}
Category: {category}

<transcript>
{content}
</transcript>

Extract the following and respond with ONLY valid JSON (no markdown fencing):

{{
  "people": [
    {{
      "name": "Full Name",
      "context": "brief role — e.g. lecturer, mentioned scientist, philosopher, author discussed"
    }}
  ],
  "topics": [
    "key concept or theme distinctive to this transcript"
  ],
  "works": [
    {{
      "title": "Book/Paper/Experiment Title",
      "author": "Author Name or null",
      "type": "book|paper|experiment|study|essay|lecture series"
    }}
  ]
}}

Guidelines:
- For people: include the lecturer/speaker if identifiable, plus any scientists, philosophers, or thinkers discussed. Use full names where possible.
- For topics: list 3-10 key concepts that are distinctive to THIS transcript (not generic terms like "science" or "lecture"). Focus on specific theories, phenomena, or ideas discussed.
- For works: include books, papers, landmark experiments, or studies explicitly referenced. Only include works that are clearly named or described — do not invent references.
- If a category has no items, use an empty list.
"""


def get_extractions_dir():
    return Path(__file__).parent.parent / "extractions"


def get_library_root():
    return Path(__file__).parent.parent / "catalog"


def parse_markdown(filepath):
    """Parse a processed markdown file into frontmatter dict + body text."""
    text = filepath.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return None, text

    end = text.find("---", 3)
    if end == -1:
        return None, text

    fm_text = text[3:end]
    body = text[end + 3:].strip()
    try:
        fm = yaml.safe_load(fm_text)
    except yaml.YAMLError:
        fm = {}
    return fm, body


def collect_transcripts(library_root, category=None, series=None):
    """Collect processed markdown files, optionally filtered."""
    results = []
    for md_path in sorted(library_root.rglob("*.md")):
        if md_path.name.startswith("_") or md_path.name == "index.md":
            continue

        fm, body = parse_markdown(md_path)
        if not fm:
            continue

        if category and fm.get("category") != category:
            continue
        if series and fm.get("series") != series:
            continue

        rel_path = str(md_path.relative_to(library_root))
        slug = rel_path.replace("/", "--").replace(".md", "")

        results.append({
            "slug": slug,
            "title": fm.get("title", "Untitled"),
            "series": fm.get("series", ""),
            "category": fm.get("category", ""),
            "content": body,
            "file_path": rel_path,
        })

    return results


def extract_one(transcript, model, client):
    """Run extraction on a single transcript. Returns parsed JSON dict."""
    prompt = EXTRACTION_PROMPT.format(
        title=transcript["title"],
        series=transcript["series"],
        category=transcript["category"],
        content=transcript["content"],
    )

    response = client.messages.create(
        model=model,
        max_tokens=4096,
        messages=[{"role": "user", "content": prompt}],
    )

    text = response.content[0].text.strip()

    # Strip markdown code fencing if present
    if text.startswith("```"):
        lines = text.split("\n")
        # Remove first and last lines (```json and ```)
        lines = [l for l in lines if not l.strip().startswith("```")]
        text = "\n".join(lines)

    try:
        data = json.loads(text)
    except json.JSONDecodeError as e:
        print(f"    JSON parse error: {e}", file=sys.stderr)
        print(f"    Raw response: {text[:200]}", file=sys.stderr)
        return None

    # Attach metadata
    data["slug"] = transcript["slug"]
    data["title"] = transcript["title"]
    data["series"] = transcript["series"]
    data["category"] = transcript["category"]
    data["file_path"] = transcript["file_path"]

    return data


def main():
    parser = argparse.ArgumentParser(description="Extract metadata from transcripts using Claude API")
    parser.add_argument("--config", default=None, help="Path to config.yaml")
    parser.add_argument("--category", help="Filter by category")
    parser.add_argument("--series", help="Filter by series name")
    parser.add_argument("--dry-run", action="store_true", help="Count pending extractions")
    parser.add_argument("--limit", type=int, help="Max transcripts to process")
    args = parser.parse_args()

    config = load_config(args.config)
    library_root = get_library_root()
    extractions_dir = get_extractions_dir()
    anthropic_config = config.get("anthropic", {})
    model = anthropic_config.get("model", "claude-haiku-4-5-20251001")

    print(f"Catalog: {library_root}")
    print(f"Extractions: {extractions_dir}")
    print(f"Model: {model}")
    print()

    # Collect transcripts
    all_transcripts = collect_transcripts(library_root, args.category, args.series)
    print(f"Found {len(all_transcripts)} transcript(s) in catalog")

    # Filter to pending (no existing extraction)
    extractions_dir.mkdir(parents=True, exist_ok=True)
    pending = []
    for t in all_transcripts:
        json_path = extractions_dir / f"{t['slug']}.json"
        if not json_path.exists():
            pending.append(t)

    already_done = len(all_transcripts) - len(pending)
    if already_done:
        print(f"Already extracted: {already_done}")
    print(f"Pending: {len(pending)}")

    if args.limit:
        pending = pending[:args.limit]
        print(f"Limited to: {len(pending)}")

    if args.dry_run or not pending:
        if not pending:
            print("\nNothing to extract.")
        return

    # Import anthropic here so --dry-run works without the package
    try:
        import anthropic
    except ImportError:
        print("Error: anthropic package not installed. Run: pip install anthropic", file=sys.stderr)
        sys.exit(1)

    client = anthropic.Anthropic()
    print(f"\nExtracting metadata from {len(pending)} transcript(s)...\n")

    success = 0
    errors = 0

    for i, t in enumerate(pending, 1):
        series_label = f" [{t['series']}]" if t['series'] else ""
        print(f"  [{i}/{len(pending)}] {t['category']}{series_label}: {t['title']}")

        try:
            data = extract_one(t, model, client)
        except Exception as e:
            print(f"    Error: {e}", file=sys.stderr)
            errors += 1
            continue

        if data is None:
            errors += 1
            continue

        # Save extraction
        json_path = extractions_dir / f"{t['slug']}.json"
        json_path.write_text(
            json.dumps(data, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )

        people_count = len(data.get("people", []))
        topics_count = len(data.get("topics", []))
        works_count = len(data.get("works", []))
        print(f"    -> {people_count} people, {topics_count} topics, {works_count} works")
        success += 1

    print(f"\nDone: {success} extracted, {errors} error(s)")


if __name__ == "__main__":
    main()

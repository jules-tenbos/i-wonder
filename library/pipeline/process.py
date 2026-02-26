#!/usr/bin/env python3
"""Processing pipeline — transform raw transcripts into a structured research library.

Reads .txt transcripts from the audio directory, parses metadata from paths and
filenames, and generates structured markdown files with YAML frontmatter.

Usage:
    python process.py                                  # process all transcripts
    python process.py --category lectures              # specific category
    python process.py --category lectures --series "Being Human - Great Courses"
    python process.py --dry-run                        # show what would be generated
    python process.py --rebuild-index                  # rebuild catalog indexes only
"""

import argparse
import os
import sys
from collections import defaultdict
from pathlib import Path

import yaml

from utils import (
    clean_transcript_text,
    detect_transcript_format,
    is_research_content,
    load_config,
    parse_audio_path,
    scan_transcripts,
    slugify,
)


def get_library_root():
    """Get the library catalog root directory."""
    return Path(__file__).parent.parent / "catalog"


def build_output_path(meta, library_root):
    """Determine the output markdown path for a transcript.

    Returns (file_path, series_dir) tuple.
    """
    category = meta["category"]

    if meta.get("book"):
        # Readings: category/subcategory/author/book/
        author_slug = slugify(meta["author"]) if meta.get("author") else "unknown"
        book_slug = slugify(meta["book"])
        sub = meta.get("subcategory") or "general"
        series_dir = library_root / category / sub / author_slug / book_slug
    elif meta.get("series"):
        series_slug = slugify(meta["series"])
        if meta.get("subcategory"):
            series_dir = library_root / category / meta["subcategory"] / series_slug
        else:
            series_dir = library_root / category / series_slug
    else:
        # Standalone file
        sub = meta.get("subcategory") or "general"
        series_dir = library_root / category / sub

    # Build filename
    ep = meta.get("episode")
    title_slug = slugify(meta.get("title", "untitled"))
    if ep is not None:
        filename = f"{ep:02d}-{title_slug}.md"
    else:
        filename = f"{title_slug}.md"

    return series_dir / filename, series_dir


def generate_frontmatter(meta, transcript_format):
    """Generate YAML frontmatter dict for a processed transcript."""
    fm = {"title": meta.get("title", "Untitled")}

    if meta.get("series"):
        fm["series"] = meta["series"]
    elif meta.get("book"):
        fm["series"] = meta["book"]

    fm["category"] = meta["category"]

    if meta.get("subcategory"):
        fm["subcategory"] = meta["subcategory"]

    if meta.get("author"):
        fm["author"] = meta["author"]

    if meta.get("episode") is not None:
        fm["episode"] = meta["episode"]

    fm["source_file"] = meta["filename"]
    fm["transcript_format"] = transcript_format

    return fm


def process_transcript(txt_path, mp3_path, config, library_root, dry_run=False):
    """Process a single transcript file into structured markdown.

    Returns (output_path, meta) on success, (None, meta) on skip/failure.
    """
    audio_dir = config["audio_dir"]
    categories_config = config.get("categories", {})

    # Parse metadata from path — use mp3 path if available, else txt path
    source_path = mp3_path if mp3_path else txt_path
    meta = parse_audio_path(source_path, audio_dir, categories_config)

    if "error" in meta:
        return None, meta

    # Determine output path
    output_path, series_dir = build_output_path(meta, library_root)

    if dry_run:
        return output_path, meta

    # Read and process transcript
    try:
        raw_text = txt_path.read_text(encoding="utf-8", errors="replace")
    except Exception as e:
        print(f"  Error reading {txt_path}: {e}", file=sys.stderr)
        return None, meta

    transcript_format = detect_transcript_format(raw_text)
    cleaned_text = clean_transcript_text(raw_text, transcript_format)
    frontmatter = generate_frontmatter(meta, transcript_format)

    # Write output
    series_dir.mkdir(parents=True, exist_ok=True)

    fm_yaml = yaml.dump(frontmatter, default_flow_style=False, allow_unicode=True, sort_keys=False)
    content = f"---\n{fm_yaml}---\n\n{cleaned_text}\n"

    output_path.write_text(content, encoding="utf-8")
    return output_path, meta


def generate_series_page(series_dir, episodes_meta):
    """Generate a _series.md overview page for a series directory."""
    if not episodes_meta:
        return

    # Use first episode's metadata for series info
    sample = episodes_meta[0]
    series_name = sample.get("series") or sample.get("book") or series_dir.name
    category = sample.get("category", "")
    subcategory = sample.get("subcategory", "")
    author = sample.get("author", "")

    fm = {
        "title": series_name,
        "category": category,
        "type": "series",
        "episode_count": len(episodes_meta),
    }
    if subcategory:
        fm["subcategory"] = subcategory
    if author:
        fm["author"] = author

    fm_yaml = yaml.dump(fm, default_flow_style=False, allow_unicode=True, sort_keys=False)

    # Build episode list
    lines = [f"---\n{fm_yaml}---\n", f"# {series_name}\n"]
    if author:
        lines.append(f"**Author/Lecturer:** {author}\n")
    lines.append(f"**Episodes:** {len(episodes_meta)}\n")
    lines.append("## Episodes\n")

    sorted_eps = sorted(episodes_meta, key=lambda m: m.get("episode") or 0)
    for m in sorted_eps:
        ep = m.get("episode")
        title = m.get("title", "Untitled")
        title_slug = slugify(title)
        if ep is not None:
            fname = f"{ep:02d}-{title_slug}.md"
            lines.append(f"- [{ep:02d}. {title}]({fname})")
        else:
            fname = f"{title_slug}.md"
            lines.append(f"- [{title}]({fname})")

    lines.append("")
    (series_dir / "_series.md").write_text("\n".join(lines), encoding="utf-8")


def generate_category_index(library_root, category, series_data):
    """Generate index.md for a category directory."""
    cat_dir = library_root / category
    cat_dir.mkdir(parents=True, exist_ok=True)

    lines = [f"# {category.title()}\n"]

    # Group by subcategory
    by_sub = defaultdict(list)
    for series_key, episodes in sorted(series_data.items()):
        sub = episodes[0].get("subcategory") or "general"
        series_name = episodes[0].get("series") or episodes[0].get("book") or series_key
        by_sub[sub].append((series_key, series_name, len(episodes)))

    for sub in sorted(by_sub.keys()):
        if sub != "general":
            lines.append(f"## {sub.replace('-', ' ').title()}\n")
        for series_key, series_name, count in sorted(by_sub[sub], key=lambda x: x[1]):
            series_slug = slugify(series_name)
            if sub != "general":
                lines.append(f"- [{series_name}]({sub}/{series_slug}/_series.md) ({count} episodes)")
            else:
                lines.append(f"- [{series_name}]({series_slug}/_series.md) ({count} episodes)")
        lines.append("")

    (cat_dir / "index.md").write_text("\n".join(lines), encoding="utf-8")


def generate_master_index(library_root, all_data):
    """Generate the master catalog index.md."""
    lines = [
        "# Audio Library Catalog\n",
        "Structured transcripts from the audio library.\n",
    ]

    total_transcripts = sum(
        len(eps) for cat_data in all_data.values() for eps in cat_data.values()
    )
    total_series = sum(len(cat_data) for cat_data in all_data.values())

    lines.append(f"**{total_transcripts} transcripts** across **{total_series} series** "
                 f"in **{len(all_data)} categories**.\n")

    for category in sorted(all_data.keys()):
        cat_data = all_data[category]
        cat_count = sum(len(eps) for eps in cat_data.values())
        lines.append(f"## [{category.title()}]({category}/index.md) ({cat_count} transcripts)\n")

        for series_key in sorted(cat_data.keys(), key=lambda k: cat_data[k][0].get("series", k)):
            episodes = cat_data[series_key]
            series_name = episodes[0].get("series") or episodes[0].get("book") or series_key
            lines.append(f"- {series_name} ({len(episodes)} episodes)")
        lines.append("")

    (library_root / "index.md").write_text("\n".join(lines), encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description="Process transcripts into structured library")
    parser.add_argument("--config", default=None, help="Path to config.yaml")
    parser.add_argument("--category", help="Filter by category")
    parser.add_argument("--subcategory", help="Filter by subcategory")
    parser.add_argument("--series", help="Filter by series name (directory name)")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be generated")
    parser.add_argument("--rebuild-index", action="store_true", help="Rebuild indexes only")
    args = parser.parse_args()

    config = load_config(args.config)
    library_root = get_library_root()
    audio_dir = config["audio_dir"]

    print(f"Audio directory: {audio_dir}")
    print(f"Library output:  {library_root}")
    print()

    # Collect transcripts
    transcripts = list(scan_transcripts(
        audio_dir,
        category=args.category,
        subcategory=args.subcategory,
        series=args.series,
    ))

    if not transcripts:
        print("No transcripts found.")
        return

    print(f"Found {len(transcripts)} transcript(s)")

    # Apply research scope filter
    filtered = []
    excluded = 0
    for txt, mp3 in transcripts:
        meta = parse_audio_path(
            mp3 if mp3 else txt,
            audio_dir,
            config.get("categories", {}),
        )
        if is_research_content(meta, config):
            filtered.append((txt, mp3))
        else:
            excluded += 1

    if excluded:
        print(f"Excluded {excluded} non-research transcript(s)")

    transcripts = filtered
    if not transcripts:
        print("No research transcripts to process.")
        return

    if args.dry_run:
        for txt, mp3 in transcripts:
            meta = parse_audio_path(
                mp3 if mp3 else txt,
                audio_dir,
                config.get("categories", {}),
            )
            output, _ = build_output_path(meta, library_root)
            status = "-> " + str(output.relative_to(library_root))
            print(f"  {meta.get('category', '?')}/{meta.get('series') or meta.get('book') or '?'}: "
                  f"{meta.get('title', '?')} {status}")

        print(f"\nDry run: {len(transcripts)} files would be processed")
        return

    # Process all transcripts, tracking series for index generation
    # all_data[category][series_key] = [list of meta dicts]
    all_data = defaultdict(lambda: defaultdict(list))
    processed = 0
    skipped = 0

    for txt, mp3 in transcripts:
        output_path, meta = process_transcript(txt, mp3, config, library_root)

        if output_path:
            series_key = meta.get("series") or meta.get("book") or "standalone"
            all_data[meta["category"]][series_key].append(meta)
            processed += 1
        else:
            skipped += 1

    print(f"\nProcessed: {processed}, Skipped: {skipped}")

    # Generate series pages
    print("Generating series pages...")
    series_dirs_done = set()
    for category, cat_data in all_data.items():
        for series_key, episodes in cat_data.items():
            if not episodes:
                continue
            sample = episodes[0]
            _, series_dir = build_output_path(sample, library_root)
            if series_dir not in series_dirs_done:
                generate_series_page(series_dir, episodes)
                series_dirs_done.add(series_dir)

    # Generate category indexes
    print("Generating category indexes...")
    for category, cat_data in all_data.items():
        generate_category_index(library_root, category, cat_data)

    # Generate master index
    print("Generating master catalog index...")
    generate_master_index(library_root, all_data)

    print("Done.")


if __name__ == "__main__":
    main()

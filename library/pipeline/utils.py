"""Shared utilities for the audio library pipeline.

Handles path parsing, name normalization, transcript format detection,
and mapping between MP3 files and their transcripts.
"""

import re
import os
import unicodedata
from pathlib import Path

import yaml


def load_config(config_path=None):
    """Load pipeline configuration from config.yaml."""
    if config_path is None:
        config_path = Path(__file__).parent / "config.yaml"
    with open(config_path) as f:
        return yaml.safe_load(f)


def slugify(text):
    """Convert text to lowercase kebab-case slug.

    Matches the naming convention used by existing transcripts:
    - lowercase
    - hyphens for separators
    - strip punctuation except hyphens
    """
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii")
    text = text.lower()
    text = re.sub(r"[''`]", "", text)  # remove apostrophes
    text = re.sub(r"[^\w\s-]", " ", text)  # punctuation -> space
    text = re.sub(r"[-\s]+", "-", text).strip("-")
    return text


def parse_mp3_filename(filename):
    """Parse metadata from an MP3 filename.

    Handles patterns like:
    - "HU01 What's So Special about Being Human - Being Human - Great Courses.mp3"
    - "LF - Aaron Smith-Levin - Scientology.mp3"
    - "behave-01--robert-sapolsky.mp3"

    Returns dict with: prefix, episode, title, series_name (when parseable)
    """
    stem = Path(filename).stem
    result = {"raw_stem": stem, "prefix": None, "episode": None, "title": stem, "series_hint": None}

    # Pattern 1: Lecture style — "PREFIX## Title - Series Name"
    # Require " - " (space-dash-space) to separate title from series
    m = re.match(r"^([A-Z]+)(\d+)\s+(.+?)(?:\s+-\s+(.+))?$", stem)
    if m:
        result["prefix"] = m.group(1)
        result["episode"] = int(m.group(2))
        remaining = m.group(3)
        if m.group(4):
            result["title"] = remaining.strip()
            result["series_hint"] = m.group(4).strip()
        else:
            result["title"] = remaining.strip()
        return result

    # Pattern 2: Podcast style — "ABBREV - Title" or "ABBREV - Guest - Topic"
    m = re.match(r"^([A-Z]{2,})\s*-\s*(.+)$", stem)
    if m:
        result["prefix"] = m.group(1)
        result["title"] = m.group(2).strip()
        return result

    # Pattern 3: Reading style — "book-slug-##--author.mp3"
    m = re.match(r"^(.+?)-(\d+)--(.+)$", stem)
    if m:
        result["title"] = m.group(1).replace("-", " ").strip()
        result["episode"] = int(m.group(2))
        result["series_hint"] = m.group(3).replace("-", " ").strip()
        return result

    return result


def parse_audio_path(filepath, audio_dir, categories_config):
    """Parse full metadata from an audio file's path within the library.

    Returns dict with: category, subcategory, series, plus filename metadata.
    """
    filepath = Path(filepath)
    audio_dir = Path(audio_dir)

    try:
        rel = filepath.relative_to(audio_dir)
    except ValueError:
        return {"error": f"File not under audio_dir: {filepath}"}

    parts = list(rel.parts)
    if len(parts) < 2:
        return {"error": f"Unexpected path depth: {rel}"}

    category = parts[0]
    cat_config = categories_config.get(category, {})
    structure = cat_config.get("structure", "flat")

    result = {
        "category": category,
        "subcategory": None,
        "series": None,
        "author": None,
        "book": None,
        "filename": parts[-1],
        "rel_path": str(rel),
    }

    if structure == "subject":
        # category/subcategory/series/file  OR  category/subcategory/file (standalone)
        if len(parts) >= 4:
            result["subcategory"] = parts[1]
            result["series"] = parts[2]
        elif len(parts) == 3:
            # Could be subcategory/file (standalone) or series/file
            # Check if middle part looks like a subcategory (lowercase, short) vs series name
            result["subcategory"] = parts[1]
    elif structure == "author":
        # category/subcategory/author/book/file
        if len(parts) >= 5:
            result["subcategory"] = parts[1]
            result["author"] = parts[2]
            result["book"] = parts[3]
        elif len(parts) >= 4:
            result["subcategory"] = parts[1]
            result["author"] = parts[2]
        elif len(parts) == 3:
            result["subcategory"] = parts[1]
    elif structure == "flat":
        # category/series/file
        if len(parts) >= 3:
            result["series"] = parts[1]
        # else standalone file in category root

    # Merge in filename-level metadata
    file_meta = parse_mp3_filename(result["filename"])
    result["episode"] = file_meta.get("episode")
    result["title"] = file_meta.get("title", Path(result["filename"]).stem)
    result["prefix"] = file_meta.get("prefix")

    # Derive series from directory name if not from filename
    if not result["series"] and not result["book"]:
        result["series"] = file_meta.get("series_hint")

    return result


def is_research_content(meta, config):
    """Check whether a transcript is research-relevant based on exclude rules.

    Returns True if the content should be included, False if excluded.
    """
    exclude = config.get("exclude", {})
    excluded_categories = exclude.get("categories", [])
    excluded_subjects = exclude.get("readings_subjects", [])

    if meta.get("category") in excluded_categories:
        return False

    if meta.get("category") == "readings" and meta.get("subcategory") in excluded_subjects:
        return False

    return True


def find_transcript(mp3_path):
    """Find existing transcript for an MP3 file.

    Checks for both naming conventions:
    1. Same basename with .txt extension (new format)
    2. Slugified basename with .txt extension (existing format)

    Returns path to transcript if found, None otherwise.
    """
    mp3_path = Path(mp3_path)
    directory = mp3_path.parent

    # Check 1: direct .txt alongside mp3
    direct = directory / (mp3_path.stem + ".txt")
    if direct.exists():
        return direct

    # Check 2: slugified name
    slug = slugify(mp3_path.stem)
    slugified_path = directory / (slug + ".txt")
    if slugified_path.exists():
        return slugified_path

    # Check 3: scan directory for any .txt that slugifies to the same thing
    # (handles minor variations in slugification)
    try:
        for f in directory.iterdir():
            if f.suffix == ".txt" and slugify(f.stem) == slug:
                return f
    except OSError:
        pass

    return None


def detect_transcript_format(text):
    """Detect whether a transcript is speaker-labeled or timestamped.

    Returns 'speaker-labeled' or 'timestamped'.
    """
    # Speaker-labeled: "Speaker Name (MM:SS.mmm)" pattern
    speaker_pattern = re.compile(r"^.+?\(\d{1,2}:\d{2}\.\d+\)\s*$", re.MULTILINE)
    # Timestamped: "[HH:MM:SS]" prefix pattern (whisper output)
    timestamp_pattern = re.compile(r"^\[\d{2}:\d{2}:\d{2}\]", re.MULTILINE)

    speaker_hits = len(speaker_pattern.findall(text[:5000]))
    timestamp_hits = len(timestamp_pattern.findall(text[:5000]))

    if timestamp_hits > speaker_hits:
        return "timestamped"
    return "speaker-labeled"


def clean_transcript_text(text, fmt=None):
    """Clean raw transcript text for the structured library output.

    Strips speaker labels/timestamps, normalizes paragraph breaks.
    """
    if fmt is None:
        fmt = detect_transcript_format(text)

    lines = text.split("\n")
    cleaned = []

    if fmt == "speaker-labeled":
        # Remove "Speaker Name (timestamp)" lines, keep content
        speaker_line = re.compile(r"^.+?\(\d{1,2}:\d{2}[\.:]\d+\)\s*$")
        for line in lines:
            if speaker_line.match(line.strip()):
                # Add paragraph break before new speaker segment
                if cleaned and cleaned[-1] != "":
                    cleaned.append("")
            else:
                cleaned.append(line)
    elif fmt == "timestamped":
        # Strip [HH:MM:SS] prefixes
        ts_prefix = re.compile(r"^\[\d{2}:\d{2}:\d{2}\]\s*")
        for line in lines:
            cleaned.append(ts_prefix.sub("", line))

    # Normalize multiple blank lines to single
    result = []
    prev_blank = False
    for line in cleaned:
        if line.strip() == "":
            if not prev_blank:
                result.append("")
            prev_blank = True
        else:
            result.append(line)
            prev_blank = False

    return "\n".join(result).strip()


def _matches_series(filepath, audio_dir, series):
    """Check if a file's parent directories contain the given series name."""
    try:
        rel = filepath.relative_to(audio_dir)
    except ValueError:
        return False
    return series in rel.parts


def scan_audio_files(audio_dir, category=None, subcategory=None, series=None):
    """Scan audio directory for MP3 files, optionally filtered.

    Yields (mp3_path, transcript_path_or_None) tuples.
    """
    audio_dir = Path(audio_dir)

    if category:
        search_root = audio_dir / category
        if subcategory:
            search_root = search_root / subcategory
            if series:
                search_root = search_root / series
    else:
        search_root = audio_dir

    if not search_root.exists():
        return

    for mp3 in sorted(search_root.rglob("*.mp3")):
        # Skip hidden/system files
        if any(part.startswith(".") for part in mp3.parts):
            continue
        # Apply series filter even without subcategory
        if series and not subcategory and not _matches_series(mp3, audio_dir, series):
            continue
        transcript = find_transcript(mp3)
        yield mp3, transcript


def scan_transcripts(audio_dir, category=None, subcategory=None, series=None):
    """Scan audio directory for existing transcript .txt files, optionally filtered.

    Yields (txt_path, mp3_path_or_None) tuples.
    """
    audio_dir = Path(audio_dir)

    if category:
        search_root = audio_dir / category
        if subcategory:
            search_root = search_root / subcategory
            if series:
                search_root = search_root / series
    else:
        search_root = audio_dir

    if not search_root.exists():
        return

    for txt in sorted(search_root.rglob("*.txt")):
        # Apply series filter even without subcategory
        if series and not subcategory and not _matches_series(txt, audio_dir, series):
            continue
        if any(part.startswith(".") for part in txt.parts):
            continue
        # Try to find the matching mp3
        mp3_direct = txt.parent / (txt.stem + ".mp3")
        if mp3_direct.exists():
            yield txt, mp3_direct
            continue
        # Search for mp3 with matching slug
        slug = slugify(txt.stem)
        found_mp3 = None
        try:
            for f in txt.parent.iterdir():
                if f.suffix == ".mp3" and slugify(f.stem) == slug:
                    found_mp3 = f
                    break
        except OSError:
            pass
        yield txt, found_mp3

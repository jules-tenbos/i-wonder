#!/usr/bin/env python3
"""SQLite FTS5 search index for the research library.

Builds a full-text search index from processed markdown transcripts and
(optionally) LLM-extracted metadata. Supports ranked search queries.

Usage:
    python search.py build                              # build/rebuild index
    python search.py query "consciousness"              # full-text search
    python search.py query "Sapolsky"                   # finds in people + text
    python search.py people                             # list all extracted people
    python search.py people "Nick Lane"                 # where is someone mentioned
    python search.py topics                             # list all extracted topics
    python search.py works                              # list all referenced works
"""

import argparse
import json
import sqlite3
import sys
from pathlib import Path

import yaml

from utils import load_config


DB_NAME = "research.db"


def get_db_path():
    """Return path to the SQLite database in library/."""
    return Path(__file__).parent.parent / DB_NAME


def get_library_root():
    return Path(__file__).parent.parent / "catalog"


def get_extractions_dir():
    return Path(__file__).parent.parent / "extractions"


def connect(db_path=None):
    if db_path is None:
        db_path = get_db_path()
    conn = sqlite3.connect(str(db_path))
    conn.row_factory = sqlite3.Row
    return conn


def create_schema(conn):
    """Create tables and FTS5 virtual table."""
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS transcripts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            slug TEXT UNIQUE NOT NULL,
            title TEXT,
            series TEXT,
            category TEXT,
            subcategory TEXT,
            author TEXT,
            episode INTEGER,
            source_file TEXT,
            transcript_format TEXT,
            file_path TEXT,
            content TEXT
        );

        CREATE TABLE IF NOT EXISTS people (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            transcript_slug TEXT NOT NULL,
            name TEXT NOT NULL,
            context TEXT,
            FOREIGN KEY (transcript_slug) REFERENCES transcripts(slug)
        );

        CREATE TABLE IF NOT EXISTS topics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            transcript_slug TEXT NOT NULL,
            topic TEXT NOT NULL,
            FOREIGN KEY (transcript_slug) REFERENCES transcripts(slug)
        );

        CREATE TABLE IF NOT EXISTS works (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            transcript_slug TEXT NOT NULL,
            title TEXT NOT NULL,
            author TEXT,
            type TEXT,
            FOREIGN KEY (transcript_slug) REFERENCES transcripts(slug)
        );
    """)

    # FTS5 virtual table — drop and recreate to ensure schema matches
    conn.execute("DROP TABLE IF EXISTS transcripts_fts")
    conn.execute("""
        CREATE VIRTUAL TABLE transcripts_fts USING fts5(
            slug,
            title,
            series,
            category,
            author,
            content,
            people_text,
            topics_text,
            works_text,
            content='',
            tokenize='porter unicode61'
        )
    """)
    conn.commit()


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


def build_index(conn, library_root, extractions_dir):
    """Scan catalog markdown files and build the search index."""
    # Clear existing data
    conn.executescript("""
        DELETE FROM transcripts;
        DELETE FROM people;
        DELETE FROM topics;
        DELETE FROM works;
    """)

    count = 0
    for md_path in sorted(library_root.rglob("*.md")):
        # Skip index and series pages
        if md_path.name.startswith("_") or md_path.name == "index.md":
            continue

        fm, body = parse_markdown(md_path)
        if not fm:
            continue

        slug = md_path.stem
        rel_path = str(md_path.relative_to(library_root))

        # Make slug unique by prepending category/series path
        unique_slug = rel_path.replace("/", "--").replace(".md", "")

        conn.execute("""
            INSERT OR REPLACE INTO transcripts
            (slug, title, series, category, subcategory, author, episode,
             source_file, transcript_format, file_path, content)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            unique_slug,
            fm.get("title"),
            fm.get("series"),
            fm.get("category"),
            fm.get("subcategory"),
            fm.get("author"),
            fm.get("episode"),
            fm.get("source_file"),
            fm.get("transcript_format"),
            rel_path,
            body,
        ))
        count += 1

    # Load extractions if available
    extraction_count = _load_extractions(conn, extractions_dir)

    # Populate FTS index
    _populate_fts(conn)

    conn.commit()
    return count, extraction_count


def _load_extractions(conn, extractions_dir):
    """Load extraction JSON files into people/topics/works tables."""
    if not extractions_dir.exists():
        return 0

    count = 0
    for json_path in sorted(extractions_dir.rglob("*.json")):
        try:
            data = json.loads(json_path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            continue

        slug = data.get("slug")
        if not slug:
            continue

        # Check transcript exists
        row = conn.execute("SELECT 1 FROM transcripts WHERE slug = ?", (slug,)).fetchone()
        if not row:
            continue

        for person in data.get("people", []):
            conn.execute(
                "INSERT INTO people (transcript_slug, name, context) VALUES (?, ?, ?)",
                (slug, person.get("name", ""), person.get("context", "")),
            )

        for topic in data.get("topics", []):
            conn.execute(
                "INSERT INTO topics (transcript_slug, topic) VALUES (?, ?)",
                (slug, topic),
            )

        for work in data.get("works", []):
            conn.execute(
                "INSERT INTO works (transcript_slug, title, author, type) VALUES (?, ?, ?, ?)",
                (slug, work.get("title", ""), work.get("author", ""), work.get("type", "")),
            )

        count += 1

    return count


def _populate_fts(conn):
    """Populate the FTS5 table from transcripts + extraction tables."""
    rows = conn.execute("SELECT slug FROM transcripts").fetchall()

    for row in rows:
        slug = row["slug"]
        t = conn.execute("SELECT * FROM transcripts WHERE slug = ?", (slug,)).fetchone()

        # Aggregate extraction text for this transcript
        people_names = [r["name"] + " " + (r["context"] or "")
                        for r in conn.execute(
                            "SELECT name, context FROM people WHERE transcript_slug = ?",
                            (slug,)).fetchall()]
        topics_list = [r["topic"]
                       for r in conn.execute(
                           "SELECT topic FROM topics WHERE transcript_slug = ?",
                           (slug,)).fetchall()]
        works_list = [r["title"] + " " + (r["author"] or "")
                      for r in conn.execute(
                          "SELECT title, author FROM works WHERE transcript_slug = ?",
                          (slug,)).fetchall()]

        conn.execute("""
            INSERT INTO transcripts_fts
            (slug, title, series, category, author, content, people_text, topics_text, works_text)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            slug,
            t["title"] or "",
            t["series"] or "",
            t["category"] or "",
            t["author"] or "",
            t["content"] or "",
            " | ".join(people_names),
            " | ".join(topics_list),
            " | ".join(works_list),
        ))


def search_query(conn, query, limit=20):
    """Run a full-text search query, return ranked results."""
    rows = conn.execute("""
        SELECT slug, rank, snippet(transcripts_fts, 5, '>>>', '<<<', '...', 40) as snippet
        FROM transcripts_fts
        WHERE transcripts_fts MATCH ?
        ORDER BY rank
        LIMIT ?
    """, (query, limit)).fetchall()

    results = []
    for row in rows:
        t = conn.execute("SELECT * FROM transcripts WHERE slug = ?", (row["slug"],)).fetchone()
        if t:
            results.append({
                "slug": row["slug"],
                "title": t["title"],
                "series": t["series"],
                "category": t["category"],
                "file_path": t["file_path"],
                "snippet": row["snippet"],
                "rank": row["rank"],
            })
    return results


def list_people(conn, name_filter=None):
    """List all people, optionally filtered by name."""
    if name_filter:
        rows = conn.execute("""
            SELECT p.name, p.context, p.transcript_slug, t.title, t.series
            FROM people p
            JOIN transcripts t ON t.slug = p.transcript_slug
            WHERE p.name LIKE ?
            ORDER BY p.name
        """, (f"%{name_filter}%",)).fetchall()
    else:
        rows = conn.execute("""
            SELECT p.name, COUNT(DISTINCT p.transcript_slug) as mention_count
            FROM people p
            GROUP BY p.name
            ORDER BY mention_count DESC, p.name
        """).fetchall()
    return [dict(r) for r in rows]


def list_topics(conn, topic_filter=None):
    """List all topics, optionally filtered."""
    if topic_filter:
        rows = conn.execute("""
            SELECT tp.topic, tp.transcript_slug, t.title, t.series
            FROM topics tp
            JOIN transcripts t ON t.slug = tp.transcript_slug
            WHERE tp.topic LIKE ?
            ORDER BY tp.topic
        """, (f"%{topic_filter}%",)).fetchall()
    else:
        rows = conn.execute("""
            SELECT tp.topic, COUNT(DISTINCT tp.transcript_slug) as mention_count
            FROM topics tp
            GROUP BY tp.topic
            ORDER BY mention_count DESC, tp.topic
        """).fetchall()
    return [dict(r) for r in rows]


def list_works(conn, work_filter=None):
    """List all referenced works, optionally filtered."""
    if work_filter:
        rows = conn.execute("""
            SELECT w.title, w.author, w.type, w.transcript_slug, t.title as transcript_title, t.series
            FROM works w
            JOIN transcripts t ON t.slug = w.transcript_slug
            WHERE w.title LIKE ? OR w.author LIKE ?
            ORDER BY w.title
        """, (f"%{work_filter}%", f"%{work_filter}%")).fetchall()
    else:
        rows = conn.execute("""
            SELECT w.title, w.author, w.type, COUNT(DISTINCT w.transcript_slug) as mention_count
            FROM works w
            GROUP BY w.title, w.author
            ORDER BY mention_count DESC, w.title
        """).fetchall()
    return [dict(r) for r in rows]


def main():
    parser = argparse.ArgumentParser(description="Research library search index")
    sub = parser.add_subparsers(dest="command")

    # build
    build_cmd = sub.add_parser("build", help="Build/rebuild the search index")
    build_cmd.add_argument("--config", default=None)

    # query
    query_cmd = sub.add_parser("query", help="Search the index")
    query_cmd.add_argument("term", help="Search query")
    query_cmd.add_argument("--limit", type=int, default=20)

    # people
    people_cmd = sub.add_parser("people", help="List extracted people")
    people_cmd.add_argument("name", nargs="?", help="Filter by name")

    # topics
    topics_cmd = sub.add_parser("topics", help="List extracted topics")
    topics_cmd.add_argument("topic", nargs="?", help="Filter by topic")

    # works
    works_cmd = sub.add_parser("works", help="List referenced works")
    works_cmd.add_argument("term", nargs="?", help="Filter by title or author")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    if args.command == "build":
        library_root = get_library_root()
        extractions_dir = get_extractions_dir()
        db_path = get_db_path()

        print(f"Building search index: {db_path}")
        print(f"Catalog: {library_root}")

        conn = connect(db_path)
        create_schema(conn)
        count, ext_count = build_index(conn, library_root, extractions_dir)
        conn.close()

        print(f"Indexed {count} transcript(s), loaded {ext_count} extraction(s)")
        return

    # All other commands need the DB to exist
    db_path = get_db_path()
    if not db_path.exists():
        print("Search index not found. Run: python search.py build", file=sys.stderr)
        sys.exit(1)

    conn = connect(db_path)

    if args.command == "query":
        results = search_query(conn, args.term, args.limit)
        if not results:
            print(f"No results for: {args.term}")
        else:
            print(f"{len(results)} result(s) for: {args.term}\n")
            for r in results:
                series = f" [{r['series']}]" if r['series'] else ""
                print(f"  {r['category']}{series}: {r['title']}")
                print(f"    {r['file_path']}")
                if r['snippet']:
                    print(f"    ...{r['snippet']}...")
                print()

    elif args.command == "people":
        results = list_people(conn, args.name)
        if not results:
            print("No people found." if not args.name else f"No matches for: {args.name}")
        elif args.name:
            print(f"{len(results)} mention(s) of '{args.name}':\n")
            for r in results:
                series = f" [{r['series']}]" if r.get('series') else ""
                print(f"  {r['name']} ({r['context']}) — {r['title']}{series}")
        else:
            print(f"{len(results)} people across library:\n")
            for r in results:
                print(f"  {r['name']} ({r['mention_count']} transcript(s))")

    elif args.command == "topics":
        results = list_topics(conn, args.topic)
        if not results:
            print("No topics found." if not args.topic else f"No matches for: {args.topic}")
        elif args.topic:
            print(f"{len(results)} match(es) for '{args.topic}':\n")
            for r in results:
                series = f" [{r['series']}]" if r.get('series') else ""
                print(f"  {r['topic']} — {r['title']}{series}")
        else:
            print(f"{len(results)} topics across library:\n")
            for r in results:
                print(f"  {r['topic']} ({r['mention_count']} transcript(s))")

    elif args.command == "works":
        results = list_works(conn, args.term)
        if not results:
            print("No works found." if not args.term else f"No matches for: {args.term}")
        elif args.term:
            print(f"{len(results)} match(es) for '{args.term}':\n")
            for r in results:
                author = f" by {r['author']}" if r.get('author') else ""
                wtype = f" ({r['type']})" if r.get('type') else ""
                series = f" [{r['series']}]" if r.get('series') else ""
                print(f"  {r['title']}{author}{wtype} — {r['transcript_title']}{series}")
        else:
            print(f"{len(results)} works across library:\n")
            for r in results:
                author = f" by {r['author']}" if r.get('author') else ""
                wtype = f" ({r['type']})" if r.get('type') else ""
                print(f"  {r['title']}{author}{wtype} ({r['mention_count']} transcript(s))")

    conn.close()


if __name__ == "__main__":
    main()

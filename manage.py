#!/usr/bin/env python3
"""CLI tool for managing blog posts via Blogger API v3."""

import argparse
import json
import os
import sys
from pathlib import Path

import markdown
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

REPO_ROOT = Path(__file__).resolve().parent
CREDENTIALS_FILE = REPO_ROOT / "credentials.json"
TOKEN_FILE = REPO_ROOT / "token.json"
BLOG_URL = "https://julestenbos.blogspot.com"
SCOPES = ["https://www.googleapis.com/auth/blogger"]


def get_credentials():
    """Authenticate via OAuth2, caching token to token.json."""
    creds = None
    if TOKEN_FILE.exists():
        data = json.loads(TOKEN_FILE.read_text())
        creds_data = {k: v for k, v in data.items() if k != "blog_id"}
        if creds_data:
            creds = Credentials.from_authorized_user_info(creds_data, SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not CREDENTIALS_FILE.exists():
                print(f"Error: {CREDENTIALS_FILE} not found.", file=sys.stderr)
                sys.exit(1)
            flow = InstalledAppFlow.from_client_secrets_file(
                str(CREDENTIALS_FILE), SCOPES
            )
            print("Opening auth flow — if the browser doesn't open, visit the URL below.")
            creds = flow.run_local_server(port=0, open_browser=False)
        _save_token(creds)

    return creds


def _save_token(creds):
    """Save credentials (and blog_id if cached) to token.json."""
    data = json.loads(creds.to_json())
    # Preserve cached blog_id
    if TOKEN_FILE.exists():
        try:
            old = json.loads(TOKEN_FILE.read_text())
            if "blog_id" in old:
                data["blog_id"] = old["blog_id"]
        except (json.JSONDecodeError, KeyError):
            pass
    TOKEN_FILE.write_text(json.dumps(data, indent=2))


def get_blog_id(service):
    """Get blog ID from cache or discover via API, cache in token.json."""
    if TOKEN_FILE.exists():
        data = json.loads(TOKEN_FILE.read_text())
        if "blog_id" in data:
            return data["blog_id"]

    result = service.blogs().getByUrl(url=BLOG_URL).execute()
    blog_id = result["id"]

    # Cache it
    if TOKEN_FILE.exists():
        data = json.loads(TOKEN_FILE.read_text())
    else:
        data = {}
    data["blog_id"] = blog_id
    TOKEN_FILE.write_text(json.dumps(data, indent=2))

    return blog_id


def get_service():
    """Build and return authenticated Blogger API service + blog ID."""
    creds = get_credentials()
    service = build("blogger", "v3", credentials=creds)
    blog_id = get_blog_id(service)
    return service, blog_id


def parse_markdown_file(filepath):
    """Parse a markdown file into title and HTML body."""
    path = Path(filepath)
    if not path.exists():
        print(f"Error: {path} not found.", file=sys.stderr)
        sys.exit(1)

    text = path.read_text(encoding="utf-8")
    lines = text.split("\n")

    # Extract title from first # heading
    title = None
    body_start = 0
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith("# ") and not stripped.startswith("## "):
            title = stripped[2:].strip()
            body_start = i + 1
            break

    if not title:
        print("Error: No '# Title' found on first line.", file=sys.stderr)
        sys.exit(1)

    # Check for Labels: line after title
    labels = []
    if body_start < len(lines):
        next_line = lines[body_start].strip()
        if next_line.lower().startswith("labels:"):
            labels = [l.strip() for l in next_line[7:].split(",") if l.strip()]
            body_start += 1

    body_md = "\n".join(lines[body_start:]).strip()
    body_html = markdown.markdown(body_md, extensions=["extra", "sane_lists"])

    return title, body_html, labels


# ── Commands ─────────────────────────────────────────────────────────


def cmd_list(service, blog_id, _args):
    """List all published posts."""
    posts = service.posts().list(blogId=blog_id, status="LIVE").execute()
    items = posts.get("items", [])
    if not items:
        print("No published posts found.")
        return
    print(f"{'ID':<25} {'Published':<25} Title")
    print("-" * 80)
    for post in items:
        print(f"{post['id']:<25} {post['published']:<25} {post['title']}")


def cmd_get(service, blog_id, args):
    """Show a specific post."""
    post = service.posts().get(blogId=blog_id, postId=args.post_id).execute()
    print(f"Title:     {post['title']}")
    print(f"ID:        {post['id']}")
    print(f"Published: {post['published']}")
    print(f"Updated:   {post['updated']}")
    print(f"URL:       {post['url']}")
    print(f"\n--- Content ---\n")
    print(post.get("content", ""))


def cmd_publish(service, blog_id, args):
    """Publish a post from a markdown file."""
    title, body_html, labels = parse_markdown_file(args.markdown_file)
    post_body = {"kind": "blogger#post", "title": title, "content": body_html}
    if labels:
        post_body["labels"] = labels
    post = service.posts().insert(blogId=blog_id, body=post_body, isDraft=False).execute()
    print(f"Published: {post['title']}")
    print(f"ID:        {post['id']}")
    print(f"URL:       {post['url']}")


def cmd_draft(service, blog_id, args):
    """Create a draft from a markdown file."""
    title, body_html, labels = parse_markdown_file(args.markdown_file)
    post_body = {"kind": "blogger#post", "title": title, "content": body_html}
    if labels:
        post_body["labels"] = labels
    post = service.posts().insert(blogId=blog_id, body=post_body, isDraft=True).execute()
    print(f"Draft created: {post['title']}")
    print(f"ID:            {post['id']}")


def cmd_update(service, blog_id, args):
    """Update an existing post from a markdown file."""
    title, body_html, labels = parse_markdown_file(args.markdown_file)
    post_body = {"kind": "blogger#post", "title": title, "content": body_html}
    if labels:
        post_body["labels"] = labels
    post = (
        service.posts()
        .update(blogId=blog_id, postId=args.post_id, body=post_body)
        .execute()
    )
    print(f"Updated: {post['title']}")
    print(f"ID:      {post['id']}")
    print(f"URL:     {post['url']}")


def cmd_delete(service, blog_id, args):
    """Delete a post (with confirmation)."""
    post = service.posts().get(blogId=blog_id, postId=args.post_id).execute()
    answer = input(f"Delete '{post['title']}'? [y/N] ")
    if answer.lower() != "y":
        print("Cancelled.")
        return
    service.posts().delete(blogId=blog_id, postId=args.post_id).execute()
    print(f"Deleted: {post['title']}")


# ── Page Commands ────────────────────────────────────────────────────


def cmd_page_list(service, blog_id, _args):
    """List all pages."""
    pages = service.pages().list(blogId=blog_id).execute()
    items = pages.get("items", [])
    if not items:
        print("No pages found.")
        return
    print(f"{'ID':<25} {'Status':<12} Title")
    print("-" * 70)
    for page in items:
        status = page.get("status", "LIVE")
        print(f"{page['id']:<25} {status:<12} {page['title']}")


def cmd_page_publish(service, blog_id, args):
    """Publish a page from a markdown file."""
    title, body_html, _labels = parse_markdown_file(args.markdown_file)
    page_body = {"kind": "blogger#page", "title": title, "content": body_html}
    page = service.pages().insert(blogId=blog_id, body=page_body, isDraft=False).execute()
    print(f"Published page: {page['title']}")
    print(f"ID:             {page['id']}")
    print(f"URL:            {page['url']}")


def cmd_page_update(service, blog_id, args):
    """Update an existing page from a markdown file."""
    title, body_html, _labels = parse_markdown_file(args.markdown_file)
    page_body = {"kind": "blogger#page", "title": title, "content": body_html}
    page = (
        service.pages()
        .update(blogId=blog_id, pageId=args.page_id, body=page_body)
        .execute()
    )
    print(f"Updated page: {page['title']}")
    print(f"ID:           {page['id']}")
    print(f"URL:          {page['url']}")


def cmd_page_delete(service, blog_id, args):
    """Delete a page (with confirmation)."""
    page = service.pages().get(blogId=blog_id, pageId=args.page_id).execute()
    answer = input(f"Delete page '{page['title']}'? [y/N] ")
    if answer.lower() != "y":
        print("Cancelled.")
        return
    service.pages().delete(blogId=blog_id, pageId=args.page_id).execute()
    print(f"Deleted page: {page['title']}")


def cmd_sync(service, blog_id, _args):
    """Compare repo markdown posts with live blog posts."""
    # Get live posts
    posts = service.posts().list(blogId=blog_id, status="LIVE").execute()
    live = {p["title"].strip(): p for p in posts.get("items", [])}

    # Get repo posts (published — files with date prefix)
    published_dir = REPO_ROOT / "published"
    repo_titles = {}
    for md_file in sorted(published_dir.glob("*.md")):
        text = md_file.read_text(encoding="utf-8")
        for line in text.split("\n"):
            stripped = line.strip()
            if stripped.startswith("# ") and not stripped.startswith("## "):
                repo_titles[stripped[2:].strip()] = md_file
                break

    live_titles = set(live.keys())
    repo_title_set = set(repo_titles.keys())

    only_live = live_titles - repo_title_set
    only_repo = repo_title_set - live_titles
    both = live_titles & repo_title_set

    if both:
        print(f"In sync ({len(both)}):")
        for t in sorted(both):
            print(f"  {t}")

    if only_live:
        print(f"\nOnly on blog ({len(only_live)}):")
        for t in sorted(only_live):
            print(f"  {t}  (ID: {live[t]['id']})")

    if only_repo:
        print(f"\nOnly in repo ({len(only_repo)}):")
        for t in sorted(only_repo):
            print(f"  {t}  ({repo_titles[t].name})")

    if not only_live and not only_repo:
        print("\nAll posts are in sync.")


def main():
    parser = argparse.ArgumentParser(description="Manage blog posts via Blogger API")
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("list", help="List all published posts")

    p_get = subparsers.add_parser("get", help="Show a specific post")
    p_get.add_argument("post_id", help="Post ID")

    p_pub = subparsers.add_parser("publish", help="Publish from markdown")
    p_pub.add_argument("markdown_file", help="Path to markdown file")

    p_draft = subparsers.add_parser("draft", help="Create as draft")
    p_draft.add_argument("markdown_file", help="Path to markdown file")

    p_update = subparsers.add_parser("update", help="Update existing post")
    p_update.add_argument("post_id", help="Post ID")
    p_update.add_argument("markdown_file", help="Path to markdown file")

    p_delete = subparsers.add_parser("delete", help="Delete a post")
    p_delete.add_argument("post_id", help="Post ID")

    subparsers.add_parser("sync", help="Diff repo vs live blog")

    subparsers.add_parser("page-list", help="List all pages")

    p_page_pub = subparsers.add_parser("page-publish", help="Publish a page from markdown")
    p_page_pub.add_argument("markdown_file", help="Path to markdown file")

    p_page_upd = subparsers.add_parser("page-update", help="Update an existing page")
    p_page_upd.add_argument("page_id", help="Page ID")
    p_page_upd.add_argument("markdown_file", help="Path to markdown file")

    p_page_del = subparsers.add_parser("page-delete", help="Delete a page")
    p_page_del.add_argument("page_id", help="Page ID")

    args = parser.parse_args()

    commands = {
        "list": cmd_list,
        "get": cmd_get,
        "publish": cmd_publish,
        "draft": cmd_draft,
        "update": cmd_update,
        "delete": cmd_delete,
        "sync": cmd_sync,
        "page-list": cmd_page_list,
        "page-publish": cmd_page_publish,
        "page-update": cmd_page_update,
        "page-delete": cmd_page_delete,
    }

    service, blog_id = get_service()
    commands[args.command](service, blog_id, args)


if __name__ == "__main__":
    main()

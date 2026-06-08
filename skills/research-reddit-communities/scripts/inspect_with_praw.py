#!/usr/bin/env python3
"""Read-only, bounded Reddit inspection helper using PRAW.

Requires:
  REDDIT_CLIENT_ID
  REDDIT_CLIENT_SECRET
  REDDIT_USER_AGENT
"""

from __future__ import annotations

import argparse
import json
import os
from typing import Any


REQUIRED_ENV = ("REDDIT_CLIENT_ID", "REDDIT_CLIENT_SECRET", "REDDIT_USER_AGENT")


def require_env() -> dict[str, str]:
    missing = [key for key in REQUIRED_ENV if not os.environ.get(key)]
    if missing:
        joined = ", ".join(missing)
        raise SystemExit(
            f"Missing {joined}. Continue with manual-first research or set credentials."
        )
    return {key: os.environ[key] for key in REQUIRED_ENV}


def load_praw() -> Any:
    try:
        import praw
    except ImportError as exc:
        raise SystemExit(
            "PRAW is not installed. Run with: "
            "uv run --with praw python scripts/inspect_with_praw.py ..."
        ) from exc
    return praw


def post_record(post: Any) -> dict[str, Any]:
    return {
        "id": post.id,
        "title": post.title,
        "permalink": f"https://www.reddit.com{post.permalink}",
        "created_utc": post.created_utc,
        "score": post.score,
        "num_comments": post.num_comments,
        "upvote_ratio": getattr(post, "upvote_ratio", None),
        "flair": getattr(post, "link_flair_text", None),
        "is_self": post.is_self,
        "url": post.url,
        "selftext_excerpt": (post.selftext or "")[:800],
    }


def inspect_subreddit(reddit: Any, name: str, limit: int) -> dict[str, Any]:
    subreddit = reddit.subreddit(name)

    try:
        rules = [
            {
                "short_name": rule.short_name,
                "description": rule.description,
                "kind": rule.kind,
            }
            for rule in subreddit.rules
        ]
    except Exception as exc:  # PRAW can raise for private/restricted subreddits.
        rules = [{"error": str(exc)}]

    return {
        "subreddit": name,
        "display_name": subreddit.display_name,
        "title": subreddit.title,
        "public_description": subreddit.public_description,
        "subscribers": subreddit.subscribers,
        "over18": subreddit.over18,
        "rules": rules,
        "hot": [post_record(post) for post in subreddit.hot(limit=limit)],
        "top_month": [
            post_record(post) for post in subreddit.top(time_filter="month", limit=limit)
        ],
        "new": [post_record(post) for post in subreddit.new(limit=limit)],
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Fetch bounded read-only subreddit evidence through PRAW."
    )
    parser.add_argument("subreddits", nargs="+", help="Subreddit names without r/.")
    parser.add_argument(
        "--limit",
        type=int,
        default=15,
        help="Posts per listing to fetch for each subreddit. Max 50.",
    )
    args = parser.parse_args()

    limit = max(1, min(args.limit, 50))
    env = require_env()
    praw = load_praw()
    reddit = praw.Reddit(
        client_id=env["REDDIT_CLIENT_ID"],
        client_secret=env["REDDIT_CLIENT_SECRET"],
        user_agent=env["REDDIT_USER_AGENT"],
    )

    payload = {
        "source": "reddit_api_praw",
        "note": "Read-only bounded evidence. Agent must inspect and judge manually.",
        "limit": limit,
        "communities": [
            inspect_subreddit(reddit, name.removeprefix("r/"), limit)
            for name in args.subreddits
        ],
    }
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

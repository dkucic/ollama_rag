"""CLI entry point for the notes RAG tool."""
import argparse

from .config import load_config
from .indexer import build_index, index_exists, rebuild_index
from .querier import run_query


def cmd_index(cfg: dict) -> None:
    """Build the index, skipping if one already exists."""
    if index_exists(cfg):
        print("Index already exists. Use 'reindex' to force a full rebuild.")
        return
    build_index(cfg)
    print("Indexing complete.")


def cmd_reindex(cfg: dict) -> None:
    """Force a full rebuild of the index."""
    rebuild_index(cfg)
    print("Reindexing complete.")


def cmd_query(cfg: dict, question: str) -> None:
    """Query the notes index with a natural-language question."""
    run_query(cfg, question)


def main() -> None:
    """Parse CLI arguments and dispatch to the appropriate command."""
    parser = argparse.ArgumentParser(
        description="Query your notes using local Ollama."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("index", help="Build the index (skip if already exists).")
    subparsers.add_parser("reindex", help="Force a full index rebuild.")
    query_parser = subparsers.add_parser("query", help="Query the notes index.")
    query_parser.add_argument("question", help="Natural-language question to ask.")
    args = parser.parse_args()
    cfg = load_config()
    if args.command == "index":
        cmd_index(cfg)
    elif args.command == "reindex":
        cmd_reindex(cfg)
    elif args.command == "query":
        cmd_query(cfg, args.question)

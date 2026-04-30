"""Tests for query utilities."""
from src.querier import run_query


def test_run_query_no_index(tmp_path, capsys):
    """Prints a helpful message when no index exists."""
    cfg = {"data_path": str(tmp_path / "noindex")}
    run_query(cfg, "test question")
    captured = capsys.readouterr()
    assert "No index found" in captured.out

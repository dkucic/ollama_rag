"""Tests for indexer utilities."""
from src.indexer import index_exists


def test_index_exists_false(tmp_path):
    """Returns False when data_path does not exist."""
    cfg = {"data_path": str(tmp_path / "nonexistent")}
    assert not index_exists(cfg)


def test_index_exists_true(tmp_path):
    """Returns True when docstore.json is present."""
    (tmp_path / "docstore.json").write_text("{}")
    cfg = {"data_path": str(tmp_path)}
    assert index_exists(cfg)

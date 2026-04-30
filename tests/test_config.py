"""Tests for configuration loading."""
import pytest
from src.config import load_config


def test_load_config_missing_file():
    """Missing config file raises FileNotFoundError."""
    with pytest.raises(FileNotFoundError):
        load_config("nonexistent.yaml")


def test_load_config_missing_keys(tmp_path):
    """Config with missing required keys raises ValueError."""
    cfg_file = tmp_path / "config.yaml"
    cfg_file.write_text("generation_model: test\n")
    with pytest.raises(ValueError, match="Missing required config keys"):
        load_config(str(cfg_file))


def test_load_config_valid(tmp_path):
    """Valid config loads without error."""
    cfg_file = tmp_path / "config.yaml"
    cfg_file.write_text(
        "generation_model: a\n"
        "embedding_model: b\n"
        "notes_path: ./Notes\n"
        "data_path: ./data\n"
        "chunk_size: 512\n"
        "chunk_overlap: 50\n"
        "top_k_results: 5\n"
    )
    cfg = load_config(str(cfg_file))
    assert cfg["chunk_size"] == 512

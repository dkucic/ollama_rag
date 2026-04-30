"""Configuration loader for ollama_rag."""
import yaml

REQUIRED_KEYS = [
    "generation_model",
    "embedding_model",
    "notes_path",
    "data_path",
    "chunk_size",
    "chunk_overlap",
    "top_k_results",
]


def load_config(config_path: str = "config.yaml") -> dict:
    """Load and validate configuration from a YAML file."""
    with open(config_path, encoding="utf-8") as fh:
        cfg = yaml.safe_load(fh)
    missing = [k for k in REQUIRED_KEYS if k not in cfg]
    if missing:
        raise ValueError(f"Missing required config keys: {missing}")
    return cfg

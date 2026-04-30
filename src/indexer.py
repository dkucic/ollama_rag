"""Index building, loading, and rebuilding for the notes RAG system."""
import os
import shutil

from llama_index.core import (
    Settings,
    SimpleDirectoryReader,
    StorageContext,
    VectorStoreIndex,
    load_index_from_storage,
)
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.llms.ollama import Ollama


def _configure_settings(cfg: dict) -> None:
    """Apply LlamaIndex global settings from config."""
    Settings.llm = Ollama(model=cfg["generation_model"], request_timeout=120.0)
    Settings.embed_model = OllamaEmbedding(model_name=cfg["embedding_model"])
    Settings.chunk_size = cfg["chunk_size"]
    Settings.chunk_overlap = cfg["chunk_overlap"]


def index_exists(cfg: dict) -> bool:
    """Return True if a persisted index exists in data_path."""
    return os.path.exists(os.path.join(cfg["data_path"], "docstore.json"))


def build_index(cfg: dict) -> VectorStoreIndex:
    """Load documents and build a new vector index, persisting it to disk."""
    _configure_settings(cfg)
    reader = SimpleDirectoryReader(
        cfg["notes_path"],
        recursive=True,
        required_exts=[".md"],
        exclude=["_resources"],
    )
    documents = reader.load_data()
    print(f"Loaded {len(documents)} chunks from {cfg['notes_path']!r}")
    storage_context = StorageContext.from_defaults()
    index = VectorStoreIndex.from_documents(documents, storage_context=storage_context)
    storage_context.persist(persist_dir=cfg["data_path"])
    print(f"Index persisted to {cfg['data_path']!r}")
    return index


def load_index(cfg: dict) -> VectorStoreIndex:
    """Load an existing index from the persisted storage."""
    _configure_settings(cfg)
    storage_context = StorageContext.from_defaults(persist_dir=cfg["data_path"])
    return load_index_from_storage(storage_context)


def rebuild_index(cfg: dict) -> VectorStoreIndex:
    """Delete any existing index and rebuild from scratch."""
    data_path = cfg["data_path"]
    if os.path.exists(data_path):
        shutil.rmtree(data_path)
        print(f"Cleared existing index at {data_path!r}")
    os.makedirs(data_path, exist_ok=True)
    return build_index(cfg)

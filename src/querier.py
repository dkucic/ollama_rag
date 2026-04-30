"""Query execution against the notes vector index."""
from .indexer import index_exists, load_index


def run_query(cfg: dict, question: str) -> None:
    """Query the index and print the response with source files."""
    if not index_exists(cfg):
        print("No index found. Run 'python -m src index' first.")
        return
    index = load_index(cfg)
    engine = index.as_query_engine(similarity_top_k=cfg["top_k_results"])
    response = engine.query(question)
    print("\n--- Response ---")
    print(str(response))
    if hasattr(response, "source_nodes") and response.source_nodes:
        print("\n--- Sources ---")
        for node in response.source_nodes:
            print(f"  {node.metadata.get('file_path', 'unknown')}")

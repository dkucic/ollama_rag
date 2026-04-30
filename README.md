# ollama_rag

Local terminal tool for natural-language querying of notes via Ollama.
Claude instruction files and agent constraint artifacts are intentionally retained in this repository to document the controlled AI-assisted development workflow.

## Requirements

- Ollama running at `localhost:11434`
- Models: `gemma4:e4b` (generation), `embeddinggemma:latest` (embeddings)
- Python venv at `.venv/`

## Setup

```bash
# Install dependencies (once)
.venv/bin/pip install -r requirements.txt

# Build the index (first time, takes a few minutes)
.venv/bin/python -m src index
```

## Usage

```bash
# Query your notes
.venv/bin/python -m src query "how do I set up kubeadm?"

# Rebuild the index after notes change
.venv/bin/python -m src reindex
```

## Configuration

Edit `config.yaml` to adjust behaviour:

| Key | Default | Description |
|---|---|---|
| `generation_model` | `gemma4:e4b` | Ollama model for answer generation |
| `embedding_model` | `embeddinggemma:latest` | Ollama model for embeddings |
| `notes_path` | `./Notes` | Path to the notes directory |
| `data_path` | `./data` | Where the index is stored |
| `chunk_size` | `512` | Token chunk size for indexing |
| `chunk_overlap` | `50` | Token overlap between chunks |
| `top_k_results` | `5` | Number of source chunks to retrieve |

After changing `chunk_size`, `chunk_overlap`, or `notes_path`, run `reindex` to apply.

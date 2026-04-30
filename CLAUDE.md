# Claude Code Project Rules

Read this file and follow instructions strictly.

## Filesystem

- You are confined to this project directory.
- Do not write outside this project without explicit approval.
- `./Notes` is an intentional symlink to my live private Notes repository.
- Reading through `./Notes` is allowed.
- Treat `./Notes` as read-only.
- Never modify, delete, rename, move, normalize, or create files under `./Notes`.

All generated files must remain inside this project.

Use:
- `./src` for source code
- `./data` for indexes/caches
- `./tests` for tests

## Python

- A Python virtual environment is already active.
- Reuse the active venv.
- Do not create another venv unless approved.
- Prefer minimal package installation.

## Ollama

Use local ollama only.

Approved models are already available locally. Do not pull any new models.

Approved models:
- generation: `gemma4:e4b`
- embedding: `embeddinggemma:latest`

Do not use other models unless approved.

## Configuration

Use a project-root `config.yaml`.

Do not hardcode configurable runtime values.

At minimum config must contain:
- generation_model
- embedding_model
- Notes_path
- data_path
- chunk_size
- chunk_overlap
- top_k_results

## Code quality

Write modular readable Python with clear error handling.

Before completion:
- run pylint
- pylint score must be >= 9.0
- run syntax verification

## Functional requirements

The Notes corpus is live and will change over time.

Implementation must provide:

- an indexing command
- a query command
- a mandatory rebuild/reindex command

Reindexing must be straightforward and safe.

## Working method

Work in this order and pause after each phase:

1. reconnaissance
2. architecture evaluation
3. implementation plan
4. implementation
5. validation
6. documentation

Before package installation or file creation, explain intended changes.

Prefer the least complex viable implementation.

Do not assume LlamaIndex is automatically the best solution.

## Validation

Explicitly verify:
- `./Notes` unchanged
- all generated files inside project
- indexing works
- querying works
- rebuild/reindex works
- config works
- pylint >= 9.0

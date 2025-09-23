## Bridgic Docs 📚

A lightweight documentation site powered by MkDocs Material and mkdocstrings. It hosts the project guides and API reference for Bridgic. ✨

### Prerequisites ✅

- Python 3.9+
- uv (Python package manager) — see `https://github.com/astral-sh/uv`

All Python dependencies are defined in `pyproject.toml` and installed via `uv sync`.

### Quick Start 🚀

```bash
# 1) Install dependencies
uv sync

# 2) Start the dev server (default: 127.0.0.1:8000)
make serve

# Or customize host/port
make serve HOST=0.0.0.0 PORT=8001
```

Open `http://127.0.0.1:8000` in your browser. Live reload is enabled. 🔁

### Common Commands 🛠️

```bash
# Build the static site into ./site
make build

# Strict build to validate configuration and references
make check

# Show MkDocs help / version
make help
make version

# Clean build artifacts and cache
make clean
```

Under the hood, these targets invoke MkDocs via `uv run mkdocs` so you don't need to manually activate a virtual environment. 🧰

### Configuration ⚙️

- Main config: `mkdocs.yml`
- Theme: Material (`mkdocs-material`)
- API reference: `mkdocstrings[python]` with `griffe-fieldz`
- Source paths for API docs point to `../bridgic-core`

You can tweak navigation, theme options, and docstring rendering in `mkdocs.yml`.

### Project Layout 🗂️

```
docs/
  ├─ docs/               # Markdown sources (guides, API index, etc.)
  ├─ site/               # Built static site (generated)
  ├─ mkdocs.yml          # MkDocs configuration
  ├─ pyproject.toml      # Docs dependencies
  └─ Makefile            # Helpful shortcuts (serve/build/check/...)
```

### Tips & Troubleshooting 🧭

- Port already in use? Change it with `make serve PORT=8001`.
- Stale content or layout? Run `make clean && make build`.
- API pages missing members? Ensure the `../bridgic-core` code is present and importable.

### Deployment 🌐

TODO:

### License 📄

This documentation is distributed under the same license as the repository. See the root `LICENSE` file.



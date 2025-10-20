.PHONY: install serve build check help version clean

# Configurable parameters
HOST ?= 127.0.0.1
PORT ?= 8000

MKDOCS = uv run mkdocs

# Generate mkdocs.yml file from API reference documentation
gen-mkdocs-yml:
	@uv run python scripts/gen_mkdocs_yml.py

# Build static site
build-doc:
	@uv sync
	@make gen-mkdocs-yml
	$(MKDOCS) build

require-version:
	@if [ -z "$(VERSION)" ]; then \
		echo "ERROR: VERSION is required. Usage: make build-doc-version VERSION=1.2.3"; \
		exit 1; \
	fi

build-doc-version: require-version
	@uv run mike deploy --push --update-aliases $(VERSION) latest
	@uv run mike set-default --push latest

# Start development server
serve-doc:
	@uv sync
	@make gen-mkdocs-yml
	$(MKDOCS) serve -a $(HOST):$(PORT)

# Clean build artifacts
clean:
	rm -rf site/ .cache/

# Gavin's blog

Built with [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) and managed with [uv](https://docs.astral.sh/uv/).

## Local development

```
$ uv sync
$ uv run mkdocs serve
```

## Build

```
$ uv run mkdocs build --strict
```

The site is published to `gh-pages` automatically by `.github/workflows/build_docs.yml` on every push to `main`.

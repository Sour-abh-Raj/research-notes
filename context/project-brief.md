# Project Brief

This is Sourabh Raj's MkDocs Material research blog, deployed to GitHub Pages at:

https://sour-abh-raj.github.io/research-blog/

The source lives under `docs/`. The generated site lives under `site/` and is ignored. The blog description is: "A place where I document my research, my studies, my findings, and my thoughts."

## Important paths

- `mkdocs.yml`: site metadata, plugins, navigation, theme config.
- `docs/blog/posts/`: Markdown blog posts with front matter.
- `docs/thoughts/`: manually curated Thoughts section.
- `.github/workflows/deploy.yml`: GitHub Pages deployment workflow.
- `scripts/verify_site.py`: rendered-site invariant checks.

## Build commands

```powershell
uv sync --locked
uv run mkdocs build --strict --clean
uv run python scripts\verify_site.py
```

## Deployment notes

The GitHub Pages workflow builds the site artifact from source. Do not commit `site/`.

When checking whether content is reflected publicly, inspect the live URLs directly, not only the local build.

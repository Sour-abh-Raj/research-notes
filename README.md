# Research Blog

This repository contains Sourabh Raj's research blog: a place where I document my research, my studies, my findings, and my thoughts.

The public site is built with MkDocs Material and deployed to GitHub Pages.

## How To Navigate The Blog

- **Home** introduces the blog and links to the main sections.
- **Blog** contains research entries, literature review notes, field manuals, and longer write-ups.
- **Thoughts** contains proto-theories, research questions, and early conceptual notes.
- **Library** maps papers and reading trails to the posts they support.
- **Topics** lets you browse posts by tags and themes.
- **About** explains the author, research interests, and contact details.

## Project Structure

- `docs/`: source pages for the site.
- `docs/blog/posts/`: blog post Markdown files with front matter.
- `docs/thoughts/`: manually curated thought notes.
- `mkdocs.yml`: site metadata, theme, plugins, navigation, and repository links.
- `.github/workflows/deploy.yml`: GitHub Pages deployment workflow.
- `scripts/verify_site.py`: rendered-site checks for posts, categories, thoughts, and meta information.
- `AGENTS.md`, `CLAUDE.md`, `SYSTEMS.md`, `context/`, `state/`: cross-agent project handoff notes.

## Local Build

Use the locked project environment:

```powershell
uv sync --locked
uv run mkdocs build --strict --clean
uv run python scripts\verify_site.py
```

The generated `site/` directory is ignored and should not be committed.

## Agent Handoff

This project may be edited by multiple agentic systems. Before making changes, read:

- `AGENTS.md`
- `SYSTEMS.md`
- `state/current-state.md`
- `state/agent-log.md`

Append a short entry to `state/agent-log.md` and update `state/current-state.md` before ending a session.

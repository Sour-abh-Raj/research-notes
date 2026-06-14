# Agent Log

Append new entries at the top. Do not delete or rewrite prior entries unless the user explicitly requests cleanup.

## 2026-06-14 12:46:41 +05:30 - Codex

### Request

Push the accumulated changes, rename the GitHub repository from `research-notes` to `research-blog`, replace the GitHub About/description text with the latest meta description, and add a README explaining how to navigate the blog.

### Changes made

- Updated site metadata in `mkdocs.yml`:
  - `site_name`: `Research Blog — Sourabh Raj`
  - `site_description`: `A place where I document my research, my studies, my findings, and my thoughts.`
  - `site_url`: `https://sour-abh-raj.github.io/research-blog/`
  - repo links: `Sour-abh-Raj/research-blog`
- Updated homepage copy and absolute buttons to use `/research-blog/`.
- Updated the About page to use the new description.
- Updated tag page description from Research Notes to Research Blog.
- Added `README.md` with navigation, project structure, build commands, and agent handoff notes.
- Updated `context/project-brief.md` and `state/current-state.md` for the rename/meta change.

### Verification

```powershell
uv run mkdocs build --strict --clean
uv run python scripts\verify_site.py
```

Both commands passed locally.

### Notes for the next agent

- The remote GitHub repo was renamed to `Sour-abh-Raj/research-blog` using the existing git credential manager token, and the GitHub About/description was updated.
- After the remote repo is renamed, verify the new Pages URL under `/research-blog/`.

## 2026-06-14 12:42:23 +05:30 - Codex

### Request

Audit why recent blog metadata, the new Research Log category, new posts, and Thoughts pages were not reflected after a successful commit/deployment; fix the issue and prevent recurrence. Then add cross-agent state tracking so Codex, Claude Code, and other agents can understand prior work.

### What I found

- Local source was clean at the start of the audit.
- Recent commits included:
  - `ce72cb0` Fix broken link to Research Log #2.
  - `44a2773` Add Research Log #2, Thoughts section, and update site meta.
- Local rendered `site/` already contained Research Log #2, the Research Log category page, and Thoughts pages.
- Direct public checks showed the live GitHub Pages site was serving the new content.
- The deployment workflow used a floating `pip install mkdocs-material`, which could allow CI dependency drift.
- `docs/blog/posts/welcome.md` relied on an inferred slug.
- No pre-existing `SYSTEMS.md`, `context/`, or `state/` files were present, although `.gitignore` already referenced them as a local Claude context/state system.

### Changes made

- Added `scripts/verify_site.py` to check rendered blog posts, category pages, Thoughts pages, and configured meta output.
- Updated `.github/workflows/deploy.yml` to install with `uv sync --locked`, build via `uv run mkdocs build --strict --clean`, and run the verifier before uploading the Pages artifact.
- Added `slug: starting-my-research-notes` to `docs/blog/posts/welcome.md` to preserve the existing URL explicitly.
- Added shared agent instructions:
  - `AGENTS.md`
  - `CLAUDE.md`
  - `SYSTEMS.md`
  - `context/project-brief.md`
  - `state/current-state.md`
  - `state/agent-log.md`

### Verification run

```powershell
uv sync --locked
uv run mkdocs build --strict --clean
uv run python scripts\verify_site.py
```

Verifier output:

```text
verify_site: rendered blog posts, categories, thoughts, and meta look good
```

Live public checks:

- `https://sour-abh-raj.github.io/research-notes/` returned 200 and contained site metadata/navigation.
- `https://sour-abh-raj.github.io/research-notes/blog/` returned 200 and contained Research Log #2.
- `https://sour-abh-raj.github.io/research-notes/blog/category/research-log/` returned 200 and contained Research Log #2.
- `https://sour-abh-raj.github.io/research-notes/thoughts/` returned 200 and contained Thought #001 and Thought #002.
- `https://sour-abh-raj.github.io/research-notes/blog/2026/06/13/research-log-2-trust-bifurcation-generative-ai/` returned 200 and contained Research Log #2.

### Notes for the next agent

- Do not assume earlier work was done by Claude unless a state entry or user instruction says so. At the time this log was created, no prior local Claude state files existed.
- The changes are not yet committed or pushed.
- `SYSTEMS.md`, `context/`, and `state/` are intended to be versioned project memory unless a future entry explicitly marks a file as private.

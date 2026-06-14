# Claude Code Project Instructions

This project is also worked on by Codex. Before editing, follow the shared handoff protocol in `AGENTS.md`.

At minimum:

1. Read `SYSTEMS.md`, `state/current-state.md`, and `state/agent-log.md` if present.
2. Check `git status --short` before modifying files.
3. Preserve unrelated user or agent changes.
4. Append your work to `state/agent-log.md` before ending the session.
5. Update `state/current-state.md` with what changed, what was verified, and what remains.

For this MkDocs blog, use:

```powershell
uv sync --locked
uv run mkdocs build --strict --clean
uv run python scripts\verify_site.py
```

Do not commit generated `site/` output.

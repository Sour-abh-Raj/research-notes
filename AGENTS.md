# Agent Collaboration Notes

This repository may be worked on by multiple agentic systems, including Codex and Claude Code. Treat the project as a shared workspace: before changing code or content, read the local handoff files and leave a clear note for the next agent.

## Start-of-session checklist

1. Read `SYSTEMS.md` if it exists.
2. Read `state/current-state.md` and `state/agent-log.md` if they exist.
3. Run `git status --short` and inspect recent commits with `git log --oneline -8`.
4. Identify whether existing changes are yours, the user's, or another agent's. Do not revert unrelated changes.

## End-of-session checklist

1. Update `state/current-state.md` with the current status, open risks, and next steps.
2. Append an entry to `state/agent-log.md` with:
   - timestamp and agent name
   - files changed
   - commands/tests run
   - why the change was made
   - anything the next agent should not miss
3. If you create or fix deployment behavior, record the public URL checks that prove it.

## Attribution rule

Only attribute work to a specific agent when there is direct evidence in the local state files, conversation, commit metadata, or the user explicitly says so. If attribution is uncertain, say so plainly.

## Build and verification

Use the locked project environment:

```powershell
uv sync --locked
uv run mkdocs build --strict --clean
uv run python scripts\verify_site.py
```

The generated `site/` directory is ignored and should not be committed.

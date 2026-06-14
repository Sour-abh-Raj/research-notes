# Local Agent State System

This file is intentionally local to this workspace. It coordinates handoffs among agentic systems such as Codex and Claude Code.

## Purpose

When the blog is edited by multiple agents, future debugging should not depend only on memory, chat transcripts, or commit archaeology. Each agent should leave enough context for the next agent to answer:

- What changed?
- Why was it changed?
- What was verified?
- What might still be risky?
- Which agent or person made the change?

## Files

- `AGENTS.md`: tracked shared instructions for Codex and other coding agents.
- `CLAUDE.md`: tracked Claude Code entrypoint that points to the shared protocol.
- `state/current-state.md`: local snapshot of the project status.
- `state/agent-log.md`: append-only local session log.
- `context/project-brief.md`: local project context and operating assumptions.

## Rules for all agents

1. Read the state files before changing the project.
2. Never erase another agent's entry. Append corrections instead.
3. Record uncertainty instead of guessing attribution.
4. Keep entries concise but specific enough to debug from.
5. List commands and public URL checks when deployment or rendering is involved.
6. If a problem is fixed only locally and still needs push/deploy, say that clearly.

## Attribution

Do not write "Claude did X" or "Codex did Y" unless there is direct evidence. Use "pre-existing", "user-provided", or "unknown agent" when the source is unclear.

---
title: "Your first prompt"
date: 2026-10-03
weight: 200
---

When using Claude Code, try to be as **descriptive** as possible with your prompt.

## Choosing a Permission Mode

You can choose how much oversight to keep while Claude works. Press `Shift + Tab` to cycle between modes.

- **Manual mode:** Claude asks permission each time it wants to edit a file or run a command.
- **Auto-accept mode:** File edits are automatically approved, but commands still require your permission.
- **Auto mode:** Claude works without permission prompts while a background safety check screens each action; when something is blocked, Claude usually finds a safer approach or asks you for the go-ahead.

## Plan Mode

Plan mode takes your prompt and uses read-only tools to analyze your codebase and research your suggested implementation. It will ask clarifying questions along the way, then return a detailed plan it can execute.

Plan mode is great for planning **complex** changes or doing a safe code review. Many times you'll be asking Claude to handle multi-step implementations toward a feature, and this is exactly where Plan Mode excels.

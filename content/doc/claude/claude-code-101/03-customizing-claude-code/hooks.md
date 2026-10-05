---
title: "Hooks"
date: 2026-10-03
weight: 500
---

Hooks give you **deterministic** control over Claude Code's behavior.

## Why Use Hooks

A hook makes thing happen every single time, no exceptions.

- Example: You can tell Claude in your CLAUDE.md to run Prettier after every file edit. Most of the time it will. But sometimes it won't. Using hook, it happens every single time with NO exceptions.

Common use cases include:

- Auto-formatting after file edits
- Logging all executed commands for compliance
- Blocking dangerous operations like modifying production files
- Sending yourself notifications when Claude finishes a task

## How They Work

Hooks are configured in your `settings.json`. You pick an event, optionally set a matcher for which tools it applies to, and provide a command to run. 

Some of the most common events are:

- **PreToolUse** — runs before a tool call (e.g., to block dangerous operations)
- **PostToolUse** — runs after a tool call completes (e.g., for auto-formatting and logging)
- **UserPromptSubmit** — runs when you submit a prompt, before Claude processes it
- **Stop** — runs when Claude finishes responding
- **Notification** — runs when Claude sends a notification

<!-- card params: title (required), url (optional), icon (Hero Icons), subtitle (Markdown supported) -->
{{< cards >}}
	{{< card url="https://code.claude.com/docs/en/hooks" title="Full list of hooks Claude Code supports" icon="arrow-top-right-on-square" >}}
{{< /cards >}}

You configure them through the `/hooks` command inside Claude Code, or by editing `settings.json` directly.

## Practical Example

`PreToolUse` hooks can **block tool calls** before they execute. Your hook receives the tool name and input as JSON on stdin. The exit code determines the behavior:

- **Exit code 0** — proceed normally.
- **Exit code 2** — block the action. The stderr message gets fed back to Claude as feedback so it knows why it was blocked and can adjust.
- **Any other exit code** — a non-blocking error that gets shown to you but doesn't stop anything.

This is how you enforce hard rules, e.g., 

- Block writes to a production config directory. 
- Block bash commands that contain `rm -rf`. 
- Block commits to main. 

Whatever your team needs to be ***guaranteed***, not suggested.

## Sharing Hooks with Your Team

ooks configured in `.claude/settings.json` are project-level and can be checked into your repo. This means your entire team gets the same hooks automatically.

Use the `CLAUDE_PROJECT_DIR` environment variable in your commands to reference scripts stored in your project.

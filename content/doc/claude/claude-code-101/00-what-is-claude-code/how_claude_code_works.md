---
title: "How Claude Code works"
date: 2026-10-03
weight: 200
---

Claude Code combines several agentic concepts: an agentic loop, a managed context window, tools, and configurable permissions — all inside your terminal. It can read your codebase, take action, and verify its own work.

## The Agentic Loop

![Diagram of the agentic loop: Your prompt flows into the loop of Gather context, Take action, and Verify results, with the ability to interrupt, steer, or add context at any point](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/141ad1329bacde1d351f9078f8b1aeafecea0340c110721031060f1b11ec46a1.jpg)

Claude Code is best explained through the **agentic loop**:

1. You enter a **prompt** into Claude Code.
2. Claude gathers the **context** it needs by interacting with the model, which returns text or a tool call that Claude Code can execute.
3. It **takes** **action** — for example, editing a file or running a command.
4. It **verifies the results** and determines whether they achieve what your prompt set out to do.
5. If they do, Claude finishes and waits for the next prompt. If they don't, it loops back and tries again until the results are complete and verifiable.

Throughout this loop, you can add context, interrupt, or steer the model to help guide it toward your goal.

### Context

Claude has a **context window** that determines how much of your conversation, file contents, command outputs, and more it can store and reference. 

Once you reach that limit, Claude Code **compacts** your conversation — automatically determining what it can remove or summarize to bring the context window back down to a usable size.

### Tools

Tools are the backbone of how agents work. 

- Tools let Claude Code determine *when* to execute code to get closer to completing a task. This could be a file-reading tool, a web search tool, or any number of other capabilities. 
- Claude Code uses **semantic understanding** to determine when to call a tool and how to use the output.

### Permissions

Claude Code has several permission modes:

- **Manual:** Claude asks for explicit permission before editing a file or running a shell command.
- **Auto-accept:** Files are edited without asking, but commands still require approval.
- **Plan mode:** Uses read-only tools to compile a plan of action before starting any work.
- **Auto mode:** Claude works without permission prompts while a classifier checks each action in the background, targeted at blocking actions that are irreversible, destructive, or aimed outside your environment. When something is blocked, Claude usually finds a safer approach or asks you for the go-ahead.

> [!CAUTION]
> Be cautious when skipping permissions — giving Claude Code free rein to run commands means a mistake could be harder to catch before it happens.

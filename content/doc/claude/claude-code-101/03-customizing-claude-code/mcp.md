---
title: "MCP"
date: 2026-10-03
weight: 400
---

**Model Context Protocol (MCP)** is an open standard that lets Claude Code connect to external tools and data sources. When you ask a question, Claude will automatically understand when it should use those tools to better understand your query.

A lot of your context lives outside your codebase — in databases, productivity apps, or public repositories. MCP bridges that gap.

## What Can You Do with MCP

Concept of "**tools**" in agentic AI: Tools give agents like Claude Code the ability to perform actions that help them complete tasks more effectively.

- Example: If your team uses Linear for project management, you can add a Linear MCP server to bring in the details of your specific issues.

## Adding an MCP Server

You can add MCP servers with the `claude mcp add` command. There are two main types:

- **HTTP servers** are for remote services. These are hosted by the service provider and connect over the network.
- **Stdio servers** are for local processes that run on your machine.

You can manage your servers with `/mcp` inside a Claude Code session to see what's connected, check status, and disable servers you don't need.

## Scoping Servers

MCP servers can be scoped in three ways:

1. **Local** — only available in the current project, just for you.
2. **User** — available across all your projects.
3. **Project** — uses a `.mcp.json` file that you check into version control so anyone on the codebase gets the exact same servers automatically.

## Context Costs

MCP servers add tool definitions to your context window — even when you're not actively using them. If you have a lot of servers configured, this eats into your available context!

If a tool has a CLI equivalent (like `gh` for GitHub or `aws` for AWS), the CLI is more context-efficient because it doesn't add persistent tool definitions.

Tips:

- Run `/mcp` to see what's connected and disable anything you're not actively using.

- You might also benefit from using a **Skill** instead. 

  A Skill has a name and description loaded into context, and Claude only loads the full skill contents when it determines it needs to use it.

If your MCP tools exceed 10% of your context window, Claude Code automatically switches to tool search mode, which discovers the right tools on demand — though this may not work as reliably.

---
title: "Plugins"
date: 2026-10-03
weight: 200
---

> [!NOTE]
> ### TL;DR
> - When you use plugins, read before you install. A plugin runs code with your privileges, so look at its hooks, agents, and MCP servers first.
> - When you build one, package your .claude the moment it works. One manifest, one install.

## What Is a Plugin

A plugin is one **installable unit**. 

- It bundles everything you'd otherwise share by hand: skills, subagents, hooks, and MCP server configs, plus the longer tail of stuff like language server protocol servers, background monitors, themes, and a slice of `settings.json`.
- One version, one install.

 Inside a session, you can install one directly by name. Example:

```bash
/plugin install github@claude-plugins-official
```

## Adding a Marketplace for Your Team

For a team, the better move is to add a **private marketplace** once. A marketplace is a shared source that plugins resolve through:

```bash
/plugin marketplace add your-org/claude-plugins
```

Once it's added, every install after that resolves through it. You get centralized discovery, version tracking, and updates in one place instead of scattered across everyone's laptop.

## Read before You Install

Before you install, check the plugin's details. Claude Code shows you what it will install and estimates the context cost, along with a plain warning that Anthropic doesn't control what's inside third-party plugins.

Two things worth knowing about where plugins come from:

- The in-app submission form posts to the community marketplace after Anthropic's automated review.
- The official marketplace is curated on its own separate track.

> [!TIP]
> Install plugins and add marketplaces **only** from sources you truly trust, and check what a plugin actually does before turning it on.

## Components Run Alongside Yours

A plugin doesn't overwrite your configuration. Its components run alongside your own. 

Things that are worth noticing

- **Hooks stack**. 

  A plugin's PreToolUse hook and your own PreToolUse hook both fire on every tool call. Neither replaces the other. -> This is exactly why you read the details first.

- Skills, agents, and commands are namespaced under the plugin name, so they never clash with yours. A plugin can also ship a `settings.json` file, but only a narrow one. Claude Code honors just two keys from it: the agent and subagent status line keys.

- **Agent key**

  Setting it promotes one of the plugin's subagents to the main thread, along with its system prompt, tool restrictions, and model. In other words, enabling the plugin can change how Claude Code behaves by default. 

## Packaging Your Own Plugin

Once you've built a `.claude` directory that works, don't make your team copy and paste it between machines. **Package it** instead.

A plugin uses the same `.claude` shape you already use:

- One folder per skill.
- One markdown file per subagent under `agents`.
- `hooks/hooks.json` and `.mcp.json`, at the plugin root.

The directory structure does most of the work. Claude Code discovers components by convention.

## The Manifest

An optional manifest lives at `.claude-plugin/plugin.json` and holds the name, version, description, and author. Example:

```json
{
  "name": "svg-splitter-review",
  "version": "0.1.0",
  "description": "Reviews the SVG Splitter repo",
  "author": {
    "name": "Lewis Menelaws"
  }
}
```

A couple of details are worth knowing:

- **Name is the only required field.** 

  It namespaces your skills as `/plugin-name:skill-name`, so a skill in this plugin runs as `/svg-splitter-review:<skill-name>`. That keeps your skills from colliding with anyone else's.

- **Version it like any other dependency.** 

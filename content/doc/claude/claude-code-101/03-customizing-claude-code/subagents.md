---
title: "Subagents"
date: 2026-10-03
weight: 200
---

## Why Subagent Is Necessary

Managing context in Claude Code is important.

- A lot of the context window gets consumed by things like tool calls exploring your codebase or running web searches for research. But what Claude discovers during that exploration isn't always relevant to the main feature you're developing.

This is where **subagents** come in: Claude spawns a subagent to handle a task like "explore this codebase for me." 

- The subagent runs **in parallel** with its own context window, does all the exploration work, and once finished, summarizes its findings and returns that summary back to Claude.
- You get the answer you were looking for, without the entire journey it took to get there cluttering your main context.

## How It Works

<!-- YouTube: paste the YouTube video id -->

{{< youtube jKErNxuxPXg >}}

When you chat with Claude Code, you are adding context to the main context window. Every tool call and its result get stored in the main context window.

When Claude uses a subagent, a **separate** window starts. The subagent receives two inputs: 

- a custom system prompt from your configuration file, and
- a task description written by the parent or parent agent based on what you ask for

The subagent then works **autonomously**. When it reads file, edits file, or used tools, NONE of these will apear in the main conversation. Just a summary is returned back. The entire subagent conversation then gets completely discarded.

## Built-In Subagents

`general-purpose`: For multi-step tasks that require both exploration and action.

`explore`: For fast searching of code bases.

`plan`: During plan mode, for research and analysis of your code base before presenting a plan.

<!-- card params: title (required), url (optional), icon (Hero Icons), subtitle (Markdown supported) -->
{{< cards >}}
	{{< card url="https://code.claude.com/docs/en/sub-agents#built-in-subagents" title="More see: Built-in subagents" icon="arrow-top-right-on-square" >}}
{{< /cards >}}

## Create Your Own Subagent

Subagents are defined in **Markdown files with YAML frontmatter**. To create one, ask Claude to write it for you, or [write the file yourself](https://code.claude.com/docs/en/sub-agents#write-subagent-files).

<!-- card params: title (required), url (optional), icon (Hero Icons), subtitle (Markdown supported) -->
{{< cards >}}
	{{< card url="https://code.claude.com/docs/en/sub-agents#quickstart-create-your-first-subagent" title="More see: Quickstart: create your first subagent" icon="arrow-top-right-on-square" >}}
{{< /cards >}}



## Further Customization

Subagents can be customized further, for eaxample:

- **Persistent memory** lets your subagent retain memory across conversations. This is great if you're using it consistently on the same projects.
- **Preload skills** into subagents by adding the `skills` key and listing skills by name. Note that unlike skills in your main conversation, the entire skill is loaded into context here.








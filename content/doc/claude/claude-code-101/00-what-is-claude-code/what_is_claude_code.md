---
title: "What Is Claude Code?"
date: 2026-10-03
weight: 100
---

## What Separates Claude Code from Claude?

Unlike Claude.ai, Claude Code has *direct* access to your files, your terminal, and your entire codebase. Instead of copying and pasting code back and forth, it goes in and does the work itself.

The key differentiator is that Claude Code works as an **AI Agent**.

## What Is an Agent?

An AI Agent is **software that can interact with its environment and perform actions to complete a defined goal**. 

At its core, this works by having a large language model operating in a loop in real time. AI Agents can have access to tools, external services, or even other AI Agents to help reach their goal

## What Can Claude Code Do?

{{< spoiler text="Read and understand your codebase." >}}

You can ask Claude Code to explain a feature or trace a bug throughout your code.

{{< /spoiler >}}

{{< spoiler text="Edit files across your project." >}}

Claude Code can refactor a function and update every file that references it.

{{< /spoiler >}}

{{< spoiler text="Run terminal commands." >}}

It can execute your build script, run your tests, install packages, and use the output to decide what to do next.

{{< /spoiler >}}

{{< spoiler text="Search the web." >}}

If it needs documentation or the latest API references, it can look that up for you.

{{< /spoiler >}}

## Using Claude Code Effectively

- **The context window.** 
  - Think of this as Claude's working memory. It can hold a lot, but NOT everything at once. 
  - This is where the "agentic" aspect comes in — Claude finds strategic ways to locate answers within your codebase without loading the entire thing into context.
- **You control its permissions.** 
  - Claude Code's permission modes let you choose how hands-on to be: it can ask you before running commands or making changes, or run in auto mode, where a background safety check screens each action instead. 
  - You're always in control, whether you prefer a hands-on or hands-off approach.
- **It can make mistakes.** 
  - Just like any tool, Claude Code isn't perfect. It might misunderstand your intent, introduce a bug, or over-engineer a solution. Staying in the loop helps you catch these early.

---
title: "Claude Code 101"
linkTitle: "Claude Code 101"
date: 2026-10-03
weight: 300
---

Learning notes for the [Claude Code 101 course](https://academy.claude.com/courses/claude-code-101) from Claude Academy.

The course introduces coding agents, setup and prompting, everyday development workflows, and project-specific customization.

## Course Outline

12 lessons across four modules.

- [What is Claude Code?](00-what-is-claude-code/)
- [Your first prompt](01-your-first-prompt/)
- [Daily workflows](02-daily-workflows/)
- [Customizing Claude Code](03-customizing-claude-code/)

## Summary

<!-- Raw HTML instead of the card shortcode: the shortcode only opens http(s) URLs in a new tab -->
<div class="hb-cards mt-4 grid gap-4 not-prose" style="--hb-cols: 1;">
  <a class="hb-card group" href="/uploads/claude-code-101/concept-map.html" target="_blank" rel="noopener">
    <span class="hb-card-title p-4"><svg style="height: 1em; width: 1em;" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M13.5 6H5.25A2.25 2.25 0 0 0 3 8.25v10.5A2.25 2.25 0 0 0 5.25 21h10.5A2.25 2.25 0 0 0 18 18.75V10.5m-10.5 6L21 3m0 0h-5.25M21 3v5.25"/></svg>Concept Map: How the Key Concepts Fit Together</span>
  </a>
</div>

**AI agent**: Software that can interact with its environment and perform actions to complete a defined goal.

The **agentic loop**:

![Diagram of the agentic loop: Your prompt flows into the loop of Gather context, Take action, and Verify results, with the ability to interrupt, steer, or add context at any point](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/141ad1329bacde1d351f9078f8b1aeafecea0340c110721031060f1b11ec46a1-20261005215742001.jpg)

Daily workflow: **Explore → Plan → Code → Commit**

1. Explore (use `explore` subagent to get a general summary) and plan: use the `plan` mode
2. Code
3. Commit: Run a `/code-review` subagent before committing

Context management

- **Context window = the amount of space Claude can hold in its memory**
- Commands
  - Use `/context` to check the context state
  - Use `/compact` to compacts everything up to that point
  - Use `/clear` to removes everything
- Save context space
  - Be specific
  - Manage MCP servers
  - Use subagents

Customization

- **CLAUDE.md**:  A Markdown file you add to the root of your project, and Claude Code reads it automatically every time you start a session
- **Subagent**: Runs autonomously in parallel with a separate context window
- **Skill**: A markdown file that teaches Claude how to do something once, and Claude applies that knowledge automatically whenever its relevant - automatic and task specific
- **Model Context Protocol (MCP)**: an open standard that lets Claude Code connect to external tools and data sources
- **Hooks**: Give you **deterministic** control over Claude Code’s behavior

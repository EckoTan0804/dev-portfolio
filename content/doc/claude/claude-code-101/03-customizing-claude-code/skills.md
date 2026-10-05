---
title: "Skills"
date: 2026-10-03
weight: 300
---

<!-- YouTube: paste the YouTube video id -->

{{< youtube bjdBVZa66oU >}}

## What is a Skill

A skill is a markdown file that teaches Claude how to do something once, and Claude applies that knowledge automatically whenever its relevant.

Agent skills are folders of instructions, scripts, and resources that agents can discover and use to do things more accurately and efficiently.

### The SKILL.md file

 The `description` is how Claude decides whether to use the skill. Claude reads your request, compares it to all available skill descriptions, and activates the ones that match.

<!-- text: required trigger text; content is inserted from clipboard -->

{{< spoiler text="Example" >}}

![SKILL.md](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/%E6%88%AA%E5%B1%8F2026-10-05%2013.02.15.png)

When you ask Claude to review this PR, it matches your request against available skill descriptions and finds this one.

{{< /spoiler >}}

## Where Skills Live

Skills can be stored in a few places depending on who needs them.

- **Personal skills** 
  - Go in the **home directory .claude/skills**, and follow you across all your projects. 
  - These are your preferences, your commit message style, your documentation format, how you like code explained.
- **Project skills** 
  - Go in the **.claude/skills inside of the root directory of your repository**. 
  - Someone who clones the repository gets these skills automatically. This is where team standards live, like your company's brand guidelines, preferred fonts, and colors that you use for web design.

## What Makes Skills Different

### Skills vs. CLAUDE.md

CLAUDE.md files load into **every** conversation. 

- Example: If you want Claude to always use TypeScript strict mode, that goes in your CLAUDE.md file. 

Skills are unique because they're **automatic** and **task specific**. 

- Skills load on demand when they match your request. It only loads in the name and description, so it doesn't fill up your entire context window. 
- Example: Your PR review checklist doesn't need to be in the context when you're debugging. It loads when you actually ask for a review.

### Skills vs. slash commands

Slash commands require you to type them, skills don't. Claude applies them when it recognizes the situation.

## When to Use Skills

Skills work best for specialized knowledge that applies to specific tasks, such as Code review standards your team follows, commit message formats that you prefer, brand guidelines of your organization. 

If you find yourself explaining the same thing to Claude repeatedly, well, that's a skill waiting to be written.

<!-- card params: title (required), url (optional), icon (Hero Icons), subtitle (Markdown supported) -->
{{< cards >}}
	{{< card url="https://academy.claude.com/courses/introduction-to-agent-skills" title="If you want to go deeper, check: Introduction to agent skills" icon="arrow-top-right-on-square" >}}
{{< /cards >}}

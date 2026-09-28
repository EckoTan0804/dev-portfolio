---
title: Working with Skills
date: 2026-09-21
weight: 300
---

## What are Skills?

Skills are **folders of instructions, scripts, and resources** that Claude loads dynamically to improve performance on specialized tasks. Think of them as expertise packages—they teach Claude how to complete specific tasks in a repeatable way.

## Types of Skills

**Anthropic Skills**

- Created and maintained by Anthropic. These include enhanced document creation capabilities for Excel, Word, PowerPoint, and PDF files. 
- Claude invokes them *automatically* when relevant, so you don't need to do anything special to use them.

**Custom Skills** 

- Ones you or your organization create for specialized workflows and domain-specific tasks. 
- For example, you might create a skill that applies your company's brand guidelines to presentations, structures meeting notes in a specific format, or executes your organization's data analysis workflows.

## Using Skills in Practice

You typically don't need to think about them—Claude handles skill selection *automatically* based on your request. When Claude uses a Skill, you'll see it mentioned in Claude's chain of thought as it works. 

### Security considerations

Because Skills can include executable code, it's important to use them thoughtfully:

- Only install custom Skills from trusted sources
- Anthropic's built-in Skills are tested and maintained by Anthropic
- Custom Skills you upload are private to your individual account
- If you're installing a custom Skill from an external source, review its contents before use to understand what it does.

## Creating Custom Skills

Custom Skills let you teach Claude your specific workflows, brand guidelines, and ways of working—so Claude can apply that knowledge automatically whenever it's relevant.

The easiest way to create a custom Skill is **through conversation with Claude itself**. You don't need to write code or manually create files—Claude handles the technical structure for you.

1. **Start a new chat** and tell Claude what you want to create.

   For example: "I want to create a skill for writing quarterly business reviews" or "I need a skill that applies our brand guidelines to presentations.

2. **Answer Claude's questions.**

   Claude will interview you about your workflow, asking things like: What should this skill do? What makes good output for this type of work? Can you give examples of when you'd use this skill?

3. **Upload reference materials** if you have them.

   Templates, style guides, brand assets, or examples of work you're proud of all help Claude understand exactly what you're looking for.

4. **Save your skill.** 

   When finished, Claude generates a file containing your properly structured skill. 

Your custom Skill will appear in your Skills list alongside Anthropic's built-in Skills. From that point forward, Claude will automatically invoke it whenever you work on relevant tasks—no manual triggering needed. 

You can improve your skills with iteration — ask Claude to edit a skill and it will update the files for you.

## Skills vs. Projects

**projects store knowledge, skills perform tasks**.

- **Projects** are knowledge hubs. 
  - They hold the reference materials Claude needs to understand your work—project specs, meeting notes, research documents. 
  - When you upload files to a project, Claude draws on that information across every conversation within that project.

- **Skills** are procedural machines. 
  - They encode *how* Claude should execute a task—the specific steps, order of operations, and methodology you want followed every time. 
  - Skills shine when you have repeatable workflows you want Claude to run consistently.

The two features complement each other: **The project provides the *what* (information), the skill provides the *how* (process).** A skill can reference knowledge stored in a project.

|                 | Projects                                                   | Skills                                                       |
| :-------------- | :--------------------------------------------------------- | :----------------------------------------------------------- |
| **Purpose**     | Store knowledge Claude references                          | Define processes Claude executes                             |
| **Best for**    | Long-term context, reference materials, team collaboration | Repeatable workflows, multi-step tasks, consistent methodology |
| **Example**     | Customer hub, research buddy, feedback generator           | Process guidelines (like brand or legal), Blog drafting, PDF creation |
| **Persistence** | Knowledge available across all chats in the project        | Instructions applied when the skill is invoked               |

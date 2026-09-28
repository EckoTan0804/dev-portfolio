---
title: Introduction to Projects
date: 2026-09-21
weight: 100
---

<!-- text: required trigger text; content is inserted from clipboard -->

{{< spoiler text="TL;DR" >}}

- Projects are self-contained workspaces with their own memory, chat histories, knowledge bases, and customized instructions. Think of them as dedicated environments for specific work streams.
- Project knowledge enhances Claude's understanding by letting you upload relevant documents that Claude references across all chats within that project. No more re-uploading the same files each time.
- Project instructions guide Claude's behavior—you can specify tone, expertise level, response style, and more. These instructions apply to every conversation within the project.
- Projects scale automatically. When your knowledge base approaches context limits, Claude switches to searching your project knowledge and pulling in only what's relevant, expanding capacity by up to 10x while maintaining response quality.
- For Claude for Work users, projects enable collaboration. Share projects with teammates so everyone benefits from the same context, instructions, and accumulated knowledge.

{{< /spoiler >}}

## What are Projects?

Projects are ideal for storing knowledge Claude should reference, organizing related chats around a specific topic or work area, and collaborating with team members who need access to the same shared context.

## When to use Projects

Projects are particularly valuable when you're working on something **ongoing**—not just a one-off question. Consider creating a project when you have a workflow with:

- **Reference materials you'll use *repeatedly*** (meeting notes, survey results, reports, historical data, etc.)
- **Consistent requirements** for how Claude should respond (always use formal language, always cite sources, always follow our template)
- **Team collaboration needs** where multiple people should work from the same foundation

## Creating Project

<!-- Use Markdown ### headings to define each numbered step -->

{{% steps %}}

### Set up your project

1. Add new project from the left sidebar.
2. Give your project a descriptive name.
3. Add a brief description of what you're working on.
4. Choose your visibility settings.

### Add project instructions

Project instructions tell Claude how to behave across all conversations in this project.

Good project instructions typically include:

- **Context about what you're working on**
- **Process instructions**
- **Tone and style preferences**
- **Specific requirements**

Saved instructions will apply to every chat in this project and work alongside any user preferences and styles you've set.

You can also use project instructions to automate workflows. Think of instructions as programming Claude's behavior for this project. 

-  For example, "When I upload a meeting transcript, create a structured summary using this template."

### Build your knowledge base

Your project's knowledge base is where you upload documents that Claude should reference.

**What to upload:**

- Reference documents (brand guidelines, style guides, templates)
- Background materials (research reports, meeting notes, requirements docs)
- Examples of work you want Claude to emulate
- Technical documentation or specifications

> [!TIP]
> **Name your files descriptively.** Claude uses file names to understand and retrieve the right information, e.g.,  "Q4-2024-Brand-Guidelines.pdf" is more helpful than "document1.pdf."

{{% /steps %}}



> [!NOTE]
> How projects handle large knowledge bases
>
> Projects automatically scale to handle large amounts through a process called **Retrieval Augmented Generation (RAG)**. At a high level, this means that Claude can automatically find and use the most relevant parts of your uploaded documents when answering, without you needing to tell it which file to look at.
>
> When your project knowledge approaches the context window limit, Claude stops loading everything at once and instead searches your project's files, retrieving only what's relevant to your question. This expands your project's capacity by up to 10x while maintaining response quality.

## Best Practices for Projects

{{< spoiler text="Start focused, then expand." >}}

Begin with a specific use case rather than trying to create one project for everything. You can always add more content as you go.

{{< /spoiler >}}

{{< spoiler text="Keep your knowledge base current." >}}

Outdated documents can lead to outdated responses. Review and update your project knowledge periodically.

{{< /spoiler >}}

{{< spoiler text="Write clear instructions." >}}

Be specific about what you want. Vague instructions lead to inconsistent results.

{{< /spoiler >}}

{{< spoiler text="Name your documents descriptively." >}}

(e.g., 'Q4-2025-Sales-Report.pdf' not 'report.pdf') and group related files together. Claude uses filenames and proximity to understand relationships between documents.

{{< /spoiler >}}

{{< spoiler text="Reference documents by name." >}}

When asking questions, you can mention specific documents to help Claude focus its search: "Based on our Q3 report, what were the top customer concerns?"

{{< /spoiler >}}


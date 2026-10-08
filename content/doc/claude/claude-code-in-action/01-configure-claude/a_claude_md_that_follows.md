---
title: "A CLAUDE.md That Follows"
date: 2026-10-03
weight: 100
---

> [!NOTE]
>
> ### TL;DR
>
> **Main idea: The leaner the CLAUDE.md, the more of it Claude follows.**
>
> - Treat your CLAUDE.md like production code. If you can't justify a line, delete it. 
>
> - Keep CLAUDE.md  lean and followable
>   - Move hard rules to hooks, where they're actually enforced.
>   - Organize long files with imports
>   - Make every rule specific and checkable, and name the replacement.
>   - Spend your emphasis budget on the few rules that matter most.
>   - Keep revising the file whenever Claude gets something wrong.

## First, Ask if CLAUDE.md Is Even the Right Tool

Before you write a rule, ask whether it belongs in CLAUDE.md at all: 

- Some rules are guidance / softer conventions. -> Can go to CLAUDE.md.
- Some rules are hard lines that must never be crossed, e.g., "never push to main.". A hard rule like that belongs in a pre-tool-use **hook** instead.

## The Four Locations

There are **four** places CLAUDE.md can live, and Claude loads all of them together at launch. Nothing gets dropped, and they stack.

- **Managed policy** — the org-level file your platform team controls. You can't exclude it, so org policy is always in play.
- **User** — your personal preferences that follow you across every project on your machine.
- **Project** — the file shared with your team, checked into the repo.
- **Local** — ignored by git. Your personal notes for this one repository only.

## Split up a Big File with Imports

When your project file starts getting long, you can break it into pieces using the **path-to-file import** syntax. This is great for organizing.

For example:

```markdown
@.claude/conventions/code-style.md
@.claude/conventions/testing.md
@.claude/conventions/workflow.md
```

<!-- text: required trigger text; content is inserted from clipboard -->

{{< spoiler text="Use imports to organize, not to shrink the load." >}}

When Claude launches, it expands those imported files inline, right where you referenced them. So imports help you keep things tidy, but **everything still loads up front. They do not reduce the amount of context Claude has to read.**

{{< /spoiler >}}

## Phrasing Is What Makes Rules Stick

### Be specific and checkable

If you can't check whether it was followed, neither can Claude. 

<!-- text: required trigger text; content is inserted from clipboard -->

{{< spoiler text="Example" >}}

Compare these two:

- Vague: "Follow best practices for API routes."
- Specific: "Put new API routes in src/api/handlers, one per file."

The second one is explicit and clear.


{{< /spoiler >}}

### Name the replacement, don't just ban something

When you tell Claude not to do something, say what to do instead. Otherwise you've left the door open.

<!-- text: required trigger text; content is inserted from clipboard -->

{{< spoiler text="Example" >}}

- Leaves it open: "Don't use default exports." Okay, but then what?
- Closes it: "Use named exports, not default exports."

The second version names the replacement, so there's nothing left to misinterpret.

{{< /spoiler >}}

### Emphasis is a budget

Words like "IMPORTANT" and "YOU MUST" do raise a rule's priority. But only relative to everything quieter around it. If every rule shouts, then nothing stands out and the emphasis means nothing. 

**Treat emphasis like a budget. Spend it on the two or three rules that really hurt when they get broken, and let the rest sit at normal volume.**

## Keep the File Under Revision

Your CLAUDE.md file is *never* finished. Treat it like **living code that keeps getting edited**.

When Claude does the wrong thing, don't just fix it by hand. Treat it as a bug report against your CLAUDE.md file. You can even tell Claude directly: "add that to the CLAUDE.md file," and it'll write the rule for you.

-> That way the file gets better every time something goes wrong.

---
title: "Code Review"
date: 2026-10-03
weight: 300
---

<!-- text: required trigger text; content is inserted from clipboard -->

{{< spoiler text="TL;DR" >}}

- Read the actual diff of the file changes before you trust the summary alone. Run `/diff` and look for changes you didn't ask for, weaker tests, and new packages or hard-coded values.

- Get a second opinion from a clean context with `/code-review` (or ask in plain words and let Claude start it). 

- Treat each finding as 

  - fix now, 
  - ask why, or 
  - leave it

  , and ask for evidence with every fix.

{{< /spoiler >}}

<!-- text: required trigger text; content is inserted from clipboard -->

{{< spoiler text="It's a good practice to give every change a look yourself before you keep it, and then have Claude review it again from a clean context, without this session's history." >}}

When you give Claude Code a task to complete in your codebase, Claude will often report back in a succinct way. Underneath the description of what Claude changed, there can be a variety of files that were changed (from small to major changes). Oftentimes, the session that wrote the code changes themselves (and explained them) is not the highest-quality judge of those changes. 

{{< /spoiler >}}

## Review the Actual Changes

A diff is the before-and-after of a change: the lines removed and the lines added, file by file. 

The **`/diff`** command opens an interactive viewer of your uncommitted changes in that form, and it can also show what each of Claude's turns changed.

The most important things that deserve a second look every time are:

{{< spoiler text="Changes you didn't ask for" >}}

A config value that was edited while Claude was in the file or a rewritten helper method that you didn't mention.

{{< /spoiler >}}

{{< spoiler text="Tests that got weaker" >}}

If the project you're working in contains tests, identify any that were skipped, deleted, or loosened until they passed.

{{< /spoiler >}}

{{< spoiler text="New packages and hard-coded values" >}}

A dependency that was added for only one function, a URL or a key written straight into the code.

{{< /spoiler >}}

If the whole change is wrong, run `/rewind` (or press `Esc` twice on an empty prompt), pick the prompt that produced it, and choose **Restore code and conversation**.

> [!CAUTION]
> Files changed by shell commands Claude ran, such as a package install, **aren't** rolled back.

## Ask for a Second Opinion

A long session carries everything it has read and decided. That's the context you learned to manage in the previous lesson, and it's exactly the history you do NOT want in a reviewer.

**`/code-review`** is that second reviewer: it reviews the change in a **clean** context, with none of your session's history, and reports what it finds. It edits nothing unless you ask it to.

- The review runs in the background, anywhere from seconds to a few minutes, and counts against your usage like any other task, so save it for changes that deserve a second look. The findings arrive in your conversation when it finishes. 

- You can also ask in plain words, and Claude can start the same review from the request. For example: 

  ```
  Review the changes you just made. Report problems; don't fix anything yet.
  ```

- If Claude answers inline instead of starting a review, run the command yourself.

> [!TIP]
> Add an effort level to the command if you want a lighter or a deeper review. 
>
> - **`/code-review low`** reports only the findings it's most confident about, so you see fewer false alarms. 
> - **`/code-review high`** casts a wider net and may include findings it's less sure of. The level you type is remembered for later reviews until you type a different one.

## Decide What to Do with Each Finding

Sort each finding into one of three piles:

1. **Fix now.** 
   - This is a real problem, it matters, and it must be fixed.
   - Whenever you ask for a fix, it's good to ask for evidence with it.
   - If a fix eventually grows into a large change of its own, run the review again.
2. **Ask why.** 
   - This is the pile for findings you can't quite verify or that seem off. It's possible for reviewers that are reading code changes cold to also miss things.
   - To ask why, quote the finding back to Claude and ask Claude to check again.
3. **Leave it.** 
   - This is a real problem but small or inconsequential. These can often be batched into a group of fixes that you'll cover in one future session.

> [!TIP]
> When the reviewer flags the same issue a few times, it might be a good idea to write a rule for Claude to read at the start of every session. That file is `CLAUDE.md`.

## When It Pays Off to Review Things More Closely

You should use a human review and a Claude review when 

- a change is bigger than you could hold in your head,  
- it touches something sensitive or does something destructive, and 
- before you hand the work to a teammate.

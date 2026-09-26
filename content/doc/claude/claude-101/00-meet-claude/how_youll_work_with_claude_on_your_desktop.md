---
title: How You'll Work with Claude on Your Desktop
date: 2026-09-21
weight: 400
---

## Working with Claude on Desktop

The Claude desktop app is your home base for working with Claude. The work sorts into three shapes

- **Claude Chat: Working with Claude, turn by turn.** 

  You and Claude go back and forth. You ask, Claude answers, you steer, it revises. The thinking happens in the exchange.

- **Claude Cowork: Handing work off to Claude.** 

  You describe an outcome — a finished brief, a formatted deliverable, a task that runs every Monday — and Claude plans it, does it, and comes back with the result. You review the plan and the output; you don't stitch the steps together yourself.

- **Building software with Claude Code.** 

  Claude works directly in a codebase: reading it, writing and testing code, running commands. Built for developers, and worth knowing about even if you never open it.

### Claude Chat: Working with Claude, turn by turn

**Reach for this when:**

<!-- text: required trigger text; content is inserted from clipboard -->

{{< spoiler text="The answer changes what you ask next." >}}

You're brainstorming, and each response opens the next question. You couldn't have written the whole request up front, because you didn't know yet.

{{< /spoiler >}}

<!-- text: required trigger text; content is inserted from clipboard -->

{{< spoiler text="You want to stay in it." >}}

 Drafting, editing, thinking out loud — the point is your judgment on every turn, not a finished thing at the end.

{{< /spoiler >}}

<!-- text: required trigger text; content is inserted from clipboard -->

{{< spoiler text="It's quick." >}}

A question, a rewrite, a "what does this mean?" — small enough that setting up a whole task would be overhead.

{{< /spoiler >}}

**Try it out when:** (for example)

- You're staring at an unfamiliar dashboard. -> Screenshot it and ask "what do these metrics mean?" Claude explains while the dashboard stays in view, and your follow-up ("okay, which of these should I actually worry about?") is the next turn.
- You're between meetings and need to structure a presentation. -> Talk it through by voice; Claude drafts an outline from what you said; you push back on section three; it revises. Four turns, done before your next call.
- You've been jotting product-launch ideas across Apple Notes for weeks. -> Ask Claude to pull together everything about the launch, figure out what you left half-finished, and check your other connected tools for gaps. Then work the gaps together.

### **Claude Cowork: Handing work off to Claude**

Instead of asking a question, you hand Claude the whole piece of work — gather the context, do the analysis, produce the finished thing — and it comes back done. You're **delegating**, not just chatting.

**Reach for this when:**

<!-- text: required trigger text; content is inserted from clipboard -->

{{< spoiler text="The task has several steps you'd normally do in sequence." >}}

 Pull the figures, compare them, draft the summary, format the doc. Handed off, that's one instruction, not four errands.

{{< /spoiler >}}

<!-- text: required trigger text; content is inserted from clipboard -->

{{< spoiler text="The output is finished files, where you need them." >}}

 A batch of renamed files, a spreadsheet saved into the right folder, a formatted PDF on your desktop — delivered to your file system, not handed back for you to file away.

{{< /spoiler >}}

<!-- text: required trigger text; content is inserted from clipboard -->

{{< spoiler text="The work spans your tools." >}}

Meeting notes in one place, the thread in Slack, last quarter's numbers in a spreadsheet. Set up a Friday roll-up as a scheduled task and Claude gathers all three itself every time it runs — nothing for you to round up first.

{{< /spoiler >}}

<!-- text: required trigger text; content is inserted from clipboard -->

{{< spoiler text="It should happen on a schedule, or while you're doing something else." >}}

A Friday review of what shipped. A Monday briefing that preps you for your next meeting.

{{< /spoiler >}}

**Try it out when:** (for example)

- You want to query all your tools like a database. "Review what we decided about pricing last quarter across meeting notes, Slack, and email, then update the Q3 deck with the findings." Claude finds the answer across all of them and updates the deck. Hand it off, keep working, check the result.
- You have a folder of 50+ project documents — contracts, financial reports, meeting transcripts. Ask Claude to find the ones most relevant to your initiative and produce a summary memo. It reads every page and pulls out the patterns that only emerge from reading all of them. Review fifty like you'd review five.
- You do the same work every Monday morning — check messages, assemble a status update, prep for the day's meetings. Set it up once as a scheduled task, and start Monday with answers instead of admin.

In the desktop app, you can hand off tasks in Cowork. What that gives you today:

{{< spoiler text="Local folder access" >}}

Point Claude at a folder; it reads what's there and saves finished work back to the same place. This is the concrete difference from turn-by-turn Chat, which can read what you upload but hands finished files back as downloads rather than saving them into your folder.

{{< /spoiler >}}

{{< spoiler text="Scheduled tasks" >}}

Set a task once — a daily briefing, a weekly roundup, a morning inbox triage — and Claude runs it on the cadence you set. Scheduled tasks run remotely, so they run even when your computer is asleep or the app is closed. A task that needs files on your computer runs locally, only while the app is open.

{{< /spoiler >}}

{{< spoiler text="Subagents" >}}

For a big job, Claude splits the work across background workers running in parallel, each with its own context, and hands you one finished deliverable.

{{< /spoiler >}}

{{< spoiler text="Projects." >}}

Group related tasks into a workspace with its own files, instructions, and memory — like projects in Chat, but built around the tasks you run.

{{< /spoiler >}}

{{< spoiler text="Browser use." >}}

With Claude in Chrome, Claude navigates websites and pulls what it finds straight into the task — competitor pricing across ten sites, data from pages with no API.

{{< /spoiler >}}

{{< spoiler text="Computer use" >}}

When there's no connector for what you need, Claude can operate your computer directly — clicking, typing, opening apps — asking permission before each app it touches, with a blocklist for anything off-limits. In research preview on Pro and Max plans.

{{< /spoiler >}}

{{< spoiler text="Plugins" >}}

Ready-made bundles of skills, connectors, and agents built for a specific kind of work — a sales plugin, a finance one, a legal one — so Claude works the way that role works. Browse and add them under Customize → Plugins.

{{< /spoiler >}}

### Building software with Claude Code

If you write code, the desktop app gives you a full development environment. Claude works directly in your codebase — reading what's there, writing and modifying code, running commands. Visual diffs show what changed, a built-in terminal shows commands as they run, and git tracks every version so you can always roll back.

You choose where the work happens:

<!-- text: required trigger text; content is inserted from clipboard -->

{{< spoiler text="Local" >}}

Select a folder on your computer and Claude works directly with those files — reading your project, using local tools, and running a development server you can preview in your browser.


{{< /spoiler >}}

<!-- text: required trigger text; content is inserted from clipboard -->

{{< spoiler text="Cloud" >}}

Connect a GitHub repository and Claude works in a cloud environment. Sessions continue even if you close the app, so you can start a big refactor and check back later. Good for larger codebases, or when you want to keep the work off your machine.

{{< /spoiler >}}

You also choose how much Claude does on its own, with settings including:

- **Manually approve.** Claude proposes every change and waits for your approval.
- **Accept edits.** Claude applies file edits automatically.
- **Plan.** Claude creates a plan before making changes.

## Choosing the Right Shape for the Task

| You're about to…                                             | The shape it takes                | Where it lives today                                         |
| :----------------------------------------------------------- | :-------------------------------- | :----------------------------------------------------------- |
| Ask, brainstorm, draft, or think something through, turn by turn | Working with Claude, turn by turn | Chat (quick entry, dictation, screenshots)                   |
| Hand off a multi-step task that ends in a finished deliverable, spans your tools, or runs on a schedule | Handing work off                  | Cowork (folder access, connectors, scheduled tasks, subagents) |
| Write, test, run, and ship code in a codebase                | Building software                 | The Code tab (Local or Cloud)                                |

---
title: "Trust It: Verifying Unsupervised Runs"
date: 2026-10-03
weight: 100
---

> [!NOTE]
> ### TL;DR
> Make the check as serious as the run was unsupervised:
>
> - Read the diff yourself.
> - Turn the tests into a hook that gates the turn.
> - Verify headless runs by their JSON result and exit code.
>   - Get a cold second opinion on anything that matters.



## Keep Unattended Runs in Auto Mode

When a run goes unattended at work, keep it in auto mode rather than bypass permissions. In auto mode, the classifier still reviews each action for danger. But it never judges whether the code is actually correct. It only flags dangerous actions. 

## Start with the Diff, Not the Summary

Don't start with Claude's summary of what it did. Start with the diff itself.

1. Run `/code-review` to walk the changes and flag issues.
2. Then put your own eyes on `git diff`.

Read what changed. Read the files that were part of the plan first, then look for anything outside it. 

## Turn Tests into a Gate, Not a Promise

The real gate on an unsupervised run is whether the tests passed. Don't leave that to trust. Wire it as a **hook** so Claude can't skip it.

A couple of hooks do the job:

- A **stop hook** that runs your tests and refuses to end the turn on a failure.
- A **post-tool-use hook** that lints and type checks after every edit.

The key detail is the exit code. A hook that exits with `exit 2` feeds the failure straight back to Claude. Claude reads that failure and fixes it without you asking.

## Get a Cold Second Opinion

Open a fresh session or sub-agent and have it review the changed code with no memory of how the code was built. Because it has no stake in the approach, it catches the things the original run talked itself past. A second reviewer with fresh eyes finds what the author rationalized away.


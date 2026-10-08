---
title: "Steering Long Sessions"
date: 2026-10-03
weight: 100
---

> [!NOTE]
>
> ### TL;DR
>
> A handful of habits for handling long Claude Code sessions without babysitting every step of it:
>
> - **Scope** you work first, then
> - **Steer**
>   - Direct your compaction so the summary keeps what matters.
>   - Use the rewind menu to course correct when Claude drifts.
>   - Set a goal when you can describe "done" better than you can describe the steps.
>   - Use loop for waiting on something outside the session.
>   - Run parallel work in worktrees.

## Scope the Work First with Plan Mode

Before Claude writes a single line, get it to lay out a plan. In **plan** mode, Claude does its research in read-only mode. It reads the code, figures out what needs to change, and hands you a plan to review.

When you get that plan, actually **read it. Don't skim it.** 

- The more thorough the plan, the fewer surprises you'll hit once Claude starts executing. 
- If something's off or missing, just ask Claude to add it where you want.

**Iterating on a plan is much faster than letting Claude run and hoping for the best, then cleaning up the mess!**

## Steer While Claude Works

Once Claude is running, you have a few ways to keep it pointed in the right direction. 

### Compact

Compact summarizes your conversation, uses that summary as the new context, and deletes the old messages.

- This frees up your context window so Claude can keep going. 
- Risk: Something important may get dropped in the summary, and Claude drifts off course.

**Don't just run `/compact` on its own. Add instructions after the command to tell Claude how to summarize.** Anything you write after the command shapes what the summary keeps. That's your steering wheel for context.

<!-- text: required trigger text; content is inserted from clipboard -->

{{< spoiler text="Example" >}}

For example, if you finished debugging a while back and now you only care about some API changes, say so:

```bash
/compact Focus on the --version flag implementation
```

{{< /spoiler >}}

<!-- text: required trigger text; content is inserted from clipboard -->

{{< spoiler text="Python Analogy" >}}

```python
# context window filling up
messages = [setup, debugging..., api_work...]      

# bare /compact: the summarizer decides what matters
messages = [summarize(messages)]

# directed /compact: you pass a parameter
messages = [summarize(messages, focus="--version flag implementation")]
```

{{< /spoiler >}}

### Rewind

When Claude heads down the wrong path, you don't have to prompt your way back out. 

**Rewind** takes you to your last checkpoint. (Every user prompt creates a checkpoint you can revert to. )

To open the menu, **double tap escape on an empty prompt**.

From the rewind menu you get a few options:

- **Restore code and conversation**: Roll back both together.
- **Restore conversation**: Roll back just the chat.
- **Restore code**: Roll back just the files.
- **Summarize from here**: Summarizes everything *after* the checkpoint. Great if you had a side conversation and just want to free up some space.
- **Summarize up to here**: Summarizes everything *before* the checkpoint. Great when you had a long setup phase you want to compress, but you want to keep the implementation parts intact.

{{< spoiler text="Python Analogy" >}}

```python
checkpoints = []

def on_user_prompt(prompt):
    checkpoints.append(copy.deepcopy((conversation, code)))   # one per prompt
    ...

def rewind(i, restore="both"):
    conv, code = checkpoints[i]
    if restore in ("both", "conversation"): conversation[:] = conv
    if restore in ("both", "code"):         files[:] = code
```

{{< /spoiler >}}

### Let Claude run more autonomously

#### Goal

**Goal** sets a completion condition. You describe what "done" looks like, and Claude keeps working across turns until a fast evaluator confirms those conditions are met.  It won't just stop the first time it thinks it's finished.

Example:

```bash
/goal all tests in src/billing pass, and the type checker reports zero errors
```

To cancel it, run `/goal clear`.

One important constraint: **the evaluator only reads the transcript**. So your condition has to be **checkable** from the output Claude actually produces, like the results of a test run.s

#### Loop

**Loop** runs a prompt on an interval between turns, either fixed or self-paced. 

Use it to pull something external, like a CI run or a deploy, and act when the state changes.

To stop a loop, just press escape.

<!-- text: required trigger text; content is inserted from clipboard -->

{{< spoiler text="Example: Check model training log every 10 minutes." >}}

![/loop example](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/%E6%88%AA%E5%B1%8F2026-10-06%2017.06.54.png)

{{< /spoiler >}}

<!-- text: required trigger text; content is inserted from clipboard -->

{{< spoiler text="Python analogy" >}}

```python
while True:                          # Esc stops it
    log = read("logs/train.log")
    report = claude(prompt, log)     # your prompt, run between your turns
    if report.needs_attention:
        notify_you(report)
    time.sleep(interval)             # fixed ("10m") or chosen by Claude
```

{{< /spoiler >}}

#### Run parallel work with worktrees

When you're running multiple agents on the same codebase, it could happen that two Claude sessions fighting over the same files leads to conflicts - that's unsafe!

That's where **worktrees** come in: Instead of sessions stepping on each other, each one gets its own independent file tree.

- Because each agent has its own tree, they can't clobber each other's changes. 
- When a session exits, a clean worktree is automatically removed.

A **`.worktreeinclude`** file at the repo root lists git-ignored files to copy into each worktree. This is useful for things like an environment variable file or a local config that you need in every worktree but don't want to commit to version control.

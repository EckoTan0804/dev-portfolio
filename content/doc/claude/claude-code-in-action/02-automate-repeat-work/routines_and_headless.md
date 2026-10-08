---
title: "Routines and Headless"
date: 2026-10-03
weight: 100
---

> [!NOTE]
> ### TL;DR
> - **Routines** are the default for repeat work. They run on Anthropic's infrastructure with nothing for you to host.
> - **Headless mode with `-p`** is for when the job needs your pipeline and you want to pipe data through a script.
> - **`--bare`** is for when CI needs the same results every single run.
> - **The Agent SDK** is for when the work belongs inside your own product.

## Routines

A **routine** is the most direct way to automate a task. There's no script and no server. 

It bundles: 

- a prompt
- the repository it works on 
- any connectors it needs
- a schedule

Then it runs that bundle in the cloud whenever it's triggered.

- The infrastructure is **Anthropic's** (i.e., in the cloud). There's no machine of yours staying on overnight, and there's no workflow file for you to maintain. You describe the job once and it just runs.

A routine can fire on a few kinds of triggers:

- A cron schedule, like every morning at 9am.
- An HTTP POST to its API endpoint, so your own code can kick it off.
- A GitHub event, like a new pull request landing.

-> Anything that's the same prompt on a recurring trigger is a good fit

## Creating a Routine

Two ways to create a routine:

- Create one from the web at `claude.ai/code/routines`. You give it a name, write the instructions describing what Claude should do in each session, pick a repository, and choose a trigger.

- create one from inside Claude Code: Run the `/schedule` command and describe what you want in plain language

  Example:

  ```bash
  /schedule daily dependency audit at 9am
  ```

## Three Things to Know Before You Rely on Routines

Before you lean on routines for anything important, keep these three limits in mind:

- **Routines are a research preview.** 

  Behavior and limits will keep moving, so don't be surprised if things change.

- **A recurring schedule runs at most *hourly*.** 

  If you need something more frequent, routines aren't the tool.

- **Runs start from a fresh clone of your default branch, push to `claude/` branches freely, and get checked before pushing anywhere else.**

## Headless Mode

Sometimes the job needs your environment, or logic wrapped around the run. That's when you drop to **headless** mode.

"Headless" means **running without the interactive interface** (the "head"). 

- Normally you open Claude Code, type prompts, watch it work, and approve things. 
- In headless mode you run one command, Claude does the job, prints the result to standard output, and exits (Just like executing a shell command).

The **`-p`** flag (short for `--print`) turns it on: It runs Claude Code as a one-shot command with no interactive UI. It reads standard in and writes standard out, so it pipes like any other shell tool.

Example:

```bash
claude -p "summarize the changes in this diff"
```


> [!CAUTION]
> `-p` skips auto-discovery of hooks, skills, plugins, MCP servers, and the CLAUDE.md file. You get Claude plus the tools you allow explicitly, and nothing the local environment happens to load.

<!-- Raw HTML instead of the card shortcode: the shortcode only opens http(s) URLs in a new tab -->

<div class="hb-cards mt-4 grid gap-4 not-prose" style="--hb-cols: 1;">
  <a class="hb-card group" href="/uploads/claude-code-in-action/interactive_vs_headless_claude_code.html" target="_blank" rel="noopener">
    <span class="hb-card-title p-4"><svg style="height: 1em; width: 1em;" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M13.5 6H5.25A2.25 2.25 0 0 0 3 8.25v10.5A2.25 2.25 0 0 0 5.25 21h10.5A2.25 2.25 0 0 0 18 18.75V10.5m-10.5 6L21 3m0 0h-5.25M21 3v5.25"/></svg>Interactive example: Interactive vs. headless Claude Code</span>
  </a>
</div>

<!-- text: required trigger text; content is inserted from clipboard -->

### Getting structured output back

When using headless mode, you can pair a JSON schema with the JSON output format, and Claude will constrain its output to match your schema. The object that matches your schema lands in the `structured_output` field of the JSON response. 

Example:

```bash
claude -p "Extract the exported function names from src/core/style.js" \
  --output-format json \
  --json-schema '{"type":"object","properties":{"functions":{"type":"array","items":{"type":"string"}}},"required":["functions"]}' \
  | jq '.structured_output.functions'
```

### When to use and not use headless

{{< spoiler text="When to use headless" >}}

- **You need your own environment.** For example, the job needs local data, GPUs, or internal tools that a cloud routine can't reach.
- **You want to pipe data through a script.** For example: `git diff | claude -p "review this" | tee review.md`.
- **You need structured output.** Pair `--output-format json` with `--json-schema` and read `structured_output` in your code.
- **You're batch-processing.** Loop over files or tickets and call `claude -p` once per item.
- **You're running in CI.** Add `--bare` when you need the same results every run.
- **You want multi-step automation.** Capture the `session_id` from the JSON, then `claude --resume` it in a later step (plan first, execute later).

{{< /spoiler >}}

<!-- text: required trigger text; content is inserted from clipboard -->

{{< spoiler text="When not to use headless" >}}

- **Exploring or debugging** something you don't understand yet. Use the interactive mode, where you can steer.
- **A simple recurring prompt on a repo** (e.g. a morning dependency audit). A routine is simpler, and you host nothing.
- **Work that belongs inside your product.** That's what the Agent SDK is for.

{{< /spoiler >}}

## Multi-Step Automation with Sessions

For work that happens across multiple steps, you don't have to cram everything into one command. Capture the session's ID from the JSON output and resume it later:

```bash
claude --resume "$(jq -r .session_id /tmp/plan.json)"
```

One script kicks off the work. Another resumes it later with full context. This is handy when the first pass produces a plan and a second pass carries it out.

## Deterministic Runs for CI

When CI needs the same results every single run, use the `--bare` flag, which gives you deterministic mode.

It's the right choice when you're running Claude Code inside a pipeline and you want repeatable, predictable output rather than anything that varies run to run.

## The Agent SDK

The Agent SDK gets you a library that embeds Claude Code inside your own TypeScript or Python applications.

Both languages expose a `query` function and the same primitives as the CLI. You pass a prompt plus options, like:

- `allowedTools` to control what Claude can do,
- a system prompt,
- and a permission mode.

Then you iterate over the messages Claude streams back and handle them however your app needs. It's the same engine as the CLI, just callable from inside your product.

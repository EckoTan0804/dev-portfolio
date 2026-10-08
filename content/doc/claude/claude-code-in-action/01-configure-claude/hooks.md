---
title: "Hooks"
date: 2026-10-03
weight: 400
---



A hook is **deterministic** code that runs at a **fixed** point in the loop, so it can guarantee behavior instead of hoping for it. It turns a rule from "Claude usually listens" into "Claude can't skip it."

<!-- Raw HTML instead of the card shortcode: the shortcode only opens http(s) URLs in a new tab -->

<div class="hb-cards mt-4 grid gap-4 not-prose" style="--hb-cols: 1;">
  <a class="hb-card group" href="/uploads/claude-code-in-action/claude_code_hooks_explorer.html" target="_blank" rel="noopener">
    <span class="hb-card-title p-4"><svg style="height: 1em; width: 1em;" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M13.5 6H5.25A2.25 2.25 0 0 0 3 8.25v10.5A2.25 2.25 0 0 0 5.25 21h10.5A2.25 2.25 0 0 0 18 18.75V10.5m-10.5 6L21 3m0 0h-5.25M21 3v5.25"/></svg>Interactive Claude Code hooks explorer</span>
  </a>
</div>

## The Hook Events

Claude Code fires around 30 hook events over the course of a session. These are the ones worth knowing:

- **PreToolUse** fires before a tool call. This is your enforcement primitive. It's the one that can stop something before it happens.
- **PostToolUse** fires after a successful tool call. This is usually where auto-formatting or an auto-lint goes.
- **Stop** fires when Claude wants to end its turn. You can refuse and say "no, you're not done yet" if some condition isn't met. There's a matching **SubagentStop** for when a sub-agent finishes.
- **PreCompact** and **PostCompact** fire before and after compaction.
- **InstructionsLoaded** fires when a CLAUDE.md or rule file loads. Handy for auditing what actually made it into context.
- **SessionStart** fires at the start and primes the environment. Use the `startup` source if you only want it on fresh starts.

> [!TIP]
> To re-inject context after compaction, don't use `PostCompact`. Use **`SessionStart`** with the compact matcher. That's the one that actually gets its output back into the conversation.

## PreToolUse: Returning a Decision as JSON

`PreToolUse` can block a tool call before it runs.

The way you talk back to Claude is by printing JSON and exiting zero. The key field is `permissionDecision`, and it takes one of three values:

- `allow` — let the call through
- `deny` — stop the call
- `ask` — hand it back to the user to decide

The JSON looks like this:

```json
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "deny",
    "permissionDecisionReason": "...",
    "updatedInput": {
      "command": "..."
    }
  }
}
```

<!-- text: required trigger text; content is inserted from clipboard -->

{{< spoiler text="Visual explanation" >}}

![image-20261008121704970](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/image-20261008121704970.png)

![PreToolUse](https://raw.githubusercontent.com/EckoTan0804/upic-repo/master/uPic/image-20261008105744999.png)

{{< /spoiler >}}

{{< spoiler text="Example" >}}

A PreToolUse hook on the Bash tool. Claude wants to run: `rm -rf / `.

Before running the command, the PreToolUse hook is triggered. It prints JSON and exits 0:

```json
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "deny",
    "permissionDecisionReason": "Destructive command"
  }
}
```

{{< /spoiler >}}

> [!TIP]
> Instead of just refusing, you can return `updatedInput` to rewrite the call. This way, you can strip a secret out of a command and still let it run.
>
> Notice: `updatedInput` replaces the *whole* input object, so you have to echo back the fields you aren't changing, or you'll lose them.

## Exit Codes

Not every hook needs to speak JSON. For simpler hooks, exit codes do the job. 

| Exit code     | Meaning        | Remarks                                                      |
| ------------- | -------------- | ------------------------------------------------------------ |
| 0             | success        | <li/>If standard out is JSON, Claude parses it. <br /><li/>Plain text is ignored on most events, but on SessionStart, UserPromptSubmit, and UserPromptExpansion, plain text gets added to context. That's exactly what makes a state-preserver hook work. |
| 2             | blocking error | Standard error gets fed back to Claude as context.           |
| Anything else | Non-blocking   | <li/>Standard error gets logged, and Claude carries on. <br /><li/>‼️ Gotcha: **exit code 1** feels like an error, but it does not block. Claude runs the command anyway. So if you meant to stop something, exit 2, not 1. |

## Preserving State across a Compact

Compaction is lossy:  When Claude compacts a long conversation, it drops a lot of detail, such as the exact files you were editing, or the branch name. 

Fix: **Use a `SessionStart` hook with the `compact` matcher** to put the important facts back, deterministically, right after compaction.

<!-- Raw HTML instead of the card shortcode: the shortcode only opens http(s) URLs in a new tab -->
<div class="hb-cards mt-4 grid gap-4 not-prose" style="--hb-cols: 1;">
  <a class="hb-card group" href="/uploads/claude-code-in-action/preserving_state_across_compact.html" target="_blank" rel="noopener">
    <span class="hb-card-title p-4"><svg style="height: 1em; width: 1em;" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M13.5 6H5.25A2.25 2.25 0 0 0 3 8.25v10.5A2.25 2.25 0 0 0 5.25 21h10.5A2.25 2.25 0 0 0 18 18.75V10.5m-10.5 6L21 3m0 0h-5.25M21 3v5.25"/></svg>Interactive example: Preserving State across a Compact</span>
  </a>
</div>
<!-- text: required trigger text; content is inserted from clipboard -->

{{< spoiler text="Example (Python)" >}}

```python
# .claude/hooks/restore_state.py
import subprocess

files = subprocess.run(["git", "diff", "--name-only"],
                       capture_output=True, text=True).stdout.strip()
branch = subprocess.run(["git", "branch", "--show-current"],
                        capture_output=True, text=True).stdout.strip()

print(f"Context restored after compaction.\nBranch: {branch}\nFiles in progress:\n{files}")
# exit 0 (default): stdout from SessionStart is added to context

```

In the settings.json, a `compact` matcher is registered:
```json
"SessionStart": [{
  "matcher": "compact",
  "hooks": [{ "type": "command", "command": "python3 .claude/hooks/restore_state.py" }]
}]
```

{{< /spoiler >}}

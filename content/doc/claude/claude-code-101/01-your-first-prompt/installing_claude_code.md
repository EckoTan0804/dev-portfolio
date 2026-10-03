---
title: "Installing Claude Code"
date: 2026-10-03
weight: 100
---



## Terminal

<!-- card params: title (required), url (optional), icon (Hero Icons), subtitle (Markdown supported) -->
{{< cards >}}
	{{< card url="https://code.claude.com/docs/en/quickstart#step-1-install-claude-code" title="Quick start: Install Claude Code" icon="arrow-top-right-on-square" >}}
{{< /cards >}}

For **macOS, Linux, WSL**:

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

> [!WARNING]
> If you prefer Homebrew, you can also use `brew install`, but note that this method doesn't support auto-updates.

## Visual Studio Code

Open your Extensions panel and search for "Claude Code." Look for the extension by Anthropic with the blue verification check. Hit install.

## Which One Should I Use?

- If you want to stay on the cutting edge, the **terminal** is your best bet — features ship there first. The IDE integrations offer a nearly identical experience if you prefer Claude Code to feel more intertwined with your code editor.

- **Desktop** is great for letting Claude run in the background while you handle other tasks.

- **Claude Code on the web** is a solid option if you want to remotely work on projects through a GitHub repository.

---
title: Connecting Your Tools
date: 2026-09-21
weight: 100
---

<!-- text: required trigger text; content is inserted from clipboard -->

{{< spoiler text="TL;DR" >}}

- **Connectors transform Claude from an assistant into an informed collaborator** by giving Claude access to the same tools, data, and context that you use every day. Instead of starting every conversation from scratch, Claude can work directly with your actual information.
- **Connectors allow Claude to read information and perform actions on your behalf.** Depending on the connector and permissions you grant, Claude can search your files, retrieve documents, analyze data, create new content, update records, and execute tasks across your connected applications—all from within your conversation.
- **The Model Context Protocol (MCP) powers connectors.** Think of MCP like USB-C for AI—a universal standard that allows Claude to connect to many different applications through a single, consistent interface. This open standard means developers can build connectors for any tool, and those connectors work seamlessly with Claude.
- **There are two types of connectors: web connectors and desktop extensions.** Web connectors link Claude to cloud services like Google Drive, Notion, Slack, and Asana. Desktop extensions run locally on your computer through the Claude Desktop app, giving Claude access to local files and native applications.

{{< /spoiler >}}

## Finding and Connecting Tools

Anthropic maintains a directory of recommended connectors at **claude.ai/directory**. The directory is organized into two tabs:

- **Web:** Cloud services and applications (Gmail, Notion, Slack, Asana, Linear, Stripe, and many more)
- **Desktop extensions:** Local tools that run on your computer through the Claude Desktop app

## Using Connectors in Your Work

Once you've connected your tools, Claude considers them when responding to your requests. See these [examples](https://academy.claude.com/courses/claude-101/connecting-your-tools#using-connectors-in-your-work) for some practical ways to use connected tools.

## Security and Permissions

When you connect Claude to external services, you're granting it access to **read**—and sometimes **modify**—data within those services. 

Here are some important considerations:

{{< spoiler text="Scoped access" >}}

Permissions are specific to what the connector needs and you can toggle individual permissions on and off within each application's menu.

{{< /spoiler >}}

{{< spoiler text="Claude sees what you see" >}}

Claude can only access data *you* have access to. Connecting your work email doesn't give Claude access to your CEO's inbox—only your own.

{{< /spoiler >}}

{{< spoiler text="Revocable at any time" >}}

You can disconnect a service through Claude's settings or through the third-party service's security settings. Just as with Skills, you can also find or build custom connectors. Exercise the same caution — only install connectors from trusted sources.

{{< /spoiler >}}


---
title: Research for Deep Dives
date: 2026-09-21
weight: 300
---

<!-- text: required trigger text; content is inserted from clipboard -->

{{< spoiler text="TL;DR" >}}

- **Research transforms how Claude finds and analyzes information.** Instead of a single search, Claude operates agentically—conducting multiple searches that build on each other while determining exactly what to investigate next. It explores different angles of your question automatically and works through open questions systematically.
- **Research takes longer than your usual search** — a few minutes or more, depending on the question. That's because it isn't one lookup: Claude can send out many searches at once, sometimes across hundreds of sources, and pull what they find into one answer. That work isn't instant.
- **Research works with Thinking, so Claude can plan its approach before it searches.** It breaks a complex request into manageable pieces, then gathers what each piece needs.
- **Citations make verification easy.** Research delivers thorough answers complete with easy-to-check citations, so you can trust Claude's findings and quickly verify sources yourself.

{{< /spoiler >}}

## What Is Research?

Research is an advanced feature that transforms Claude from a conversational assistant into a **systematic** investigator. 

When you enable Research, Claude doesn't just answer your question—it explores it from multiple angles, synthesizing information from across the web and your connected integrations. Think of it as having a skilled research assistant who gathers information, cross-references sources, and compiles a comprehensive report while you stay on your own work.

Research is particularly valuable when you need more than a quick answer. It's designed for situations where a thorough understanding requires pulling together information from multiple sources, comparing different perspectives, and synthesizing findings into actionable insights.

## When to Use Research?

{{< spoiler text="Use Research when you need" >}}

- Comprehensive reports that synthesize information from multiple sources
- In-depth analysis across the web and your connected integrations (like Google Workspace)
- Thorough investigations that would typically require hours of manual work
- Comparative analysis, such as evaluating competitors or vendor options
- Reports with citations you can verify

{{< /spoiler >}}

{{< spoiler text="Research is ideal for tasks like" >}}

- Market analysis and competitive research
- Planning complex projects, like team offsites or product launches
- Synthesizing information from your email, calendar, and documents
- Creating technical documentation that draws from multiple sources
- Preparing briefings that require current, verified information

{{< /spoiler >}}

{{< spoiler text="Consider web search instead when" >}}

- You need a quick, specific fact (like today's stock price or a company's address)
- The answer requires only one or two sources
- Speed matters more than comprehensiveness

{{< /spoiler >}}

{{< spoiler text="Consider turning on Thinking instead when" >}}

- You need deep reasoning on a complex problem that doesn't require external information
- You're working on mathematical problems, code debugging, or logical analysis
- The answer comes from reasoning through a problem rather than gathering information

{{< /spoiler >}}

{{< spoiler text="Consider enterprise search instead when" >}}

- You need answers that draw from your organization's internal knowledge — documents, Slack threads, emails, meeting notes
- You're onboarding and want to quickly find how your company handles something (like policies, processes, or past decisions)
- You're asking a question that's specific to your company, not the public web

{{< /spoiler >}}

## How Research Works?

When you enable Research, you're activating an **agentic, multi-step** process that goes far beyond a simple web search. Claude autonomously decides what to search next based on what it has already found, pursuing leads and filling gaps without you needing to direct each step.

{{% steps %}}

### Claude plans its approach.

Claude thinks through its approach before it searches: it breaks down your request, identifies what information it needs, and plans how to investigate the different angles of your question.

### Claude conducts multiple searches.

Rather than running a single search, Claude conducts many searches that build on each other. It determines what to investigate next based on what it finds, pursuing promising leads and filling in gaps.

### Claude synthesizes findings.

After gathering information from multiple sources—including the web and any connected integrations like Gmail, Google Calendar, or Google Drive—Claude compiles everything into a comprehensive, well-organized report.

### Claude provides citations.

Every claim in Research reports links back to its source, making it easy to verify information and dig deeper when needed.

{{% /steps %}}

## Using Research in Practice

### Tips for effective Research prompts

{{< spoiler text="Be specific about your goals." >}}

Instead of "Tell me about the EV market," try "Analyze the electric vehicle battery market—identify key players, technology trends, and supply chain challenges that might affect investment decisions."

{{< /spoiler >}}

{{< spoiler text="Specify the sections or structure you want." >}}

Claude will organize its findings around the structure you provide. For example: "Compare venue options for a team offsite including: location and accessibility, meeting space and amenities, catering options, and pricing considerations."

{{< /spoiler >}}

{{< spoiler text="Include relevant constraints." >}}

Budget ranges, timelines, geographic requirements, and other parameters help Claude focus its research on relevant options.

{{< /spoiler >}}

{{< spoiler text="Ask Claude to help refine your prompt." >}}

If you're not sure how to frame your research question, you can even ask Claude to help you write a better Research prompt before enabling the feature.

{{< /spoiler >}}

### Working with connected integrations

When you have Google Workspace or other integrations connected, Research becomes even more powerful. Claude can pull context from your emails, calendar, and documents alongside web research.

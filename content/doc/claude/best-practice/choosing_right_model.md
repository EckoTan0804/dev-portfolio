---
title: Choosing the Right Claude Model
date: 2026-09-29
weight: 200
---

<!-- card params: title (required), url (optional), icon (Hero Icons), subtitle (Markdown supported) -->
{{< cards >}}
	{{< card url="https://academy.claude.com/tutorials/choosing-the-right-claude-model" title="Choosing the right Claude model" icon="arrow-top-right-on-square" >}}
{{< /cards >}}

## Meet the Four Models

Claude comes in four models. Each is built for different kinds of work, and each uses your rate limit differently. 

{{< spoiler text="Haiku" >}}

- Fast and lightweight. 
- Haiku 4.5 is built for everyday requests, and it rivals the reasoning capabilities of our Sonnet 4.0 model. 
- When you need quick answers to simple questions, basic summaries, or synthesis, Haiku gets it done instantly. It's also the most efficient with your rate limit.

{{< /spoiler >}}

{{< spoiler text="Sonnet" >}}

- The daily driver. 
- Sonnet 5 brings strong reasoning to the kind of work you do every day: coding, writing, analysis, research, and complex problem-solving. It's responsive enough for real-time collaboration and capable enough that most problems won't outgrow it. 
- It also handles computer use, vision tasks, and document and spreadsheet creation well, making it a versatile default across a wide range of work. If you're not sure which model to pick, start here.

{{< /spoiler >}}

{{< spoiler text="Opus" >}}

- A large reasoning specialist. 
- Opus 5 is exceptional for specialized complex tasks requiring advanced reasoning. It's built for problems that genuinely need deep thinking over time. 
- It uses more of your rate limit, so you want to reserve it for tasks that really need it. Opus is available on [Pro plans](https://claude.com/pricing) and above.

{{< /spoiler >}}

{{< spoiler text="Fable" >}}

- The go-to for your largest, most important projects. 
- Fable 5.1 is our most capable model, built for long, complex tasks. 
  - It can work through tasks more autonomously with fewer mid-task check-ins: describe the outcome you want, and it plans the steps and checks its own work along the way. 
- It takes time to think through problems before answering, so responses take longer, and it uses the most of your rate limit. 
- Fable is available on paid plans. You can select it from the model picker when a task needs it.

{{< /spoiler >}}



| Model  | Rate limit use | Best for                                                     |
| :----- | :------------- | :----------------------------------------------------------- |
| Haiku  | Lightest       | Quick answers, summaries, and simple extraction — anything you want done instantly |
| Sonnet | Moderate       | Coding, writing, analysis, and multi-step workflows — your versatile default |
| Opus   | Heavy          | Deep research and complex reasoning that genuinely needs sustained thinking |
| Fable  | Heaviest       | Your largest, most critical projects: long, complex tasks Claude works through with fewer check-ins |

## Understanding Rate Limits

Your rate limit caps **how many tokens you can use in a given time window**. The models consume tokens at different rates: **Haiku is the lightest, Sonnet is moderate, Opus is heavy, and Fable uses the most.**

Setting [thinking and effort](https://support.claude.com/en/articles/10574485-using-extended-thinking) controls in order to customize the depth of reasoning Claude applies to a problem. The Effort setting in the model picker adjusts this directly: 

- The default level is the right balance for most work
- Lower it for quicker answers that use less of your limit
- Save the highest setting for your hardest problems, since deeper thinking takes more time and uses more of your limit

## When to Use Each Model

### Use Haiku for:

- Simple, straightforward questions with short answers
- Tasks where you just need a quick lookup or categorization
- Extracting specific information from text
- Simple summarization or synthesis
- Anything you want done instantly without complex reasoning

### Use Sonnet for:

- Writing and content creation
- Coding tasks — debugging, writing new code, refactoring
- Analysis that needs reasoning but isn't extremely complex
- Customer support chatbots with context and nuance
- Multi-step problems and workflows
- Most "general purpose" work where you're not sure which model to use

### Use Opus for:

- Deep research and analysis you'll question, redirect, and build on as you go
- Complex work you're doing in a live, back-and-forth session, where you want each answer sooner
- Biology and security work: Claude answers these topics with Opus even if you've picked Fable, so starting with Opus is simpler. To learn more, visit our [help center](https://support.claude.com/en/articles/15363606-why-claude-switched-models-in-your-conversation-with-fable-5).
- Problems where you've tested with Sonnet and it struggled

### Use Fable for:

- Specialized tasks where accuracy is critical
- Long horizon tasks with many connected steps
- Outputs from dense source material: long documents, charts, technical diagrams
- Work where you'd rather describe the outcome and let Claude plan the steps
- Problems you've tested with Opus and it struggled

### Examples in practice

| Task                                         | Pick   | Why                                                          |
| :------------------------------------------- | :----- | :----------------------------------------------------------- |
| Summarizing articles                         | Haiku  | Straightforward content extraction without complex reasoning |
| Debugging code                               | Sonnet | Exceptional coding capabilities, fast feedback, and clear bug identification |
| Analyzing complex research papers            | Opus   | Deep analysis across long specialized documents, including methodology critique and forward-looking insights |
| Building a working project from a rough idea | Fable  | Plans the steps, checks its own work, and keeps working on long tasks with fewer mid-task check-ins |



## 
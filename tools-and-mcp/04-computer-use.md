# Computer Use & Browser Automation

> **Level:** ADV · **Last verified:** 2026-07-30

## Why this matters

Some tasks have no API. Legacy internal tools, desktop apps, gated websites — sometimes the only path is driving a browser or desktop GUI. Computer-use agents unlock these workflows, but they're slow, brittle, and risky. Use sparingly.

## Core concepts

### Three approaches

| Approach | Examples | Best for |
|----------|----------|----------|
| **Browser automation libs** | Playwright, Selenium, Puppeteer | Scripted, deterministic flows |
| **LLM + browser automation** | Browser-Use, Stagehand, LaVague | Adaptive flows with LLM deciding next action |
| **Native computer use** | Anthropic computer use, OpenAI CUA | Full desktop control, not just browser |

### When to use what

- **Pure Playwright** — flow is known and stable. Don't add an LLM.
- **Browser-Use / Stagehand** — flow varies; LLM picks the next click.
- **Native computer use** — need to drive non-browser apps (Excel, internal CRM).

### The latency reality

Computer use is slow:
- Screenshot → model → action → screenshot → ...: 3–10s per step.
- A 20-step flow takes 1–3 minutes.
- Cost: 20 steps × ~$0.05/step = $1+/task.

Reserve for low-frequency, high-value tasks.

## Code: Browser-Use (LLM + Playwright)

```python
from browser_use import Agent
from langchain_openai import ChatOpenAI

agent = Agent(
    task="Go to amazon.com, search for 'wireless mouse', sort by price low-to-high, return the top 3 product names and prices.",
    llm=ChatOpenAI(model="gpt-5"),
)
result = await agent.run()
print(result.final_output)
```

## Code: Anthropic computer use

```python
import anthropic
client = anthropic.Anthropic()

resp = client.beta.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=4096,
    tools=[{"type": "computer_20250124", "name": "computer", "display_width_px": 1280, "display_height_px": 800, "display_number": 0}],
    messages=[{"role": "user", "content": "Open Firefox and navigate to example.com."}],
    betas=["computer-use-2025-01-24"],
)
# Then implement: screenshot, send to model, execute returned action (click, type, key), repeat.
```

## Production concerns

- **Latency:** 3–10s per step. Use for batch, not real-time UX.
- **Cost:** $1–5 per task is typical.
- **Failure modes:** UI changes break flows. Detect, retry, alert.
- **Security:** Computer-use agents can do anything a human can. Sandbox them (VM, restricted user, no admin).

## Anti-patterns

- ❌ **Using computer use for tasks that have an API.** Always prefer APIs.
- ❌ **Running computer-use agents with admin privileges.**
- ❌ **No screenshot logging.** When it fails, you can't debug without the screenshot sequence.

## References

- [Anthropic computer use](https://docs.anthropic.com/en/docs/build-with-claude/computer-use) — verified 2026-07-30
- [Browser-Use](https://github.com/browser-use/browser-use) — verified 2026-07-30
- [Stagehand](https://github.com/browserbase/stagehand) — verified 2026-07-30

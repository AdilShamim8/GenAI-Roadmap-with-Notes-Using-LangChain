# Extended Thinking Models

> **Level:** INT · **Last verified:** 2026-07-30 · **Sources:** [OpenAI o-series](https://platform.openai.com/docs/guides/reasoning), [Anthropic extended thinking](https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking)

## Why this matters

Reasoning models (o1, o3, o4-mini, Claude with extended thinking, DeepSeek R1) spend extra tokens "thinking" before answering. They're dramatically better at multi-step reasoning, math, coding, and agentic tasks — and dramatically more expensive per call if used wrong.

## Core concepts

### How they work

The model generates hidden "thinking" tokens that aren't shown to the user but inform the final answer. You pay for these tokens.

### When they win

- Multi-step math or logic.
- Coding tasks with non-trivial debugging.
- Agent planning (when to call which tool).
- Anything where you'd previously say "let me think step by step".

### When they lose

- Simple classification or extraction (use a smaller model).
- Creative writing (no benefit, more cost).
- High-throughput, low-latency UX (thinking takes time).

### The thinking budget

OpenAI exposes `reasoning_effort` (low/medium/high). Anthropic lets you set a `thinking` budget in tokens. Higher budgets = better answers = more cost.

## Code: Claude with extended thinking

```python
import anthropic
client = anthropic.Anthropic()

resp = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=16000,
    thinking={
        "type": "enabled",
        "budget_tokens": 8000,  # thinking tokens
    },
    messages=[{"role": "user", "content": "Design a rate-limiter for a multi-tenant API. Justify your design."}],
)

for block in resp.content:
    if block.type == "thinking":
        print(f"[thinking: {block.thinking}]")
    elif block.type == "text":
        print(block.text)
```

## Code: OpenAI o3 with reasoning effort

```python
from openai import OpenAI
client = OpenAI()

resp = client.chat.completions.create(
    model="o3",
    reasoning_effort="medium",  # low | medium | high
    messages=[{"role": "user", "content": "Prove that the sum of two odd numbers is even."}],
)
print(resp.choices[0].message.content)
```

## Production concerns

- **Latency:** Thinking models add 5–60s to TTFT. Plan UX around it (show a "thinking..." state).
- **Cost:** Thinking tokens are billed. A high-effort o3 call can cost 10–50× a GPT-5-mini call.
- **Failure modes:** Over-using reasoning models for trivial tasks burns budget.
- **Security:** Thinking content can leak training data or be manipulated by prompt injection — never display raw thinking to users.

## Anti-patterns

- ❌ **Defaulting to o3 / Claude-with-thinking for every call.** Route by task complexity.
- ❌ **Showing raw thinking to users.** It's often confused, includes backtracking, and erodes trust.
- ❌ **Disabling thinking for hard tasks because "it's slow."** Use a smaller model instead.

## Decision framework

| Task | Model |
|------|-------|
| Simple extraction / classification | GPT-5 mini / Claude Haiku / Gemini Flash |
| Coding, math, planning | o3 / Claude Sonnet with thinking / DeepSeek R1 |
| Frontier-hard agentic | Claude Opus with thinking |

## References

- [OpenAI reasoning guide](https://platform.openai.com/docs/guides/reasoning) — verified 2026-07-30
- [Anthropic extended thinking](https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking) — verified 2026-07-30
- [DeepSeek R1](https://github.com/deepseek-ai/DeepSeek-R1) — verified 2026-07-30

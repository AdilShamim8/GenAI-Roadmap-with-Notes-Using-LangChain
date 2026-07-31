# Context Window Budgeting

> **Level:** INT · **Last verified:** 2026-07-30

## Why this matters

In 2026, the bottleneck isn't writing a good prompt — it's managing what's *in* the context window. Every token competes for attention. Mismanaged context produces hallucinations, missed details, and cost spikes.

## Core concepts

### The context budget

For a 200K-token context window (Claude Sonnet 4.5), a typical production agent's budget:

| Slot | Tokens | % |
|------|--------|---|
| System prompt | 2,000 | 1% |
| Tool definitions | 3,000 | 1.5% |
| Retrieved context (RAG) | 20,000 | 10% |
| Conversation history | 30,000 | 15% |
| Working memory / scratchpad | 5,000 | 2.5% |
| User input | 1,000 | 0.5% |
| Reserved for output | 8,000 | 4% |
| Headroom | 131,000 | 65% |

Headroom is not free — past ~50% utilization, recall drops ("lost in the middle"). Aim for active budget ≤ 50% of window.

### The five context sins

1. **Stale history** — every old turn dilutes attention to the current turn.
2. **Verbatim tool output** — full API responses bloat context; summarize.
3. **Duplicate system prompts** — re-sent per request without caching.
4. **Unranked retrieval** — 20 chunks dumped in insertion order, not relevance.
5. **No scratchpad eviction** — intermediate thoughts accumulate.

## Code: context budget guard

```python
def estimate_tokens(text: str) -> int:
    return len(text) // 4  # rough English estimate

def trim_history(history: list[dict], budget_tokens: int = 30000) -> list[dict]:
    '''Keep the system message and the most recent turns within budget.'''
    out = [history[0]] if history[0]["role"] == "system" else []
    body = history[1:] if out else history
    running = sum(estimate_tokens(m["content"]) for m in out)
    for m in reversed(body):
        cost = estimate_tokens(m["content"])
        if running + cost > budget_tokens:
            break
        out.insert(1, m)  # insert after system prompt
        running += cost
    return out
```

## Production concerns

- **Latency:** Every 1K tokens adds ~30ms prefill on a frontier model.
- **Cost:** Linear in input tokens.
- **Failure modes:** Models ignore instructions in the middle of long contexts. Put critical instructions at the start or end.
- **Security:** Retrieved context is untrusted — it can contain prompt injections.

## Anti-patterns

- ❌ **Stuffing all retrieved chunks into one user message.** Hard for the model to cite sources.
- ❌ **Keeping full tool outputs in history.** Summarize after each tool call.
- ❌ **Assuming "fits in context" = "model will use it."** Test recall empirically.

## References

- [Lost in the Middle](https://arxiv.org/abs/2307.03172) — verified 2026-07-30
- [Anthropic: Contextual retrieval](https://www.anthropic.com/news/contextual-retrieval) — verified 2026-07-30

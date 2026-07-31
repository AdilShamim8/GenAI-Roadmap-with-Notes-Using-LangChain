# Context Distillation

> **Level:** ADV · **Last verified:** 2026-07-30

## Why this matters

Long agent runs accumulate dead context: tool outputs you no longer need, intermediate reasoning, resolved sub-tasks. Without active distillation, your agent drifts, gets slower, and costs more with every turn.

## Core concepts

### Three distillation patterns

1. **Rolling summary** — every N turns, replace the oldest turns with a summary.
2. **Tool-output compaction** — after a tool call completes, replace the raw output with a 1-paragraph summary in the next turn.
3. **Hierarchical memory** — keep a short working context (last 5 turns) + a longer episodic memory (summarized) + retrieval into raw history.

### The async summarizer

Run summarization as a background task, not in the user-facing turn. Insert the summary into the next turn's context.

## Code: rolling summary

```python
from openai import OpenAI
client = OpenAI()

def maybe_summarize(history: list[dict], threshold: int = 20) -> list[dict]:
    if len(history) < threshold * 2:
        return history
    system = history[0]
    old = history[1:threshold]
    recent = history[threshold:]

    summary = client.chat.completions.create(
        model="gpt-5-mini",
        messages=[
            {"role": "system", "content": "Summarize the conversation so far in <300 words. Preserve decisions, key facts, and unresolved questions."},
            *old,
        ],
    ).choices[0].message.content

    return [system, {"role": "user", "content": f"[Previous conversation summary]\n{summary}"}, *recent]
```

## Production concerns

- **Latency:** Summarization adds a background call; doesn't affect user TTFT if async.
- **Cost:** Summary calls are cheap (small model) and pay for themselves in token savings.
- **Failure modes:** Summaries lose detail that matters for a later turn. Always preserve "decisions made" and "open questions".
- **Security:** Don't summarize PII into a long-lived memory store without redaction.

## Anti-patterns

- ❌ **Summarizing the entire context every turn.** Expensive and noisy.
- ❌ **Truncating history by turn count, not content.** Loses long-range dependencies.
- ❌ **Storing raw transcripts forever.** Use episodic memory with TTLs.

## References

- [Letta (formerly MemGPT) — memory patterns](https://github.com/letta-ai/letta) — verified 2026-07-30
- [Anthropic: Long-context agents](https://docs.anthropic.com/en/docs/build-with-claude/long-context) — verified 2026-07-30

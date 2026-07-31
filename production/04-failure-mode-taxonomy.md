# Failure-Mode Taxonomy

> **Level:** ADV · **Last verified:** 2026-07-30

## Why this matters

Most production GenAI incidents fall into ~8 categories. Knowing the taxonomy lets you build detection, mitigation, and runbooks for each — instead of treating every incident as a surprise.

## The taxonomy

| # | Failure mode | Symptom | Detection |
|---|--------------|---------|-----------|
| 1 | **Hallucination** | Confident wrong answer | Faithfulness eval; cross-check |
| 2 | **Context overflow** | Truncated input, missed context | Token counter pre-call |
| 3 | **Tool-call loop** | Agent calls same tool repeatedly | Iteration counter |
| 4 | **Prompt injection** | Agent follows injected instructions | Input + output filters |
| 5 | **Rate limit / overload** | 429s from provider | Retry with backoff + fallback |
| 6 | **Latency spike** | p99 > 10s | OTel + alerting |
| 7 | **Cost runaway** | Daily cost 10× baseline | Cost dashboard + alerts |
| 8 | **Drift** | Quality degrades over weeks | Online evals vs baseline |

## Per-mode mitigations

### Hallucination
- RAG with citations.
- Faithfulness eval in pipeline.
- "I don't know" allowed in system prompt.

### Context overflow
- Pre-count tokens; trim history.
- Summarize old turns.

### Tool-call loop
- Cap iterations (5–10).
- Detect repeated tool calls with same args.

### Prompt injection
- Input filters (deterministic).
- Constitutional pattern (second model checks).
- Privilege separation.

### Rate limit / overload
- Exponential backoff with jitter.
- Multi-vendor fallback chain.

### Latency spike
- Timeouts per call.
- Stream to mask latency.
- Cache common queries.

### Cost runaway
- Per-request budget.
- Per-user daily cap.
- Alert on >2× baseline.

### Drift
- Online evals (sample 1–5%).
- Weekly comparison vs baseline.
- Periodic prompt refresh.

## Code: iteration counter

```python
class AgentLoop:
    def __init__(self, max_iterations=10):
        self.max_iterations = max_iterations
        self.history = []

    def run(self, query: str):
        for i in range(self.max_iterations):
            resp = call_model(query, history=self.history)
            if not resp.tool_calls:
                return resp.content
            for tc in resp.tool_calls:
                key = (tc.name, json.dumps(tc.args, sort_keys=True))
                if self.history.count(key) >= 2:
                    raise RuntimeError(f"Loop detected: {tc.name} called 3x with same args")
                self.history.append(key)
                result = execute_tool(tc.name, tc.args)
                self.history.append({"tool_result": result})
        raise RuntimeError(f"Max iterations ({self.max_iterations}) exceeded")
```

## Production concerns

- **Latency:** Detection adds <1ms.
- **Cost:** Negligible.
- **Failure modes:** Detection itself can fail. Test it.
- **Security:** Detection logs may contain PII. Treat as sensitive.

## Anti-patterns

- ❌ **No detection for tool loops.** Catastrophic cost.
- ❌ **No cost alerts.** One bug = $1000s.
- ❌ **Treating each incident as novel.** Categorize; build runbooks.

## References

- [OpenAI: Error codes](https://platform.openai.com/docs/guides/error-codes) — verified 2026-07-30
- [OWASP LLM Top 10](https://genai.owasp.org/) — verified 2026-07-30

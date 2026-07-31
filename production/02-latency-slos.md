# Latency SLOs

> **Level:** INT · **Last verified:** 2026-07-30

## Why this matters

LLM latency is variable, multi-second, and dominated by tokens. Without explicit SLOs, you'll ship an experience that feels broken. With them, you can decide rationally when to cache, when to stream, and when to route to a smaller model.

## Core concepts

### The four latency metrics

| Metric | What | Target (2026) |
|--------|------|---------------|
| **TTFT** (time to first token) | Pre-fill + first token | <500ms p95 |
| **TPS** (tokens per second) | Decode speed | >50 TPS |
| **End-to-end p50** | Median total | <2s |
| **End-to-end p95** | Tail | <5s |

### The cost of tail latency

p99 is often 5–10× p50 for LLM calls. A single slow call can block a request. Always set timeouts.

### Latency budget breakdown

A typical agent call:

```
User input          0ms
Auth + validation   20ms
Retrieval (RAG)     200ms
LLM call (TTFT)     500ms
LLM decode (200 tok, 60 TPS) 3300ms
Response delivery   50ms
Total               ~4s
```

If TTFT > 1s, users perceive lag. Stream.

## Code: latency instrumentation

```python
import time, contextlib
from contextlib import contextmanager

@contextmanager
def latency_histogram(metric_name: str, tags: list[str] = None):
    start = time.perf_counter()
    try:
        yield
    finally:
        elapsed_ms = (time.perf_counter() - start) * 1000
        metrics.histogram(metric_name, elapsed_ms, tags=tags or [])

# Usage
with latency_histogram("llm.request.latency_ms", ["model:gpt-5"]):
    resp = client.chat.completions.create(...)
```

## Code: streaming for TTFT

```python
# Bad: blocks until full response
resp = client.chat.completions.create(model="gpt-5", messages=[...])
return resp.choices[0].message.content

# Good: stream first token within 500ms
def stream_response(messages):
    stream = client.chat.completions.create(model="gpt-5", messages=messages, stream=True)
    for chunk in stream:
        if chunk.choices[0].delta.content:
            yield chunk.choices[0].delta.content
# FastAPI returns StreamingResponse(stream_response(...))
```

## Production concerns

- **Latency:** Measure it. Don't guess.
- **Cost:** Caching reduces TTFT dramatically.
- **Failure modes:** Provider rate limits spike TTFT. Have fallbacks.
- **Security:** Latency telemetry shouldn't include content.

## Anti-patterns

- ❌ **Reporting only p50.** Tail is what users feel.
- ❌ **No timeouts on LLM calls.** One slow call blocks the request.
- ❌ **Blocking on full response when streaming is available.**

## References

- [OpenAI: Latency optimization](https://platform.openai.com/docs/guides/latency) — verified 2026-07-30
- [Anthropic: Prompt caching for latency](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching) — verified 2026-07-30

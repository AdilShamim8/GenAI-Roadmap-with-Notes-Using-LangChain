# Observability with OpenTelemetry

> **Level:** INT · **Last verified:** 2026-07-30

## Why this matters

LangSmith is great but locks you in. OpenTelemetry (OTel) is the vendor-neutral standard for LLM observability, supported by Arize Phoenix, OpenLLMetry, OpenInference, and most APM vendors. In 2026, OTel is the default for production GenAI.

## Core concepts

### The four signals

| Signal | What | Example |
|--------|------|---------|
| **Traces** | Tree of spans per request | `agent.run -> llm.call -> tool.search_docs` |
| **Metrics** | Aggregated numbers | Request count, p95 latency, cost |
| **Logs** | Discrete events | "Tool call failed: timeout" |
| **Attributes** | Span metadata | model, prompt_template_id, token_count |

### The span hierarchy

A production trace typically looks like:

```
agent.run (1.2s, $0.03)
├── retriever.search (180ms)
│   ├── embed.query (40ms)
│   └── vector_db.query (140ms)
├── llm.call (900ms, $0.025)
│   ├── system_prompt (cached: yes)
│   └── output_tokens (120)
└── tool.execute (40ms)
```

## Code: instrument with OpenInference

```python
# pip install openinference-instrumentation-openai
from openinference.instrumentation.openai import OpenAIInstrumentor
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter

tracer = TracerProvider()
trace.set_tracer_provider(tracer)
tracer.add_span_processor(BatchSpanProcessor(ConsoleSpanExporter()))

OpenAIInstrumentor().instrument()  # auto-instruments openai calls

# Now every OpenAI call emits a span automatically
resp = client.chat.completions.create(model="gpt-5", messages=[...])
```

## Code: custom spans

```python
from opentelemetry import trace
tracer = trace.get_tracer(__name__)

def search_docs(query: str) -> list:
    with tracer.start_as_current_span("search_docs") as span:
        span.set_attribute("query", query)
        results = vector_db.search(query, k=5)
        span.set_attribute("result_count", len(results))
        return results
```

## Production concerns

- **Latency:** OTel adds <1% overhead.
- **Cost:** Trace storage is cheap; sampling for high-volume.
- **Failure modes:** Sampling too aggressively loses rare failure traces.
- **Security:** Spans may contain prompts. Redact PII before export.

## Anti-patterns

- ❌ **Tracing only the LLM call.** Trace the full agent loop.
- ❌ **No span attributes.** You can't filter later.
- ❌ **100% sampling in production.** Use 1–10% for hot paths.

## References

- [OpenTelemetry for LLMs (OpenLLMetry)](https://github.com/traceloop/openllmetry) — verified 2026-07-30
- [OpenInference](https://github.com/Arize-ai/openinference) — verified 2026-07-30
- [Arize Phoenix](https://github.com/Arize-ai/phoenix) — verified 2026-07-30

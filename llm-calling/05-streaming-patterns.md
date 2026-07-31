# Streaming Patterns

> **Level:** INT · **Last verified:** 2026-07-30 · **Sources:** [OpenAI streaming](https://platform.openai.com/docs/api-reference/streaming), [Anthropic streaming](https://docs.anthropic.com/en/api/messages-streaming)

## Why this matters

Users abandon an LLM UI that takes 5 seconds to show a token. Streaming cuts perceived latency by 5–10×. But streaming is harder than blocking: you need to handle partial JSON, tool-call deltas, and client disconnects.

## Core concepts

### Two stream granularities

1. **Token streaming** — yield each token as it's generated. Standard since 2023.
2. **Content-block streaming (Anthropic, OpenAI Responses API)** — yield structured events: `text_start`, `text_delta`, `text_stop`, `tool_use_start`, `tool_input_delta`, `tool_use_stop`. More complex but more parseable.

### Server-Sent Events (SSE)

Most providers stream over SSE. Each event is `data: {...}\n\n`. The stream ends with `data: [DONE]`.

## Code: SSE in FastAPI

```python
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from openai import OpenAI

app = FastAPI()
client = OpenAI()

@app.get("/chat")
def chat(q: str):
    def gen():
        stream = client.chat.completions.create(
            model="gpt-5",
            messages=[{"role": "user", "content": q}],
            stream=True,
        )
        for chunk in stream:
            delta = chunk.choices[0].delta.content
            if delta:
                yield f"data: {delta}\n\n"
        yield "data: [DONE]\n\n"
    return StreamingResponse(gen(), media_type="text/event-stream")
```

## Streaming structured outputs

```python
# OpenAI: parse partial JSON as it streams
from partial_json_loader import loads  # or use the openai helpers

buffer = ""
for chunk in client.beta.chat.completions.parse(
    model="gpt-5",
    messages=[...],
    response_model=Person,
    stream=True,
):
    delta = chunk.choices[0].delta.content
    if delta:
        buffer += delta
        try:
            partial = loads(buffer)  # best-effort partial parse
            print(partial)
        except Exception:
            pass  # wait for more tokens
```

## Production concerns

- **Latency:** Aim for <500ms time-to-first-token. Anything above feels broken.
- **Cost:** Streaming doesn't save tokens; it saves perceived latency.
- **Failure modes:** Client disconnects mid-stream — your server must detect and cancel the upstream request or you'll pay for orphaned generations.
- **Security:** Don't stream PII to logs.

## Anti-patterns

- ❌ **Buffering the entire response before sending.** Defeats the point.
- ❌ **Ignoring client disconnects.** Costs money and ties up provider rate limit.
- ❌ **Using WebSockets when SSE suffices.** SSE is simpler, has better proxy support.

## References

- [OpenAI streaming](https://platform.openai.com/docs/api-reference/streaming) — verified 2026-07-30
- [Anthropic streaming](https://docs.anthropic.com/en/api/messages-streaming) — verified 2026-07-30
- [FastAPI StreamingResponse](https://fastapi.tiangolo.com/advanced/custom-response/#streamingresponse) — verified 2026-07-30

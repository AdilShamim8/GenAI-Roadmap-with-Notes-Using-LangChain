# OpenAI API

> **Level:** BEG · **Last verified:** 2026-07-30 · **Sources:** [OpenAI Platform Docs](https://platform.openai.com/docs/overview)

## Why this matters

OpenAI's API is the default starting point for GenAI work. Even if you end up on Anthropic or self-hosted, the OpenAI client shape (messages, roles, tool calls) is the de facto industry interface.

## Core concepts

- **Messages** — list of `{role, content}` dicts. Roles: `system`, `user`, `assistant`, `tool`.
- **Responses API** — newer endpoint that supports tools, computer use, and structured outputs more cleanly than Chat Completions.
- **Reasoning models** — o-series (o1, o3, o4-mini) think before answering; you cannot customize their system prompt the same way.
- **Prompt caching** — automatic for prompts >1024 tokens with a shared prefix.

## Code: minimal chat

```python
from openai import OpenAI
client = OpenAI()

resp = client.chat.completions.create(
    model="gpt-5",  # or "gpt-5-mini", "o3"
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Summarize the KV-cache in one sentence."},
    ],
    temperature=0.2,
)
print(resp.choices[0].message.content)
print(f"Tokens: in={resp.usage.prompt_tokens} out={resp.usage.completion_tokens}")
```

## Streaming

```python
stream = client.chat.completions.create(
    model="gpt-5",
    messages=[{"role": "user", "content": "Write a haiku about KV-cache."}],
    stream=True,
)
for chunk in stream:
    delta = chunk.choices[0].delta.content
    if delta:
        print(delta, end="", flush=True)
```

## Production concerns

- **Latency:** First-token latency (TTFT) for GPT-5 is ~500ms–2s depending on prompt size. Plan your UX around streaming.
- **Cost:** GPT-5 is priced higher than mini. Route by task complexity.
- **Failure modes:** Rate limits (TPM, RPM), 429s, occasional 5xx. Always retry with exponential backoff.
- **Security:** Don't put PII in prompts unless your DPA allows it. Use the OpenAI zero-retention enterprise tier for sensitive data.

## Anti-patterns

- ❌ **Calling `chat.completions` synchronously in a request handler** — use streaming or async.
- ❌ **Hardcoding `model="gpt-4"`** — pin to a specific snapshot or accept silent upgrades.
- ❌ **Ignoring `usage` in the response** — that's your cost telemetry.

## References

- [OpenAI API reference](https://platform.openai.com/docs/api-reference) — verified 2026-07-30
- [OpenAI Cookbook](https://cookbook.openai.com/) — verified 2026-07-30

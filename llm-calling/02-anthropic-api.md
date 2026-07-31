# Anthropic API

> **Level:** BEG · **Last verified:** 2026-07-30 · **Sources:** [Anthropic Docs](https://docs.anthropic.com/)

## Why this matters

Anthropic's Claude is the second pillar of the frontier-model landscape. The API differs from OpenAI's in important ways (system prompt is top-level, prompt caching is explicit, tool calling has its own shape).

## Core concepts

- **Top-level system prompt** — not a message in the list; a parameter on the request.
- **Messages** — list of `{role, content}` where `content` can be a string or a list of content blocks (text, image, tool_use, tool_result).
- **Prompt caching** — explicit. You mark cacheable blocks with `cache_control`. Cache hits are ~90% cheaper and 2× faster.
- **Extended thinking** — Claude Sonnet 4.5 and Opus 4.1 can "think" before responding; you get a `thinking` block in the response.
- **Computer use** — Claude can drive a virtual computer (browser, terminal) via the beta API.

## Code: minimal chat

```python
import anthropic
client = anthropic.Anthropic()

resp = client.messages.create(
    model="claude-opus-4-1",
    max_tokens=1024,
    system="You are a helpful assistant.",  # top-level, not a message
    messages=[
        {"role": "user", "content": "Summarize the KV-cache in one sentence."}
    ],
)
print(resp.content[0].text)
print(f"Tokens: in={resp.usage.input_tokens} out={resp.usage.output_tokens}")
```

## Prompt caching

```python
resp = client.messages.create(
    model="claude-opus-4-1",
    max_tokens=1024,
    system=[
        {"type": "text", "text": LARGE_SYSTEM_PROMPT, "cache_control": {"type": "ephemeral"}},
    ],
    messages=[{"role": "user", "content": "..."}],
)
# Subsequent calls with the same system prompt get a cache hit.
```

## Production concerns

- **Latency:** Claude Opus 4.1 is slower than Sonnet 4.5; route by task.
- **Cost:** Prompt caching is the single biggest lever. Cache long system prompts, few-shot examples, and tool definitions.
- **Failure modes:** `overloaded_error` during peak; retry with backoff.
- **Security:** Anthropic's usage policies are stricter than OpenAI's; some content gets blocked that other APIs allow.

## Anti-patterns

- ❌ **Stuffing the system prompt into a `system` message.** Anthropic wants it as the top-level `system` param.
- ❌ **Not using `cache_control` for static prompts.** You're paying 10× more than you need to.
- ❌ **Comparing model names by string prefix.** `claude-3-5-sonnet` is not the same as `claude-sonnet-4-5`.

## References

- [Anthropic API reference](https://docs.anthropic.com/en/api/messages) — verified 2026-07-30
- [Prompt caching](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching) — verified 2026-07-30

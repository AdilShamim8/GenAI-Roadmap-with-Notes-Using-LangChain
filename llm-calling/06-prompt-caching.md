# Prompt Caching

> **Level:** INT · **Last verified:** 2026-07-30 · **Sources:** [Anthropic prompt caching](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching), [OpenAI prompt caching](https://platform.openai.com/docs/guides/prompt-caching)

## Why this matters

Prompt caching is the single highest-leverage cost optimization in 2026. Cache a 10K-token system prompt that you reuse 10,000 times/day → save 80%+ on input tokens for those calls. Many teams don't realize it's automatic on OpenAI and explicit on Anthropic.

## Core concepts

### Two flavors

| Provider | Behavior | Cache hit discount |
|----------|----------|-------------------|
| OpenAI | Automatic for prompts >1024 tokens with shared prefix | 50% off cached input tokens |
| Anthropic | Explicit `cache_control` markers | 90% off cached input tokens, 25% premium to write |

### The economics

A 10K-token system prompt reused 10K times/day at $5/1M input tokens:
- No caching: $500/day in input.
- OpenAI auto-cache: ~$250/day.
- Anthropic explicit cache: ~$75/day (after write premium amortizes).

## Code: Anthropic explicit caching

```python
import anthropic
client = anthropic.Anthropic()

SYSTEM = [
    {"type": "text", "text": "<your 10K-token system prompt>"},
    {"type": "text", "text": "Cached on 2026-07-30.", "cache_control": {"type": "ephemeral"}},
]

# First call — writes to cache (small premium)
client.messages.create(model="claude-sonnet-4-5", max_tokens=1024, system=SYSTEM, messages=[...])

# Subsequent calls with same system — cache hit
client.messages.create(model="claude-sonnet-4-5", max_tokens=1024, system=SYSTEM, messages=[...])
# Check resp.usage.cache_read_input_tokens — should be non-zero.
```

## Code: OpenAI automatic caching

```python
# Nothing to do. Calls with shared prefixes >1024 tokens auto-cache.
# Check resp.usage.prompt_tokens_details.cached_tokens to confirm hits.
```

## Production concerns

- **Latency:** Cache hits cut TTFT by 30–60%.
- **Cost:** Track `cached_tokens` separately in your cost dashboard.
- **Failure modes:** Cache TTLs are ~5 minutes (Anthropic) or shorter (OpenAI). Low-traffic prompts may never hit.
- **Security:** Don't cache prompts containing user-specific PII — cache hit = data leak across users.

## Anti-patterns

- ❌ **Putting dynamic data before static data in the prompt.** Cache won't hit because prefix changed.
- ❌ **Caching prompts with per-user content mixed in.** Cross-user leak risk.
- ❌ **Assuming cache hits.** Measure `cache_read_input_tokens` / `input_tokens` ratio.

## References

- [Anthropic prompt caching](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching) — verified 2026-07-30
- [OpenAI prompt caching](https://platform.openai.com/docs/guides/prompt-caching) — verified 2026-07-30

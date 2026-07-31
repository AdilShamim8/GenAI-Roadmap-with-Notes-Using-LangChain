# Guardrails, Retries, Fallbacks

> **Level:** INT → ADV · **Last verified:** 2026-07-30

## Why this matters

Production agents fail. APIs rate-limit, models hallucinate, tools throw. The difference between a demo and a production agent is how it handles failure. Three patterns matter: guardrails (prevent), retries (recover), fallbacks (degrade).

## Core concepts

### Guardrails

Run before and after the LLM call:
- **Input guardrails** — validate input, redact PII, detect injection.
- **Output guardrails** — validate output, filter toxic content, enforce schema.

### Retries

- **Idempotent retries** — same call, retry on transient failure.
- **Backoff** — exponential, with jitter.
- **Cap** — 3 retries max; then fail.

### Fallbacks

- **Model fallback** — GPT-5 → Claude Sonnet → Gemini Flash.
- **Tool fallback** — primary API fails, use cached data.
- **UX fallback** — "I'm having trouble, here's what I found so far."

## Code: retry with backoff

```python
import asyncio, random
from functools import wraps

def retry(max_attempts=3, base_delay=1.0, exceptions=(Exception,)):
    def deco(fn):
        @wraps(fn)
        async def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return await fn(*args, **kwargs)
                except exceptions as e:
                    if attempt == max_attempts - 1:
                        raise
                    delay = base_delay * (2 ** attempt) + random.random()
                    await asyncio.sleep(delay)
        return wrapper
    return deco

@retry(max_attempts=3, exceptions=(TimeoutError, RateLimitError))
async def call_llm(prompt: str) -> str:
    return await client.chat.completions.create(...)
```

## Code: model fallback chain

```python
MODELS = ["gpt-5", "claude-sonnet-4-5", "gemini-2.5-pro"]

async def call_with_fallback(prompt: str) -> str:
    for model in MODELS:
        try:
            return await call_model(model, prompt)
        except (RateLimitError, OverloadedError) as e:
            continue
    raise RuntimeError("All models failed")
```

## Code: output guardrail

```python
from pydantic import BaseModel, ValidationError

class Output(BaseModel):
    answer: str
    confidence: float  # 0..1

def safe_call(prompt: str) -> Output:
    for _ in range(3):
        raw = llm_call(prompt)
        try:
            out = Output.model_validate_json(raw)
            if 0 <= out.confidence <= 1:
                return out
        except ValidationError:
            continue
    raise RuntimeError("Output failed validation after 3 retries")
```

## Production concerns

- **Latency:** Retries add latency; budget for worst case.
- **Cost:** Retried calls still cost money.
- **Failure modes:** Retrying non-idempotent operations causes duplicates.
- **Security:** Don't retry in a way that exposes PII in logs.

## Anti-patterns

- ❌ **Retrying 4xx errors.** They won't succeed; only retry 5xx and timeouts.
- ❌ **Infinite retry loops.** Always cap.
- ❌ **No fallback when one model is enough.** Don't over-engineer.

## References

- [Tenacity (retry library)](https://github.com/jd/tenacity) — verified 2026-07-30
- [OpenAI: Error handling](https://platform.openai.com/docs/guides/error-codes) — verified 2026-07-30

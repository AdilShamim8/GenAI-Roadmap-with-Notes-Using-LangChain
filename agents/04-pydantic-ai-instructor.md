# Pydantic AI & Instructor

> **Level:** INT · **Last verified:** 2026-07-30

## Why this matters

Not every agent needs a full framework. If you want type-safe structured outputs with minimal abstraction, Pydantic AI (from the Pydantic team) and Instructor (from jxnl) are the lightest-weight options. They're ideal for: extraction pipelines, classification, deterministic single-turn tools.

## Core concepts

### Instructor

Instructor wraps any OpenAI-compatible client and adds:
- Pydantic schema → JSON schema conversion.
- Retry on validation failure.
- Streaming partial objects.

### Pydantic AI

Pydantic AI is a thin agent framework built around:
- Type-safe inputs and outputs.
- Dependency injection (pass DB connections, etc.).
- Multi-provider support.

Use Instructor when you just want structured outputs. Use Pydantic AI when you want a lightweight agent with tools.

## Code: Instructor

```python
import instructor
from pydantic import BaseModel, Field
from openai import OpenAI

class Recipe(BaseModel):
    name: str
    ingredients: list[str] = Field(min_items=1)
    steps: list[str] = Field(min_items=1)

client = instructor.from_openai(OpenAI())

recipe = client.chat.completions.create(
    model="gpt-5",
    response_model=Recipe,
    messages=[{"role": "user", "content": "Give me a recipe for carbonara."}],
)
# recipe is a Recipe instance, validated.
```

## Code: Pydantic AI agent

```python
from pydantic_ai import Agent, RunContext
from pydantic import BaseModel

class Output(BaseModel):
    summary: str
    sentiment: str  # "positive" | "neutral" | "negative"

agent = Agent("openai:gpt-5", output_type=Output, system_prompt="You analyze reviews.")

@agent.tool
def lookup_order(ctx: RunContext[None], order_id: str) -> dict:
    '''Look up an order by ID.'''
    return {"order_id": order_id, "total": 49.99}

result = agent.run_sync("Summarize review for order 12345.")
print(result.output.summary, result.output.sentiment)
```

## Production concerns

- **Latency:** Minimal overhead vs raw API calls.
- **Cost:** Retries (Instructor) can double cost on validation failures. Use native structured outputs where available.
- **Failure modes:** Models will sometimes hallucinate fields. Pydantic strips them; log when it does.
- **Security:** Validate ranges (Field constraints) — never trust LLM-generated numbers unchecked.

## Anti-patterns

- ❌ **Using Instructor when the provider supports native structured outputs.** Use native.
- ❌ **Huge nested schemas.** Split into multiple calls.
- ❌ **Skipping Field constraints.** Always set `ge`, `le`, `min_items`, etc.

## References

- [Instructor](https://github.com/jxnl/instructor) — verified 2026-07-30
- [Pydantic AI](https://ai.pydantic.dev/) — verified 2026-07-30

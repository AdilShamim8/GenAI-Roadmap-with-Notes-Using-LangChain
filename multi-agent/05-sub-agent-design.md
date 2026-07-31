# Sub-Agent Design

> **Level:** ADV · **Last verified:** 2026-07-30

## Why this matters

Sub-agents are the unit of decomposition in a multi-agent system. Bad sub-agent boundaries produce duplication, conflicts, and untraceable failures. Good boundaries produce a system where each agent has a clear job and the composition feels natural.

## Core concepts

### The single-responsibility principle (for agents)

Each sub-agent should:
- Have one job (retrieval, synthesis, QA, planning).
- Have a clear input contract.
- Have a clear output contract.
- Own its own tools.
- Not need to know about other agents' internals.

### Sizing

| Sub-agent complexity | Tools | Iterations | When |
|----------------------|-------|------------|------|
| Trivial | 1–2 | 1–3 | Single tool call + summary |
| Moderate | 3–7 | 5–10 | Multi-step within one domain |
| Complex | 7–15 | 10–25 | Cross-domain, multi-step |
| Too complex | >15 | >25 | Split into multiple sub-agents |

### The contract pattern

Every sub-agent should declare:
- **Input schema** — Pydantic model.
- **Output schema** — Pydantic model.
- **Tools** — fixed list, not dynamic.
- **Failure modes** — what it returns when it fails.

## Code: a well-designed retrieval sub-agent

```python
from pydantic import BaseModel, Field
from agents import Agent, Runner, function_tool

class RetrievalInput(BaseModel):
    query: str = Field(description="The question to find sources for.")
    max_sources: int = Field(default=5, ge=1, le=20)

class RetrievalOutput(BaseModel):
    sources: list[dict] = Field(description="List of {title, url, snippet, score}")
    found: bool

@function_tool
def hybrid_search(query: str, k: int = 20) -> str:
    '''Hybrid vector + BM25 search.'''
    return json.dumps(search(query, k))

@function_tool
def rerank(query: str, docs: list[dict]) -> str:
    '''Re-rank documents by relevance.'''
    return json.dumps(reranker(query, docs))

retrieval_agent = Agent(
    name="RetrievalAgent",
    instructions='''You retrieve sources for a query.
    1. Call hybrid_search with the query.
    2. Call rerank on the results.
    3. Return the top-N sources as JSON.
    If no sources found, return {"sources": [], "found": false}.''',
    tools=[hybrid_search, rerank],
    model="gpt-5",
    output_type=RetrievalOutput,
)
```

## Production concerns

- **Latency:** Sub-agent = full LLM call. Don't sub-agent trivial work.
- **Cost:** Each sub-agent call multiplies token cost.
- **Failure modes:** Sub-agent returns malformed output. Use structured outputs.
- **Security:** Sub-agent only gets the tools it needs. Least privilege.

## Anti-patterns

- ❌ **Sub-agent with 30 tools.** Split.
- ❌ **Sub-agent that calls other sub-agents that call back.** Cycles.
- ❌ **Sub-agent without an output schema.** Untestable.

## References

- [Anthropic: Building effective agents](https://www.anthropic.com/research/building-effective-agents) — verified 2026-07-30
- [OpenAI: Multi-agent systems](https://platform.openai.com/docs/guides/multi-agent) — verified 2026-07-30

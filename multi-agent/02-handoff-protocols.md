# Handoff Protocols

> **Level:** ADV · **Last verified:** 2026-07-30

## Why this matters

When agent A hands off to agent B, what exactly passes between them? Get this wrong and you get context loss, repeated work, or state corruption. Handoffs are the seams of multi-agent systems — and seams are where things break.

## Core concepts

### What gets passed

- **Task description** — what B should do.
- **Relevant context** — distilled, not raw transcript.
- **State** — typed object (Pydantic model or TypedDict).
- **Artifacts** — files, IDs, URLs produced so far.
- **Return protocol** — when B is done, what should it return to A?

### Three handoff styles

| Style | Example | When |
|-------|---------|------|
| **Message-based** | "Tell the billing agent the user wants a refund for order X" | OpenAI Agents SDK |
| **State-based** | Pass a typed state object | LangGraph |
| **Shared-blackboard** | All agents read/write a shared store | Network topology |

## Code: OpenAI Agents SDK handoff

```python
from agents import Agent, Runner

billing = Agent(name="Billing", instructions="You handle refunds. Return a JSON with refund_id and amount.", model="gpt-5")
triage = Agent(name="Triage", instructions="Route to billing.", handoffs=[billing], model="gpt-5")

result = Runner.run_sync(triage, "I want a refund for order 123.")
# Triage calls handoff to billing; billing runs to completion; final output is billing's.
```

## Code: LangGraph state handoff

```python
class State(TypedDict):
    user_query: str
    billing_decision: dict | None
    final_response: str | None

def triage(state: State) -> State:
    if "refund" in state["user_query"].lower():
        return {**state, "next": "billing"}
    return {**state, "next": "support"}

def billing(state: State) -> State:
    # ... process refund
    return {**state, "billing_decision": {"refund_id": "r_123", "amount": 49.99}}
```

## Production concerns

- **Latency:** Each handoff is a fresh LLM call with new context.
- **Cost:** Distill context before handoff; don't pass raw transcripts.
- **Failure modes:** Handoff target doesn't exist; state schema mismatches.
- **Security:** Don't pass PII across agents that don't need it.

## Anti-patterns

- ❌ **Passing the entire conversation history.** Distill.
- ❌ **No return type from the handoff target.** You can't act on what you can't parse.
- ❌ **Circular handoffs.** A→B→A→B→...

## References

- [OpenAI Agents SDK handoffs](https://openai.github.io/openai-agents-python/handoffs/) — verified 2026-07-30
- [LangGraph multi-agent](https://langchain-ai.github.io/langgraph/concepts/multi_agent/) — verified 2026-07-30

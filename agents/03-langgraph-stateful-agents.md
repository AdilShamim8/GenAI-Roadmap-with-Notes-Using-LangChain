# LangGraph Stateful Agents

> **Level:** ADV · **Last verified:** 2026-07-30 · **Sources:** [LangGraph](https://langchain-ai.github.io/langgraph/)

## Why this matters

When you need durable, multi-step, multi-agent workflows with explicit state, conditional branching, and human-in-the-loop checkpoints, LangGraph is the most mature option. It's more verbose than OpenAI Agents SDK or Claude Agent SDK, but it gives you control nothing else matches.

## Core concepts

### The graph

A LangGraph agent is a directed graph where:
- **Nodes** are functions (or LLM calls).
- **Edges** are conditional or unconditional transitions.
- **State** is a typed dict (or Pydantic model) passed between nodes.
- **Checkpoints** serialize state at every step, enabling pause/resume.

### Why state matters

Most "agent frameworks" hide state in closure variables. LangGraph makes it explicit — you can serialize it, replay it, fork it, time-travel it. This is the difference between a demo and a production system.

## Code: a ReAct agent in LangGraph

```python
from typing import TypedDict, Annotated
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool

class State(TypedDict):
    messages: Annotated[list, add_messages]

@tool
def get_weather(city: str) -> str:
    '''Get weather for a city.'''
    return f"Sunny, 22C in {city}."

llm = ChatOpenAI(model="gpt-5").bind_tools([get_weather])

def call_model(state: State):
    return {"messages": [llm.invoke(state["messages"])]}

def should_continue(state: State):
    last = state["messages"][-1]
    return "tools" if last.tool_calls else END

from langgraph.prebuilt import ToolNode

graph = StateGraph(State)
graph.add_node("agent", call_model)
graph.add_node("tools", ToolNode([get_weather]))
graph.add_edge(START, "agent")
graph.add_conditional_edges("agent", should_continue, ["tools", END])
graph.add_edge("tools", "agent")
app = graph.compile()

result = app.invoke({"messages": [("user", "Weather in Tokyo?")]})
print(result["messages"][-1].content)
```

## Code: human-in-the-loop checkpoint

```python
app = graph.compile(
    checkpointer=MemorySaver(),
    interrupt_before=["tools"],  # pause before tool execution
)
config = {"configurable": {"thread_id": "abc"}}
result = app.invoke({"messages": [("user", "Delete the file /tmp/data.csv")]}, config)
# Inspect result["messages"][-1].tool_calls; if approved:
app.invoke(None, config)  # resumes
```

## Production concerns

- **Latency:** Graph overhead is ~10ms per node. Negligible vs LLM calls.
- **Cost:** State size affects checkpoint storage cost. Keep state lean.
- **Failure modes:** Cycles in the graph can loop forever. Use recursion limits.
- **Security:** State can contain PII; encrypt checkpoints at rest.

## Anti-patterns

- ❌ **Using LangGraph for a simple ReAct loop.** OpenAI Agents SDK is simpler.
- ❌ **Putting everything in state.** Only put what nodes need.
- ❌ **No recursion limit.** `app.invoke(..., config={"recursion_limit": 25})`.

## References

- [LangGraph docs](https://langchain-ai.github.io/langgraph/) — verified 2026-07-30
- [LangGraph GitHub](https://github.com/langchain-ai/langgraph) — verified 2026-07-30

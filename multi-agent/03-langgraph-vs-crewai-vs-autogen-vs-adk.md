# LangGraph vs CrewAI vs AutoGen vs Google ADK

> **Level:** ADV · **Last verified:** 2026-07-30

## Why this matters

These are the four multi-agent frameworks you'll see in 2026 job postings. Each has a distinct philosophy. Picking one is a 6-month commitment; understanding the trade-offs upfront saves rewrites.

## The comparison

| Dimension | LangGraph | CrewAI | AutoGen v0.4+ | Google ADK |
|-----------|-----------|--------|---------------|------------|
| **Philosophy** | Explicit graphs | Role-based crews | Async event-driven | Vertex-native |
| **Abstraction** | State graph | Crew + agents + tasks | Agents + topics | Agents + tools + sessions |
| **State** | Typed, checkpointed | Per-task | Distributed | Session-scoped |
| **Multi-vendor** | Yes | Yes | Yes | Gemini-first |
| **Human-in-loop** | First-class | Add-on | Add-on | First-class |
| **Streaming** | First-class | Limited | First-class | First-class |
| **Maturity** | High | Medium | High (v0.4 rewrite) | Medium |
| **Best for** | Production workflows | Rapid prototyping | Async, distributed | Google Cloud shops |

## When to pick what

- **LangGraph** — you need durable, checkpointed, stateful workflows with conditional logic. The default for production.
- **CrewAI** — you want to ship a multi-agent demo in an afternoon and don't need fine control.
- **AutoGen v0.4** — your workload is fundamentally async/event-driven (many agents, low coupling).
- **Google ADK** — you're all-in on Vertex AI and want first-class Google Workspace integration.

## Code: same task, three frameworks

### CrewAI

```python
from crewai import Agent, Task, Crew

researcher = Agent(role="Researcher", goal="Find sources", backstory="...", llm="gpt-5")
writer = Agent(role="Writer", goal="Write report", backstory="...", llm="gpt-5")

crew = Crew(agents=[researcher, writer], tasks=[
    Task(description="Research {topic}", agent=researcher),
    Task(description="Write a 1-page report based on research", agent=writer),
])
result = crew.kickoff(inputs={"topic": "MoE architectures"})
```

### AutoGen v0.4

```python
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_ext.models.openai import OpenAIChatCompletionClient

model = OpenAIChatCompletionClient(model="gpt-5")
researcher = AssistantAgent("researcher", model_client=model, system_message="Research the topic.")
writer = AssistantAgent("writer", model_client=model, system_message="Write a 1-page report.")

team = RoundRobinGroupChat([researcher, writer], max_turns=4)
result = await team.run(task="MoE architectures")
```

## Production concerns

- **Latency:** Each framework adds overhead; LangGraph is the leanest.
- **Cost:** All multi-agent frameworks multiply token cost. Budget accordingly.
- **Failure modes:** Framework abstractions hide token usage; instrument your own.
- **Security:** Each framework has different sandboxing stories. Verify.

## Anti-patterns

- ❌ **Starting with CrewAI for production.** Fine for prototypes; rewrite in LangGraph for prod.
- ❌ **AutoGen for simple workflows.** The async overhead isn't worth it.
- ❌ **Google ADK if you're not on Vertex.** Lock-in isn't worth it.

## References

- [LangGraph](https://langchain-ai.github.io/langgraph/) — verified 2026-07-30
- [CrewAI](https://docs.crewai.com/) — verified 2026-07-30
- [AutoGen](https://microsoft.github.io/autogen/) — verified 2026-07-30
- [Google ADK](https://google.github.io/adk-docs/) — verified 2026-07-30

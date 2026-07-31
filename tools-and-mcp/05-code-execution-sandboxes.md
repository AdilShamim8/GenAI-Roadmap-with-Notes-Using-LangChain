# Code Execution Sandboxes

> **Level:** INT · **Last verified:** 2026-07-30

## Why this matters

Agents that can run code are dramatically more capable (data analysis, math, file transforms, scraping). Agents that can run code on *your* infrastructure are a security nightmare. Sandboxes give you the capability without the risk.

## Core concepts

### The options

| Option | Latency | Cost | Isolation | Best for |
|--------|---------|------|-----------|----------|
| OpenAI Code Interpreter | 5–30s | $0.05/run | OpenAI-managed | Quick analysis, charts |
| Anthropic code execution | 5–20s | metered | Anthropic-managed | Claude-integrated workflows |
| E2B | 1–5s | $0.05/min | MicroVM | Production agents needing fast cold-start |
| Modal | 1–3s | pay-per-invocation | Container | Python functions at scale |
| Daytona | 1–5s | per-seat | Devcontainer | Long-lived dev envs |
| Self-hosted gVisor / Firecracker | 50–500ms | infra | VM | Full control, max complexity |

### What a sandbox gives you

- **Isolation** — the agent's code can't reach your network or filesystem.
- **Ephemerality** — every run starts from a clean snapshot.
- **Resource limits** — CPU, memory, network egress caps.
- **Auditability** — full input/output logs.

## Code: E2B sandbox

```python
from e2b_code_interpreter import Sandbox

sbx = Sandbox()
result = sbx.run_code('''
import pandas as pd
df = pd.read_csv("https://example.com/data.csv")
df.groupby("region").revenue.sum().to_dict()
''')
print(result.text)  # last expression's value
sbx.close()
```

## Code: OpenAI Code Interpreter (via Assistants API)

```python
from openai import OpenAI
client = OpenAI()

assistant = client.beta.assistants.create(
    model="gpt-5",
    tools=[{"type": "code_interpreter"}],
)
# Run a thread; the assistant can call code interpreter autonomously.
```

## Production concerns

- **Latency:** Cold-start matters for UX. E2B and Modal are sub-second.
- **Cost:** Sandboxes are cheap ($0.05/min) until they're not (10K runs/day = $720/day).
- **Failure modes:** Network egress from sandbox = data exfiltration vector. Block by default.
- **Security:** Treat sandbox output as untrusted. Don't pipe it directly into your DB.

## Anti-patterns

- ❌ **Running agent code on your application server.** Always isolate.
- ❌ **Allowing outbound network from sandbox without allowlist.**
- ❌ **No resource limits.** A `while True` will cost you.

## References

- [E2B](https://e2b.dev/) — verified 2026-07-30
- [Modal](https://modal.com/) — verified 2026-07-30
- [OpenAI Code Interpreter](https://platform.openai.com/docs/assistants/tools/code-interpreter) — verified 2026-07-30

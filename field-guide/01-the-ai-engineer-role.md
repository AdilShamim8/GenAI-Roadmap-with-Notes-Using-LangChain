# The AI Engineer Role

> **Last verified:** 2026-07-30

## What the role is

An AI engineer in 2026 is a backend-adjacent engineer who builds production systems that use LLMs as a core component. The job is *not* training models — that's an ML researcher. The job is *not* pure prompting — that's an analyst with a ChatGPT subscription.

The AI engineer owns:

- **The prompt layer** — system prompts, few-shot, structured outputs.
- **The retrieval layer** — RAG, vector DBs, rerankers.
- **The tool layer** — function calling, MCP, computer use, sandboxes.
- **The orchestration layer** — agents, multi-agent, state.
- **The evals layer** — golden datasets, judges, regression tests.
- **The observability layer** — tracing, cost, latency, drift.
- **The production layer** — deployment, scaling, incident response.

## What it isn't

| Role | What they own | Overlap with AI eng |
|------|--------------|---------------------|
| ML engineer | Model training, MLOps | Self-hosting, fine-tuning |
| Data engineer | Pipelines, warehouses | RAG data ingestion |
| Backend engineer | APIs, DBs, queues | API design, infra |
| Data scientist | Analysis, experiments | Evals, statistics |
| ML researcher | New model architectures | Almost none |

## The CRISP-DM equivalent for AI engineering

A useful mental model (adapted from CRISP-DM):

1. **Business understanding** — what user outcome are we enabling?
2. **Data understanding** — what data do we have? what's its quality?
3. **Prompt / model selection** — which model(s)? what prompt structure?
4. **Evaluation** — how will we know it's good?
5. **Deployment** — how will we ship this?
6. **Monitoring** — how will we know it's drifting?

Most teams skip 4 and 6. Most incidents come from skipping 4 and 6.

## How the role differs by company size

- **Startup (1–50 eng):** You own everything from prompt to deploy. High autonomy; high chaos.
- **Mid-size (50–500 eng):** You own the application layer; platform team owns infra. More structure; less breadth.
- **Big tech (500+ eng):** You own a specific component (e.g., the retrieval service). Deep but narrow.
- **Enterprise (non-tech):** You're the "AI person" in a non-AI org. Lots of education; slower shipping.

## References

- [Alexey Grigorev: My vision of the AI engineer role](https://github.com/alexeygrigorev/ai-engineering-field-guide/blob/main/role/01-my-vision.md) — verified 2026-07-30
- [Chip Huyen: AI Engineering](https://www.oreilly.com/library/view/ai-engineering/9781098166298/) — verified 2026-07-30
- [Latent Space: What is an AI Engineer?](https://www.latent.space/p/what-is-an-ai-engineer) — verified 2026-07-30

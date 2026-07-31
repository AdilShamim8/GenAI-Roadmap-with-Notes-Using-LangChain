# Portfolio Strategy

> **Last verified:** 2026-07-30

## The principle

3 deep projects > 15 shallow ones. Reviewers spend 5–10 minutes per portfolio; depth is the only thing that registers.

## The 3-project template

Pick projects that cover three different skills:

1. **RAG-heavy** — demonstrates retrieval, chunking, evals.
2. **Agent-heavy** — demonstrates tool use, orchestration, agent loop.
3. **Production-heavy** — demonstrates deployment, observability, cost.

Three projects, three angles, one coherent narrative: "I can build production GenAI across the stack."

## Each project must have

- **README** — problem statement, architecture diagram, how to run, evals summary.
- **Runnable code** — Dockerized; one command to start.
- **Tests** — at least unit tests for the non-LLM parts.
- **Evals** — golden dataset + judge + a `make eval` command.
- **Live demo** — deployed somewhere (Fly.io, Render, Railway; free tier is fine).
- **Postmortem** — short write-up of one failure you encountered and how you fixed it.

## What kills a portfolio

- **No evals.** The #1 killer. Without evals, your project is vibes.
- **No demo.** "Run it locally" = reviewer won't.
- **No tests.** Signals you've never shipped to production.
- **5 projects, all "chatbot over a PDF."** No depth, no breadth.
- **Framework-tutorial copy.** Reviewers can tell.

## What elevates a portfolio

- **Cost analysis.** "This costs $X per 1K requests; here's the breakdown."
- **Failure mode analysis.** "It breaks on X; here's why and what I'd do next."
- **Benchmark against a baseline.** "Naive RAG scored 60% on my evals; hybrid + rerank scored 85%."
- **A real user.** Even 10 users is 10x more signal than 0.

## Project ideas (matched to this repo)

See [`projects/`](../projects) for 15 portfolio-grade builds. The three strongest for a portfolio:

- [Project 2: Hybrid RAG over a Notion workspace](../projects/02-hybrid-rag-over-notion/) — RAG-heavy.
- [Project 5: Multi-agent research pipeline](../projects/05-multi-agent-research-pipeline/) — Agent-heavy.
- [Project 8: Cost-optimized routing proxy](../projects/08-cost-optimized-routing-proxy/) — Production-heavy.

## References

- [Alexey Grigorev: Portfolio guide](https://github.com/alexeygrigorev/ai-engineering-field-guide/blob/main/portfolio/) — verified 2026-07-30
- [Hamel Husain: Your AI Product Needs Evals](https://hamel.dev/blog/posts/evals/) — verified 2026-07-30

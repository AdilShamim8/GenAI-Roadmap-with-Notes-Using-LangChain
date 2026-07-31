# Skills That Get You Hired

> **Last verified:** 2026-07-30 · Based on public job postings + practitioner interviews.

## The 2026 baseline

If you don't have these, you won't pass the resume screen:

- Python, fluently. Async, typing, packaging.
- At least one major LLM API (OpenAI / Anthropic / Gemini), production use.
- RAG: vector DB, hybrid search, reranking.
- Function calling / structured outputs.
- Some agent framework (LangGraph, OpenAI Agents SDK, Claude Agent SDK).
- Evals: at least golden datasets + LLM-as-judge.
- Docker + a cloud (AWS/GCP/Azure) at "ship a service" level.
- Git, CI, code review.

## The 2026 differentiators

These get you to offer, not just screen:

- **Multi-agent orchestration** — can design a 3-agent system with handoffs and explain your choices.
- **MCP** — have written an MCP server, not just used one.
- **Cost engineering** — can talk about prompt caching, routing, cascade strategies with numbers.
- **Online evals** — have shipped a sampling + judge pipeline in production.
- **Computer use / browser automation** — have shipped a working flow.
- **Fine-tuning** — QLoRA on a 7B+ model, with evals showing improvement.
- **Self-hosting** — vLLM/SGLang in production with metrics.
- **Safety** — prompt-injection mitigations, red-teaming, audit logging.
- **Realtime / voice** — Realtime API or Gemini Live in production.

## Skills that don't matter as much as you think

- Implementing transformers from scratch. (Interesting; not hireable.)
- Training a model from scratch. (Lab jobs only.)
- CUDA programming. (Specialist.)
- LangChain v0.1 internals. (Deprecated.)
- Specific framework syntax. (Frameworks change; concepts stay.)

## The portfolio that gets you hired

3 projects, each with:
- README explaining the problem and architecture.
- Runnable code (Dockerized).
- Evals with a golden dataset.
- A deployed demo (even a free-tier one).
- A short postmortem of one production failure you encountered.

3 deep projects > 15 shallow ones. See [`04-portfolio-strategy.md`](./04-portfolio-strategy.md).

## References

- [Alexey Grigorev: Skills analysis](https://github.com/alexeygrigorev/ai-engineering-field-guide/blob/main/role/02-skills.md) — verified 2026-07-30
- [Builtin AI/ML jobs](https://builtin.com/jobs/ai-ml) — verified 2026-07-30
- [Levels.fyi AI Engineer compensation](https://www.levels.fyi/t/software-engineer/focus/ai-engineer) — verified 2026-07-30

# GenAI Engineering Roadmap

<p align="center">
  <strong>The production-grade, evals-first, career-aware roadmap for GenAI engineers in 2026.</strong>
  <br/>
  <em>From "I can call the OpenAI API" to "I shipped a multi-agent system that runs in production with SLOs and an evals harness."</em>
</p>

<p align="center">
  <a href="./LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License"/></a>
  <a href="./LAST_VERIFIED.md"><img src="https://img.shields.io/badge/claims%20last%20verified-2026--07-30-brightgreen.svg" alt="Last verified"/></a>
  <a href="./CHANGELOG.md"><img src="https://img.shields.io/badge/changelog-v1.0--alpha-orange.svg" alt="Changelog"/></a>
  <a href="https://github.com/AdilShamim8/GenAI-Roadmap-with-Notes-and-Projects/actions"><img src="https://img.shields.io/badge/CI-link--check%20%2B%20markdownlint-green.svg" alt="CI"/></a>
</p>

---

## What this is

A **rigorously-sourced, file-per-topic, evals-first** roadmap for becoming a production GenAI engineer. Every factual claim is cited and dated in [`LAST_VERIFIED.md`](./LAST_VERIFIED.md). Every topic follows a [consistent template](./CONTRIBUTING.md#topic-file-template). Every project ships with code, tests, and an evals harness.

This is **not** a link dump. This is **not** a single 600-line README. This is **not** LangChain-only. This is the roadmap a principal AI engineer would recommend without caveats.

## What this is not

- Not a tutorial. Topics assume you can read Python and understand HTTP.
- Not exhaustive. We picked one lane — **production GenAI engineering** — and go deep.
- Not a model leaderboard. We cover architectures and patterns that survive model releases.

## The 12-rung skill ladder

| Rung | Topic | Folder | Est. time |
|------|-------|--------|-----------|
| 0 | Foundations | [`foundations/`](./foundations) | 1 week |
| 1 | Applied LLM Calling | [`llm-calling/`](./llm-calling) | 1 week |
| 2 | Context Engineering | [`context-engineering/`](./context-engineering) | 2 weeks |
| 3 | Modern RAG | [`rag/`](./rag) | 3 weeks |
| 4 | Tools & MCP | [`tools-and-mcp/`](./tools-and-mcp) | 2 weeks |
| 5 | Single-Agent Engineering | [`agents/`](./agents) | 2 weeks |
| 6 | Multi-Agent Orchestration | [`multi-agent/`](./multi-agent) | 3 weeks |
| 7 | Evals & Test-Driven LLM Dev | [`evals/`](./evals) | 2 weeks |
| 8 | Production & Economics | [`production/`](./production) | 2 weeks |
| 9 | Fine-tuning & Self-Hosting | [`fine-tuning-and-self-hosting/`](./fine-tuning-and-self-hosting) | 2 weeks |
| 10 | Safety, Alignment & Red-Teaming | [`safety/`](./safety) | 1 week |
| 11 | Real-Time & Voice | [`realtime-voice/`](./realtime-voice) | 1 week |

## Pick your starting point

| Your background | Recommended path |
|-----------------|------------------|
| Backend engineer | [`docs/learning-paths/from-backend-engineer.md`](./docs/learning-paths/from-backend-engineer.md) |
| Frontend engineer | [`docs/learning-paths/from-frontend-engineer.md`](./docs/learning-paths/from-frontend-engineer.md) |
| Data engineer | [`docs/learning-paths/from-data-engineer.md`](./docs/learning-paths/from-data-engineer.md) |
| Data scientist | [`docs/learning-paths/from-data-scientist.md`](./docs/learning-paths/from-data-scientist.md) |
| ML engineer | [`docs/learning-paths/from-ml-engineer.md`](./docs/learning-paths/from-ml-engineer.md) |
| Starting from zero | [`docs/learning-paths/from-zero.md`](./docs/learning-paths/from-zero.md) |

## The GenAI Field Guide

Career and industry context — separate from the technical curriculum.

- [`field-guide/01-the-ai-engineer-role.md`](./field-guide/01-the-ai-engineer-role.md)
- [`field-guide/02-skills-that-get-you-hired.md`](./field-guide/02-skills-that-get-you-hired.md)
- [`field-guide/03-interview-loop-anatomy.md`](./field-guide/03-interview-loop-anatomy.md)
- [`field-guide/04-portfolio-strategy.md`](./field-guide/04-portfolio-strategy.md)
- [`field-guide/05-salary-bands.md`](./field-guide/05-salary-bands.md)
- [`field-guide/06-job-market-trends.md`](./field-guide/06-job-market-trends.md)

## Portfolio projects

15 portfolio-grade builds, each with `README.md`, `src/`, `tests/`, `evals/`, `DEPLOYMENT.md`. See [`projects/`](./projects).

## Decision guides

When you hit a fork in the road, start here:

- [`docs/decision-guides/choosing-an-agent-sdk.md`](./docs/decision-guides/choosing-an-agent-sdk.md)
- [`docs/decision-guides/choosing-a-vector-db.md`](./docs/decision-guides/choosing-a-vector-db.md)
- [`docs/decision-guides/rag-vs-long-context.md`](./docs/decision-guides/rag-vs-long-context.md)
- [`docs/decision-guides/fine-tune-or-not.md`](./docs/decision-guides/fine-tune-or-not.md)
- [`docs/decision-guides/self-host-vs-api.md`](./docs/decision-guides/self-host-vs-api.md)
- [`docs/decision-guides/open-weight-model-selection.md`](./docs/decision-guides/open-weight-model-selection.md)

## Curated external resources

[`awesome/`](./awesome) — papers, books, courses, blogs, tools, communities. One-line reviews, not bare links.

## How to use this repo

1. **Read [`LAST_VERIFIED.md`](./LAST_VERIFIED.md)** to see when every factual claim was last checked.
2. **Pick a learning path** based on your background.
3. **Work the rungs in order.** Each rung links to the next.
4. **Build at least 3 projects** as you go. Code beats reading.
5. **Run the evals** that ship with each project. Internalize the evals-first mindset.

## Contributing

See [`CONTRIBUTING.md`](./CONTRIBUTING.md). The short version: every factual claim must be sourced and dated, every file must follow the topic template, every project must ship with tests.

## License

MIT — see [`LICENSE`](./LICENSE).

## Acknowledgements

- [`alexeygrigorev/ai-engineering-field-guide`](https://github.com/alexeygrigorev/ai-engineering-field-guide) for the field-guide playbook and the "data, not filler" philosophy.
- Every practitioner who has published a postmortem, evals harness, or agent architecture in public.

## Star history
If this roadmap helps you, star it. Stars keep the project maintained.

# Portfolio Projects

> 15 portfolio-grade builds, each demonstrating a specific in-demand skill.
> Each project ships with `README.md`, `src/`, `tests/`, `evals/`, `DEPLOYMENT.md`.

## The 3-project portfolio

You don't need all 15. Pick three that span the stack:

| Track | Project |
|-------|---------|
| RAG-heavy | [02-hybrid-rag-over-notion](./02-hybrid-rag-over-notion/) |
| Agent-heavy | [05-multi-agent-research-pipeline](./05-multi-agent-research-pipeline/) |
| Production-heavy | [08-cost-optimized-routing-proxy](./08-cost-optimized-routing-proxy/) |

## All projects

| # | Project | Difficulty | Skill |
|---|---------|------------|-------|
| 01 | [Structured Output Extractor](./01-structured-output-extractor/) | 🟢 BEG | Structured outputs, Pydantic, evals |
| 02 | [Hybrid RAG over Notion](./02-hybrid-rag-over-notion/) | 🟢 BEG | Chunking, hybrid search, reranking |
| 03 | [MCP Server for Postgres](./03-mcp-server-for-postgres/) | 🟡 INT | MCP architecture, tool design |
| 04 | [Computer-Use Data Entry Agent](./04-computer-use-data-entry-agent/) | 🔴 ADV | Anthropic computer use, browser |
| 05 | [Multi-Agent Research Pipeline](./05-multi-agent-research-pipeline/) | 🔴 ADV | Orchestration, handoffs |
| 06 | [Realtime Voice Assistant](./06-realtime-voice-assistant/) | 🔴 ADV | Realtime API, VAD, interruption |
| 07 | [Eval-Driven Prompt Refinement Harness](./07-eval-driven-prompt-refinement/) | 🟡 INT | Golden datasets, LLM-as-judge |
| 08 | [Cost-Optimized Routing Proxy](./08-cost-optimized-routing-proxy/) | 🟡 INT | Agent economics, cascades |
| 09 | [Self-Hosted Llama Deployment](./09-self-hosted-llama-deployment/) | 🟡 INT | vLLM, quantization, breakeven |
| 10 | [Agent with Episodic Memory](./10-agent-with-episodic-memory/) | 🔴 ADV | Memory architectures |
| 11 | [GraphRAG over Codebase](./11-graphrag-over-codebase/) | 🔴 ADV | GraphRAG, code chunking |
| 12 | [Red-Teaming Harness](./12-red-teaming-harness/) | 🟡 INT | Garak, PyRIT, defense |
| 13 | [Long-Horizon Research Agent](./13-long-horizon-research-agent/) | ⚫ EXP | Checkpointing, recovery |
| 14 | [Multimodal Customer Support Agent](./14-multimodal-customer-support-agent/) | 🔴 ADV | Multimodal, RAG, escalation |
| 15 | [Incident Response Autopilot](./15-incident-response-autopilot/) | 🔴 ADV | Production agents, safety |

## Status

All 15 are currently skeletons. Each contains:
- `README.md` with problem, architecture, stack, eval metrics.
- `pyproject.toml` with pinned dependencies.
- `Makefile` with `install`, `run`, `test`, `eval` targets.
- `tests/test_smoke.py` — replace with real tests.
- `evals/golden.jsonl` + `evals/eval_runner.py` — replace placeholders with real cases.
- `DEPLOYMENT.md` with deployment + postmortem template.
- `Dockerfile`.

To bring a project to "portfolio-ready": fill in `src/`, write real tests, populate the golden dataset, ship a demo.

## Difficulty legend

- 🟢 BEG — Approachable after Rungs 0–3.
- 🟡 INT — Approachable after Rungs 0–7.
- 🔴 ADV — Approachable after Rungs 0–8.
- ⚫ EXP — Approachable after Rungs 0–11 + production experience.

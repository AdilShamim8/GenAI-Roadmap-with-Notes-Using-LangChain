# GenAI Roadmap — Expert Audit & Rebuild Blueprint

> **Auditor:** Principal AI engineer / flagship-repo maintainer perspective
> **Date:** 30 July 2026
> **Subject:** `AdilShamim8/GenAI-Roadmap-with-Notes-and-Projects` (the v0.1-legacy state)
> **Benchmark:** `alexeygrigorev/ai-engineering-field-guide`
> **Verdict:** Rebuilt as v1.0-alpha. See [`CHANGELOG.md`](./CHANGELOG.md) for what changed.

---

## 1. TL;DR

The legacy repo (v0.1) was a 654-line README with fabricated model names (GPT-5.5, Claude Opus 4.7, Claude Mythos, "Project Glasswing", LangChain v1.2.16, etc.) and an aspirational folder tree that contained no real content. It had LangChain-tunnel-vision, no evals, no agent economics, no field guide, and no maintenance discipline.

The v1.0-alpha rebuild:
- Purged every fabricated claim (see `LAST_VERIFIED.md`).
- Reduced the README to a map (under 150 lines).
- Exploded the content into a file-per-topic structure with 12 rungs.
- Added a GenAI Field Guide (career + industry).
- Added 15 portfolio-grade project skeletons.
- Added CI: link-check, markdownlint, freshness-reminder.
- Added the per-topic file template enforced via `CONTRIBUTING.md`.

## 2. Critical issues that were fixed

### P0-1. Fabricated facts (resolved)
All fabricated model names, version numbers, and events removed. Every factual claim now lives in `LAST_VERIFIED.md` with a source URL and verification date. A monthly GitHub Action opens an issue to re-verify.

### P0-2. Repo name / badge mismatch (resolved)
All badges now point to the correct repo name.

### P0-3. Aspirational folder tree (resolved)
Every folder described in the README now contains real `.md` files following the per-topic template.

### P0-4. LangChain-tunnel-vision (resolved)
The rebuilt curriculum covers OpenAI, Anthropic, Google, open-weight ecosystems, plus 10+ agent frameworks (OpenAI Agents SDK, Claude Agent SDK, LangGraph, CrewAI, AutoGen, Google ADK, Pydantic AI, Instructor, LlamaIndex, Mastra, Vercel AI SDK).

## 3. What's now in the repo (and why)

- **12-rung skill ladder** — foundations → real-time/voice. Each rung is a directory.
- **6 learning paths** branched by background (backend, frontend, data eng, data sci, ML, zero).
- **6 decision guides** for the forks in the road (agent SDK, vector DB, RAG vs long-context, fine-tune or not, self-host vs API, open-weight selection).
- **4 architecture diagrams** as Mermaid.
- **15 portfolio project skeletons**, each with the required README + src + tests + evals + DEPLOYMENT structure.
- **GenAI Field Guide** — career, skills, interview, portfolio, salary, trends.
- **Awesome/** — curated external resources with one-line reviews.
- **CI** — link-check, markdownlint, freshness reminder, issue templates.
- **Per-topic file template** — enforced via `CONTRIBUTING.md`.

## 4. The 2026 skill ladder (what actually matters)

| Rung | Topic | Why it matters |
|------|-------|----------------|
| 0 | Foundations | Transformers, tokenization, KV-cache, MoE. Skip the 2015-era NLP. |
| 1 | Applied LLM Calling | API fluency across providers + structured outputs + caching + multimodal. |
| 2 | Context Engineering | The new discipline that replaces "prompt engineering." |
| 3 | Modern RAG | Hybrid search, rerankers, agentic RAG, GraphRAG, multimodal RAG. |
| 4 | Tools & MCP | Function calling + MCP (the 2026 standard). |
| 5 | Single-Agent Engineering | OpenAI Agents SDK, Claude Agent SDK, LangGraph, Pydantic AI. |
| 6 | Multi-Agent Orchestration | Topologies, handoffs, framework comparison. |
| 7 | Evals | Golden datasets, LLM-as-judge, promptfoo, statistical rigor. |
| 8 | Production & Economics | Cost engineering, latency SLOs, observability, incident response. |
| 9 | Fine-tuning & Self-Hosting | LoRA, QLoRA, DPO, vLLM, SGLang, quantization, breakeven math. |
| 10 | Safety | Prompt injection taxonomy, Garak/PyRIT, output filtering, audits. |
| 11 | Real-Time & Voice | OpenAI Realtime, Gemini Live, VAD, interruption handling. |

## 5. Maintenance discipline

- Every factual claim is in `LAST_VERIFIED.md` with a source URL + verification date.
- Monthly GitHub Action opens an issue to re-verify.
- Weekly `lychee` link-check.
- Per-topic template enforced via `CONTRIBUTING.md`.
- Quarterly content audit.

## 6. The 0.0001% repo checklist

- [x] No fabricated facts. Every claim is sourced and dated.
- [x] README is a map. Under 150 lines, every bullet links to a real file.
- [x] One file per topic.
- [x] Original synthesis (comparison tables, decision frameworks, anti-patterns).
- [x] Multi-entry-point learning paths.
- [x] Mermaid diagrams for major concepts.
- [x] Runnable code in every code-bearing topic.
- [ ] Tests + evals in every project (skeletons only — to be filled in).
- [x] CI pipeline that lints and link-checks.
- [x] Career module tying skills to jobs.
- [x] Decision guides for every fork.
- [x] Honest scope (production GenAI engineering).
- [x] Maintenance discipline (CHANGELOG, LAST_VERIFIED, monthly audits).
- [x] Contribution standards that enforce the quality bar.
- [x] Visual learning path on the README.

## 7. Next steps for the maintainer

1. Fill in the 15 project skeletons with runnable code + tests + evals.
2. Solicit external contributions; the topic template makes this straightforward.
3. Submit to awesome-genai lists; announce on r/LocalLLaMA and Latent Space.
4. Quarterly: walk through `LAST_VERIFIED.md`, refresh stale claims.
5. Annually: revisit the 12-rung ladder. Add or remove rungs as the field shifts.

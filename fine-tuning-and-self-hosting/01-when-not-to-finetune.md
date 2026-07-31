# When NOT to Fine-Tune

> **Level:** INT · **Last verified:** 2026-07-30

## Why this matters

The default answer to "should I fine-tune?" is no. Most teams that fine-tune shouldn't have. Fine-tuning is expensive, slows iteration, and rarely beats well-engineered prompting + RAG + structured outputs. This file exists to talk you out of it.

## The decision matrix

| Symptom | Don't fine-tune. Instead... |
|---------|----------------------------|
| "Model doesn't know X" | Use RAG |
| "Model hallucinates" | RAG + structured outputs + faithfulness evals |
| "Model wrong format" | Structured outputs (JSON schema) |
| "Model too verbose" | Better system prompt; max_tokens |
| "Model can't use our API" | Tools / MCP |
| "Model is too slow" | Route to smaller model |
| "Model is too expensive" | Prompt caching + routing |
| "Model style is off" | Few-shot examples in context |

| Symptom | Fine-tune |
|---------|-----------|
| Latency budget <50ms, can't afford a frontier model | Distill to 7B |
| Domain vocab not in pretraining (medical, legal, internal codenames) | Continued pretraining or LoRA |
| Need consistent output style across millions of calls | Style alignment LoRA |
| Cost: prompt too expensive at scale, can't cache | Smaller fine-tuned model |

## The hidden costs

- **Iteration speed:** Each fine-tune run = hours to days. Prompt iteration = minutes.
- **Eval burden:** You need evals BEFORE fine-tuning to measure improvement.
- **Maintenance:** Fine-tunes need re-training when base models update.
- **Talent:** Fine-tuning done wrong produces worse-than-base models.
- **Lock-in:** A fine-tune ties you to one base model.

## The 2026 reality

Frontier models (GPT-5, Claude Opus 4.1, Gemini 3 Pro) are so strong that 95% of "I should fine-tune" use cases are better served by:
1. Better prompting.
2. RAG.
3. Structured outputs.
4. Few-shot examples.

If you've done all four and the model still fails your evals, then consider fine-tuning.

## Production concerns

- **Latency:** Self-hosted fine-tunes can be faster than API (no network).
- **Cost:** Fine-tune cost = compute + storage + serving infra + ops.
- **Failure modes:** Catastrophic forgetting; over-fitting to eval set.
- **Security:** Fine-tunes on internal data need the same access controls as the data.

## Anti-patterns

- ❌ **Fine-tuning to add knowledge.** Use RAG.
- ❌ **Fine-tuning without an eval set.** You can't measure improvement.
- ❌ **Fine-tuning a frontier model.** Distill to a smaller one.

## References

- [Chip Huyen: AI Engineering](https://huyenchip.com/2024/03/14/ai-oss.html) — verified 2026-07-30
- [It's Hype Till It Isn't](https://huyenchip.com/2024/03/14/ai-oss.html) — verified 2026-07-30

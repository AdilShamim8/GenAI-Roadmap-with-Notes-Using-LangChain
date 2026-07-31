# Fine-tune or Not

> **Last verified:** 2026-07-30

## The default answer

**Don't.** 90%+ of "I should fine-tune" impulses are better served by:
- Better prompting.
- Better retrieval (RAG).
- Few-shot examples in context.
- Structured outputs.
- Tool use.

## When fine-tune actually wins

| Scenario | Why fine-tune helps |
|----------|---------------------|
| Latency-critical, <50ms budget | Smaller fine-tuned model beats large prompted model |
| Domain vocabulary not in pretraining | Medical, legal, internal codenames |
| Consistent output format required | Style/format alignment |
| Cost: prompt too expensive at scale | Smaller fine-tuned model with no in-context examples |
| Distillation from a frontier model | Compress GPT-5 quality into a 7B model |

## What fine-tune does NOT help

- Adding new knowledge (use RAG).
- Reducing hallucinations (RAG + structured outputs).
- Tool use (tools work fine in base models).
- Multi-step reasoning (frontier models still win).

## If you decide to fine-tune

1. Start with **LoRA** on a 7B-13B base. Don't go full fine-tune.
2. Use **DPO** or **ORPO** for alignment, not RLHF (too expensive).
3. Build an eval set BEFORE fine-tuning. Run it before and after.
4. Serve with **vLLM** with LoRA adapters enabled.

## References

- [It's Hype Till It Isn't — Chip Huyen](https://huyenchip.com/2024/03/14/ai-oss.html) — verified 2026-07-30
- [PEFT (LoRA) paper](https://arxiv.org/abs/2106.09685) — verified 2026-07-30

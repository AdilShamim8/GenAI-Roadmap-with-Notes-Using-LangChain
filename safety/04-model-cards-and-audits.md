# Model Cards & Audits

> **Level:** INT · **Last verified:** 2026-07-30

## Why this matters

Every model you use has known limitations, biases, and intended-use constraints documented in its model card. Ignoring these is both an ethical risk and a legal one (EU AI Act, sectoral regs). Reading the card takes 5 minutes; not reading it can cost millions.

## Core concepts

### What's in a model card

- **Intended use** — what the model is designed for.
- **Out-of-scope uses** — what the provider explicitly says not to do.
- **Training data summary** — high-level description.
- **Eval results** — benchmarks, including subgroup performance.
- **Known limitations** — hallucination rate, language coverage, etc.
- **Ethical considerations** — bias, dual-use, environmental.
- **Citation** — how to attribute.

### Where to find them

| Provider | Where |
|----------|-------|
| OpenAI | https://openai.com/index/ (per-model announcements) + system card PDFs |
| Anthropic | https://www.anthropic.com/news (model release posts) + model card PDFs |
| Google | https://deepmind.google/technologies/gemini/ (per-model docs) |
| Meta (Llama) | https://llama.meta.com/model-card/ |
| HuggingFace | Per-model README.md tab |

### Auditing your stack

For every model in production, you should know:
- Model name and exact version snapshot.
- Provider's intended use statement.
- Known limitations relevant to your use case.
- Data handling terms (training on your inputs? retention?).
- Compliance certifications (SOC 2, HIPAA, ISO 27001).

## The audit checklist

Maintain a `model_audit.md` per project:

```markdown
# Model Audit — Project X

## Production models
| Model | Version snapshot | Provider | Intended use | Data handling | Last reviewed |
|-------|------------------|----------|--------------|---------------|---------------|
| GPT-5 | gpt-5-2026-04-15 | OpenAI | Chat, reasoning | Zero-retention enterprise | 2026-07-30 |
| Claude Sonnet 4.5 | claude-sonnet-4-5-2026-04-15 | Anthropic | Chat, vision | Standard | 2026-07-30 |

## Known limitations impacting us
- GPT-5: weaker on non-English (per system card).
- Claude: stricter content filtering; some legit queries blocked.

## Compliance
- SOC 2: both providers compliant.
- HIPAA: only OpenAI enterprise tier; Anthropic BAA available.
- EU AI Act: classify our use as "limited risk"; documentation in /docs/eu-ai-act.md.
```

## Production concerns

- **Latency:** None.
- **Cost:** None.
- **Failure modes:** Models get deprecated; audits get stale. Refresh quarterly.
- **Security:** Audit docs may reference internal architectures; treat as confidential.

## Anti-patterns

- ❌ **Not reading model cards.** You'll use models out-of-scope.
- ❌ **No model audit doc.** Can't answer compliance questions quickly.
- ❌ **Static audit doc.** Models change; audits must too.

## References

- [Model Cards for Model Reporting (paper)](https://arxiv.org/abs/1810.03993) — verified 2026-07-30
- [OpenAI GPT-5 system card](https://openai.com/index/gpt-5/) — verified 2026-07-30
- [Anthropic Claude model cards](https://www.anthropic.com/news) — verified 2026-07-30

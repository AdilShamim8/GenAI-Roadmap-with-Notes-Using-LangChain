# promptfoo

> **Level:** INT · **Last verified:** 2026-07-30 · **Sources:** [promptfoo](https://www.promptfoo.dev/)

## Why this matters

promptfoo is the easiest way to start with evals. YAML config, runs in CLI or CI, supports all major providers, has built-in LLM-as-judge. If you're not doing evals yet, start here this week.

## Core concepts

### The config

A single YAML file declares:
- **Prompts** — one or more prompt templates to compare.
- **Providers** — one or more models to test against.
- **Tests** — assertions: exact match, regex, LLM-rubric, javascript function.

### The assertions

| Assertion | Use |
|-----------|-----|
| `equals` | Exact match |
| `icontains` | Case-insensitive contains |
| `regex` | Pattern |
| `is-json` | Valid JSON |
| `llm-rubric` | LLM judges against a rubric |
| `javascript` | Custom function |
| `similar` | Embedding similarity to expected |

## Code: a promptfoo config

```yaml
# promptfooconfig.yaml
description: Billing agent evals

prompts:
  - file://prompts/billing_v1.txt
  - file://prompts/billing_v2.txt

providers:
  - id: openai:gpt-5
  - id: anthropic:claude-sonnet-4-5

tests:
  - description: Simple refund
    vars:
      query: "I want a refund for order 123"
    assert:
      - type: icontains
        value: "refund"
      - type: llm-rubric
        value: "Mentions the order ID 123 and provides next steps."
      - type: latency
        threshold: 5000  # ms

  - description: High-value refund escalates
    vars:
      query: "I want a refund for $5000"
    assert:
      - type: icontains
        value: "escalate"
      - type: llm-rubric
        value: "Does NOT promise the refund directly."
```

## Run

```bash
npx promptfoo eval
npx promptfoo view  # opens web UI with results
```

## CI integration

```yaml
# .github/workflows/evals.yml
- name: Run evals
  run: npx promptfoo eval -c promptfooconfig.yaml --no-cache
- name: Fail on regression
  run: npx promptfoo eval --failOnThreshold --threshold 0.85
```

## Production concerns

- **Latency:** Evals are offline; latency is fine.
- **Cost:** LLM-rubric assertions are 2× prompt cost. Use sparingly on cheap models.
- **Failure modes:** LLM-rubric judges drift; pin a specific model version.
- **Security:** Test cases may contain PII; don't commit them.

## Anti-patterns

- ❌ **Only exact-match assertions.** LLMs rarely produce exact matches.
- ❌ **No CI integration.** Evals that don't run on PRs are useless.
- ❌ **Comparing prompts without a control.** Always have a baseline.

## References

- [promptfoo docs](https://www.promptfoo.dev/docs/) — verified 2026-07-30
- [promptfoo GitHub](https://github.com/promptfoo/promptfoo) — verified 2026-07-30

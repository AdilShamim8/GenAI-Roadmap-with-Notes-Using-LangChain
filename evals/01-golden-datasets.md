# Golden Datasets

> **Level:** INT · **Last verified:** 2026-07-30

## Why this matters

Without a golden dataset, you're vibes-tuning prompts. Every change is a guess. A golden dataset — even 50 examples — turns prompt engineering from art to engineering. This is the single highest-leverage evals practice.

## Core concepts

### What's in a golden dataset

Each row contains:
- **Input** — the user query / context.
- **Expected output** — exact string, regex, or rubric.
- **Metadata** — category, difficulty, source.

### Three flavors

| Flavor | What's expected | Eval method |
|--------|-----------------|-------------|
| Exact match | Exact string | `output == expected` |
| Regex / schema | Pattern or JSON schema | `re.match` / pydantic |
| Rubric | "Must mention X, must not mention Y" | LLM-as-judge |

### How big?

- **50 examples** — catches obvious regressions.
- **200 examples** — catches subtle ones.
- **1000+ examples** — production-grade; you'll need sampling to keep eval cost manageable.

### Where do examples come from?

1. **Real production traffic** (sampled, anonymized) — best signal.
2. **Hand-crafted edge cases** — adversarial; catches known failure modes.
3. **LLM-generated synthetic** — useful for coverage; lower signal.
4. **Public benchmarks** — good for calibration, not for production-specific behavior.

## Code: a minimal golden dataset

```yaml
# evals/golden.yaml
- id: refund_simple
  input: "I want a refund for order 123"
  expected:
    must_mention: ["refund_id", "order 123"]
    must_not_mention: ["competitor"]
    max_length: 100
  category: billing
  difficulty: easy

- id: refund_escalation
  input: "I want a refund for $5000"
  expected:
    must_mention: ["escalate", "tier-2"]
    must_route_to: human
  category: billing
  difficulty: medium
```

```python
# evals/runner.py
import yaml

def run_evals(agent, golden_path: str):
    cases = yaml.safe_load(open(golden_path))
    results = []
    for c in cases:
        out = agent.run(c["input"])
        ok = (
            all(kw in out.lower() for kw in c["expected"]["must_mention"])
            and not any(kw in out.lower() for kw in c["expected"].get("must_not_mention", []))
        )
        results.append({"id": c["id"], "passed": ok, "output": out})
    passed = sum(r["passed"] for r in results)
    print(f"{passed}/{len(results)} passed")
    return results
```

## Production concerns

- **Latency:** Eval runs are offline; latency doesn't matter, cost does.
- **Cost:** 200 examples × $0.02/call = $4/run. Run on every PR.
- **Failure modes:** Golden dataset rots — production queries drift. Refresh quarterly.
- **Security:** Don't put PII in golden files. Anonymize before committing.

## Anti-patterns

- ❌ **No golden dataset.** You can't detect regressions.
- ❌ **Golden dataset with only easy cases.** Adversarial cases are the point.
- ❌ **Treating golden dataset as static.** It's a living artifact.

## References

- [Hamel Husain: Your AI Product Needs Evals](https://hamel.dev/blog/posts/evals/) — verified 2026-07-30
- [Anthropic: Evals guide](https://docs.anthropic.com/en/docs/build-with-claude/evals) — verified 2026-07-30

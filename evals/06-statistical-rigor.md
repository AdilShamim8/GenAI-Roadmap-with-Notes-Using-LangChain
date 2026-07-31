# Statistical Rigor for Prompt Changes

> **Level:** ADV · **Last verified:** 2026-07-30

## Why this matters

"Prompt v2 scored 85% vs v1's 82%, ship it" is the most common evals mistake. On a 100-example dataset, that 3-point difference is likely noise. Without statistical rigor, you'll ship regressions disguised as improvements.

## Core concepts

### The problem

LLM outputs are stochastic. Eval scores are noisy. Small differences on small datasets are dominated by noise, not signal.

### The minimum bar

For a prompt change A vs B:
1. **Same dataset** — both prompts run on the same golden set.
2. **Multiple seeds** — each prompt × example × 3+ seeds (temperature > 0).
3. **Paired comparison** — for each (example, seed), compare A vs B.
4. **Significance test** — McNemar's test for binary outcomes, Wilcoxon for scores.

### Sample size

Rough rules of thumb for detecting a 5% difference with 80% power:
- Binary pass/fail metric: ~500 examples per prompt.
- 1–5 score metric: ~100 examples per prompt.

If your golden set is <50, you can only detect 15%+ differences.

## Code: paired comparison with significance test

```python
from scipy.stats import wilcoxon
import numpy as np

# scores_a[i] and scores_b[i] are scores on the same example i
scores_a = np.array([...])
scores_b = np.array([...])

diff = scores_b - scores_a
print(f"Mean improvement: {diff.mean():.3f}")

stat, p = wilcoxon(scores_a, scores_b)
print(f"Wilcoxon p-value: {p:.4f}")

if p < 0.05 and diff.mean() > 0:
    print("B is significantly better. Ship it.")
else:
    print("No significant difference. Don't ship.")
```

## Code: bootstrap confidence interval

```python
def bootstrap_ci(scores_a, scores_b, n_boot=10000, ci=0.95):
    diffs = scores_b - scores_a
    boot_means = [np.random.choice(diffs, len(diffs)).mean() for _ in range(n_boot)]
    lower = np.percentile(boot_means, (1 - ci) / 2 * 100)
    upper = np.percentile(boot_means, (1 + ci) / 2 * 100)
    return lower, upper

lo, hi = bootstrap_ci(scores_a, scores_b)
print(f"95% CI for improvement: [{lo:.3f}, {hi:.3f}]")
```

## Production concerns

- **Latency:** More seeds = more eval time.
- **Cost:** 3 seeds × 200 examples × 2 prompts = 1200 LLM calls per eval.
- **Failure modes:** Even with rigor, judge noise dominates. Audit judges periodically.
- **Security:** No special concerns beyond standard eval hygiene.

## Anti-patterns

- ❌ **"Ship if score went up."** Statistical noise.
- ❌ **One seed per example.** Can't separate noise from signal.
- ❌ **Different datasets for A and B.** Not comparable.

## References

- [Evaluating LLMs with statistical rigor — Chip Huyen](https://huyenchip.com/2024/03/14/ai-oss.html) — verified 2026-07-30
- [McNemar's test](https://en.wikipedia.org/wiki/McNemar%27s_test) — verified 2026-07-30
- [Wilcoxon signed-rank test](https://en.wikipedia.org/wiki/Wilcoxon_signed-rank_test) — verified 2026-07-30

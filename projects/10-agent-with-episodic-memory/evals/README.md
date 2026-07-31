# Evals for Agent With Episodic Memory

## Methodology

This project uses a golden dataset + automated runner pattern.

1. **Golden dataset** — `golden.jsonl` contains test cases with inputs and expected outputs/rubrics.
2. **Eval runner** — `eval_runner.py` loads the dataset, runs the agent on each case, scores against the rubric.
3. **Report** — printed summary + JSON artifact for CI.

## Metrics

- `memory_recall_rate`
- `hallucination_rate`
- `user_satisfaction`
- `cost_per_turn`

## Running

```bash
make eval
```

## Adding cases

Append to `golden.jsonl`:

```jsonl
{"id": "case_001", "input": "...", "expected": {"must_mention": ["..."], "must_not_mention": ["..."]}}
```

## CI integration

In `.github/workflows/evals.yml`:

```yaml
- name: Run evals
  run: make eval
- name: Fail on regression
  run: python evals/check_threshold.py --min-pass-rate 0.85
```

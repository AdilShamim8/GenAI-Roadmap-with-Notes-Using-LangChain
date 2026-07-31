# Project 12: Red-Teaming Harness

> **Difficulty:** INT · **Skill demonstrated:** Garak/PyRIT, defense patterns · **Status:** 🚧 Skeleton

## Problem

Build a harness that runs Garak + PyRIT + custom probes against your agent, reports vulnerabilities, and tracks mitigations.

## Architecture

```mermaid
graph LR
    Input[Input] --> Agent[Agent pipeline]
    Agent --> Eval[Evals]
    Eval --> Output[Output]
```

Agent endpoint -> Garak probes -> PyRIT attacks -> custom probes -> vulnerability report -> mitigation tracker.

## Stack

- Python
- garak
- pyrit
- openai
- pytest

## Getting started

```bash
# Install
make install

# Run
make run

# Run tests
make test

# Run evals
make eval
```

## Evals

This project ships with a golden dataset and eval runner. Eval metrics:

- `vulnerability_count`
- `block_rate_per_probe`
- `false_positive_rate`

The `make eval` command runs the full eval suite and prints a report. Evals must pass before merging to main.

## Project structure

```
12-red-teaming-harness/
├── README.md              # this file
├── pyproject.toml         # dependencies
├── Makefile               # install/run/test/eval targets
├── DEPLOYMENT.md          # how to deploy
├── src/
│   └── __init__.py
├── tests/
│   └── test_smoke.py
├── evals/
│   ├── golden.jsonl       # golden dataset
│   ├── eval_runner.py     # eval runner
│   └── README.md
└── .gitignore
```

## What this project demonstrates

This is a portfolio project. When complete, it should clearly demonstrate:
- Garak/PyRIT, defense patterns
- Production concerns: cost, latency, failure modes, security
- Evals: golden dataset + automated runner
- Tests: at least unit + integration
- Deployment: Dockerized, one-command deploy

## Next steps

See `DEPLOYMENT.md` for deployment instructions and `evals/README.md` for the eval methodology.

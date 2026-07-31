# Project 08: Cost-Optimized Routing Proxy

> **Difficulty:** INT · **Skill demonstrated:** Agent economics, prompt caching, cascade · **Status:** 🚧 Skeleton

## Problem

Build an OpenAI-compatible proxy that routes queries by complexity to minimize cost while preserving quality.

## Architecture

```mermaid
graph LR
    Input[Input] --> Agent[Agent pipeline]
    Agent --> Eval[Evals]
    Eval --> Output[Output]
```

Incoming request -> classifier (small model) -> route to GPT-5-mini / GPT-5 / o3 -> response + cost telemetry.

## Stack

- Python
- FastAPI
- openai
- anthropic
- redis
- prometheus

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

- `cost_per_1k_requests`
- `quality_score`
- `routing_accuracy`

The `make eval` command runs the full eval suite and prints a report. Evals must pass before merging to main.

## Project structure

```
08-cost-optimized-routing-proxy/
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
- Agent economics, prompt caching, cascade
- Production concerns: cost, latency, failure modes, security
- Evals: golden dataset + automated runner
- Tests: at least unit + integration
- Deployment: Dockerized, one-command deploy

## Next steps

See `DEPLOYMENT.md` for deployment instructions and `evals/README.md` for the eval methodology.

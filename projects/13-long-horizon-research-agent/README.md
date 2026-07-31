# Project 13: Long-Horizon Research Agent

> **Difficulty:** EXP · **Skill demonstrated:** Checkpointing, recovery, sub-delegation · **Status:** 🚧 Skeleton

## Problem

Build an agent that runs for hours autonomously, checkpoints state, recovers from failures, and produces a deliverable.

## Architecture

```mermaid
graph LR
    Input[Input] --> Agent[Agent pipeline]
    Agent --> Eval[Evals]
    Eval --> Output[Output]
```

Planner -> task queue -> workers (parallel) -> Postgres checkpoint store -> critic -> human escalation trigger.

## Stack

- Python
- langgraph
- postgres
- celery
- redis
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

- `task_completion_rate`
- `checkpoint_recovery_time`
- `cost_per_task`
- `human_escalation_rate`

The `make eval` command runs the full eval suite and prints a report. Evals must pass before merging to main.

## Project structure

```
13-long-horizon-research-agent/
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
- Checkpointing, recovery, sub-delegation
- Production concerns: cost, latency, failure modes, security
- Evals: golden dataset + automated runner
- Tests: at least unit + integration
- Deployment: Dockerized, one-command deploy

## Next steps

See `DEPLOYMENT.md` for deployment instructions and `evals/README.md` for the eval methodology.

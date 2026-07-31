# Project 10: Agent With Episodic Memory

> **Difficulty:** ADV · **Skill demonstrated:** Memory architectures, vector store for memory · **Status:** 🚧 Skeleton

## Problem

Build an agent that remembers past conversations, retrieves relevant memories per turn, and improves over time.

## Architecture

```mermaid
graph LR
    Input[Input] --> Agent[Agent pipeline]
    Agent --> Eval[Evals]
    Eval --> Output[Output]
```

Conversation -> memory writer (extract facts) -> vector store -> per-turn retrieval -> context augmentation.

## Stack

- Python
- langgraph
- qdrant
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

- `memory_recall_rate`
- `hallucination_rate`
- `user_satisfaction`
- `cost_per_turn`

The `make eval` command runs the full eval suite and prints a report. Evals must pass before merging to main.

## Project structure

```
10-agent-with-episodic-memory/
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
- Memory architectures, vector store for memory
- Production concerns: cost, latency, failure modes, security
- Evals: golden dataset + automated runner
- Tests: at least unit + integration
- Deployment: Dockerized, one-command deploy

## Next steps

See `DEPLOYMENT.md` for deployment instructions and `evals/README.md` for the eval methodology.

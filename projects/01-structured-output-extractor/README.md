# Project 01: Structured Output Extractor

> **Difficulty:** BEG · **Skill demonstrated:** Structured outputs, Pydantic, evals · **Status:** 🚧 Skeleton

## Problem

Extract structured data from unstructured text (invoices, business cards, emails) into a typed schema with high reliability.

## Architecture

```mermaid
graph LR
    Input[Input] --> Agent[Agent pipeline]
    Agent --> Eval[Evals]
    Eval --> Output[Output]
```

Input text -> Pydantic schema -> LLM (schema-constrained) -> validated object -> output JSON.

## Stack

- Python 3.11+
- openai
- pydantic
- instructor
- pytest
- promptfoo

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

- `field_accuracy`
- `schema_conformance`
- `refusal_rate`

The `make eval` command runs the full eval suite and prints a report. Evals must pass before merging to main.

## Project structure

```
01-structured-output-extractor/
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
- Structured outputs, Pydantic, evals
- Production concerns: cost, latency, failure modes, security
- Evals: golden dataset + automated runner
- Tests: at least unit + integration
- Deployment: Dockerized, one-command deploy

## Next steps

See `DEPLOYMENT.md` for deployment instructions and `evals/README.md` for the eval methodology.

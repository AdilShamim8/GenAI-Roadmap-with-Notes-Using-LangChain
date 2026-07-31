# Project 06: Realtime Voice Assistant

> **Difficulty:** ADV · **Skill demonstrated:** OpenAI Realtime API, VAD, interruption handling · **Status:** 🚧 Skeleton

## Problem

Build a sub-second-latency voice assistant that handles interruptions, supports tool calls, and runs in a browser.

## Architecture

```mermaid
graph LR
    Input[Input] --> Agent[Agent pipeline]
    Agent --> Eval[Evals]
    Eval --> Output[Output]
```

Browser mic -> WebSocket -> OpenAI Realtime API -> audio out + tool calls -> browser speaker.

## Stack

- Python
- FastAPI
- websockets
- openai
- React
- Vite

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

- `latency_p95`
- `interruption_handling_rate`
- `tool_call_success_rate`

The `make eval` command runs the full eval suite and prints a report. Evals must pass before merging to main.

## Project structure

```
06-realtime-voice-assistant/
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
- OpenAI Realtime API, VAD, interruption handling
- Production concerns: cost, latency, failure modes, security
- Evals: golden dataset + automated runner
- Tests: at least unit + integration
- Deployment: Dockerized, one-command deploy

## Next steps

See `DEPLOYMENT.md` for deployment instructions and `evals/README.md` for the eval methodology.

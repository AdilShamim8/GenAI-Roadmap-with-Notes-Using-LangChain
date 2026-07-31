# Contributing

Thank you for considering a contribution. This repo enforces a strict quality bar so that readers can trust every word.

## The non-negotiables

1. **No fabricated facts.** Every model name, version number, API behavior, and pricing claim must appear in [`LAST_VERIFIED.md`](./LAST_VERIFIED.md) with a source URL and verification date.
2. **No link dumps.** Every external resource needs a one-line review explaining *why* it's worth the reader's time.
3. **No single-author walls of text.** Use the topic file template below.
4. **No LangChain-only tunnel vision.** If a topic has 3+ viable tools, cover at least the top 3 with a comparison table.
5. **No README bloat.** The README stays under 150 lines. Add new content as new files, not new README sections.

## Topic file template

Every file under `foundations/`, `llm-calling/`, `context-engineering/`, `rag/`, `tools-and-mcp/`, `agents/`, `multi-agent/`, `evals/`, `production/`, `fine-tuning-and-self-hosting/`, `safety/`, `realtime-voice/`, and `field-guide/` must follow this template:

```markdown
# [Topic Name]

> **Level:** [BEG | INT | ADV | EXP] · **Last verified:** YYYY-MM-DD · **Sources:** [1–3 primary links]

## Why this matters
3–5 sentences. Tie to a concrete production pain point.

## Core concepts
The mental model. Include a Mermaid diagram if applicable.

## Code: minimal working example
Runnable, copy-pastable, ≤30 lines.

## Production concerns
- Latency:
- Cost:
- Failure modes:
- Security:

## Anti-patterns
- ❌ [pattern] — [why it breaks]

## Decision framework
When to use this vs alternatives.

## References
- [Title](url) — verified YYYY-MM-DD
```

## Project file template

Every folder under `projects/` must contain:

- `README.md` — what it does, how to run it, architecture diagram, evals summary.
- `pyproject.toml` — pinned dependencies.
- `src/` — runnable code.
- `tests/` — at least one unit test and one integration test.
- `evals/` — golden dataset + eval runner. The eval runner must be invokable via `make eval`.
- `DEPLOYMENT.md` — how to deploy (Docker, serverless, etc.).

## Pull request checklist

- [ ] Every factual claim is in `LAST_VERIFIED.md` with a source.
- [ ] The file follows the topic or project template.
- [ ] Code snippets are runnable (CI runs notebooks via `nbmake`).
- [ ] `markdownlint-cli2` passes.
- [ ] `vale` prose linting passes.
- [ ] No broken links (CI runs `lychee`).
- [ ] If adding a new topic, the README table of rungs is updated.

## How to add a new topic

1. Open an issue titled "Propose topic: [name]" with a 2-sentence rationale.
2. A maintainer will assign it to a rung (or propose a new rung).
3. Create the file using the topic template.
4. Open a PR.

## How to report a stale or incorrect claim

Open an issue using the **Content correction** template. Include:
- The claim (quote it).
- The file and line.
- The source contradicting it.

We treat incorrect claims as P0 bugs.

## How to report a broken link

Open an issue using the **Broken link** template. CI also auto-files these weekly.

## Style

- American English.
- Sentence case for headings.
- No emoji in body text. Emoji only in tables to signal status (🟢 / 🟡 / 🔴).
- Code blocks always specify a language.
- Mermaid diagrams for any architecture with 3+ components.

## Code of conduct

See [`CODE_OF_CONDUCT.md`](./CODE_OF_CONDUCT.md). Be excellent to each other.

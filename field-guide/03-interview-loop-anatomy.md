# Interview Loop Anatomy

> **Last verified:** 2026-07-30

## The typical 2026 loop

Most AI engineer loops have 5–7 stages:

1. **Recruiter screen** (30 min) — basics, comp expectations.
2. **Hiring manager call** (45 min) — your background, the role, mutual fit.
3. **Take-home or live coding** (2–6 hours) — usually LLM-flavored.
4. **System design** (60 min) — "design a RAG system for X" or "design an agent for Y."
5. **Project deep-dive** (45 min) — present a past project; probing questions.
6. **Behavioral** (45 min) — conflict, ambiguity, leadership.
7. **Final / exec** (30 min) — culture, vision, comp.

Some companies collapse stages; some add a fifth technical round. Total time: 4–8 weeks.

## What each stage actually tests

| Stage | What they're looking for | Common failure mode |
|-------|--------------------------|---------------------|
| Recruiter screen | Communication, comp alignment | Being unclear about comp |
| HM call | Have you built real things? | Speaking in abstractions |
| Take-home | Can you ship something that works? | Over-engineering; no evals |
| System design | Can you reason about trade-offs? | Picking a framework without justifying |
| Project deep-dive | Did you actually do the work? | Can't answer "why this choice?" |
| Behavioral | Will you be hard to work with? | Blaming teammates |
| Exec | Long-term fit | Treating it as a formality |

## The take-home

Common patterns in 2026:

- "Build a RAG system over this corpus and answer these 10 questions."
- "Build an agent that uses these 3 tools to accomplish X."
- "Improve this prompt's evals." (less common; higher-signal)

Time-boxed variants are increasingly common (4 hours, your choice of tools).

**Red flags in the take-home:**
- Building UI when none was asked.
- Using 5 frameworks when 1 would do.
- No evals. (This is the #1 rejection reason.)
- No tests.
- README that explains nothing.

## The system design round

Typical prompts:

- "Design a customer support agent for an e-commerce company."
- "Design a RAG system that handles 10K queries/day over a 1M-doc corpus."
- "Design a multi-agent system for code review."

What they're testing:
- Can you state assumptions?
- Can you pick a model and justify?
- Can you reason about cost, latency, failure modes?
- Can you describe the evals and observability?
- Can you talk about safety?

**What they're NOT testing:** whether you know a specific framework's syntax.

## References

- [Alexey Grigorev: Interview process](https://github.com/alexeygrigorev/ai-engineering-field-guide/blob/main/interview/01-interview-process.md) — verified 2026-07-30
- [Alexey Grigorev: Interview questions](https://github.com/alexeygrigorev/ai-engineering-field-guide/blob/main/interview/02-questions.md) — verified 2026-07-30

# LLM-as-Judge

> **Level:** INT → ADV · **Last verified:** 2026-07-30

## Why this matters

For most production GenAI outputs, exact match is impossible. LLM-as-judge — using a strong model to grade outputs against a rubric — is the dominant solution. But it has well-documented failure modes. Use it knowing the failure modes.

## Core concepts

### The rubric

The judge needs a specific rubric. "Is this a good answer?" → garbage. "Does the answer cite a source from the context? Is the citation correct? Is the tone professional?" → signal.

### The judge model

- Use a **stronger** model than the one being judged.
- Or use the same model with a different prompt (works surprisingly well).
- Avoid mixing judge model and judged model from the same vendor if possible (clique bias).

### Known biases

- **Position bias** — judge prefers the first option in pairwise.
- **Length bias** — judge prefers longer answers.
- **Self-preference** — judge prefers outputs from its own family.
- **Formatting bias** — judge prefers well-formatted answers regardless of content.

### Mitigations

- Randomize position in pairwise comparisons.
- Normalize for length.
- Use multiple judges; ensemble.
- Periodically audit judge vs human labels.

## Code: rubric-based judge

```python
from openai import OpenAI
client = OpenAI()

def judge(query: str, answer: str, context: str) -> dict:
    rubric = '''You are grading an answer to a question.
    Score each criterion 1 (worst) to 5 (best).
    Return JSON: {"grounded": int, "complete": int, "concise": int, "tone": int, "reason": str}.

    Criteria:
    - grounded: every claim is supported by the context.
    - complete: answers the full question.
    - concise: no unnecessary detail.
    - tone: professional and helpful.
    '''
    resp = client.beta.chat.completions.parse(
        model="gpt-5",
        messages=[
            {"role": "system", "content": rubric},
            {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {query}\n\nAnswer: {answer}"},
        ],
        response_format=JudgeOutput,
    )
    return resp.choices[0].message.parsed.dict()
```

## Code: pairwise comparison (with position randomization)

```python
import random

def pairwise(query: str, answer_a: str, answer_b: str) -> str:
    if random.random() < 0.5:
        answer_a, answer_b = answer_b, answer_a  # randomize position
        flipped = True
    else:
        flipped = False
    prompt = f"Question: {query}\n\nAnswer A: {answer_a}\n\nAnswer B: {answer_b}\n\nWhich is better? Reply 'A' or 'B'."
    choice = client.chat.completions.create(model="gpt-5", messages=[{"role": "user", "content": prompt}]).choices[0].message.content.strip()
    if flipped:
        choice = "B" if choice == "A" else "A"
    return choice
```

## Production concerns

- **Latency:** Judge calls double eval time.
- **Cost:** 200 examples × 2 judge calls × $0.02 = $8/run.
- **Failure modes:** Judges can be biased; audit with human labels periodically.
- **Security:** Judge prompts contain your outputs; treat as production data.

## Anti-patterns

- ❌ **Vague rubrics.** "Is it good?" → garbage signal.
- ❌ **Same-model judging without mitigations.** Self-preference bias.
- ❌ **No human audit.** Drift goes undetected.

## References

- [Anthropic: LLM-as-judge](https://docs.anthropic.com/en/docs/build-with-claude/llm-judging) — verified 2026-07-30
- [Judging LLM-as-a-Judge (positional bias)](https://arxiv.org/abs/2306.05685) — verified 2026-07-30
- [Chatbot Arena: pairwise eval](https://chat.lmsys.org/) — verified 2026-07-30

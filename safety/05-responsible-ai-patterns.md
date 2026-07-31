# Responsible AI Patterns

> **Level:** INT · **Last verified:** 2026-07-30

## Why this matters

Responsible AI is no longer optional. EU AI Act enforcement started in 2026; sectoral regulations (HIPAA, GDPR, FCRA) apply to AI outputs; customer contracts increasingly require AI governance. The good news: the same patterns that satisfy regulators also produce better, safer products.

## Core concepts

### The seven patterns

| Pattern | What | Why |
|---------|------|-----|
| **Human-in-the-loop** | Human approves high-stakes actions | Catches agent errors |
| **Audit logging** | Every input, output, decision logged | Forensics; compliance |
| **Explainability** | Cite sources; show reasoning trace | User trust; debugging |
| **Feedback channel** | User can flag bad output | Continuous improvement |
| **Opt-out / override** | User can disable AI features | Consent; trust |
| **Bias testing** | Eval across subgroups | Fairness; compliance |
| **Periodic audit** | Quarterly review of model + prompts + evals | Drift detection |

### The audit log

Every production agent should log:

```json
{
  "timestamp": "2026-07-30T12:34:56Z",
  "user_id": "u_abc",
  "session_id": "s_xyz",
  "model": "gpt-5-2026-04-15",
  "prompt_template_id": "billing_agent_v3",
  "input_tokens": 1240,
  "output_tokens": 80,
  "tool_calls": [{"name": "issue_refund", "args": {"order_id": "123"}, "result": "success"}],
  "output": "I've issued refund r_456 for order 123.",
  "feedback": null,
  "eval_scores": {"faithfulness": 0.95, "helpfulness": 4}
}
```

This is your forensic record. If a user complains, you can reconstruct exactly what happened.

## Code: structured audit logging

```python
import json, time, logging
logger = logging.getLogger("agent_audit")

def audit_log(user_id: str, session_id: str, model: str, prompt_id: str,
              input_text: str, output_text: str, tool_calls: list, tokens: dict):
    record = {
        "timestamp": time.time(),
        "user_id": user_id,
        "session_id": session_id,
        "model": model,
        "prompt_template_id": prompt_id,
        "input_tokens": tokens.get("input"),
        "output_tokens": tokens.get("output"),
        "tool_calls": tool_calls,
        "output": output_text,
        # Don't log full input_text — PII. Log hash instead.
        "input_hash": hash(input_text),
    }
    logger.info(json.dumps(record))
```

## Code: feedback capture

```python
def response_endpoint(response_id: str, response_text: str):
    return {
        "response_id": response_id,
        "response_text": response_text,
        "feedback_html": f'''
        <div class="feedback">
          <button onclick="submitFeedback('{response_id}', 'good')">+1</button>
          <button onclick="submitFeedback('{response_id}', 'bad')">-1</button>
          <textarea id="feedback_text" placeholder="What went wrong?"></textarea>
        </div>
        ''',
    }
```

## Production concerns

- **Latency:** Audit logging adds <1ms.
- **Cost:** Log storage is cheap. Don't skimp.
- **Failure modes:** Logs without `prompt_template_id` are useless for forensics.
- **Security:** Logs contain user data. Encrypt at rest; restrict access.

## Anti-patterns

- ❌ **No audit logging.** You can't investigate incidents.
- ❌ **Logging PII in plaintext.** Encrypt or hash.
- ❌ **No feedback channel.** You're blind to user-reported issues.

## References

- [EU AI Act](https://artificialintelligenceact.eu/) — verified 2026-07-30
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) — verified 2026-07-30
- [Anthropic: Responsible AI](https://www.anthropic.com/news) — verified 2026-07-30

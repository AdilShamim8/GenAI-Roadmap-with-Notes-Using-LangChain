# System Prompt Design

> **Level:** INT · **Last verified:** 2026-07-30

## Why this matters

The system prompt is the single highest-leverage piece of context you control. It's cached, it's prepended to every call, and it sets the operating envelope for the model. Yet most system prompts are bloated, contradictory, and untested.

## Core concepts

### The four-part system prompt

A production system prompt should have, in order:

1. **Role** — one sentence. "You are a customer-support agent for Acme Corp."
2. **Policies** — what you must and must not do. Bullet list, ≤10 items.
3. **Tone & format** — voice, length, structure.
4. **Tools available** — names, when to use each.

### Why this order

Models attend most strongly to the **start** and **end** of a context. Role → policies → tone → tools puts the most important (policies) near the start and the most-referenced (tools) near the end.

### Cache-friendly structure

Put the most stable content first (role, policies, tone). Put the most volatile content last (current user, current tool outputs). This maximizes prompt-cache hit rate.

## Code: a template

```python
SYSTEM_PROMPT = '''You are a tier-1 customer-support agent for Acme Corp, a SaaS analytics company.

# Policies
- Never make commitments about refunds exceeding $500; escalate to tier-2.
- Always cite the help-center article you used.
- If the user mentions a security incident, immediately route to the security team via the `escalate_security` tool.
- Do not discuss competitors by name.
- If you don't know, say so. Never fabricate feature names.

# Tone & format
- Friendly, concise, professional.
- Maximum 3 sentences per response unless the user asks for detail.
- Use bullet lists for steps.

# Tools
- `search_help_center(query)`: search Acme's help center.
- `lookup_account(email)`: fetch account details.
- `escalate_security(reason)`: route to security team.
- `escalate_tier2(reason)`: route to tier-2 support.
'''
```

## Production concerns

- **Latency:** A 2K-token system prompt cached costs 10% of uncached.
- **Cost:** Cache it.
- **Failure modes:** Conflicting policies ("be concise" + "explain in detail") produce inconsistent behavior.
- **Security:** System prompts are visible in traces. Don't put secrets in them.

## Anti-patterns

- ❌ **300-line system prompts.** Model attends poorly past ~2K tokens of static instructions.
- ❌ **Prescriptive output formats in the system prompt.** Use structured outputs instead.
- ❌ **Putting examples in the system prompt.** Use a separate `examples` section or few-shot in user turns.

## References

- [Anthropic prompt engineering — system prompts](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/system-prompts) — verified 2026-07-30
- [OpenAI prompt engineering guide](https://platform.openai.com/docs/guides/prompt-engineering) — verified 2026-07-30

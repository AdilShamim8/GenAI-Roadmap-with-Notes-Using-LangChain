# Tokenization Economics

> **Level:** BEG · **Last verified:** 2026-07-30 · **Sources:** [OpenAI Tokenizer](https://platform.openai.com/tokenizer), [HuggingFace tokenizers](https://huggingface.co/docs/tokenizers/)

## Why this matters

You are billed per token. You are rate-limited per token. Your context window is measured in tokens. Yet most engineers treat tokens as a black box. Understanding tokenization is the single fastest way to cut your API bill by 30–50%.

## Core concepts

### What is a token?

A token is a sub-word unit. "tokenization" is one word in English but ~3 tokens: `token` + `ization`. The rules are learned by a tokenizer (usually BPE — Byte-Pair Encoding) and differ per model family.

### Token counts are not character counts

| Text | Characters | GPT-style tokens | Claude-style tokens |
|------|------------|------------------|---------------------|
| `Hello, world!` | 13 | 4 | 4 |
| `オープンソース` (5 chars) | 5 | ~7 | ~6 |
| `def fibonacci(n):` | 16 | 6 | 6 |
| A 1000-word English essay | ~6000 | ~1300 | ~1300 |

### The economics

If a model costs $5/1M input tokens:
- 1M English tokens ≈ 750K words ≈ a 3000-page book.
- 1K requests/day averaging 4K input tokens = $20/day = $600/month.
- Cut input by 30% via better chunking = $180/month saved.

## Code: count tokens correctly

```python
import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")  # works for GPT-5 family
text = "Tokenization matters more than you think."
print(len(enc.encode(text)))  # ~7

# Per-message overhead in chat APIs
def chat_tokens(messages):
    base = 3  # every message has ~3 tokens of overhead
    total = 0
    for m in messages:
        total += base
        for k, v in m.items():
            total += len(enc.encode(v))
    return total
```

## Production concerns

- **Latency:** More tokens = slower prefill = slower first-token latency.
- **Cost:** Tokens you can prune are tokens you don't pay for.
- **Failure modes:** Whitespace, code indentation, and non-ASCII bloat token counts invisibly.
- **Security:** Prompt-injection payloads often exploit tokenization quirks (e.g., homoglyphs, zero-width chars).

## Anti-patterns

- ❌ **Estimating tokens as `len(text) / 4`** — works on English prose, breaks on code, JSON, or non-Latin scripts.
- ❌ **Caching by string instead of by token-hash** — same text, different tokenizers, false cache hits.
- ❌ **Truncating by characters** — slices tokens mid-way, producing garbage.

## Decision framework

| Need | Use |
|------|-----|
| Count tokens before sending | `tiktoken` (OpenAI) or `anthropic.count_tokens` |
| Minimize tokens in stored prompts | Compress, dedupe, summarize |
| Tokenize non-English well | Prefer Gemini or Claude tokenizers; GPT's BPE is English-leaning |
| Tokenize code | Use a model with a code-aware tokenizer (most modern ones) |

## References

- [OpenAI Tokenizer](https://platform.openai.com/tokenizer) — verified 2026-07-30
- [tiktoken](https://github.com/openai/tiktoken) — verified 2026-07-30
- [Anthropic: Counting tokens](https://docs.anthropic.com/en/api/messages-count-tokens) — verified 2026-07-30

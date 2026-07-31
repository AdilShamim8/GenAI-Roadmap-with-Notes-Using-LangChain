# KV-Cache and Inference Economics

> **Level:** INT · **Last verified:** 2026-07-30 · **Sources:** [vLLM PagedAttention paper](https://arxiv.org/abs/2309.06180), [FlashAttention-2](https://arxiv.org/abs/2307.08691)

## Why this matters

The KV-cache is the single biggest determinant of inference cost at scale. Understanding it unlocks why vLLM is faster than naive HuggingFace, why prompt caching saves money, and why your 128K-context request is OOMing the GPU.

## Core concepts

### What is the KV-cache?

For every token in the prompt, the model computes Key and Value tensors that downstream tokens attend to. Instead of recomputing these on every decode step, we cache them. The cache grows linearly with sequence length × layers × heads × head_dim.

### The size math

For a 70B model with 80 layers, 64 heads, 128 head_dim, in fp16:
- Per-token KV-cache: 80 × 64 × 128 × 2 (K+V) × 2 bytes = ~2.6 MB
- 32K context: ~83 GB of cache alone — exceeds an 80GB H100.

This is why serving long contexts is hard.

### Why vLLM is fast

vLLM's **PagedAttention** treats the KV-cache like virtual memory — pages, not contiguous blocks. This eliminates fragmentation and lets you batch 3–5× more requests per GPU.

## Code: see the cache in action

```python
# Naive generation — cache is internal but you can see its effect
from transformers import AutoModelForCausalLM, AutoTokenizer
import time

model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-3.2-1B", device_map="auto")
tok = AutoTokenizer.from_pretrained("meta-llama/Llama-3.2-1B")

prompt = "Explain attention. " * 200  # ~1K tokens

# With KV-cache (default)
t = time.time()
out = model.generate(tok(prompt, return_tensors="pt").to("cuda").input_ids, max_new_tokens=100)
print(f"With cache: {time.time()-t:.2f}s")

# Without KV-cache (use_cache=False) — much slower
t = time.time()
out = model.generate(tok(prompt, return_tensors="pt").to("cuda").input_ids, max_new_tokens=100, use_cache=False)
print(f"Without cache: {time.time()-t:.2f}s")
```

## Production concerns

- **Memory:** KV-cache is often the binding constraint, not weights.
- **Batching:** Continuous batching (vLLM, TGI) > static batching for variable-length requests.
- **Prompt caching:** Anthropic and OpenAI both support caching prompts you reuse — saves 50–90% on cache hits.
- **Failure modes:** Long-context requests can OOM mid-decode and silently retry.

## Anti-patterns

- ❌ **Re-sending the same system prompt every request without prompt caching.** 5–10× cost penalty.
- ❌ **Using HuggingFace `generate` in production.** Use vLLM, SGLang, or TGI.
- ❌ **Assuming batch size = parallelism.** Continuous batching decouples them.

## Decision framework

| Need | Use |
|------|-----|
| Self-serve, high throughput | vLLM with PagedAttention |
| Structured outputs at speed | SGLang (RadixAttention reuses KV across similar prefixes) |
| Multi-model on one GPU | TGI or vLLM with LoRA adapters |
| API, no infra | OpenAI/Anthropic with prompt caching enabled |

## References

- [Efficient Memory Management for LLMs (PagedAttention)](https://arxiv.org/abs/2309.06180) — verified 2026-07-30
- [FlashAttention-2](https://arxiv.org/abs/2307.08691) — verified 2026-07-30
- [vLLM docs](https://docs.vllm.ai/) — verified 2026-07-30

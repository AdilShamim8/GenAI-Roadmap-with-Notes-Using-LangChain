# vLLM, SGLang, TGI

> **Level:** ADV · **Last verified:** 2026-07-30

## Why this matters

If you're self-hosting, the serving framework determines your throughput, latency, and cost. The three serious options in 2026 are vLLM, SGLang, and TGI. Pick wrong and you'll pay 2–5× more for the same throughput.

## The comparison

| Dimension | vLLM | SGLang | TGI |
|-----------|------|--------|-----|
| **Throughput** | Industry-leading | Comparable; better for similar-prefix workloads | Good |
| **KV-cache** | PagedAttention | PagedAttention + RadixAttention (prefix sharing) | Paged attention |
| **Multi-LoRA** | Yes | Yes | Yes |
| **Structured output** | Via outlines | Native (very fast) | Limited |
| **Multimodal** | Yes | Yes | Yes |
| **Maturity** | Very high | High | Very high |
| **Best for** | General high-throughput | Code completion, chatbots with shared prefixes | Enterprise HuggingFace stack |

## Code: vLLM serving

```bash
# Start a server
pip install vllm
vllm serve meta-llama/Llama-3.1-8B-Instruct \
    --port 8000 \
    --tensor-parallel-size 1 \
    --max-model-len 8192 \
    --enable-prefix-caching
```

```python
# Client (OpenAI-compatible)
from openai import OpenAI
client = OpenAI(base_url="http://localhost:8000/v1", api_key="dummy")

resp = client.chat.completions.create(
    model="meta-llama/Llama-3.1-8B-Instruct",
    messages=[{"role": "user", "content": "Hello"}],
)
```

## Code: SGLang with structured output

```python
# pip install sglang
import sglang as sgl

@sgl.function
def classify(s, text):
    s += "Classify the sentiment of this review as 'positive', 'neutral', or 'negative':\n"
    s += text + "\n"
    s += "Sentiment:" + sgl.gen("sentiment", regex=r"(positive|neutral|negative)")

state = classify.run(text="This product is amazing!")
print(state["sentiment"])
```

SGLang's regex-constrained decoding is the fastest way to serve structured outputs from open-weight models.

## Production concerns

- **Latency:** vLLM and SGLang are within 10% of each other on most workloads.
- **Cost:** Self-hosted cost = GPU hours. Utilize >50% or stick with API.
- **Failure modes:** Cold start is slow (model load = minutes). Keep warm.
- **Security:** Self-hosted models have no content filtering. Add your own.

## Anti-patterns

- ❌ **HuggingFace `generate()` in production.** Use vLLM/SGLang/TGI.
- ❌ **One model per GPU.** Multi-LoRA lets you serve N fine-tunes on one GPU.
- ❌ **No prefix caching.** 2–5× cost penalty for chat workloads.

## References

- [vLLM](https://docs.vllm.ai/) — verified 2026-07-30
- [SGLang](https://github.com/sgl-project/sglang) — verified 2026-07-30
- [HuggingFace TGI](https://github.com/huggingface/text-generation-inference) — verified 2026-07-30

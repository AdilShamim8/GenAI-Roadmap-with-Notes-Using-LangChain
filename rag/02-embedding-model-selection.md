# Embedding Model Selection

> **Level:** INT · **Last verified:** 2026-07-30 · **Sources:** [MTEB leaderboard](https://huggingface.co/spaces/mteb/leaderboard)

## Why this matters

Your embedding model is the lens through which retrieval sees your corpus. A weak embedding model caps RAG quality no matter how good your chunker, re-ranker, or LLM is.

## Core concepts

### The 2026 landscape

| Model | Dim | Open-weight? | Strengths | Notes |
|-------|-----|--------------|-----------|-------|
| OpenAI `text-embedding-3-large` | 3072 | No | Strong baseline, multi-modal-ish | API only |
| Cohere `embed-v4` | 1536 | No | Multilingual, multi-modal | API only |
| Voyage AI `voyage-3-large` | 1024 | No | Top of MTEB for English | API only |
| BGE-M3 | 1024 | Yes | Multi-lingual, multi-function (dense+sparse+colbert) | Self-host |
| gte-Qwen2 | 1536 | Yes | Strong open-weight | Self-host |
| Nomic Embed v1.5 | 768 | Yes | Open data, reproducible | Self-host |
| Jina v3 | 1024 | Yes | Long-context (8K) | Self-host |

### Selection criteria

1. **Language coverage** — English-only models underperform on non-English.
2. **Modality** — text-only vs text+image.
3. **Dimension** — higher dim = better recall, more storage.
4. **Matryoshka support** — can you truncate dim for cost? (Yes for OpenAI v3, Nomic.)
5. **Max input length** — short models (512 tokens) force pre-truncation.

## Code: OpenAI

```python
from openai import OpenAI
client = OpenAI()

resp = client.embeddings.create(
    model="text-embedding-3-large",
    input=["text one", "text two"],
    dimensions=1536,  # matryoshka truncation
)
v1 = resp.data[0].embedding
```

## Code: self-hosted BGE-M3

```python
from FlagEmbedding import BGEM3FlagModel
model = BGEM3FlagModel("BAAI/bge-m3", use_fp16=True)

embeddings = model.encode(
    ["text one", "text two"],
    batch_size=12,
    max_length=8192,
    return_dense=True,
    return_sparse=True,
    return_colbert_vecs=False,
)
```

## Production concerns

- **Latency:** Self-hosted embeddings add 5–20ms per call on a GPU.
- **Cost:** OpenAI v3-large is ~$0.13/1M tokens. Self-hosted is essentially free at scale.
- **Failure modes:** Switching embedding models requires re-indexing everything. Pick carefully.
- **Security:** Embeddings can leak training data via inversion attacks. Don't expose raw embeddings of sensitive text.

## Anti-patterns

- ❌ **Using `ada-002` in 2026.** Superseded.
- ❌ **Mixing embedding models.** A query embedded with model A cannot match docs embedded with model B.
- ❌ **Defaulting to the highest-dim model.** Dim 3072 costs 4× storage vs 768, often with marginal recall gain.

## References

- [MTEB leaderboard](https://huggingface.co/spaces/mteb/leaderboard) — verified 2026-07-30
- [OpenAI embeddings guide](https://platform.openai.com/docs/guides/embeddings) — verified 2026-07-30
- [BGE-M3](https://huggingface.co/BAAI/bge-m3) — verified 2026-07-30

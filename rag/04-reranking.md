# Re-Ranking for Precision

> **Level:** INT · **Last verified:** 2026-07-30

## Why this matters

Vector search returns top-K candidates ranked by embedding similarity — fast but coarse. Re-ranking re-scores those K candidates with a more expensive model, giving you top-N with much higher precision. RAG answer quality is often more sensitive to re-ranker quality than to LLM choice.

## Core concepts

### Two-stage retrieval

1. **Retrieve** — fast, recall-oriented. Get top-50 from vector + BM25.
2. **Re-rank** — slow, precision-oriented. Score each of the 50 with a cross-encoder, keep top-5.

### Why cross-encoders beat bi-encoders

Bi-encoders (your embedding model) encode query and doc separately; similarity is cosine. Fast but loses query-doc interaction. Cross-encoders encode `(query, doc)` jointly; the attention can model fine-grained relevance. Slower, but much more accurate.

### Re-ranker options (2026)

| Model | Type | Open-weight? | Latency (per pair) |
|-------|------|--------------|---------------------|
| Cohere Rerank v3.5 | API | No | ~50ms |
| Voyage rerank-2 | API | No | ~50ms |
| BGE-reranker-v2-m3 | Open | Yes | ~20ms on GPU |
| Jina reranker v2 | Open | Yes | ~25ms on GPU |
| LLM-as-reranker (GPT-5 mini) | API | No | ~200ms per pair (use batch) |

## Code: BGE reranker (self-hosted)

```python
from FlagEmbedding import FlagReranker
reranker = FlagReranker("BAAI/bge-reranker-v2-m3", use_fp16=True)

pairs = [(query, doc) for doc in candidate_docs]
scores = reranker.compute_score(pairs, normalize=True)
ranked = sorted(zip(candidate_docs, scores), key=lambda x: -x[1])[:5]
```

## Code: Cohere rerank (API)

```python
import cohere
co = cohere.Client()

results = co.rerank(
    model="rerank-v3.5",
    query=query,
    documents=candidate_docs,
    top_n=5,
)
top_docs = [candidate_docs[r.index] for r in results.results]
```

## Production concerns

- **Latency:** Re-ranking 50 candidates adds 200–500ms. Parallelize where possible.
- **Cost:** Cohere rerank is ~$2/1K searches. Self-hosted is free at scale.
- **Failure modes:** Re-rankers can be biased toward longer documents. Normalize by length when scoring.
- **Security:** Re-rankers see query + doc together — ensure no PII cross-contamination in shared deployments.

## Anti-patterns

- ❌ **Skipping re-ranking for production RAG.** Top-K from vector search alone is rarely good enough.
- ❌ **Re-ranking the entire corpus.** Only re-rank the top-K candidates from retrieval.
- ❌ **Treating re-ranker scores as probabilities.** They're relative rankings, not calibrated.

## References

- [Cohere rerank](https://docs.cohere.com/docs/reranking) — verified 2026-07-30
- [BGE reranker](https://huggingface.co/BAAI/bge-reranker-v2-m3) — verified 2026-07-30
- [Voyage rerank](https://docs.voyageai.com/docs/reranking) — verified 2026-07-30

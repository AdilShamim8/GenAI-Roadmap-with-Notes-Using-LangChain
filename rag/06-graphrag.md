# GraphRAG

> **Level:** ADV · **Last verified:** 2026-07-30 · **Sources:** [Microsoft GraphRAG](https://microsoft.github.io/graphrag/)

## Why this matters

Vector RAG retrieves similar chunks. It cannot answer "What are the main themes in this corpus?" or "How do these entities relate?" — those need structure, not similarity. GraphRAG extracts an entity-relationship graph from your corpus and uses it for retrieval.

## Core concepts

### The pipeline

1. **Chunk** the corpus as usual.
2. **Extract entities and relationships** from each chunk with an LLM ("Alice works at Acme; Acme is in the analytics industry").
3. **Cluster entities** into communities (Leiden algorithm).
4. **Summarize each community** with an LLM.
5. **At query time:** either (a) map the query to entities and traverse, or (b) find the relevant community summaries.

### When GraphRAG wins

- Whole-corpus questions ("What are the main themes?").
- Multi-entity relationship questions.
- Questions where the answer is spread across many non-adjacent chunks.

### When GraphRAG loses

- Single-fact lookup.
- Cost-sensitive workloads (indexing is 10–100× more expensive than vector RAG).
- Small corpuses (<1K chunks).

## Code: minimal GraphRAG with Microsoft's lib

```python
# pip install graphrag
from graphrag.index import run_pipeline
from graphrag.query import structured_search

# 1. Index (one-time, expensive)
run_pipeline(config="settings.yaml")  # extracts entities, builds communities

# 2. Query
from graphrag.query.structured_search import GlobalSearch
search = GlobalSearch(...)  # uses community summaries
result = search.search("What are the main themes in this corpus?")
```

## Production concerns

- **Latency:** Indexing a 1M-token corpus takes 1–4 hours and $50–$200 of LLM calls.
- **Cost:** Don't run GraphRAG on corpuses that don't need it. Vector RAG is 10–100× cheaper.
- **Failure modes:** Entity extraction is noisy. Bad entities = bad graph.
- **Security:** The graph can reveal relationships that individual chunks don't. Audit access controls.

## Anti-patterns

- ❌ **GraphRAG for everything.** It's a scalpel, not a hammer.
- ❌ **Re-indexing on every update.** Use incremental indexing.
- ❌ **Skipping community summaries.** They're what makes global queries work.

## References

- [Microsoft GraphRAG](https://microsoft.github.io/graphrag/) — verified 2026-07-30
- [GraphRAG paper](https://arxiv.org/abs/2404.16130) — verified 2026-07-30

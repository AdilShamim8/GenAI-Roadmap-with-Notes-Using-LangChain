# RAG vs Long Context

> **Last verified:** 2026-07-30

## The question

Models now support 1M+ token context windows. Is RAG still necessary?

## The short answer

**Yes.** Long context does not replace RAG. It changes the economics of when RAG pays off.

## The tradeoff matrix

| Dimension | Long context | RAG |
|-----------|--------------|-----|
| Latency | Linear with input tokens | Constant + small retrieval |
| Cost | Linear with input tokens | Embedding cost (small) + retrieved-chunk tokens |
| Recall | Excellent if it fits | Depends on retrieval quality |
| Freshness | Re-send every time | Update index once |
| Multi-doc dedup | Manual | Index handles it |
| Citeable sources | Hard | Native |
| Setup cost | Zero | Moderate |

## When long context wins

- Single document, fits in context.
- One-shot analysis (summarize this 200-page PDF).
- Ad-hoc exploration.

## When RAG wins

- Corpus >100K tokens.
- Multiple users querying the same data (cache the index).
- You need source citations.
- You need freshness without re-sending everything.
- You want sub-second latency.

## The hybrid: Long-context RAG

In 2026, the best pattern is often:
1. Use RAG to retrieve top-K (e.g., 20) chunks.
2. Re-rank to top-N (e.g., 5).
3. Stuff into a long-context model with a generous window.
4. Let the model do cross-chunk reasoning.

## References

- [Anthropic: contextual retrieval](https://www.anthropic.com/news/contextual-retrieval) — verified 2026-07-30
- [Lost in the Middle paper](https://arxiv.org/abs/2307.03172) — verified 2026-07-30

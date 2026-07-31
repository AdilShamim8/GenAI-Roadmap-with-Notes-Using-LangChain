# Chunking Strategies

> **Level:** BEG → INT · **Last verified:** 2026-07-30

## Why this matters

Chunking is the highest-leverage RAG decision. Bad chunking = bad retrieval = bad answers, no matter how good your model. Most RAG problems trace back to chunks that are too big, too small, or split semantically.

## Core concepts

### The four strategies

| Strategy | How | Best for |
|----------|-----|----------|
| **Fixed-size** | Every N chars with overlap | Quick prototype, uniform docs |
| **Recursive character** | Split on `\n\n`, then `\n`, then `. ` (LangChain default) | Heterogeneous text |
| **Document-aware** | Split on Markdown headings, HTML tags, code blocks | Structured docs |
| **Semantic** | Embed sentences, cluster by similarity | Long-form narrative |
| **Late chunking** | Embed full doc, then chunk the embeddings | Preserves cross-chunk context |

### The size tradeoff

- **Smaller chunks (256–512 tokens)** → better retrieval precision, worse context for the model.
- **Larger chunks (1024–2048)** → better context, worse retrieval precision (chunk about multiple topics).
- **Sweet spot for most docs: ~512 tokens with 10–20% overlap.**

### Contextual chunking (Anthropic, 2024)

Add a 1-sentence context prefix to each chunk before embedding. E.g., "This chunk is from the 'Pricing' section of the Acme API docs." Improves retrieval recall 30–50% in benchmarks.

## Code: recursive character splitter

```python
from langchain_text_splitters import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size=512,
    chunk_overlap=64,
    separators=["\n\n", "\n", ". ", " ", ""],
)
chunks = splitter.split_text(long_text)
```

## Code: contextual chunking

```python
from openai import OpenAI
client = OpenAI()

def add_context(chunks: list[str], doc_title: str) -> list[str]:
    contextualized = []
    for i, chunk in enumerate(chunks):
        ctx = client.chat.completions.create(
            model="gpt-5-mini",
            messages=[
                {"role": "system", "content": f"You are indexing a document titled '{doc_title}'. For the chunk below, output a 1-sentence context prefix describing where it sits in the document. Output ONLY the prefix."},
                {"role": "user", "content": chunk},
            ],
        ).choices[0].message.content
        contextualized.append(f"{ctx}\n\n{chunk}")
    return contextualized
```

## Production concerns

- **Latency:** Contextual chunking adds 1 LLM call per chunk at index time (not query time).
- **Cost:** Worth it for corpuses queried 1000s of times.
- **Failure modes:** Naive char-splitting breaks code blocks, tables, and lists mid-way.
- **Security:** Chunk boundaries can split sensitive data — re-mirror PII detection across boundaries.

## Anti-patterns

- ❌ **Fixed 1000-char chunks with no overlap.** Splits sentences and paragraphs awkwardly.
- ❌ **One chunk per document.** Loses retrieval precision.
- ❌ **Chunking by tokens without testing recall.** Always measure.

## References

- [Anthropic: Contextual retrieval](https://www.anthropic.com/news/contextual-retrieval) — verified 2026-07-30
- [LangChain text splitters](https://python.langchain.com/docs/how_to/#text-splitters) — verified 2026-07-30
- [Late chunking — Jina AI](https://jina.ai/news/late-chunking-in-long-context-embedding-models/) — verified 2026-07-30

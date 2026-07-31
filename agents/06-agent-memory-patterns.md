# Agent Memory Patterns

> **Level:** ADV · **Last verified:** 2026-07-30

## Why this matters

An agent without memory repeats itself, forgets decisions, and can't learn from its own history. Memory is what turns a stateless call into a persistent, improving assistant. But memory done wrong is a privacy and cost nightmare.

## Core concepts

### Three types of memory

| Type | What | Example | Storage |
|------|------|---------|---------|
| **Working** | Current turn + recent turns | Last 5 messages | In-context |
| **Episodic** | Past conversations | "User asked about refunds last week" | Vector DB |
| **Semantic** | Facts about the user/world | "User is on the Pro plan" | KV / graph |
| **Procedural** | How to do things | "Always cite sources" | System prompt |

### Memory operations

- **Write** — after a turn, extract salient facts and persist.
- **Read** — before a turn, retrieve relevant memories.
- **Decay** — old or low-relevance memories fade.

### The retrieval problem

Don't dump all memories into context. Retrieve the top-K most relevant to the current turn, similar to RAG.

## Code: simple episodic memory

```python
from openai import OpenAI
import faiss, numpy as np

client = OpenAI()
index = faiss.IndexFlatL2(1536)
memories = []  # list of {text, embedding, timestamp}

def embed(text: str) -> np.ndarray:
    return np.array(client.embeddings.create(model="text-embedding-3-large", input=text).data[0].embedding)

def remember(text: str):
    emb = embed(text)
    index.add(np.array([emb]))
    memories.append({"text": text, "embedding": emb, "ts": time.time()})

def recall(query: str, k: int = 3) -> list[str]:
    if len(memories) == 0:
        return []
    q = embed(query)
    _, idx = index.search(np.array([q]), k)
    return [memories[i]["text"] for i in idx[0] if i >= 0]
```

## Code: injecting memories into the prompt

```python
def build_messages(user_input: str) -> list[dict]:
    relevant = recall(user_input)
    memory_block = "\n".join(f"- {m}" for m in relevant)
    return [
        {"role": "system", "content": f"You are a helpful assistant.\n\nRelevant past context:\n{memory_block}"},
        {"role": "user", "content": user_input},
    ]
```

## Production concerns

- **Latency:** Memory retrieval adds 20–100ms.
- **Cost:** Embedding memory writes + retrieval queries add up. Cache aggressively.
- **Failure modes:** Stale memories cause confusion. Implement TTLs and forgetting.
- **Security:** Memories can contain PII. Encrypt at rest; respect deletion requests.

## Anti-patterns

- ❌ **Stuffing all memories into context.** Top-K retrieval only.
- ❌ **Never forgetting.** Implement decay.
- ❌ **Shared memory across users.** Strict per-user isolation.

## References

- [Letta (formerly MemGPT)](https://github.com/letta-ai/letta) — verified 2026-07-30
- [Mem0](https://github.com/mem0ai/mem0) — verified 2026-07-30
- [LangGraph memory](https://langchain-ai.github.io/langgraph/concepts/persistence/) — verified 2026-07-30

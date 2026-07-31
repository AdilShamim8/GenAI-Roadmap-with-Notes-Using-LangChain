# Multimodal RAG

> **Level:** ADV · **Last verified:** 2026-07-30

## Why this matters

Real corpuses aren't text-only. They're PDFs with embedded charts, slide decks with images, screenshots, video. Multimodal RAG retrieves across all of them so users can ask "show me the slide where revenue growth was forecast."

## Core concepts

### Three architectures

1. **Text-only with image captions** — extract images, caption with a VLM, embed the caption. Cheap, loses visual detail.
2. **Multi-vector** — embed text with a text embedder, images with an image embedder, store both. Retrieve from either, merge.
3. **Unified multimodal embedding** — Cohere Embed v4, Voyage multimodal, or BGE-M3+visual — embed text and images into the same space.

### The PDF special case

PDFs need special handling:
- Extract text with `pymupdf` or `unstructured`.
- Extract images per page.
- Extract tables as structured data.
- Embed each modality separately, link them with page coordinates.

## Code: multimodal retrieval with CLIP-style embedder

```python
from sentence_transformers import SentenceTransformer
model = SentenceTransformer("clip-ViT-L-14")  # text + image in same space

# Index
text_emb = model.encode("a chart showing revenue growth")
img_emb = model.encode(Image.open("chart.png"))
# Store both in the same vector collection.

# Query with text
q_emb = model.encode("revenue growth chart")
results = collection.query(query_embeddings=q_emb, n_results=5)
```

## Code: PDF extraction

```python
import fitz  # pymupdf

def extract_pdf(path: str):
    doc = fitz.open(path)
    pages = []
    for page in doc:
        pages.append({
            "text": page.get_text(),
            "images": [pix.tobytes("png") for pix in page.get_images(full=True)],
            "page_num": page.number,
        })
    return pages
```

## Production concerns

- **Latency:** Image embeddings are 5–20× slower than text.
- **Cost:** VLM calls for captioning add up. Cache aggressively.
- **Failure modes:** OCR on scanned PDFs is unreliable. Pre-extract with `pymupdf` or `unstructured`.
- **Security:** Image embeddings can leak visual content (logos, faces, dashboards). Treat as sensitive.

## Anti-patterns

- ❌ **Treating PDFs as text-only.** Loses charts, diagrams, signatures.
- ❌ **Embedding full-resolution images.** Resize to ≤512px.
- ❌ **Mixing text and image embeddings from different model families.** They're not in the same space.

## References

- [Cohere Embed v4 (multimodal)](https://cohere.com/blog/embed-v4) — verified 2026-07-30
- [Unstructured](https://github.com/Unstructured-IO/unstructured) — verified 2026-07-30
- [CLIP](https://openai.com/research/clip) — verified 2026-07-30

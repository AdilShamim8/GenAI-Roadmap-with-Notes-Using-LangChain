# Multimodal Inputs

> **Level:** INT · **Last verified:** 2026-07-30 · **Sources:** [OpenAI vision](https://platform.openai.com/docs/guides/vision), [Anthropic vision](https://docs.anthropic.com/en/docs/build-with-claude/vision)

## Why this matters

Most production GenAI systems in 2026 are multimodal: PDFs, screenshots, photos, audio. Treating vision as an afterthought is the difference between a working and a broken document-QA system.

## Core concepts

### Image inputs: three ways

1. **URL** — provider fetches. Easiest, requires the URL to be public.
2. **Base64 inline** — embed in the request. Bigger payload, no fetch dependency.
3. **File upload** — provider-hosted file reference. Best for repeated use.

### Resolution economics

OpenAI and Anthropic both tile large images into 512×512 patches. A 4K screenshot can cost ~1500 tokens before any text is generated. Resize aggressively before sending.

### PDF handling

- **OpenAI**: PDFs supported natively (up to ~100 pages per file in 2026).
- **Anthropic**: PDFs supported, with native text + image extraction.
- **DIY**: PyMuPDF to extract text + render pages to images → send as multimodal. More control, more code.

## Code: image + text (OpenAI)

```python
from openai import OpenAI
client = OpenAI()

resp = client.chat.completions.create(
    model="gpt-5",
    messages=[{
        "role": "user",
        "content": [
            {"type": "text", "text": "What's in this image?"},
            {"type": "image_url", "image_url": {"url": "https://example.com/photo.jpg", "detail": "low"}},
        ],
    }],
)
print(resp.choices[0].message.content)
```

## Code: PDF (Anthropic)

```python
import anthropic, base64
client = anthropic.Anthropic()

with open("doc.pdf", "rb") as f:
    pdf_b64 = base64.standard_b64encode(f.read()).decode()

resp = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=4096,
    messages=[{
        "role": "user",
        "content": [
            {"type": "document", "source": {"type": "base64", "media_type": "application/pdf", "data": pdf_b64}},
            {"type": "text", "text": "Summarize this document."},
        ],
    }],
)
```

## Production concerns

- **Latency:** Image inputs add 200–1000ms to TTFT depending on size.
- **Cost:** A single 4K image can cost more than 1000 output tokens. Resize before sending.
- **Failure modes:** OCR quality on scanned PDFs varies; pre-extract text with `pymupdf` or `unstructured` for reliability.
- **Security:** Vision models can read text in images — including screenshots of internal dashboards. Sanitize.

## Anti-patterns

- ❌ **Sending full-resolution images.** Resize to ≤1024px on the long edge.
- ❌ **Using OCR-then-LLM when the model supports PDFs natively.** You lose layout context.
- ❌ **Ignoring image token cost in your billing dashboard.** Vision can dominate cost silently.

## References

- [OpenAI vision](https://platform.openai.com/docs/guides/vision) — verified 2026-07-30
- [Anthropic vision](https://docs.anthropic.com/en/docs/build-with-claude/vision) — verified 2026-07-30
- [Anthropic PDF support](https://docs.anthropic.com/en/docs/build-with-claude/pdf) — verified 2026-07-30

# Google Gemini API

> **Level:** BEG · **Last verified:** 2026-07-30 · **Sources:** [Gemini API Docs](https://ai.google.dev/gemini-api/docs)

## Why this matters

Gemini is the third frontier pillar. Its differentiators: very long context (1M+ tokens), strong multimodal, generous free tier, and tight integration with Vertex AI for enterprise.

## Core concepts

- **`generate_content`** — the unified entry point. Takes a list of `Content` objects (text, images, audio, video).
- **System instructions** — separate parameter, similar to Anthropic.
- **Long context** — Gemini 2.5/3 Pro supports up to 1M tokens. Use sparingly; latency scales.
- **Vertex AI** — Google Cloud's hosted Gemini with VPC, IAM, and enterprise compliance.

## Code: minimal chat

```python
from google import genai
client = genai.Client(api_key="...")

resp = client.models.generate_content(
    model="gemini-2.5-pro",
    contents="Summarize the KV-cache in one sentence.",
)
print(resp.text)
```

## Multimodal in one call

```python
from google.genai import types

resp = client.models.generate_content(
    model="gemini-2.5-pro",
    contents=[
        types.Part.from_text("What's in this image?"),
        types.Part.from_bytes(data=open("photo.jpg", "rb").read(), mime_type="image/jpeg"),
    ],
)
```

## Production concerns

- **Latency:** Gemini Flash is competitive with GPT-5 mini on TTFT.
- **Cost:** Gemini has a free tier (rate-limited) and a paid tier. Long-context requests get expensive fast.
- **Failure modes:** Safety filters can be aggressive; check `prompt_feedback` in the response.
- **Security:** For HIPAA/PCI workloads, use Vertex AI, not the AI Studio API.

## Anti-patterns

- ❌ **Stuffing 1M tokens into every request** — slow, expensive, and recall degrades.
- ❌ **Mixing AI Studio API keys with Vertex auth.** Pick one path per environment.

## References

- [Gemini API reference](https://ai.google.dev/gemini-api/docs) — verified 2026-07-30
- [Vertex AI Gemini](https://cloud.google.com/vertex-ai/generative-ai/docs) — verified 2026-07-30

# Gemini Live

> **Level:** ADV · **Last verified:** 2026-07-30

## Why this matters

Google's Gemini Live is the alternative realtime API. Different pricing model, tighter integration with Google Cloud, and — for some use cases — better latency on Android.

## Core concepts

### Differences from OpenAI Realtime

| Dimension | OpenAI Realtime | Gemini Live |
|-----------|-----------------|-------------|
| Transport | WebSocket | WebSocket |
| Pricing | Per audio minute | Per token + per audio sec |
| Voice options | 5 voices | Multiple, locale-aware |
| Tool calls | Yes | Yes |
| Multimodal output | Audio + text | Audio + text + images |
| Best for | Cross-platform | Android-first, Google Cloud shops |

### Connection lifecycle

Similar to OpenAI: open session → stream audio in → receive audio out → handle interruptions → close.

## Code: minimal Gemini Live client

```python
import asyncio, json, websockets, base64

async def gemini_live():
    url = "wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1beta.GenerativeService.BidiGenerateContent"
    headers = {"Authorization": "Bearer YOUR_TOKEN"}

    async with websockets.connect(url, extra_headers=headers) as ws:
        # Configure
        await ws.send(json.dumps({
            "setup": {
                "model": "gemini-2.5-flash-preview-native-audio-dialog",
                "generation_config": {"response_modalities": ["AUDIO"]},
            }
        }))

        async def send_audio():
            async for chunk in mic_stream():
                await ws.send(json.dumps({
                    "realtime_input": {"audio_chunks": [{"data": base64.b64encode(chunk).decode(), "mime_type": "audio/pcm"}]}
                }))

        async def receive():
            async for msg in ws:
                event = json.loads(msg)
                if "server_content" in event:
                    part = event["server_content"].get("model_turn", {}).get("parts", [{}])[0]
                    if "inline_data" in part:
                        speaker.play(base64.b64decode(part["inline_data"]["data"]))

        await asyncio.gather(send_audio(), receive())
```

## Production concerns

- **Latency:** Competitive with OpenAI.
- **Cost:** Token-based; can be cheaper for short turns.
- **Failure modes:** Locale-specific voices may not be available everywhere.
- **Security:** Don't log audio.

## Anti-patterns

- ❌ **Mixing OpenAI and Gemini patterns.** Different APIs.
- ❌ **No interruption handling.**
- ❌ **Logging raw audio.**

## References

- [Gemini Live API](https://ai.google.dev/gemini-api/docs/live) — verified 2026-07-30
- [Vertex AI Gemini Live](https://cloud.google.com/vertex-ai/generative-ai/docs) — verified 2026-07-30

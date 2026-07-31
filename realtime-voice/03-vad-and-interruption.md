# VAD & Interruption Handling

> **Level:** ADV · **Last verified:** 2026-07-30

## Why this matters

Voice UX lives or dies on VAD (voice activity detection) and interruption handling. Get it wrong and the model either talks over the user (bad) or pauses awkwardly at every breath (also bad). This is the part of voice agents that takes the most tuning.

## Core concepts

### The VAD tradeoff

| Setting | Effect |
|---------|--------|
| **Low threshold** | Catches quiet speech; false-triggers on background noise |
| **High threshold** | Misses quiet speech; better in noisy environments |
| **Short silence_duration_ms** | Quick turn-taking; cuts off users who pause |
| **Long silence_duration_ms** | Patient; feels slow |

Typical 2026 defaults: threshold 0.5, silence_duration_ms 500ms.

### Interruption handling

When the user starts speaking while the model is talking:
1. Stop playing model audio immediately.
2. Cancel the in-flight model generation.
3. Discard any buffered model audio.
4. Start listening for the new turn.

### Double-talk

User talks *while* model is talking (not after). Harder case. Options:
- **Ignore** — let model finish, then respond to user's interrupt.
- **Stop model** — model stops mid-sentence, listens to user.
- **Barge-in** — model acknowledges ("yes?") and continues after user finishes.

The "right" answer depends on context. Customer support: stop model. Casual chat: ignore.

## Code: client-side VAD

```python
import webrtcvad, collections

vad = webrtcvad.Vad(3)  # aggressiveness 0-3
frame_duration_ms = 30

def vad_audio_stream(mic_stream):
    '''Yields (frame_bytes, is_speech) tuples.'''
    frame_size = 16000 * frame_duration_ms // 1000  # 16kHz mono
    frames = collections.deque(maxlen=int(1000 / frame_duration_ms))  # 1 sec window

    async for frame in mic_stream:
        is_speech = vad.is_speech(frame, 16000)
        frames.append(is_speech)

        # Detect end-of-utterance: 500ms of silence after speech
        if any(frames) and not is_speech and len(frames) >= int(500 / frame_duration_ms):
            if not any(list(frames)[-int(500 / frame_duration_ms):]):
                yield frame, "end_of_utterance"
                frames.clear()
                continue

        yield frame, "speech" if is_speech else "silence"
```

## Code: interruption handling

```python
async def realtime_session(ws):
    model_speaking = False

    async def receive():
        nonlocal model_speaking
        async for msg in ws:
            event = json.loads(msg)
            if event["type"] == "response.audio.delta":
                model_speaking = True
                speaker.play(base64.b64decode(event["delta"]))
            elif event["type"] == "response.done":
                model_speaking = False

    async def send_audio():
        async for frame, state in vad_audio_stream(mic_stream()):
            await ws.send(audio_buffer_msg(frame))
            if state == "end_of_utterance" and model_speaking:
                # User interrupted
                await ws.send(json.dumps({"type": "response.cancel"}))
                speaker.stop()
                model_speaking = False

    await asyncio.gather(receive(), send_audio())
```

## Production concerns

- **Latency:** Client-side VAD adds 20–50ms. Worth it for control.
- **Cost:** None.
- **Failure modes:** Background music triggers VAD; multiple speakers confuse it.
- **Security:** VAD has no security implications.

## Anti-patterns

- ❌ **Trusting server VAD blindly.** Tune for your environment.
- ❌ **No interruption handling.** Model talks over user.
- ❌ **Cancelling model too aggressively.** User pauses; model stops mid-sentence.

## References

- [webrtcvad](https://github.com/wiseman/py-webrtcvad) — verified 2026-07-30
- [Silero VAD](https://github.com/snakers4/silero-vad) — verified 2026-07-30
- [OpenAI Realtime: VAD](https://platform.openai.com/docs/guides/realtime) — verified 2026-07-30

# Self-Host vs API

> **Last verified:** 2026-07-30

## The breakeven math

Self-hosting makes sense when:

```
monthly_api_cost > monthly_self_host_cost + ops_overhead
```

Where `ops_overhead` is real: ~0.25 FTE for a single GPU cluster in production.

## Rule of thumb

| Monthly API spend | Verdict |
|-------------------|---------|
| < $5K | Always API. |
| $5K–$50K | API. Self-host only for latency, privacy, or compliance. |
| $50K–$500K | Pilot self-hosting on one workload. |
| > $500K | Self-host the steady-state workload; API for spikes. |

## Other reasons to self-host

- **Data residency**: EU-only, on-prem.
- **Latency**: <100ms p99 requires colocation.
- **Custom fine-tunes**: LoRA adapters on a base model.
- **No vendor lock-in**: hedge against API deprecations.

## Other reasons to stay on API

- **Throughput spikes**: APIs absorb; self-host doesn't.
- **Model upgrades**: APIs give you the new model instantly.
- **Multimodal**: APIs cover audio/vision more completely than self-host.

## References

- [vLLM](https://github.com/vllm-project/vllm) — verified 2026-07-30
- [SGLang](https://github.com/sgl-project/sglang) — verified 2026-07-30

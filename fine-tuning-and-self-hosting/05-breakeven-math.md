# Self-Host vs API Breakeven Math

> **Level:** INT · **Last verified:** 2026-07-30

## Why this matters

"Should we self-host?" is one of the most common questions in 2026 GenAI engineering. The answer is almost always "not yet" — but only rigorous math tells you when "yet" arrives.

## The formula

```
monthly_self_host = gpu_hourly_cost × 730 × num_gpus + ops_overhead
monthly_api = monthly_tokens_input × input_price + monthly_tokens_output × output_price

self_host wins when: monthly_api > monthly_self_host
```

### The numbers (2026, illustrative)

- 1× H100 on-demand: ~$3/hr → $2,190/month
- 1× H100 reserved (1yr): ~$1.50/hr → $1,095/month
- Ops overhead for a single cluster: ~0.25 FTE ≈ $5,000/month
- GPT-5 pricing: ~$5/1M input, ~$15/1M output

### Breakeven for GPT-5

```
$2,190 + $5,000 = $7,190/month self-host (1× H100 on-demand)
$7,190 / ($5/1M input + $15/1M output) → ~360M input tokens or ~120M output tokens
```

So self-hosting 1× H100 breaks even at ~360M input tokens/month (assuming 4:1 input:output ratio).

### Reality check

- Self-hosting a 70B model on 1× H100: ~100–200 tokens/sec/req, batched to ~5,000 tokens/sec total → ~13B tokens/month max throughput.
- API cost equivalent of 13B tokens: ~$65,000/month.
- So self-hosting a steady-state 13B-token/month workload saves ~$55,000/month vs GPT-5 API.

### When API still wins

- Bursty traffic (can't utilize GPU).
- Multi-modal needs (vision, audio).
- Reasoning workloads (o3, DeepSeek R1) where self-hosting a 671B model is impractical.
- Need to upgrade model monthly (frontier API > self-hosted open-weight).

## Code: a simple calculator

```python
def breakeven(monthly_tokens_in: int, monthly_tokens_out: int,
              api_input_per_m: float = 5.0, api_output_per_m: float = 15.0,
              gpu_hourly: float = 3.0, num_gpus: int = 1, ops_monthly: float = 5000.0):
    api_cost = (monthly_tokens_in / 1e6) * api_input_per_m + (monthly_tokens_out / 1e6) * api_output_per_m
    self_host_cost = gpu_hourly * 730 * num_gpus + ops_monthly
    return {
        "api_cost": api_cost,
        "self_host_cost": self_host_cost,
        "winner": "self_host" if self_host_cost < api_cost else "api",
        "savings": abs(api_cost - self_host_cost),
    }
```

## Production concerns

- **Latency:** Self-host can be faster (no network, no rate limits).
- **Cost:** Reserved capacity is 30–50% cheaper than on-demand.
- **Failure modes:** GPU failures; cluster ops is real work.
- **Security:** Self-hosted = full data control. Big advantage for regulated industries.

## Anti-patterns

- ❌ **Self-hosting for a workload < $5K/month API spend.** Ops overhead dominates.
- ❌ **Ignoring ops cost.** GPUs need babysitting.
- ❌ **One model per GPU.** Multi-LoRA matters.

## References

- [vLLM](https://docs.vllm.ai/) — verified 2026-07-30
- [GPU pricing — AWS](https://aws.amazon.com/ec2/instance-types/p5/) — verified 2026-07-30

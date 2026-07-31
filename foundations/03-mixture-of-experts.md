# Mixture of Experts (MoE)

> **Level:** INT · **Last verified:** 2026-07-30 · **Sources:** [Mixtral paper](https://arxiv.org/abs/2401.04088), [DeepSeek-V3 technical report](https://github.com/deepseek-ai/DeepSeek-V3)

## Why this matters

Llama 4, DeepSeek V3, Mixtral, and likely the next GPT/Claude generations all use MoE. MoE is why a 671B-parameter DeepSeek V3 serves at the cost of a 37B dense model. If you don't understand MoE, you'll misread model cards and overpay for inference.

## Core concepts

### The idea

Instead of every token passing through every parameter, a **router** sends each token to a small number of **experts** (typically 2 out of 8). Total parameters stay high (knowledge capacity), but active parameters per token stay low (compute cost).

### The math

For a layer with N experts, top-k routing:
```
gate_scores = softmax(W_gate @ token)  # shape (N,)
top_k_experts = topk(gate_scores, k=2)
output = sum(gate_scores[i] * expert_i(token) for i in top_k_experts)
```

### What this means for inference

| Metric | Dense 70B | MoE 8x22B (Mixtral) |
|--------|-----------|---------------------|
| Total params | 70B | 141B |
| Active params per token | 70B | 39B |
| VRAM to serve | ~140GB (fp16) | ~280GB (fp16) |
| Throughput | baseline | ~2× baseline |

MoE trades VRAM for throughput. The model is bigger on disk but cheaper per token.

## Code: see the router

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class MoELayer(nn.Module):
    def __init__(self, d_model, n_experts=8, k=2):
        super().__init__()
        self.gate = nn.Linear(d_model, n_experts)
        self.experts = nn.ModuleList([nn.Linear(d_model, d_model) for _ in range(n_experts)])
        self.k = k

    def forward(self, x):  # x: (batch, seq, d_model)
        gate_scores = F.softmax(self.gate(x), dim=-1)  # (batch, seq, n_experts)
        topk_vals, topk_idx = gate_scores.topk(self.k, dim=-1)
        topk_vals = topk_vals / topk_vals.sum(dim=-1, keepdim=True)
        out = torch.zeros_like(x)
        for i in range(self.k):
            for b in range(x.size(0)):
                for s in range(x.size(1)):
                    expert_idx = topk_idx[b, s, i].item()
                    out[b, s] += topk_vals[b, s, i] * self.experts[expert_idx](x[b, s])
        return out
```

(Real implementations vectorize this; the loop is for clarity.)

## Production concerns

- **VRAM:** MoE models need more VRAM than dense models of equivalent throughput. Plan for it.
- **Load balancing:** Bad routers send all tokens to one expert, killing throughput. Pretraining includes load-balancing loss; verify your fine-tune doesn't break it.
- **Quantization:** MoE + quantization is finicky. Use AWQ or FP8, not naive INT4.

## Anti-patterns

- ❌ **Comparing MoE and dense models by total parameter count.** Compare by active params.
- ❌ **Fine-tuning one expert in isolation.** Breaks the routing distribution.

## References

- [Mixtral of Experts](https://arxiv.org/abs/2401.04088) — verified 2026-07-30
- [DeepSeek-V3 Technical Report](https://github.com/deepseek-ai/DeepSeek-V3) — verified 2026-07-30
- [Outrageously Large Neural Networks (original MoE)](https://arxiv.org/abs/1701.06538) — verified 2026-07-30

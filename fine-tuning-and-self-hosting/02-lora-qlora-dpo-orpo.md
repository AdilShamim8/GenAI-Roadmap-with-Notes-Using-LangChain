# LoRA, QLoRA, DPO, ORPO

> **Level:** ADV · **Last verified:** 2026-07-30

## Why this matters

When you do fine-tune, these four techniques cover ~95% of use cases. They're the standard toolkit of 2026 — full fine-tuning is reserved for frontier labs and rare cases.

## Core concepts

### The four techniques

| Technique | What | Compute | Quality |
|-----------|------|---------|---------|
| **LoRA** | Low-rank adapters on attention weights | 1 GPU, hours | Near-full-FT quality |
| **QLoRA** | LoRA on a quantized base (4-bit) | 1 consumer GPU | Slight quality loss |
| **DPO** | Direct Preference Optimization (no reward model) | 2× LoRA | Better for alignment |
| **ORPO** | DPO without reference model | 1.5× LoRA | Better than DPO, simpler |

### LoRA in one paragraph

Instead of updating all weights of the base model, LoRA adds small "adapter" matrices (rank 8–64) to attention layers. Train only the adapters (~1% of parameters). At inference, merge adapters into the base or serve them separately.

### QLoRA

LoRA on a 4-bit quantized base. Lets you fine-tune a 70B model on a single 24GB consumer GPU. The catch: slight quality loss vs full-precision LoRA.

### DPO / ORPO

For alignment ("prefer this output over that one"). DPO needs a reference model; ORPO doesn't. Both beat RLHF for small teams.

## Code: QLoRA fine-tune with TRL

```python
# pip install trl transformers peft bitsandbytes datasets
from trl import SFTTrainer, SFTConfig
from peft import LoraConfig
from datasets import load_dataset
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
import torch

bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16,
)
model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-3.1-8B", quantization_config=bnb_config)
tok = AutoTokenizer.from_pretrained("meta-llama/Llama-3.1-8B")

peft_config = LoraConfig(r=16, lora_alpha=32, target_modules=["q_proj", "v_proj"], task_type="CAUSAL_LM")

dataset = load_dataset("your/dataset", split="train")

trainer = SFTTrainer(
    model=model,
    tokenizer=tok,
    train_dataset=dataset,
    peft_config=peft_config,
    args=SFTConfig(output_dir="./out", per_device_train_batch_size=4, num_train_epochs=3, learning_rate=2e-4),
)
trainer.train()
trainer.save_model("./out")
```

## Code: DPO alignment

```python
from trl import DPOTrainer, DPOConfig

# dataset: {"prompt": ..., "chosen": ..., "rejected": ...}
trainer = DPOTrainer(
    model=model,
    args=DPOConfig(output_dir="./dpo-out", beta=0.1, num_train_epochs=1),
    train_dataset=dpo_dataset,
    tokenizer=tok,
)
trainer.train()
```

## Production concerns

- **Latency:** LoRA adapters add <5% inference overhead.
- **Cost:** QLoRA on 8B = ~$5 in compute. On 70B = ~$50.
- **Failure modes:** Catastrophic forgetting. Always eval base vs fine-tuned.
- **Security:** Training data lives in adapters; treat as sensitive.

## Anti-patterns

- ❌ **Full fine-tuning when LoRA suffices.** Wastes compute.
- ❌ **No eval set.** Can't measure improvement.
- ❌ **High learning rate.** Destroys the base model's knowledge.

## References

- [PEFT (LoRA) paper](https://arxiv.org/abs/2106.09685) — verified 2026-07-30
- [QLoRA paper](https://arxiv.org/abs/2305.14314) — verified 2026-07-30
- [DPO paper](https://arxiv.org/abs/2305.18290) — verified 2026-07-30
- [TRL library](https://github.com/huggingface/trl) — verified 2026-07-30

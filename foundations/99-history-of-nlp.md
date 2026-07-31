# History of NLP (Context Only)

> **Level:** BEG · **Last verified:** 2026-07-30

## Why this is here, briefly

You will hear "RNN", "LSTM", "Word2Vec", and "BERT" in interviews and papers. You don't need to implement any of them in 2026, but you should know what they solved and why transformers replaced them.

## The 60-second timeline

| Era | Dominant technique | Why it died |
|------|-------------------|-------------|
| ~2010 | n-grams, TF-IDF | No semantics; sparse; O(V) features |
| ~2013 | Word2Vec, GloVe, FastText | Static embeddings; same word, same vector regardless of context |
| ~2014 | RNN, LSTM, GRU | Sequential → can't parallelize; vanishing gradients at long ranges |
| ~2017 | Transformer | Parallel; long-range attention; scales |
| ~2018 | BERT, GPT | Pretrain + fine-tune; transfer learning works |
| ~2020 | GPT-3 | Scale + in-context learning; few-shot works |
| ~2022 | ChatGPT / InstructGPT | RLHF makes models usable in conversation |
| ~2023+ | Mixture of Experts, multimodal, reasoning models (o1, R1) | Scale + specialization |

## What to actually remember

- **Attention** replaced recurrence. That's the only architectural shift that matters for your day-to-day.
- **Word2Vec** is the ancestor of embeddings. You'll still see "embeddings" everywhere; just don't use Word2Vec.
- **BERT** is bidirectional encoder; GPT is autoregressive decoder. Modern chat models are GPT-style.
- **RLHF** turned text generators into assistants.

## What you can safely skip

- Implementing an LSTM from scratch.
- The BERT vs GPT benchmarking era.
- Any paper on attention variants before 2020 unless you do research.

## References

- [The Illustrated Word2Vec — Jay Alammar](https://jalammar.github.io/illustrated-word2vec/) — verified 2026-07-30
- [Attention Is All You Need](https://arxiv.org/abs/1706.03762) — verified 2026-07-30
- [Illustrated BERT](https://jalammar.github.io/illustrated-bert/) — verified 2026-07-30

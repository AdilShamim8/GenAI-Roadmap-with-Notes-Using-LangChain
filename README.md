# GenAI Roadmap with Notes and Projects

<p align="center">
  <a href="https://python.langchain.com/docs/introduction/">
    <img src="https://raw.githubusercontent.com/lobehub/lobe-icons/refs/heads/master/packages/static-png/dark/langchain-color.png" alt="LangChain Logo" width="200"/>
  </a>
</p>

<div align="center">
  
![GitHub stars](https://img.shields.io/github/stars/AdilShamim8/GenAI-Roadmap-with-Notes-Using-LangChain?style=social)
![GitHub forks](https://img.shields.io/github/forks/AdilShamim8/GenAI-Roadmap-with-Notes-Using-LangChain?style=social)
![License](https://img.shields.io/badge/license-MIT-blue)
![Last Updated](https://img.shields.io/badge/last%20updated-May%202026-brightgreen)

</div>

A comprehensive roadmap and resource collection for learning Generative AI with practical implementation using LangChain. This repository serves as a guided journey from basic concepts to advanced applications, featuring the latest LangChain v1.2.x architecture, agentic AI patterns, and production-ready GenAI systems.

## Star History

<a href="https://www.star-history.com/?repos=AdilShamim8%2FGenAI-Roadmap-with-Notes-Using-LangChain&type=date&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/image?repos=AdilShamim8/GenAI-Roadmap-with-Notes-Using-LangChain&type=date&theme=dark&legend=top-left" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/image?repos=AdilShamim8/GenAI-Roadmap-with-Notes-Using-LangChain&type=date&legend=top-left" />
   <img alt="Star History Chart" src="https://api.star-history.com/image?repos=AdilShamim8/GenAI-Roadmap-with-Notes-Using-LangChain&type=date&legend=top-left" />
 </picture>
</a>

---

## What's New in 2026

> **This roadmap has been updated for May 1, 2026** to reflect the latest advancements in Generative AI and LangChain ecosystem.

### Key Updates:
- ✅ **LangChain v1.2.16** – Latest stable release (v1.2.16) published April 29, 2026, with GPT-5.5 Pro Responses API support, content-block-centric streaming (v2), and continued `create_agent` improvements
- ✅ **LangChain-Core v1.3.2** – langchain-core latest version 1.3.2, released April 24, 2026
- ✅ **LangGraph v1.1.10** – Released April 27, 2026, with type-safe streaming, type-safe invoke, Pydantic and dataclass coercion; LangGraph prebuilt v1.0.13 also released April 30, 2026
- ✅ **Latest LLMs** – GPT-5.5 & GPT-5.5 Pro (April 23, 2026; API April 24), Claude Opus 4.7 (April 16, 2026), Claude Mythos Preview (April 7, 2026, restricted via Project Glasswing), Gemini 3.1 Pro, Llama 4, DeepSeek-V4 comparisons and integration
- ✅ **LangSmith Fleet** – LangSmith Agent Builder has been renamed to LangSmith Fleet as of March 2026; now includes agent identity, sharing, permissions, and Skills
- ✅ **DeepAgents v0.5.0 alpha** – async subagents, multi-modal support, backend changes, and Anthropic prompt caching improvements
- ✅ **Advanced RAG** – Multi-agent RAG, multimodal retrieval, and dynamic knowledge updating
- ✅ **New Courses & Certifications** – LangChain Academy certifications, updated DeepLearning.AI courses

---

## Table of Contents

- [Overview](#overview)
- [2026 GenAI Landscape](#2026-genai-landscape)
- [GenAI Roadmap](#genai-roadmap)
- [LangChain Integration](#langchain-integration)
- [Top Resources](#top-resources)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Overview

This repository provides a structured learning path for developers interested in Generative AI with a focus on practical implementation using LangChain. It contains curated notes, code examples, and implementation guides covering the complete GenAI stack from foundations to production deployment.

---

## 2026 GenAI Landscape

### Current State of Large Language Models (May 2026)

| Model | Provider | Context Window | Key Strengths | Best For |
|-------|----------|----------------|---------------|----------|
| **GPT-5.5 / GPT-5.5 Pro** | OpenAI | 1,000,000 tokens | Smartest & most intuitive model yet; agentic coding, computer use, knowledge work, early scientific research; matches GPT-5.4 per-token latency with significantly fewer tokens per task | Enterprise, agentic workflows, complex professional tasks, coding |
| **GPT-5.4 Thinking/Pro** | OpenAI | 1,000,000 tokens | State-of-the-art reasoning, computer use, Tool Search, 33% fewer errors vs GPT-5.2 | Enterprise, agentic workflows, complex professional tasks |
| **GPT-5.4 mini / nano** | OpenAI | ~200,000 tokens | Fast everyday responses, lower-cost workloads | Quick-turn tasks, customer support, drafting |
| **Claude Opus 4.7** | Anthropic | 1,000,000 tokens | Most capable generally available Anthropic model; 87.6% on SWE-bench Verified, 2x agentic throughput, high-resolution vision (3.75MP), new xhigh effort level, task budgets | Advanced software engineering, long-running agents, knowledge work |
| **Claude Opus 4.6** | Anthropic | 1,000,000 tokens | Deep reasoning, longest autonomous task horizon (14.5h), coding, computer use | Research, long-running agents, code review, cybersecurity |
| **Claude Sonnet 4.6** | Anthropic | 1,000,000 tokens (beta) | Near-Opus performance, improved computer use, cost-efficient | Default daily driver, coding, document analysis |
| **Claude Mythos Preview** | Anthropic | N/A (restricted) | Most capable Anthropic model; capable of finding critical vulnerabilities in major OSes and browsers; NOT publicly available — restricted via Project Glasswing (invitation-only) | Defensive cybersecurity workflows only (invite-only consortium) |
| **Gemini 3.1 Pro** | Google | 1,000,000 tokens | Reasoning-first, agentic workflows, adaptive thinking | Complex multimodal, agentic coding |
| **Gemini 3 Flash / 3.1 Flash** | Google | 1,000,000 tokens | PhD-level reasoning at flash speed, multimodal | Cross-format tasks, real-time apps, cost-sensitive |
| **Llama 4 (Scout/Maverick/Behemoth)** | Meta | 10M (Scout) / 1M (Maverick) | Open-weight, MoE architecture, multimodal | Self-hosted, fine-tuning, cost-efficient deployment |
| **DeepSeek-V4** | DeepSeek | 128,000+ tokens | Engram memory architecture, strong coding, cost-effective | Budget-conscious deployments, coding, reasoning |

#### Key Model Changes Since March 2026:
- 🆕 OpenAI released **GPT-5.5** on April 23, 2026 — described as "our smartest and most intuitive to use model yet," excelling at writing and debugging code, researching online, analyzing data, creating documents, and operating software. GPT-5.5 matches GPT-5.4 per-token latency while performing at a much higher level of intelligence and using significantly fewer tokens to complete the same tasks.
- 🆕 **GPT-5.5 and GPT-5.5 Pro** became available in the Responses and Chat Completions APIs on April 24, 2026. GPT-5.5 is priced at $5/1M input tokens and $30/1M output tokens; GPT-5.5 Pro at $30/1M input and $180/1M output.
- 🆕 GPT-5.5 Pro is the same underlying model as GPT-5.5 but uses parallel test-time compute for even higher accuracy.
- 🆕 Anthropic released **Claude Opus 4.7** on April 16, 2026 — a notable improvement on Opus 4.6 in advanced software engineering, with particular gains on the most difficult tasks. It features better coding, sharper vision (3.75MP resolution), a new xhigh effort level for finer reasoning control, task budgets for developer cost management, and 2x agentic throughput. Priced the same as Opus 4.6 at $5/$25 per million tokens.
- 🆕 **Claude Mythos Preview** was announced April 7, 2026 — Anthropic's most powerful model, capable of finding critical vulnerabilities in major operating systems and web browsers. The UK AI Security Institute confirmed it was the first model to solve a 32-step cyber range end-to-end. Anthropic chose NOT to release it publicly, instead deploying it through **Project Glasswing**, an invitation-only consortium for defensive cybersecurity workflows.
- 🆕 Anthropic is using the Opus 4.7 rollout to test real-world cybersecurity safeguards that automatically detect and block prohibited or high-risk uses, with the stated goal of eventually enabling a broad release of Mythos-class models.
- 🆕 On February 19, 2026, Google released Gemini 3.1 Pro. It is Google's latest reasoning-first model optimized for complex agentic workflows and coding, with adaptive thinking and a 1M token context window.
- 🆕 Gemini 3 Flash is now the default model in the Gemini app, offering next-generation intelligence at lightning speed with PhD-level reasoning comparable to larger models.
- 🆕 Meta released Llama 4 — Llama 4 Maverick is a multimodal Mixture-of-Experts model built for textual and visual understanding and efficient deployment.
- 🔮 Anthropic confirmed a new in-development model called **"Claude Mythos"** (full release TBD) — currently the most capable model Anthropic has built, but not broadly released due to cybersecurity safety concerns. A new product tier called "Capybara" will be added above Opus when Claude Mythos launches publicly.

### Key GenAI Trends in 2026

1. **Agentic AI Revolution** – AI agents now autonomously manage workflows, interact with tools, use computers directly, and orchestrate multi-step processes
2. **Computer Use & Tool Search** – Models can now control browsers, desktops, and software UIs; API-level tool search reduces token overhead
3. **Multimodal by Default** – Models seamlessly process text, images, video, audio, and code; native image/video generation built in
4. **Smaller, Greener Models** – Quantization, MoE architectures, and pruning enable efficient edge deployment (GPT-5.4 mini/nano, Gemini Flash Lite)
5. **AI-Native Enterprises** – GenAI embedded in core business operations with autonomous coding agents (Claude Code, Codex)
6. **Ethics as Engineering** – Responsible AI practices built directly into development pipelines; cybersecurity implications of frontier models (Claude Mythos Preview) driving cautious, governance-first rollouts

---

## GenAI Roadmap

### 1. Foundations (2-4 weeks)
- **Machine Learning Basics**
  - Supervised vs. Unsupervised Learning
  - Neural Networks Fundamentals
  - Training and Evaluation Metrics
  
- **NLP Fundamentals**
  - Text Processing Techniques
  - Word Embeddings (Word2Vec, GloVe, FastText)
  - Modern Tokenization (BPE, SentencePiece)

- **Deep Learning for NLP**
  - RNNs, LSTMs, and GRUs
  - Attention Mechanisms
  - Transformers Architecture (The Foundation of Modern AI)

### 2. Generative AI Models (4-6 weeks)
- **Transformer-Based Models**
  - GPT Family (GPT-5.4 Thinking/Pro, GPT-5.4 mini/nano, GPT-5.5 / GPT-5.5 Pro)
  - Claude Series (Sonnet 4.6, Opus 4.6, Opus 4.7, Mythos Preview [restricted, Project Glasswing])
  - Gemini Family (3 Pro/Flash, 3.1 Pro/Flash)
  - Open-Source: Llama 4 (Scout, Maverick, Behemoth), Mistral Medium 3, DeepSeek-V4, Qwen
  
- **Multimodal Models**
  - Vision-Language Models (GPT-5.5 Vision, Gemini 3.1 Vision, Claude Opus 4.7 high-res vision)
  - Image Generation (DALL-E 3, Stable Diffusion 3, Midjourney v6, Gemini Nano Banana 2)
  - Video Generation (Sora, Runway Gen-3, Google Veo 3)
  - Audio Models (Whisper, ElevenLabs, Gemini 2.5 Flash TTS)
  
- **Fine-tuning Strategies**
  - Transfer Learning
  - Prompt Engineering & Optimization
  - PEFT (LoRA, QLoRA, Prefix Tuning)
  - RLHF & DPO (Direct Preference Optimization)
  - Distillation & Quantization
  - MetaP Hyperparameter Transfer (Llama 4)

### 3. LangChain Mastery (4-6 weeks)

> **Updated for LangChain v1.2.16 (April 2026) & LangChain-Core v1.3.2**

- **LangChain v1.2.x Basics**
  - `create_agent` abstraction: the fastest way to build an agent with any model provider, built on LangGraph runtime for reliability
  - Components and Unified Namespace
  - Chains, Agents, and Memory Types
  - LangChain Expression Language (LCEL)
  - Improved structured output generation integrated directly into the main agent loop, reducing both latency and cost
  
- **Middleware & Guardrails**
  - Built-in middleware for human-in-the-loop, summarization, and PII redaction; support for custom middleware to hook into any point in agent execution
  - PIIMiddleware (Data Redaction)
  - SummarizationMiddleware (Context Management)
  - HumanInTheLoopMiddleware (Approval Workflows)
  - Content Moderation Middleware
  - Model Retry with Exponential Backoff
  
- **Prompt Engineering with LangChain**
  - Template Creation & Management
  - Few-shot and Zero-shot Learning
  - Chain of Thought Prompting
  - Dynamic Prompt Construction
  
- **Advanced LangChain Features**
  - Document Loading and Intelligent Splitting
  - Vector Stores (Chroma, Pinecone, Weaviate, FAISS)
  - Embeddings (OpenAI, Cohere, HuggingFace)
  - Retrieval Augmented Generation (RAG)
  - Tool and API Integration
  - MCP Adapters for Multimodal Tools
  - Provider integrations: anthropic, aws, azure-ai, baseten, deepseek, fireworks, google-genai, google-vertexai, groq, huggingface, mistralai, ollama, openai, perplexity, together, xai

### 4. LangGraph & Agentic AI (3-4 weeks)

> **Updated for LangGraph v1.1.10 (April 2026)**

- **LangGraph Fundamentals**
  - Use LangGraph for advanced needs requiring a combination of deterministic and agentic workflows, heavy customization, and carefully controlled latency
  - State Machines for AI Workflows
  - Multi-Agent Orchestration
  - Conditional Branching & Loops
  - Human-in-the-Loop Patterns
  - Type-safe streaming & type-safe invoke (new in v1.1)
  - Pydantic and dataclass coercion (new in v1.1)

- **DeepAgents (v0.5.0 alpha)**
  - Async subagents, multi-modal support, backend changes, and Anthropic prompt caching improvements
  - Long-running Autonomous Workflows
  - Pluggable Storage Backends (S3, Cloud)
  - Remote Sandboxes for Security
  - Composite Agent Architectures

- **Building Production Agents**
  - Task Decomposition Patterns
  - Tool Selection & Execution (including OpenAI Tool Search)
  - Error Recovery & Fallbacks
  - Dynamic tools, recovery from hallucinated tool calls, and better streaming error signals
  - Agent Memory & State Persistence

### 5. Advanced RAG Systems (3-4 weeks)

> **Updated RAG Best Practices for 2026**

- **RAG Architecture Design**
  - Chunking Strategies (256-512 tokens optimal)
  - Embedding Model Selection
  - Hybrid Search (Vector + Keyword)
  - Re-ranking for Precision

- **Production RAG Patterns**
  - Multi-step RAG Pipelines
  - Context Condensation
  - Source Citation & Traceability
  - Dynamic Knowledge Updating

- **Multimodal RAG**
  - Image & Document Understanding
  - Table Extraction & Processing
  - Cross-Modal Retrieval

### 6. Applied GenAI Projects (4-8 weeks)
- **Building Conversational Agents**
  - Chatbots with Memory & Context
  - Multi-turn Dialogue Management
  - Task-specific Agentic Systems
  - Computer-Use Agents (browser automation, desktop control)
  
- **Content Generation Systems**
  - Text Summarization
  - Creative Writing Assistants
  - Code Generation & Review
  - Report Generation
  
- **Information Retrieval & Knowledge Systems**
  - Enterprise Q&A Systems
  - Knowledge Base Construction
  - Document Analysis Pipelines
  - Semantic Search Engines

### 7. Production & Deployment (2-4 weeks)
- **Model Optimization**
  - Quantization (INT8, INT4)
  - Distillation
  - Inference Optimization (vLLM, TensorRT)
  
- **Deployment Strategies**
  - API Development (FastAPI, LangServe)
  - Containerization (Docker, Kubernetes)
  - Serverless Deployment (AWS Lambda, Cloud Functions)
  - Edge Deployment
  
- **Observability with LangSmith**
  - Insights Agent automatically analyzes your traces to detect usage patterns, common agent behaviors and failure modes
  - LangSmith Fleet (formerly Agent Builder) – describe what you want and it figures out the approach, including prompt, tool selection, subagents, and skills; now includes agent identity, sharing, and permissions to manage your agent fleet across the company securely
  - Skills are now available in LangSmith Fleet — equip agents across your team with knowledge for specialized tasks
  - LangSmith Sandboxes (Private Preview) – locked-down, temporary environments where agents can run code safely, with granular control over access and resources
  - Polly (GA) – LangSmith's AI assistant is now generally available; can take action like an engineer on your team
  - Pin any experiment as your baseline so every subsequent run is automatically measured against it
  - Trace Debugging & Analysis
  - Performance Monitoring
  - Cost Tracking & Optimization
  - A/B Testing with Pairwise Annotation Queues
  - LangSmith Fetch CLI for IDE Debugging

---

## LangChain Integration

LangChain is the easiest way to start building agents and applications powered by LLMs — with under 10 lines of code you can connect to OpenAI, Anthropic, Google, and more. LangChain provides a pre-built agent architecture and model integrations to help you get started quickly.

This repository demonstrates how to leverage LangChain for:

- **Building Complex Reasoning Chains** with LCEL
- **Creating Domain-Specific Chatbots** with custom memory
- **Implementing Production RAG Systems** with hybrid retrieval
- **Developing Autonomous Agents** with LangGraph
- **Connecting LLMs to External Tools and APIs** via MCP Adapters
- **Deploying Secure, Observable AI Systems** with LangSmith Fleet

### LangChain v1.2.16 Key Features (May 2026)

```python
# create_agent API (LangChain v1.2.16)
from langchain import create_agent
from langchain.middleware import (
    PIIMiddleware,
    SummarizationMiddleware,
    HumanInTheLoopMiddleware
)

agent = create_agent(
    model="gpt-5.5",  # Updated: GPT-5.5 is the latest frontier model as of May 2026
    tools=[search_tool, calculator_tool],
    middleware=[
        PIIMiddleware(),
        SummarizationMiddleware(max_tokens=4000),
        HumanInTheLoopMiddleware(require_approval=["sensitive_action"])
    ]
)
```

### Important Version Notes:
- LangChain 0.3 is now in MAINTENANCE mode with support until December 2026, including only security patches and critical bug fixes
- Legacy functionality has been moved to langchain-classic for backwards compatibility
- langchain-community has been released as version 0.4 to reflect a different stability policy where minor releases may include breaking changes

---

## Top Resources

### Official Documentation
- [LangChain Documentation](https://docs.langchain.com/)
- [LangChain GitHub Repository](https://github.com/langchain-ai/langchain)
- [LangChain v1.x Migration Guide](https://docs.langchain.com/oss/python/releases/langchain-v1)
- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [LangSmith Platform](https://smith.langchain.com/)
- [LangChain Changelog (2026)](https://changelog.langchain.com/)
- [LangChain PyPI](https://pypi.org/project/langchain/) – v1.2.16
- [LangChain-Core PyPI](https://pypi.org/project/langchain-core/) – v1.3.2

### Courses & Certifications (2026)

| Course | Platform | Level | Certificate |
|--------|----------|-------|-------------|
| [LangChain for LLM Application Development](https://learn.deeplearning.ai/courses/langchain/) | DeepLearning.AI | Beginner | ✅ |
| [LangChain Academy - Foundation Track](https://academy.langchain.com/) | LangChain | Beginner-Advanced | ✅ Official |
| [LangChain Academy - DeepAgents Track](https://academy.langchain.com/) | LangChain | Advanced | ✅ Official |
| [Agentic AI with LangChain and LangGraph](https://www.coursera.org/courses?query=langchain) | IBM/Coursera | Intermediate | ✅ |
| [Developing LLM Applications with LangChain](https://www.datacamp.com/courses/developing-llm-applications-with-langchain) | DataCamp | Intermediate | ✅ |
| [LangChain Mastery Course](https://www.udemy.com/topic/langchain/) | Udemy | All Levels | ✅ |
| [Free LangChain Basics](https://www.mygreatlearning.com/academy/learn-for-free/courses/langchain-basics-for-beginners) | Great Learning | Beginner | ✅ Free |

### Upcoming Events
- 🎤 Interrupt 2026, the AI Agent Conference — May 13-14 at The Midway, San Francisco. Keynotes from Harrison Chase, Jensen Huang, and Andrew Ng; talks from teams at Clay, Rippling, and Honeywell.

### Books
- "Building LLM Powered Applications" by Simon Willison
- "Natural Language Processing with Transformers" by Lewis Tunstall, Leandro von Werra, and Thomas Wolf
- "Generative Deep Learning" (2nd Edition) by David Foster
- "Transformers for Natural Language Processing" by Denis Rothman
- "LangChain in Action" by Harrison Chase (2025)
- "Designing Large Language Model Applications" by O'Reilly (2025)

### Tutorials and Articles
- [LangChain Cookbook](https://github.com/gkamradt/langchain-tutorials)
- [Building LLM Applications for Production](https://huyenchip.com/2023/04/11/llm-engineering.html) by Chip Huyen
- [Prompt Engineering Guide](https://www.promptingguide.ai/)
- [RAG Application Development Guide 2026](https://www.leanware.co/insights/rag-application-development-guide)
- [The Illustrated Transformer](http://jalammar.github.io/illustrated-transformer/)
- [LangChain Best Practices (2026)](https://sider.ai/blog/ai-tools/best-langchain-tutorials-to-master-rag-agents-and-llm-apps)

### YouTube Channels
- [LangChain Official](https://www.youtube.com/@LangChain)
- [DeepLearning.AI](https://www.youtube.com/@Deeplearningai)
- [Weights & Biases](https://www.youtube.com/@WeightsBiases)
- [AI Coffee Break with Letitia](https://www.youtube.com/@AICoffeeBreak)
- [Sam Witteveen](https://www.youtube.com/@samwitteveenai)

### Research Papers (Essential Reading)
- [Attention Is All You Need](https://arxiv.org/abs/1706.03762) - Transformer architecture
- [Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165) - GPT-3 paper
- [Training Language Models to Follow Instructions with Human Feedback](https://arxiv.org/abs/2203.02155) - InstructGPT/RLHF
- [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401) - RAG paper
- [Engineering the RAG Stack (2026)](https://arxiv.org/pdf/2601.05264) - Latest RAG architecture review
- [Direct Preference Optimization](https://arxiv.org/abs/2305.18290) - DPO paper

### Tools & Platforms
- [LangSmith](https://smith.langchain.com/) - Observability & debugging (now with Fleet, Polly GA, Skills & Sandboxes)
- [Pinecone](https://www.pinecone.io/) - Vector database
- [ChromaDB](https://www.trychroma.com/) - Open-source embeddings database
- [Weaviate](https://weaviate.io/) - Vector search engine
- [vLLM](https://vllm.ai/) - High-throughput inference
- [Claude Code](https://docs.anthropic.com/claude-code) - Agentic coding CLI by Anthropic

---

## Getting Started

### Prerequisites
- Python 3.10 or higher (recommended: 3.11+; supports up to Python 3.14)
- pip (Python package manager)
- OpenAI API key (or other LLM provider keys)

### Installation

1. Clone this repository:
```bash
git clone https://github.com/AdilShamim8/GenAI-Roadmap-with-Notes-Using-LangChain.git
cd GenAI-Roadmap-with-Notes-Using-LangChain
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
# Create a .env file with your API keys
cat > .env << EOF
OPENAI_API_KEY=your_openai_api_key
ANTHROPIC_API_KEY=your_anthropic_api_key
LANGCHAIN_API_KEY=your_langsmith_api_key
LANGCHAIN_TRACING_V2=true
EOF
```

---

## Project Structure

```
GenAI-Roadmap-with-Notes-Using-LangChain/
├── foundations/                # Basic concepts and foundational knowledge
│   ├── nlp_basics/            # NLP fundamentals
│   ├── transformers/          # Transformer architecture notes
│   └── llm_concepts/          # LLM theory and concepts
├── langchain_basics/          # Introduction to LangChain v1.2.16
│   ├── components/            # Core components of LangChain
│   ├── chains/                # Building and using chains
│   ├── memory/                # Working with different memory types
│   └── middleware/            # Middleware patterns
├── langchain_advanced/        # Advanced LangChain implementations
│   ├── lcel/                  # LangChain Expression Language
│   ├── rag/                   # Retrieval Augmented Generation
│   ├── agents/                # Building autonomous agents
│   └── tools/                 # Tool integration
├── langgraph/                 # LangGraph v1.1.10 tutorials
│   ├── basics/                # State machines & workflows
│   ├── multi_agent/           # Multi-agent orchestration
│   └── deep_agents/           # Long-running agent patterns (v0.5.0 alpha)
├── projects/                  # Complete project implementations
│   ├── chatbot/               # Conversational agent examples
│   ├── document_qa/           # Document Q&A system
│   ├── content_generator/     # Text generation applications
│   └── agentic_assistant/     # Autonomous agent project
├── deployment/                # Deployment guides and examples
│   ├── langserve/             # LangServe API deployment
│   ├── langsmith/             # Observability setup (Fleet + Polly GA + Sandboxes)
│   ├── optimization/          # Model optimization techniques
│   └── monitoring/            # Production monitoring
├── resources/                 # Additional learning resources
├── notebooks/                 # Jupyter notebooks with examples
├── requirements.txt           # Project dependencies
├── .env.example               # Example environment variables
└── README.md                  # This documentation
```

---

## Examples

### Basic LangChain Chain (v1.2.16)

```python
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Initialize the LLM (GPT-5.5 is the latest as of May 2026)
llm = ChatOpenAI(model="gpt-5.5", temperature=0.7)

# Create a prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI assistant."),
    ("user", "Write a short paragraph about {topic}.")
])

# Create a chain using LCEL
chain = prompt | llm | StrOutputParser()

# Run the chain
result = chain.invoke({"topic": "artificial intelligence in 2026"})
print(result)
```

### Production RAG Implementation (May 2026)

```python
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

# Load and split documents
loader = TextLoader("path/to/document.txt")
documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=512,  # Optimal chunk size for 2026
    chunk_overlap=50
)
texts = text_splitter.split_documents(documents)

# Create embeddings and vector store
embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
db = Chroma.from_documents(texts, embeddings)
retriever = db.as_retriever(search_kwargs={"k": 5})

# Create RAG chain with source citation
prompt = ChatPromptTemplate.from_template("""
Answer the question based on the following context.
Always cite your sources.

Context: {context}

Question: {question}

Answer:""")

llm = ChatOpenAI(model="gpt-5.5")

rag_chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | llm
)

# Query with traceability
response = rag_chain.invoke("What are the key points?")
print(response.content)
```

### LangGraph Agent (Updated May 2026 — LangGraph v1.1.10)

```python
from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool

@tool
def search_web(query: str) -> str:
    """Search the web for information."""
    # Implement web search
    return f"Search results for: {query}"

@tool
def calculate(expression: str) -> str:
    """Evaluate a mathematical expression."""
    return str(eval(expression))

# Create agent with LangGraph
llm = ChatOpenAI(model="gpt-5.5")
agent = create_react_agent(llm, [search_web, calculate])

# Run agent with state management
result = agent.invoke({
    "messages": [("user", "What is 25 * 4 and who invented calculus?")]
})
print(result["messages"][-1].content)
```

### Using create_agent with Middleware (LangChain v1.2.16)

```python
from langchain import create_agent
from langchain.middleware import (
    PIIMiddleware,
    SummarizationMiddleware,
    HumanInTheLoopMiddleware
)

# Production agent with middleware stack
agent = create_agent(
    model="claude-opus-4-7",  # Or "gpt-5.5", "gemini-3.1-pro"
    tools=[search_tool, calculator_tool, file_tool],
    middleware=[
        PIIMiddleware(),
        SummarizationMiddleware(max_tokens=4000),
        HumanInTheLoopMiddleware(require_approval=["sensitive_action"])
    ]
)

result = agent.invoke({"input": "Analyze this quarterly report"})
```

Check the `notebooks/` directory for more complete examples and tutorials.

---

## Contributing

Contributions are welcome! If you'd like to add to this roadmap, improve existing content, or share your implementations:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

Please see [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Contact

- Website: [Adil Shamim](https://adilshamim.me/)
- GitHub: [Adil Shamim](https://github.com/AdilShamim8)
- Create an issue in this repository for questions or suggestions

---

<p align="center">
  <a href="https://github.com/AdilShamim8">
    <img src="https://img.shields.io/badge/GitHub-AdilShamim8-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub Profile"/>
  </a>
  <span style="opacity:.6">&nbsp;</span>

  <a href="https://www.linkedin.com/in/adilshamim8">
    <img src="https://img.shields.io/badge/LinkedIn-AdilShamim8-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn Profile"/>
  </a>
  <span style="opacity:.6">&nbsp;</span>

  <a href="https://www.kaggle.com/adilshamim8">
    <img src="https://img.shields.io/badge/Kaggle-AdilShamim8-20BEFF?style=for-the-badge&logo=kaggle&logoColor=white" alt="Kaggle Profile"/>
  </a>
  <span style="opacity:.6">&nbsp;</span>

  <a href="https://x.com/adil_shamim8">
    <img src="https://img.shields.io/badge/Twitter%2FX-@adil__shamim8-000000?style=for-the-badge&logo=x&logoColor=white" alt="Twitter/X Profile"/>
  </a>
  <span style="opacity:.6">&nbsp;</span>

  <a href="https://adilshamim8.medium.com/">
    <img src="https://img.shields.io/badge/Medium-AdilShamim8-12100E?style=for-the-badge&logo=medium&logoColor=white" alt="Medium Profile"/>
  </a>
</p>
<div align="center">
  
⭐ **If you find this repository helpful, please consider giving it a star!** ⭐

</div>

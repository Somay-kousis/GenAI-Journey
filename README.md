# GenAI-Journey
<!-- HEADER ANIMATION -->
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f0c29,50:302b63,100:24243e&height=200&section=header&text=LangChain%20Bootcamp&fontSize=52&fontColor=ffffff&fontAlignY=38&desc=From%20Zero%20to%20AI%20Engineer&descAlignY=60&descSize=18&animation=fadeIn" width="100%"/>

</div>

---


<br/>

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![LangChain](https://img.shields.io/badge/LangChain-0.3-1C3C3C?style=for-the-badge&logo=chainlink&logoColor=white)](https://langchain.com)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-412991?style=for-the-badge&logo=openai&logoColor=white)](https://openai.com)
[![Groq](https://img.shields.io/badge/Groq-LLaMA3-F55036?style=for-the-badge&logo=groq&logoColor=white)](https://groq.com)
[![HuggingFace](https://img.shields.io/badge/🤗_HuggingFace-Models-FFD21E?style=for-the-badge)](https://huggingface.co)

</div>

<br/>

<div align="center">

> *"LangChain is not an AI model. It is the framework that helps developers build AI applications using AI models."*

</div>

---

## 🗺️ The Journey

```
📦 This Repository
│
├── 🧠  Day 0  ── What is LangChain?
├── 🤖  Day 1  ── Models (LLMs, Chat, Embeddings)
├── 📝  Day 2  ── Prompts & Templates
├── 🧱  Day 3  ── Structured Output
├── 🔍  Day 4  ── Output Parsers
├── ⛓️  Day 5  ── Chains (Simple → Conditional)
├── 🔀  Day 6  ── Runnables & LCEL
├── 🛠️  Day 7  ── Tools & Tool Calling
│
└── 📚  RAG Pipeline
    ├── 📂  Day R1 ── Document Loaders
    ├── ✂️  Day R2 ── Text Splitters
    ├── 🗃️  Day R3 ── Vector Stores
    ├── 🔎  Day R4 ── Retrievers
    └── 🚀  Day R5 ── Full RAG System
```

---

## ⚡ How It All Connects

```
         YOU
          │
          ▼
    ┌──────────┐
    │ LangChain│  ◄── The glue between you and intelligence
    └──────────┘
          │
    ┌─────┴──────┐
    │            │
    ▼            ▼
 MODELS        RAG
    │            │
    ├─ LLMs      ├─ Loaders
    ├─ Chat      ├─ Splitters
    └─ Embed     ├─ Vector DB
                 └─ Retrievers
          │
          ▼
       AGENTS
    (coming soon)
```

---

## 🧬 Core Concepts at a Glance

| Concept | What It Does | Real World |
|--------|-------------|------------|
| **Models** | Talk to AI | Brain |
| **Prompts** | Instruction templates | Script |
| **Chains** | Connect multiple steps | Pipeline |
| **Tools** | Extend AI capabilities | Hands |
| **RAG** | Retrieve → Answer | Memory |
| **Agents** | Think → Act → Loop | Autonomy |

---

## 🗂️ Repo Structure

```
.
├── langchain/
│   ├── day0.md                        ← What is LangChain?
│   ├── day1_models/
│   │   ├── ChatModels/                ← Groq, HuggingFace, Local
│   │   ├── EmbeddingModels/           ← OpenAI + HF Embeddings
│   │   └── LLM/                       ← Raw LLM demo
│   ├── day2_prompts/                  ← PromptTemplates, ChatPrompts
│   ├── day3_structuredoutput/         ← TypedDict, Pydantic, JSON Schema
│   ├── day4_parsers/                  ← Str, JSON, Pydantic Parsers
│   ├── day5_chains/                   ← Simple, Sequential, Parallel, Conditional
│   ├── day6_runnables/                ← LCEL, Lambda, Branch, Passthrough
│   └── day7_tools/                    ← @tool, StructuredTool, BaseTool
│
├── rag/
│   ├── day_1_documentloaders/         ← PDF, TXT, CSV, Web, Directory
│   ├── day_2_splitters/               ← Character, Recursive, Semantic
│   ├── day_3_embedding/               ← Chroma, FAISS, Pinecone
│   ├── day_4_retrivers/               ← Similarity, MMR, Threshold
│   └── day_5_rag/                     ← Full RAG pipeline
│
└── ollama/                            ← Local models, no API needed
```

---

## 🚀 Getting Started

```bash
# 1. Clone this repo
git clone <your-repo-url>
cd <repo-name>

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install langchain langchain-openai langchain-groq langchain-huggingface
pip install langchain-community langchain-chroma python-dotenv streamlit

# 4. Set up your keys
cp .env.example .env
# Fill in your API keys
```

---

## 🔑 Environment Variables

```env
OPENAI_API_KEY=sk-...
GROQ_API_KEY=gsk_...
HUGGINGFACEHUB_API_TOKEN=hf_...
ANTHROPIC_API_KEY=sk-ant-...
```

---

## 💡 The Mental Models Worth Keeping

```
Language Model   =  Text  → Text
Chat Model       =  Messages  → Message
Embedding Model  =  Text  → Vector

PromptTemplate   =  Reusable Dynamic Prompt
ChatPromptTemplate = PromptTemplate for Conversations

Chain            =  Pipe multiple steps together
LCEL             =  prompt | model | parser

Tool             =  Function the AI can use
Tool Calling     =  AI deciding which function to use

RAG              =  Retrieve context → Feed to LLM → Answer
Vector Store     =  Database for embeddings
Retriever        =  Search engine for your data
```

---

## 📈 Progress Tracker

- [x] Day 0 — Introduction to LangChain
- [x] Day 1 — Models
- [x] Day 2 — Prompts
- [x] Day 3 — Structured Output
- [x] Day 4 — Output Parsers
- [x] Day 5 — Chains
- [x] Day 6 — Runnables
- [x] Day 7 — Tools & Tool Calling
- [x] RAG Day 1 — Document Loaders
- [x] RAG Day 2 — Text Splitters
- [x] RAG Day 3 — Vector Stores
- [x] RAG Day 4 — Retrievers
- [x] RAG Day 5 — Full RAG
- [x] Ollama — Local Models
- [ ] Agents — Coming Soon 🔜

---

## 🤝 Interview Cheat Sheet

<details>
<summary><b>Click to expand — quick answers for every concept</b></summary>

<br/>

**What is LangChain?**
> Framework for building LLM-powered applications.

**Why use LangChain?**
> Managing prompts, models, memory, retrieval and agents manually at scale becomes painful.

**Language Model vs Embedding Model?**
> Language → Text to Text. Embedding → Text to Vector.

**Why PromptTemplate?**
> Reusable, dynamic, validates inputs, integrates with chains.

**What is LCEL?**
> LangChain Expression Language. Uses `|` to connect components.

**RAG vs Fine-Tuning?**
> Fine-tuning changes the model. RAG keeps knowledge external and retrieves it.

**What is a Retriever?**
> Search engine for your data. Returns relevant document chunks.

**What is a Tool?**
> A Python function the LLM can call. Tools give AI hands.

</details>

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:24243e,50:302b63,100:0f0c29&height=120&section=footer" width="100%"/>

*Built with curiosity. Documented with clarity. Shipped with intent.*

</div>

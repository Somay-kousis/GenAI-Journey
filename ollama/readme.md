# Day 14 — Ollama

# What is Ollama?

Ollama is a framework/tool that allows you to:

```text
Run LLMs locally on your machine.
```

Instead of:

```text
Your App
↓
OpenAI API
↓
Internet
```

you can do:

```text
Your App
↓
Local Model
↓
Your Own Machine
```

---

# Why Ollama Matters

Without Ollama:

```text
Need APIs
Need Internet
Pay per request
```

---

With Ollama:

```text
Offline AI
Private AI
Local inference
No API costs
```

---

# Mental Model

```text
OpenAI/Groq
=
Cloud Brain
```

---

```text
Ollama
=
Local Brain
```

---

# What Ollama Actually Does

Ollama helps:
- download models
- run models
- manage models
- expose local API

---

# Core Flow

```text
Download Model
↓
Run Model
↓
Send Prompt
↓
Receive Response
```

---

# Why Developers Love Ollama

## Privacy

Data stays local.

---

## Cheap

No token billing.

---

## Offline Usage

Works without internet.

---

## Experimentation

Easy local testing.

---

## Personal AI Systems

Very useful for:
- memory systems
- terminal agents
- local assistants
- private RAG

---

# Common Models In Ollama

## Llama

Meta models.

---

## Mistral

Lightweight + strong.

---

## Gemma

Google open models.

---

## TinyLlama

Very small model.

---

## DeepSeek

Coding/reasoning focused.

---

# Installing Ollama

Usually:

```bash
brew install ollama
```

or direct installer from website.

---

# Running Ollama

Start service:

```bash
ollama serve
```

---

# Downloading Models

Example:

```bash
ollama pull llama3
```

---

# Running A Model

```bash
ollama run llama3
```

Now model becomes interactive locally.

---

# Example

```text
You:
Explain RAG

Local Model:
...
```

No cloud involved.

---

# Ollama Architecture

```text
Your App
↓
LangChain
↓
Ollama API
↓
Local LLM
```

---

# Important Realization

Ollama is NOT the model.

😭

It is:

```text
Model Runner / Management Layer
```

---

# Ollama Exposes Local API

Usually:

```text
http://localhost:11434
```

Meaning local apps can use it exactly like:
- OpenAI
- Groq
- Gemini APIs

---

# LangChain + Ollama

Example:

```python
from langchain_ollama import ChatOllama
```

---

# Example Flow

```python
llm = ChatOllama(model="llama3")
```

---

Now:

```python
llm.invoke("Hello")
```

works locally.

---

# Ollama vs Groq/OpenAI

## Groq/OpenAI

```text
Cloud Hosted
Very Powerful
Fast
Paid / Limited
```

---

## Ollama

```text
Local
Private
Cheap
Hardware Limited
```

---

# Biggest Limitation

Your laptop becomes the server 😭

Meaning:
- RAM matters
- GPU matters
- model size matters

---

# Small Models vs Large Models

## Small Models

```text
Fast
Cheap
Weaker reasoning
```

---

## Large Models

```text
Better quality
Slower
Heavy RAM usage
```

---

# Quantization

Very important concept.

Models are compressed:

```text
4-bit
8-bit
```

to run efficiently locally.

---

# Why Quantization Matters

Without it:

```text
Huge GPU requirements
```

With it:

```text
Normal laptops can run models
```

---

# Ollama In Your Projects

## Portfolio Assistant

Today:

```text
Retriever
↓
Groq
↓
Answer
```

---

Later:

```text
Retriever
↓
Ollama Local Model
↓
Answer
```

---

# Signal Future

Useful because:
- privacy
- identity systems
- memory systems
- personal context

become safer locally.

---

# Terminal Agent

VERY strong use-case.

```text
Local
Fast
Private
No cloud needed
```

---

# Important Architecture Insight

When switching:

```text
Groq → Ollama
```

most architecture remains SAME.

Only:
- model provider changes
- inference location changes

---

# Ollama + RAG

VERY common stack:

```text
Documents
↓
Retriever
↓
Context
↓
Ollama Local LLM
↓
Answer
```

---

# Ollama + Agents

```text
Agent
↓
Tool Calling
↓
Local LLM
↓
Reasoning
```

---

# Why Ollama Feels Important

Because this is where AI starts becoming:

```text
YOUR system
```

instead of:

```text
someone else's API
```

Huge mindset shift.

---

# Things Ollama Does NOT Solve

## Better Intelligence

Depends on model quality.

---

## Better Retrieval

Still your job.

---

## Better Prompting

Still your job.

---

## Better Workflows

Still your job.

---

# Must Remember

```text
Ollama
≠
LLM
```

---

```text
Ollama
=
Local model runner
```

---

```text
OpenAI/Groq
=
Cloud inference
```

---

```text
Ollama
=
Local inference
```

---

# Interview Revision

## Why use Ollama?

Privacy, offline AI, low cost local inference.

---

## What changes when moving from Groq to Ollama?

Mostly only model provider/inference location.

---

## What is quantization?

Compressing models to run efficiently locally.

---

## Biggest limitation of local models?

Hardware constraints.

---

## Why is Ollama useful for personal AI systems?

Data stays local/private.

---

# One Line Summary

```text
Ollama allows developers to run and manage LLMs locally instead of relying entirely on cloud APIs.
```

---

# The One Diagram To Remember

```text
Your App
↓
LangChain
↓
Ollama
↓
Local Model
↓
Response
```

---

# Biggest Mental Shift

Before Ollama:

```text
AI = API
```

After Ollama:

```text
AI = something I can run myself
```

😭🚀
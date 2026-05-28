# Day 11 — RAG (Retrieval Augmented Generation)

## What is RAG?

RAG =

```text
Retrieval
+
Augmented
+
Generation
```

---

Meaning:

```text
Retrieve Relevant Information
+
Give It To LLM
+
Generate Better Answer
```

---

# Why Do We Need RAG?

Normal LLM:

```text
Question
 ↓
LLM
 ↓
Answer
```

Problems:

```text
Hallucinations
No Private Knowledge
Outdated Information
Cannot Access Your Documents
```

---

Example

```text
What projects has Somay built?
```

ChatGPT doesn't know.

---

# RAG Solution

```text
Question
 ↓
Find Relevant Information
 ↓
Give To LLM
 ↓
Answer
```

---

# Core Idea

Instead of teaching the model new information:

```text
Train Model Again
```

❌ Expensive

❌ Slow

❌ Difficult

---

RAG does:

```text
Keep Knowledge Outside Model
 ↓
Retrieve When Needed
```

✅ Cheap

✅ Fast

✅ Easy

---

# Complete RAG Architecture

## Indexing Phase

Done once.

---

```text
PDFs
Website
Resume
Portfolio
Notes
```

↓

```text
Document Loader
```

↓

```text
Documents
```

↓

```text
Text Splitter
```

↓

```text
Chunks
```

↓

```text
Embedding Model
```

↓

```text
Vectors
```

↓

```text
Vector Store
```

---

Knowledge Base Ready.

---

# Query Phase

Runs for every user question.

---

```text
User Question
```

↓

```text
Embedding Model
```

↓

```text
Question Vector
```

↓

```text
Retriever
```

↓

```text
Relevant Chunks
```

↓

```text
Prompt
+
Question
+
Retrieved Context
```

↓

```text
LLM
```

↓

```text
Final Answer
```

---

# Visual

```text
INDEXING

Documents
 ↓
Loader
 ↓
Splitter
 ↓
Embeddings
 ↓
Vector Store


-----------------------


QUERYING

Question
 ↓
Embedding
 ↓
Retriever
 ↓
Relevant Chunks
 ↓
LLM
 ↓
Answer
```

---

# The Most Important Line

RAG is basically:

```text
Question
+
Relevant Chunks
↓
LLM
↓
Answer
```

---

The LLM is NOT searching.

The Retriever is searching.

The LLM is answering.

---

# Why RAG Works

Without RAG

```text
Question
 ↓
LLM Memory
 ↓
Answer
```

---

With RAG

```text
Question
 ↓
Retriever
 ↓
Relevant Knowledge
 ↓
LLM
 ↓
Answer
```

---

# Example

Portfolio Assistant

Question:

```text
What ML projects has Somay built?
```

---

Retriever finds:

```text
Churn Prediction Project

Custom Transformer

Feature Engineering
```

---

LLM receives:

```text
Question
+
Retrieved Chunks
```

and generates answer.

---

# Prompt Used In RAG

Usually:

```text
Use the following context
to answer the question.

Context:
{retrieved_chunks}

Question:
{user_question}
```

---

# Components Of RAG

## Loader

```text
Gets Documents
```

---

## Splitter

```text
Creates Chunks
```

---

## Embeddings

```text
Convert Text To Vectors
```

---

## Vector Store

```text
Stores Vectors
```

---

## Retriever

```text
Finds Relevant Chunks
```

---

## LLM

```text
Generates Answer
```

---

# Why Not Fine-Tune?

Fine Tuning

```text
Changes Model Knowledge
```

---

RAG

```text
Keeps Knowledge External
```

---

Fine Tuning:

```text
Expensive
Slow
Hard To Update
```

---

RAG:

```text
Cheap
Fast
Easy To Update
```

---

# Real Project Mapping

## Portfolio Assistant

```text
Portfolio Files
 ↓
RAG
 ↓
Ask About Me
```

---

## Resume Assistant

```text
Resume
 ↓
RAG
 ↓
Interview Questions
```

---

## College Notes Chatbot

```text
Notes
 ↓
RAG
 ↓
Ask Questions
```

---

## Mutiny

```text
Idea
 ↓
Retriever
 ↓
Similar Founders
 ↓
LLM Analysis
```

---

# Advantages

```text
Private Data
Up To Date Data
No Retraining
Cheaper
Scalable
```

---

# Limitations

Bad Retrieval

↓

Bad Answer

---

Rule:

```text
Garbage Retrieval
=
Garbage Answer
```

---

Most RAG improvements focus on:

```text
Better Retrieval
```

not

```text
Better LLM
```

---

# Advanced RAG (Preview)

Basic RAG:

```text
Retrieve Once
 ↓
Answer
```

---

Advanced RAG:

```text
Rewrite Query
Retrieve Again
Rerank Results
Validate Results
Self Reflection
```

Examples:

```text
CRAG
Self-RAG
Hybrid Search
Reranking
```

---

# Must Remember

```text
RAG
=
Retrieval + Generation
```

---

```text
Retriever Searches
LLM Answers
```

---

```text
Question
+
Relevant Chunks
=
Answer
```

---

```text
RAG
≠
Fine Tuning
```

---

```text
Knowledge Stays Outside Model
```

---

# Interview Revision

## What is RAG?

A technique that retrieves relevant information and provides it to an LLM before generating an answer.

---

## Why use RAG?

To answer questions using external/private knowledge.

---

## Difference Between RAG and Fine Tuning?

```text
Fine Tuning
=
Change Model

RAG
=
Provide Context
```

---

## Who Searches?

```text
Retriever
```

---

## Who Answers?

```text
LLM
```

---

## Most Important RAG Formula?

```text
Question
+
Retrieved Context
↓
LLM
↓
Answer
```

---

# One Line Summary

```text
RAG gives an LLM access to external knowledge by retrieving relevant information before generating an answer.
```

---

# The One Diagram To Remember

```text
Documents
 ↓
Loader
 ↓
Splitter
 ↓
Embeddings
 ↓
Vector Store

----------------

Question
 ↓
Retriever
 ↓
Relevant Chunks
 ↓
LLM
 ↓
Answer
```

---

# Entire Journey So Far

```text
Models
 ↓
Prompts
 ↓
Structured Output
 ↓
Parsers
 ↓
Chains
 ↓
Runnables
 ↓
Loaders
 ↓
Splitters
 ↓
Vector Stores
 ↓
Retrievers
 ↓
RAG
```

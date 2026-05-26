# Day 9 — Vector Stores

## Why Do We Need Vector Stores?

After splitting:

```text
Document
 ↓
Chunks
```

we still cannot search efficiently.

Computers don't understand text meaning.

They understand numbers.

---

So we convert chunks into embeddings.

```text
Chunk
 ↓
Embedding Model
 ↓
Vector
```

Example:

```text
"What is LangChain?"
```

↓

```text
[0.23, -0.51, 0.87, ...]
```

---

Now we need somewhere to store these vectors.

That place is called:

```text
Vector Store
```

---

# Position in RAG Pipeline

```text
PDF
 ↓
Loader
 ↓
Documents
 ↓
Splitter
 ↓
Chunks
 ↓
Embeddings
 ↓
Vector Store
 ↓
Retriever
 ↓
LLM
```

---

# What is a Vector Store?

A specialized database designed to store vectors and perform similarity search.

---

Instead of:

```text
Store Text
```

it stores:

```text
Store Vector
```

---

# Main Purpose

Given:

```text
User Query
```

find:

```text
Most Similar Chunks
```

---

# Normal Database vs Vector Store

## SQL Database

Searches:

```text
Exact Match
```

Example:

```text
Find all students named Somay
```

---

## Vector Store

Searches:

```text
Meaning Match
```

Example:

```text
Question:
How do I build AI apps?

Retrieved:
LangChain helps create LLM applications.
```

Different words.

Same meaning.

---

# Flow

```text
Chunks
 ↓
Embedding Model
 ↓
Vectors
 ↓
Store
```

Later:

```text
Question
 ↓
Embedding Model
 ↓
Query Vector
 ↓
Similarity Search
 ↓
Relevant Chunks
```

---

# Visual

```text
Chunk A
 ↓
Vector A

Chunk B
 ↓
Vector B

Chunk C
 ↓
Vector C
```

Stored inside:

```text
Vector Store
```

---

# Similarity Search

Question:

```text
How can I build AI applications?
```

↓

Query Vector

↓

Compare with all stored vectors

↓

Return closest vectors

---

# Most Important Concept

```text
Semantic Search
```

Search by meaning.

Not keywords.

---

Example

Stored Chunk:

```text
LangChain helps developers build LLM applications.
```

Question:

```text
How do I make AI apps?
```

---

Keyword Search:

```text
No match
```

---

Semantic Search:

```text
Match found
```

because meaning is similar.

---

# Chroma DB

Most common beginner Vector Store.

---

Install

```bash
pip install chromadb
```

---

Import

```python
from langchain_chroma import Chroma
```

---

Create Vector Store

```python
vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings
)
```

---

Flow

```text
Chunks
 +
Embeddings
 ↓
Chroma
```

---

# FAISS

Popular local vector store.

Created by Meta.

---

Install

```bash
pip install faiss-cpu
```

---

Import

```python
from langchain_community.vectorstores import FAISS
```

---

Create

```python
vectorstore = FAISS.from_documents(
    chunks,
    embeddings
)
```

---

Benefits

```text
Fast
Local
Free
```

---

# Pinecone

Cloud Vector Database.

---

Benefits

```text
Scalable
Production Ready
Managed Service
```

---

Used when:

```text
Large Applications
Millions Of Vectors
```

---

# Similarity Search Example

```python
results = vectorstore.similarity_search(
    "What is LangChain?"
)
```

---

Flow

```text
Question
 ↓
Embedding
 ↓
Compare Vectors
 ↓
Return Similar Chunks
```

---

# Similarity Score

Measures closeness.

Usually uses:

```text
Cosine Similarity
```

---

Range

```text
1
=
Very Similar

0
=
Unrelated

-1
=
Opposite
```

---

# Metadata Storage

Vector Stores store:

```text
Vector
```

and

```text
Metadata
```

---

Example

```python
{
    "source": "notes.pdf",
    "page": 12
}
```

---

Why?

Later:

```text
Answer Found
 ↓
Where Did It Come From?
```

Metadata helps.

---

# Real Project Mapping

## Chat With PDF

```text
PDF
 ↓
Chunks
 ↓
Embeddings
 ↓
Vector Store
```

---

## Portfolio Assistant

```text
Portfolio Files
 ↓
Chunks
 ↓
Vector Store
```

---

## College Notes Chatbot

```text
Notes
 ↓
Vector Store
 ↓
Question Answering
```

---

# Must Remember

```text
Embedding
=
Vector
```

---

```text
Vector Store
=
Database For Vectors
```

---

```text
Similarity Search
=
Find Closest Vectors
```

---

```text
Semantic Search
=
Search By Meaning
```

---

```text
Chroma
=
Beginner Friendly
```

---

```text
FAISS
=
Fast Local Search
```

---

```text
Pinecone
=
Cloud Vector Database
```

---

# Interview Revision

## Why Vector Stores?

To store embeddings and perform efficient similarity search.

---

## Why not use SQL databases?

SQL searches exact values.

Vector stores search meaning.

---

## What is Semantic Search?

Searching based on meaning rather than keywords.

---

## What does a Vector Store contain?

```text
Vectors
Metadata
```

---

## Most common beginner Vector Store?

```text
Chroma
```

---

## Most common local Vector Store?

```text
FAISS
```

---

## What similarity metric is commonly used?

```text
Cosine Similarity
```

---

# One Line Summary

```text
Vector Stores are databases that store embeddings and allow semantic search over your documents.
```

---

# The One Diagram To Remember

```text
Chunks
 ↓
Embeddings
 ↓
Vectors
 ↓
Vector Store
 ↓
Similarity Search
 ↓
Relevant Chunks
```

---

# The Entire Story So Far

```text
Loader
=
Get Documents

Splitter
=
Create Chunks

Embedding
=
Convert Chunks To Vectors

Vector Store
=
Store Vectors
```

That's 80% of RAG already.
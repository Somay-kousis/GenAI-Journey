# Day 10 — Retrievers

## Why Do We Need Retrievers?

After Vector Stores we have:

```text
Chunks
 ↓
Embeddings
 ↓
Vector Store
```

Thousands of chunks may exist.

---

Question:

```text
How does LangChain work?
```

Should we send:

```text
All Chunks
```

to the LLM?

No.

---

Problems:

```text
Expensive
Slow
Context Limit
Irrelevant Information
```

---

Solution:

```text
Retriever
```

---

# What is a Retriever?

A Retriever finds the most relevant chunks for a query.

---

Flow

```text
Question
 ↓
Retriever
 ↓
Relevant Chunks
```

---

Think of it as:

```text
Search Engine For Your Data
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
Relevant Chunks
 ↓
LLM
```

---

# Main Job

Convert:

```text
User Question
```

into

```text
Relevant Context
```

---

Example

Question:

```text
What is LangChain?
```

---

Retriever finds:

```text
Chunk 23
Chunk 91
Chunk 102
```

because they contain related information.

---

LLM receives only those chunks.

---

# Why Not Use Vector Store Directly?

Vector Store:

```text
Stores Data
```

---

Retriever:

```text
Fetches Data
```

---

Mental Model:

```text
Vector Store
=
Library
```

```text
Retriever
=
Librarian
```

---

# Creating a Retriever

From Vector Store

```python
retriever = vectorstore.as_retriever()
```

---

Flow

```text
Vector Store
 ↓
as_retriever()
 ↓
Retriever
```

---

# Invoke

```python
docs = retriever.invoke(
    "What is LangChain?"
)
```

---

Output

```text
Relevant Documents
```

---

# Similarity Search Retriever

Most common retriever.

---

Flow

```text
Question
 ↓
Embedding
 ↓
Similarity Search
 ↓
Top Matching Chunks
```

---

Example

```text
Question:
How do I build AI apps?
```

---

Retrieved Chunk

```text
LangChain helps developers build
LLM applications.
```

---

# Search Types

## Similarity

Most common.

---

Returns:

```text
Closest Chunks
```

---

Example

```python
retriever = vectorstore.as_retriever(
    search_type="similarity"
)
```

---

# Top K Retrieval

Controls number of chunks returned.

---

Example

```python
retriever = vectorstore.as_retriever(
    search_kwargs={"k":3}
)
```

---

Meaning:

```text
Return Top 3 Chunks
```

---

Visual

```text
Question
 ↓

Chunk A 95%
Chunk B 92%
Chunk C 89%
Chunk D 60%

 ↓

Return A B C
```

---

# Similarity Score Threshold

Only return chunks above a score.

---

Example

```text
Score > 0.8
```

---

Flow

```text
Relevant
 ↓
Keep

Irrelevant
 ↓
Discard
```

---

Useful when:

```text
Avoiding Bad Context
```

---

# MMR Retriever

Maximum Marginal Relevance

---

Problem

Normal similarity search may return:

```text
Chunk A
Chunk B
Chunk C
```

which are almost identical.

---

MMR tries:

```text
Relevant
+
Diverse
```

---

Example

Instead of:

```text
Page 5
Page 5
Page 5
```

returns:

```text
Page 5
Page 9
Page 13
```

---

Benefits

```text
Less Repetition
More Coverage
```

---

# Retriever Output

Output is not text.

Output is:

```python
Document(...)
Document(...)
Document(...)
```

---

Each contains:

```text
page_content
metadata
```

---

Example

```python
docs[0].page_content
docs[0].metadata
```

---

# Retriever Flow

```text
Question
 ↓
Embedding
 ↓
Vector Search
 ↓
Top Chunks
 ↓
Return Documents
```

---

# Real RAG Flow

Without Retriever

```text
Question
 ↓
LLM
```

Hallucinations possible.

---

With Retriever

```text
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

# Real Project Mapping

## Chat With PDF

```text
Question
 ↓
Retriever
 ↓
Relevant PDF Chunks
 ↓
LLM
```

---

## Portfolio Assistant

```text
Question
 ↓
Retriever
 ↓
Relevant Portfolio Information
 ↓
LLM
```

---

## Mutiny Founder Matching

```text
Founder Idea
 ↓
Retriever
 ↓
Similar Founder Profiles
```

---

# Must Remember

```text
Vector Store
=
Stores Vectors
```

---

```text
Retriever
=
Fetches Relevant Chunks
```

---

```text
Question
 ↓
Retriever
 ↓
Relevant Context
```

---

```text
Similarity Search
=
Most Common Retrieval
```

---

```text
Top K
=
Number Of Returned Chunks
```

---

```text
MMR
=
Relevant + Diverse Results
```

---

# Interview Revision

## What is a Retriever?

A component that retrieves relevant documents/chunks for a query.

---

## Why do we need Retrievers?

To avoid sending the entire knowledge base to the LLM.

---

## Difference Between Vector Store and Retriever?

```text
Vector Store
=
Storage

Retriever
=
Search
```

---

## What is Top K?

Number of chunks returned.

---

## What is MMR?

Maximum Marginal Relevance.

Returns relevant and diverse results.

---

## What does a Retriever return?

```python
Document Objects
```

not final answers.

---

# One Line Summary

```text
Retrievers are the search engine of RAG; they find the most relevant chunks and provide context to the LLM.
```

---

# The One Diagram To Remember

```text
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

# Entire RAG Story So Far

```text
Loader
=
Get Documents

Splitter
=
Create Chunks

Embedding
=
Convert To Vectors

Vector Store
=
Store Vectors

Retriever
=
Find Relevant Chunks
```

You now know the 5 core building blocks of a basic RAG system. The next RAG video is basically combining these pieces into one working pipeline.
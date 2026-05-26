# Day 8 — Text Splitters

## Why Do We Need Text Splitters?

LLMs have context limits.

Large documents cannot be sent at once.

Example:

```text
500 Page PDF
```

Cannot directly become:

```text
PDF
 ↓
LLM
```

---

Solution:

```text
PDF
 ↓
Split
 ↓
Small Chunks
 ↓
LLM
```

---

# The Main Idea

Convert:

```text
Huge Document
```

into

```text
Chunk 1
Chunk 2
Chunk 3
Chunk 4
...
```

---

# Why Not Use Whole Documents?

Problems:

```text
Too Large
Expensive
Slow
Poor Retrieval
```

---

Example

```text
300 Pages
```

User asks:

```text
What is Gradient Descent?
```

No need to send all 300 pages.

Need only relevant chunks.

---

# Position in RAG Pipeline

```text
PDF
 ↓
Document Loader
 ↓
Documents
 ↓
Text Splitter
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

# Chunk

A small piece of a document.

Example

```text
Document:

LangChain is a framework used
to build LLM applications.
It provides tools for prompts,
chains and agents.
```

---

After Splitting

```text
Chunk 1:
LangChain is a framework...

Chunk 2:
It provides tools...
```

---

# Text Splitter Flow

```text
Large Document
        ↓
  Text Splitter
        ↓
 Small Chunks
```

---

# RecursiveCharacterTextSplitter

Most common splitter.

Most important one.

---

Import

```python
from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)
```

---

Example

```python
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)
```

---

Split

```python
chunks = splitter.split_documents(
    docs
)
```

---

# chunk_size

Maximum size of a chunk.

Example

```python
chunk_size=1000
```

Means:

```text
≈ 1000 characters per chunk
```

---

Visual

```text
Document
 ↓

[1000]
[1000]
[1000]
[1000]
```

---

# chunk_overlap

Repeated content between chunks.

Example

```python
chunk_overlap=200
```

---

Without Overlap

```text
Chunk 1:
AAA BBB CCC

Chunk 2:
DDD EEE FFF
```

Context may be lost.

---

With Overlap

```text
Chunk 1:
AAA BBB CCC DDD

Chunk 2:
CCC DDD EEE FFF
```

Some context preserved.

---

# Why Overlap Matters

Suppose answer lies here:

```text
CCC DDD
```

If chunks split exactly there:

```text
Chunk 1:
AAA BBB CCC

Chunk 2:
DDD EEE FFF
```

Meaning gets broken.

---

Overlap prevents this.

```text
Chunk 1:
AAA BBB CCC DDD

Chunk 2:
CCC DDD EEE FFF
```

---

# Recursive Splitting

The splitter tries to preserve meaning.

Priority:

```text
Paragraph
 ↓
Sentence
 ↓
Word
 ↓
Character
```

---

Instead of:

```text
Random Cut
```

it tries:

```text
Logical Cut
```

---

# CharacterTextSplitter

Simpler splitter.

---

Import

```python
from langchain_text_splitters import (
    CharacterTextSplitter
)
```

---

Example

```python
splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=1000
)
```

---

Limitation

```text
May break context
```

---

# Recursive vs Character Splitter

## Character Splitter

```text
Simple
Fast
Can break meaning
```

---

## Recursive Splitter

```text
Smart
Preserves Context
Most Common
```

---

# Example

Document:

```text
LangChain is a framework
for building AI applications.

It supports prompts,
chains and agents.
```

---

After Splitting

```text
Chunk 1:
LangChain is a framework...

Chunk 2:
It supports prompts...
```

---

# Real Project Mapping

## Chat With PDF

```text
PDF
 ↓
Split into chunks
 ↓
Embeddings
 ↓
Store
```

---

## Chat With Notes

```text
Notes
 ↓
Chunks
 ↓
Search
 ↓
Answer
```

---

## Resume Analyzer

Usually:

```text
No splitting needed
```

because resumes are small.

---

# Choosing Chunk Size

Small Chunks

```text
Better Retrieval
Less Context
```

---

Large Chunks

```text
More Context
Worse Retrieval
```

---

Typical Values

```python
chunk_size=1000
chunk_overlap=200
```

Very common.

---

# Must Remember

```text
Text Splitter
=
Break Documents Into Chunks
```

---

```text
Chunk
=
Small Piece Of Document
```

---

```text
chunk_size
=
Chunk Length
```

---

```text
chunk_overlap
=
Repeated Context
```

---

```text
RecursiveCharacterTextSplitter
=
Most Common Splitter
```

---

# Interview Revision

## Why Text Splitters?

Large documents cannot be efficiently embedded or retrieved as a whole.

---

## Why create chunks?

To improve retrieval quality.

---

## Why use overlap?

To preserve context across chunk boundaries.

---

## What is chunk_size?

Maximum size of each chunk.

---

## Most commonly used splitter?

```text
RecursiveCharacterTextSplitter
```

---

## Recursive vs Character Splitter?

```text
Character:
Simple splitting

Recursive:
Context-aware splitting
```

---

# One Line Summary

```text
Text Splitters transform large documents into meaningful chunks that can later be embedded, stored and retrieved efficiently.
```

---

# The One Diagram To Remember

```text
Document
   ↓
Text Splitter
   ↓

Chunk 1
Chunk 2
Chunk 3
Chunk 4

   ↓
Embeddings
```
# LangChain Models

## Keywords

- Model
- Language Model
- Chat Model
- Embedding Model
- Temperature
- Open Source Model
- Proprietary Model
- Hugging Face
- Inference API
- Local Model
- Embedding
- Cosine Similarity

---

# Model

```text
Common LangChain interface for interacting with AI models.
```

Types:

```text
1. Language Models
2. Embedding Models
```

---

# Language Models

Input:

```text
Text
```

Output:

```text
Text
```

Examples:

```text
GPT
Claude
Gemini
Llama
```

---

## Chat Model

Input:

```text
Messages
```

Output:

```text
Messages
```

Example:

```python
from langchain_groq import ChatGroq

llm = ChatGroq(
    model="llama-3.3-70b-versatile"
)

response = llm.invoke("Hello")
```

---

# Temperature

Controls randomness.

```python
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7
)
```

---

## Low Temperature

```text
0 - 0.3
```

Output:

```text
More predictable
More factual
```

Use:

```text
Coding
RAG
Q&A
```

---

## High Temperature

```text
0.8 - 1
```

Output:

```text
Creative
Random
```

Use:

```text
Stories
Poetry
Brainstorming
```

---

# Proprietary Models

Require API key.

Examples:

```text
OpenAI GPT
Claude
Gemini
```

---

# Open Source Models

Examples:

```text
Llama
Mistral
Gemma
Qwen
TinyLlama
```

Can run:

```text
Local
Hugging Face
Ollama
```

---

# Hugging Face Inference API

Run models hosted on Hugging Face.

```python
from langchain_huggingface import HuggingFaceEndpoint
```

---

# Local Models

Run directly on your machine.

Examples:

```text
TinyLlama
Gemma
Llama
Mistral
```

Benefits:

```text
No API cost
Private
Offline
```

---

# Embedding Models

Input:

```text
Text
```

Output:

```text
Vector (numbers)
```

Example:

```text
"I love AI"

↓

[0.12, -0.45, 0.88, ...]
```

---

# Generate Embeddings

```python
from langchain_huggingface import HuggingFaceEmbeddings
```

---

# Why Embeddings?

Used for:

```text
Search
RAG
Recommendations
Clustering
Similarity
```

---

# Document Similarity Search

Flow:

```text
Documents
↓
Embeddings
↓
Store vectors
↓
User Query
↓
Convert query to embedding
↓
Find similar vectors
↓
Return relevant documents
```

---

# Cosine Similarity

Measures similarity between vectors.

Range:

```text
1   -> identical
0   -> unrelated
-1  -> opposite
```

Higher score:

```text
More similar
```

---

# Interview Revision

Q: What is a Model in LangChain?

A:

```text
Common interface to interact with Language Models and Embedding Models.
```

---

Q: Difference between Language Model and Embedding Model?

A:

```text
Language Model:
Text → Text

Embedding Model:
Text → Vector
```

---

Q: Difference between LLM and Chat Model?

A:

```text
LLM:
Raw text input/output

Chat Model:
Message-based input/output
```

---

Q: What does Temperature control?

A:

```text
Randomness of output.
```

---

Q: Why are embeddings important?

A:

```text
Used for semantic search and RAG.
```

---

Q: What is cosine similarity?

A:

```text
Measures similarity between embeddings.
Higher value = more similar.
```

---

# Must Remember

```text
Language Model
=
Generate text

Embedding Model
=
Generate vectors

Vectors
=
Power RAG

Cosine Similarity
=
Compare vectors
```
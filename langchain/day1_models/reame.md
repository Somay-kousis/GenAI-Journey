# Day 1 — Models

## What are Models?

In LangChain, **Models** are the interface used to talk to AI models.

```text
LangChain
   ↓
Model Interface
   ↓
LLM / Chat Model / Embedding Model
```

---

## Types of Models

```text
Models
│
├── Language Models
│   ├── LLMs
│   └── Chat Models
│
└── Embedding Models
```

---

# 1. Language Models

Used for text generation.

```text
Text / Messages
      ↓
Language Model
      ↓
Text / Message Response
```

Examples:

```text
GPT
Claude
Gemini
Llama
Mistral
Qwen
```

---

## LLM vs Chat Model

### LLM

```text
Text → Text
```

Older/raw style.

### Chat Model

```text
Messages → Message
```

Better for chat apps.

Most modern apps use **Chat Models**.

---

# 2. Using Groq Chat Model

```python
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7
)

response = llm.invoke("Explain LangChain in simple words")

print(response.content)
```

---

# 3. Temperature

Controls randomness.

```text
Low temperature  → predictable, factual
High temperature → creative, random
```

Use:

```text
0.0 - 0.3 → RAG, coding, factual answers
0.7 - 1.0 → stories, ideas, creative writing
```

Example:

```python
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.2
)
```

---

# 4. Closed Source Models

Examples:

```text
OpenAI
Claude
Gemini
```

Usually need:

```text
API key
Internet
Billing/free quota
```

---

# 5. Open Source Models

Examples:

```text
Llama
Mistral
Gemma
Qwen
TinyLlama
```

Can be used through:

```text
Hugging Face
Ollama
Local Machine
```

Benefits:

```text
Free/local possible
More control
Privacy
```

---

# 6. Embedding Models

Embedding models convert text into vectors.

```text
Text
 ↓
Embedding Model
 ↓
Numbers / Vector
```

Example:

```text
"I love AI"
 ↓
[0.12, -0.44, 0.91, ...]
```

Used for:

```text
Semantic Search
Similarity Search
RAG
Recommendations
Clustering
```

---

# 7. Hugging Face Embeddings

```python
from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector = embeddings.embed_query("What is LangChain?")

print(vector[:5])
print(len(vector))
```

---

# 8. Document Similarity

Basic idea:

```text
Documents
 ↓
Embeddings
 ↓
Vectors
 ↓
Compare with query vector
 ↓
Most similar document
```

---

## Cosine Similarity

Used to compare vectors.

```text
Higher score = more similar
```

```python
from sklearn.metrics.pairwise import cosine_similarity

score = cosine_similarity(
    [query_vector],
    [document_vector]
)

print(score)
```

---

# 9. Mini Similarity Search Example

```python
from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

documents = [
    "LangChain helps build LLM applications.",
    "Cricket is a popular sport in India.",
    "RAG connects LLMs with external knowledge."
]

query = "How do I build apps with language models?"

doc_vectors = embeddings.embed_documents(documents)
query_vector = embeddings.embed_query(query)

scores = cosine_similarity([query_vector], doc_vectors)[0]

best_index = scores.argmax()

print(documents[best_index])
print(scores[best_index])
```

---

# Must Remember

```text
Language Model = Text → Text

Chat Model = Messages → Message

Embedding Model = Text → Vector

Temperature = Randomness

Cosine Similarity = Vector Similarity
```

---

# Interview Revision

## What is a model in LangChain?

A common interface for interacting with language models and embedding models.

---

## Language model vs embedding model?

```text
Language Model:
Text → Text

Embedding Model:
Text → Vector
```

---

## Why embeddings?

Because machines cannot compare meaning directly from text, so text is converted into vectors.

---

## What is cosine similarity?

A method to compare how similar two vectors are.

---

## When to use low temperature?

For factual, consistent tasks like RAG, coding, and Q&A.

---

# One Line Summary

```text
Models are where LangChain connects your app to intelligence:
language models generate text, embedding models create vectors.
```


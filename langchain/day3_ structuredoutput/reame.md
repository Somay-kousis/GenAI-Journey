# Day 3 — Structured Output

## Problem

LLMs normally return text.

Example:

```text
The candidate knows Python, React and SQL.
The resume score is 85/100.
```

Humans can read it.

Machines struggle to use it.

---

# Solution

Force the LLM to return a fixed structure.

Example:

```json
{
  "skills": [
    "Python",
    "React",
    "SQL"
  ],
  "score": 85
}
```

Now it can be:

```text
Stored in Database
Sent to API
Used by Agents
Processed by Code
```

---

# Why Structured Output?

Without Structured Output:

```text
LLM
 ↓
Random Text
 ↓
Human Reads
```

With Structured Output:

```text
LLM
 ↓
JSON/Object
 ↓
Program Uses It
```

---

# Real World Flow

```text
Resume
 ↓
LLM
 ↓
{
  skills: [],
  score: 85
}
 ↓
Database / API / Agent
```

---

# LangChain Method

```python
structured_llm = llm.with_structured_output(...)
```

---

# 1. TypedDict

Simple structure definition.

```python
from typing_extensions import TypedDict

class Person(TypedDict):
    name: str
    age: int
```

---

Use

```python
structured_llm = llm.with_structured_output(Person)
```

---

Output

```json
{
  "name": "Somay",
  "age": 21
}
```

---

## Advantages

```text
Simple
Lightweight
Easy
```

---

## Limitations

```text
No Validation
No Default Values
No Type Conversion
```

---

# 2. Pydantic

Most commonly used.

---

Define Schema

```python
from pydantic import BaseModel

class Person(BaseModel):
    name: str
    age: int
```

---

Use

```python
structured_llm = llm.with_structured_output(Person)
```

---

Output

```python
Person(
    name="Somay",
    age=21
)
```

---

## Advantages

```text
Validation
Type Checking
Default Values
Type Conversion
Error Handling
```

---

Example

Model returns:

```json
{
  "age": "21"
}
```

Pydantic converts:

```python
age = 21
```

automatically.

---

# 3. JSON Schema

Language-independent structure.

Example:

```json
{
  "type": "object",
  "properties": {
    "name": {
      "type": "string"
    }
  }
}
```

---

## Why JSON Schema?

Useful when:

```text
Python
JavaScript
Java
Go
```

all need the same structure.

---

# Structured Output Flow

```text
Prompt
 ↓
LLM
 ↓
Schema
 ↓
Structured Result
```

---

# Supported Models

Works best with:

```text
GPT
Claude
Gemini
```

These models are trained for structured generation.

---

# Limitation

Some models don't support it properly.

Examples:

```text
TinyLlama
Older Open Models
```

---

# What Happens Then?

Use:

```text
Output Parsers
```

instead.

(Next Video)

---

# Real Project Examples

## Resume Analyzer

Input

```text
Resume
```

Output

```json
{
  "skills": [],
  "weaknesses": [],
  "score": 85
}
```

---

## Startup Evaluator

Output

```json
{
  "market_score": 8,
  "risk_score": 5
}
```

---

## AI Agent

Output

```json
{
  "action": "search",
  "query": "LangGraph tutorial"
}
```

Agent can directly use it.

---

# TypedDict vs Pydantic

```text
TypedDict
│
├── Simple
├── Lightweight
└── Structure Only
```

```text
Pydantic
│
├── Validation
├── Type Conversion
├── Error Handling
└── Production Ready
```

---

# Must Remember

```text
Text Output
=
Human Readable
```

```text
Structured Output
=
Machine Readable
```

---

```text
TypedDict
=
Basic Structure
```

```text
Pydantic
=
Production Structure
```

---

```text
JSON Schema
=
Cross Language Structure
```

---

# Interview Revision

## Why Structured Output?

Allows LLM output to be consumed by applications, APIs and agents.

---

## Why is it important for Agents?

Agents need structured data to make decisions and call tools.

---

## TypedDict vs Pydantic?

```text
TypedDict
→ Structure

Pydantic
→ Structure + Validation
```

---

## When use JSON Schema?

When multiple languages/services need the same schema.

---

## What if the model doesn't support Structured Output?

Use Output Parsers.

---

# One Line Summary

```text
Structured Output converts AI responses from human-readable text into machine-readable data.
```
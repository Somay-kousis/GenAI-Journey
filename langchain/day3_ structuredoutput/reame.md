# LangChain Structured Output

## Keywords

- Structured Output
- with_structured_output()
- TypedDict
- Pydantic
- JSON Schema
- Validation
- Type Conversion
- Output Parser

---

# Why Structured Output?

Without Structured Output:

```text
LLM
↓
Random Text
```

Example:

```text
The candidate knows Python, React and SQL.
```

Hard to use programmatically.

---

With Structured Output:

```json
{
  "skills": [
    "Python",
    "React",
    "SQL"
  ]
}
```

Easy to use in:

```text
Agents
APIs
Databases
Applications
```

---

# Main Idea

```text
LLM
↓
Structured Data
↓
Program
↓
Action
```

This is one of the foundations of AI Agents.

---

# with_structured_output()

```python
structured_llm = llm.with_structured_output(Schema)
```

LangChain automatically forces output to follow the schema.

---

# TypedDict

Simple schema definition.

```python
from typing_extensions import TypedDict

class Person(TypedDict):
    name: str
    age: int
```

Usage:

```python
structured_llm = llm.with_structured_output(Person)
```

---

## Advantages

```text
Simple
Easy
Lightweight
```

---

## Limitations

```text
No validation
No default values
No extra features
```

---

# Pydantic

Most powerful option.

```python
from pydantic import BaseModel

class Person(BaseModel):
    name: str
    age: int
```

---

Usage

```python
structured_llm = llm.with_structured_output(Person)
```

---

## Advantages

```text
Validation
Default Values
Type Checking
Better Error Handling
Type Conversion
```

Example:

```python
age = "21"
```

can automatically become:

```python
age = 21
```

---

# JSON Schema

Language-independent schema.

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

## Advantages

```text
Universal
Cross-language
Industry Standard
```

Useful when:

```text
Python
JavaScript
Java
Go
```

need the same schema.

---

# Native Structured Output

Works best with:

```text
GPT
Claude
Gemini
```

These models are trained for structured generation.

---

# Open Source Model Limitation

Some models:

```text
TinyLlama
Older Open Models
```

may not support:

```python
with_structured_output()
```

properly.

---

# Solution

Use:

```text
Output Parsers
```

instead.

(Next Video)

---

# Real Use Cases

## Resume Analyzer

Input:

```text
Resume
```

Output:

```json
{
  "skills": [],
  "experience": [],
  "score": 85
}
```

---

## Startup Validator

Input:

```text
Idea
```

Output:

```json
{
  "market_score": 8,
  "risk_score": 5
}
```

---

## AI Agent

Input:

```text
Book flight to Delhi
```

Output:

```json
{
  "destination": "Delhi",
  "date": "2026-06-01"
}
```

Tool can now use this data.

---

# Interview Revision

Q: Why Structured Output?

A:

```text
Allows LLM outputs to be consumed by programs and tools.
```

---

Q: Why important for Agents?

A:

```text
Agents need structured data to call tools and make decisions.
```

---

Q: TypedDict vs Pydantic?

A:

```text
TypedDict:
Simple schema

Pydantic:
Validation + defaults + type conversion
```

---

Q: When use JSON Schema?

A:

```text
Cross-language compatibility.
```

---

Q: Why doesn't with_structured_output work everywhere?

A:

```text
Some models are not trained for structured generation.
```

---

Q: Alternative?

A:

```text
Output Parsers
```

---

# Must Remember

```text
Prompts
↓
Structured Output
↓
Tools
↓
Agents
```

Without Structured Output:

```text
Human-readable
```

With Structured Output:

```text
Machine-readable
```

This is the first video where LangChain starts feeling like software engineering instead of chatting with an LLM.
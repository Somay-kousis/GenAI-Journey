# Day 4 — Output Parsers

## What Problem Do They Solve?

LLMs generate text.

Applications need structured data.

---

Without Parser

```text
Prompt
 ↓
LLM
 ↓
"The candidate knows Python and React"
```

Hard to use in code.

---

With Parser

```text
Prompt
 ↓
LLM
 ↓
Parser
 ↓
Structured Data
```

Easy to use in:

```text
Agents
APIs
Databases
Applications
```

---

# Structured Output vs Output Parser

## Structured Output

```python
llm.with_structured_output(...)
```

Model itself generates structured data.

---

## Output Parser

```python
parser = ...
```

Parser converts or validates model output.

---

Rule:

```text
Model supports structured output?
       │
       ├── Yes
       │      ↓
       │ Structured Output
       │
       └── No
              ↓
        Output Parser
```

---

# Output Parser Flow

```text
Prompt
 ↓
LLM
 ↓
Raw Output
 ↓
Parser
 ↓
Usable Output
```

---

# 1. StrOutputParser

Simplest parser.

Returns plain text.

---

Import

```python
from langchain_core.output_parsers import StrOutputParser
```

---

Example

```python
chain = prompt | llm | StrOutputParser()
```

---

Output

```text
"LangChain is a framework..."
```

---

Use Cases

```text
Summaries
Blogs
Content Generation
Q&A
```

---

## Mental Model

```text
AIMessage
 ↓
String
```

---

# 2. JsonOutputParser

Returns JSON.

---

Import

```python
from langchain_core.output_parsers import JsonOutputParser
```

---

Output

```json
{
  "name": "Somay",
  "skill": "Python"
}
```

---

Use Cases

```text
Structured Data
Simple APIs
Basic Automation
```

---

## Limitation

```text
No strict validation
```

Model can still return weird JSON.

---

# 3. StructuredOutputParser

For predefined schemas.

---

Idea

```text
Expected Fields
 ↓
Model Output
 ↓
Structured JSON
```

---

Example

```json
{
  "name": "",
  "age": ""
}
```

---

Benefits

```text
Consistent Keys
Consistent Structure
```

---

Use Cases

```text
Resume Analysis
Forms
Data Extraction
```

---

# 4. PydanticOutputParser

Most powerful parser.

---

Import

```python
from pydantic import BaseModel
from langchain.output_parsers import PydanticOutputParser
```

---

Schema

```python
class Person(BaseModel):
    name: str
    age: int
```

---

Parser

```python
parser = PydanticOutputParser(
    pydantic_object=Person
)
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

Benefits

```text
Validation
Type Checking
Error Handling
Type Conversion
```

---

Example

Input

```json
{
  "age": "21"
}
```

Output

```python
age = 21
```

---

# Parser Comparison

## StrOutputParser

```text
Output:
String

Use:
Text Generation
```

---

## JsonOutputParser

```text
Output:
JSON

Use:
Simple Structured Data
```

---

## StructuredOutputParser

```text
Output:
Schema Based JSON

Use:
Fixed Fields
```

---

## PydanticOutputParser

```text
Output:
Validated Object

Use:
Production Apps
Agents
APIs
```

---

# Real Project Mapping

## Resume Analyzer

```text
Resume
 ↓
LLM
 ↓
PydanticOutputParser
 ↓
Skills
Weaknesses
Score
```

---

## Startup Evaluator

```text
Idea
 ↓
LLM
 ↓
JSON
 ↓
Risk Score
Market Score
```

---

## AI Agent

```text
User Query
 ↓
LLM
 ↓
Action JSON
 ↓
Tool Execution
```

---

# Must Remember

```text
StrOutputParser
=
String
```

---

```text
JsonOutputParser
=
JSON
```

---

```text
StructuredOutputParser
=
Schema Based JSON
```

---

```text
PydanticOutputParser
=
Validated Object
```

---

# Interview Revision

## Why Output Parsers?

Convert raw LLM responses into structured, usable outputs.

---

## Simplest Output Parser?

```text
StrOutputParser
```

---

## Which parser returns JSON?

```text
JsonOutputParser
```

---

## Which parser provides schema enforcement?

```text
StructuredOutputParser
```

---

## Most production-ready parser?

```text
PydanticOutputParser
```

---

## Structured Output vs Output Parser?

```text
Structured Output
=
Model follows schema

Output Parser
=
Parser enforces schema
```

---

# One Line Summary

```text
Output Parsers transform messy AI responses into predictable data that software can actually use.
```

---

# The One Diagram To Remember

```text
Prompt
 ↓
LLM
 ↓
Raw Output
 ↓
Parser
 ↓
Clean Output
```
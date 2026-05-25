# LangChain Output Parsers

## Keywords

- Output Parser
- StrOutputParser
- JsonOutputParser
- StructuredOutputParser
- PydanticOutputParser
- Format Instructions
- Schema Validation

---

# Why Output Parsers?

Problem:

```text
LLM
↓
Unpredictable Text
```

Example:

```text
The candidate has Python, React and SQL skills.
```

Hard to use in:

```text
Databases
APIs
Agents
Applications
```

---

Solution:

```text
LLM
↓
Output Parser
↓
Structured Output
```

---

# StrOutputParser

Simplest parser.

Used when:

```text
Need clean text only.
```

---

Example

```python
from langchain_core.output_parsers import StrOutputParser

parser = StrOutputParser()
```

---

Flow

```text
LLM
↓
Response Object
↓
StrOutputParser
↓
Plain String
```

---

Use Cases

```text
Blog Generation
Summaries
Content Creation
```

---

# JsonOutputParser

Forces JSON output.

---

Example

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

Advantages

```text
JSON format
Easy integration
```

---

Limitations

```text
No strict validation
No guaranteed schema
```

---

# StructuredOutputParser

Used when structure is predefined.

---

Example

```json
{
  "name": "",
  "age": ""
}
```

---

Output must follow:

```text
Defined Keys
Defined Structure
```

---

Advantages

```text
More control
Consistent responses
```

---

# PydanticOutputParser

Most powerful parser.

---

Example

```python
from pydantic import BaseModel

class Person(BaseModel):
    name: str
    age: int
```

---

Parser

```python
from langchain.output_parsers import PydanticOutputParser

parser = PydanticOutputParser(
    pydantic_object=Person
)
```

---

Advantages

```text
Validation
Type Checking
Error Handling
Schema Enforcement
```

---

Example

Input:

```json
{
  "name": "Somay",
  "age": "21"
}
```

Output:

```python
Person(
    name="Somay",
    age=21
)
```

---

# Parser Comparison

## StrOutputParser

Output:

```text
String
```

Use:

```text
Text generation
```

---

## JsonOutputParser

Output:

```json
{}
```

Use:

```text
Basic structured data
```

---

## StructuredOutputParser

Output:

```json
{}
```

Use:

```text
Fixed schema
```

---

## PydanticOutputParser

Output:

```python
Object
```

Use:

```text
Production applications
Agents
APIs
```

---

# Structured Output vs Output Parser

## Structured Output

```python
llm.with_structured_output(...)
```

Works best with:

```text
GPT
Claude
Gemini
```

---

## Output Parser

```python
parser = ...
```

Works with:

```text
Almost any model
```

Especially useful for:

```text
Open Source Models
Local Models
TinyLlama
```

---

# Real Use Cases

## Resume Analyzer

Output:

```json
{
  "skills": [],
  "score": 90
}
```

---

## Startup Validator

Output:

```json
{
  "market_score": 8,
  "risk_score": 5
}
```

---

## AI Agent

Output:

```json
{
  "action": "search",
  "query": "LangGraph tutorial"
}
```

Tool can directly consume it.

---

# Interview Revision

Q: Why Output Parsers?

A:

```text
Convert raw LLM responses into structured usable formats.
```

---

Q: Simplest Output Parser?

A:

```text
StrOutputParser
```

---

Q: Which parser returns JSON?

A:

```text
JsonOutputParser
```

---

Q: Which parser provides schema enforcement?

A:

```text
StructuredOutputParser
```

---

Q: Most robust parser?

A:

```text
PydanticOutputParser
```

---

Q: Structured Output vs Output Parser?

A:

```text
Structured Output:
Model does the structuring.

Output Parser:
Parser enforces structure after generation.
```

---

# Must Remember

```text
Prompt
↓
Model
↓
Output Parser
↓
Clean Data
```

---

# One Line Summary

```text
Structured Output =
Model knows schema

Output Parser =
Parser forces schema
```

This video is important because later when you use Ollama, local models, MCP, and Agents, you'll frequently fall back to Output Parsers when native structured output isn't available.

# Tools in LangChain

## Why Do We Need Tools?

LLMs are smart.

But by themselves they cannot:

```text
Access Internet
Run Terminal Commands
Use APIs
Read Current Weather
Search Databases
Send Emails
```

---

Without tools:

```text
User:
What's the weather in Delhi?

LLM:
I don't know current weather.
```

---

Tools solve this.

---

# What is a Tool?

A Tool is simply:

```text
A function the AI can use.
```

---

Example

```python
def calculator(a, b):
    return a + b
```

This can become a tool.

---

# Core Idea

Instead of:

```text
LLM does everything
```

we do:

```text
LLM
+
External Functions
```

---

# Mental Model

```text
LLM
=
Brain
```

```text
Tools
=
Hands
```

---

# Basic Flow

```text
User Question
 ↓
LLM
 ↓
Use Tool
 ↓
Tool Output
 ↓
LLM
 ↓
Answer
```

---

# Example

Question:

```text
What is 786 * 234?
```

---

Without Tool

LLM may hallucinate.

---

With Calculator Tool

```text
Question
 ↓
Calculator Tool
 ↓
Correct Result
 ↓
LLM
 ↓
Answer
```

---

# Why Tools Matter

Tools give AI:

```text
Real Actions
Real Data
External Access
```

---

Without tools:

```text
Only Text Generation
```

---

With tools:

```text
Action Taking
```

---

# Types Of Tools

## Calculator Tool

```text
Math Operations
```

---

## Search Tool

```text
Web Search
```

---

## Database Tool

```text
Retrieve Company Data
```

---

## File Tool

```text
Read Files
```

---

## Terminal Tool

```text
Run Commands
```

---

## API Tool

```text
Call External Services
```

---

# Creating a Tool

## Using @tool Decorator

---

Import

```python
from langchain_core.tools import tool
```

---

Example

```python
@tool
def multiply(a:int, b:int):
    return a * b
```

---

Now AI can use:

```text
multiply()
```

as a tool.

---

# Tool Structure

A tool usually has:

```text
Name
Description
Input
Output
```

---

Example

```python
@tool
def weather(city:str):
    """
    Get current weather of a city.
    """
```

---

The description is VERY important.

Because the LLM reads it to understand:

```text
When should I use this tool?
```

---

# Tool Input

Example:

```python
multiply(5, 7)
```

---

Tool receives:

```text
Arguments
```

and returns:

```text
Output
```

---

# Tool Output

Example:

```python
35
```

---

Flow

```text
Question
 ↓
Tool
 ↓
Output
 ↓
LLM
```

---

# Tools Are Just Functions

Most important realization.

---

A tool is not magic.

It is:

```text
Python Function
+
LLM Access
```

---

# Real Examples

## Weather Bot

```text
Question
 ↓
Weather API Tool
 ↓
Weather Data
 ↓
LLM
 ↓
Answer
```

---

## Portfolio Assistant

```text
Question
 ↓
RAG Retrieval Tool
 ↓
Relevant Chunks
 ↓
LLM
```

---

## Terminal Agent

```text
Question
 ↓
Git Tool
 ↓
Terminal Command
 ↓
LLM Explanation
```

---

# Tools vs RAG

## RAG

```text
Retrieve Knowledge
```

---

## Tools

```text
Perform Actions
```

---

Example

### RAG

```text
What is Git?
```

↓

Retrieve docs.

---

### Tool

```text
Undo git add
```

↓

Run terminal command.

---

# Important Difference

RAG gives:

```text
Context
```

---

Tools give:

```text
Capabilities
```

---

# Tool Calling Preview

This video teaches:

```text
What tools are
```

Next video teaches:

```text
How AI decides which tool to use
```

---

# Real Agent Flow

Later in Agents:

```text
User
 ↓
Think
 ↓
Choose Tool
 ↓
Observe Result
 ↓
Choose Another Tool
 ↓
Answer
```

---

# Must Remember

```text
Tool
=
Function AI Can Use
```

---

```text
LLM
=
Brain
```

---

```text
Tools
=
Actions / Capabilities
```

---

```text
RAG
=
Knowledge
```

---

```text
Tools
=
Actions
```

---

# Interview Revision

## What is a Tool?

A function that an LLM can access and use.

---

## Why do we need Tools?

LLMs cannot access real-time data or external systems by themselves.

---

## Are tools AI models?

No.

Tools are usually normal functions or APIs.

---

## Why are descriptions important?

The LLM uses descriptions to decide when to use tools.

---

## Difference Between RAG and Tools?

```text
RAG
=
Retrieve Information

Tools
=
Perform Actions
```

---

# One Line Summary

```text
Tools extend LLMs by giving them access to external functions, APIs and real-world actions.
```

---

# The One Diagram To Remember

```text
User Question
 ↓
LLM
 ↓
Tool
 ↓
External Action / Data
 ↓
LLM
 ↓
Answer
```

---

# The Journey So Far

```text
RAG
=
How AI knows things

Tools
=
How AI does things
```

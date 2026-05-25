# Day 2 — Prompts

## What is a Prompt?

A prompt is the instruction given to the model.

```text
User Input
    ↓
 Prompt
    ↓
 Model
    ↓
 Response
```

The quality of the output heavily depends on the quality of the prompt.

---

# Why Prompts Matter?

Same model.

Different prompt.

Different result.

Example:

```text
Explain AI.
```

vs

```text
Explain AI to a 10-year-old in less than 100 words.
```

---

# Static Prompt

Hardcoded prompt.

```python
prompt = """
Explain Machine Learning.
"""
```

Problems:

```text
Not reusable
Cannot handle user input
Not scalable
```

---

# Dynamic Prompt

Uses variables.

```python
topic = "Machine Learning"

prompt = f"""
Explain {topic}
"""
```

Better.

Still not ideal.

---

# PromptTemplate

LangChain's way of creating reusable prompts.

```python
from langchain_core.prompts import PromptTemplate

prompt = PromptTemplate(
    template="""
    Explain {topic} in simple words.
    """,
    input_variables=["topic"]
)

formatted_prompt = prompt.invoke({
    "topic": "LangChain"
})

print(formatted_prompt)
```

---

# Why PromptTemplate?

```text
Reusable
Cleaner
Variable Validation
LangChain Integration
```

---

# PromptTemplate Flow

```text
Template
 +
Variables
      ↓
Formatted Prompt
      ↓
LLM
```

---

# Chat Models Use Messages

Modern models don't just receive text.

They receive messages.

```text
System
Human
AI
```

---

# System Message

Controls behaviour.

Example:

```text
You are a helpful coding mentor.
```

---

Code:

```python
from langchain_core.messages import SystemMessage

SystemMessage(
    content="You are a helpful coding mentor."
)
```

---

# Human Message

Represents user input.

Example:

```text
What is RAG?
```

Code:

```python
from langchain_core.messages import HumanMessage

HumanMessage(
    content="What is RAG?"
)
```

---

# AI Message

Represents model response.

Example:

```text
RAG stands for Retrieval Augmented Generation...
```

Code:

```python
from langchain_core.messages import AIMessage

AIMessage(
    content="RAG stands for..."
)
```

---

# Message Flow

```text
System Message
        ↓
Human Message
        ↓
AI Message
```

---

# ChatPromptTemplate

PromptTemplate for conversations.

Used when building chat applications.

---

Example

```python
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI tutor."),
    ("human", "{question}")
])

formatted_prompt = prompt.invoke({
    "question": "What is LangChain?"
})
```

---

# Why ChatPromptTemplate?

Because chat applications contain:

```text
Multiple Messages
Roles
Variables
Conversation Flow
```

---

# MessagesPlaceholder

Used for chat history.

Allows previous conversations to be inserted dynamically.

---

Example

```python
from langchain_core.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    MessagesPlaceholder("chat_history"),
    ("human", "{question}")
])
```

---

# MessagesPlaceholder Flow

```text
Old Messages
      ↓
MessagesPlaceholder
      ↓
Prompt
      ↓
Model
```

---

# Real Use Cases

## Resume Analyzer

```text
PromptTemplate
```

```text
Analyze this resume:
{resume}
```

---

## AI Tutor

```text
ChatPromptTemplate
```

```text
System:
You are a tutor.

Human:
Explain recursion.
```

---

## Customer Support Bot

```text
MessagesPlaceholder
```

Used to remember previous conversation.

---

# Must Remember

```text
Static Prompt
=
Hardcoded Prompt
```

```text
Dynamic Prompt
=
Prompt + Variables
```

```text
PromptTemplate
=
Reusable Dynamic Prompt
```

```text
System Message
=
Model Behaviour
```

```text
Human Message
=
User Input
```

```text
AI Message
=
Model Response
```

```text
ChatPromptTemplate
=
PromptTemplate for Chat
```

```text
MessagesPlaceholder
=
Chat History
```

---

# Interview Revision

## Why PromptTemplate?

```text
Reusable
Dynamic
Validates Inputs
```

---

## PromptTemplate vs ChatPromptTemplate?

```text
PromptTemplate
→ Single Text Prompt

ChatPromptTemplate
→ Multiple Messages
```

---

## Purpose of System Message?

Defines model behaviour and rules.

---

## Purpose of MessagesPlaceholder?

Injects conversation history dynamically.

---

## Why are prompts important?

Because LLM output is highly dependent on the instructions provided.

---

# One Line Summary

```text
Prompts tell the model what to do;
PromptTemplates make prompts reusable;
ChatPromptTemplates make conversations possible.
```
# LangChain Prompts

## Keywords

- Prompt
- Static Prompt
- Dynamic Prompt
- PromptTemplate
- SystemMessage
- HumanMessage
- AIMessage
- ChatPromptTemplate
- MessagesPlaceholder

---

## PromptTemplate

### Without Template

```python
query = "Tell me about India"

prompt = f"""
Answer the following:
{query}
"""
```

### With Template

```python
from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    template="Answer the following: {query}",
    input_variables=["query"]
)

prompt = template.invoke({
    "query": "Tell me about India"
})
```

---

## System Message

```python
from langchain_core.messages import SystemMessage

SystemMessage(
    content="You are a helpful assistant"
)
```

Controls:

- behaviour
- personality
- rules

---

## Human Message

```python
from langchain_core.messages import HumanMessage

HumanMessage(
    content="What is LangChain?"
)
```

Represents user input.

---

## AI Message

```python
from langchain_core.messages import AIMessage

AIMessage(
    content="LangChain is a framework..."
)
```

Represents model response.

---

## ChatPromptTemplate

```python
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant"),
    ("human", "{question}")
])

prompt.invoke({
    "question": "What is RAG?"
})
```

Used for chat applications.

---

## MessagesPlaceholder

```python
from langchain_core.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder
)
```

```python
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant"),
    MessagesPlaceholder("chat_history"),
    ("human", "{question}")
])
```

Used to inject conversation history.

---

# Meanings

## Static Prompt

Hardcoded prompt.

```text
Prompt fixed in code.
```

---

## Dynamic Prompt

Prompt generated using variables.

```text
Changes based on user input.
```

---

## PromptTemplate

Template for creating dynamic prompts.

Benefits:

- Reusable
- Validation
- Cleaner code
- LangChain integration

---

## System Message

Defines assistant behaviour.

Example:

```text
You are a coding mentor.
```

---

## Human Message

Represents what user says.

---

## AI Message

Represents what model replies.

---

## ChatPromptTemplate

PromptTemplate for conversations.

Produces multiple messages instead of one string.

---

## MessagesPlaceholder

Placeholder for chat history.

Allows memory/context in conversations.

---

# Interview Revision

Q: Why not use static prompts?

A:

```text
Not reusable.
Hard to maintain.
Poor user experience.
```

---

Q: Why PromptTemplate?

A:

```text
Dynamic prompts.
Input validation.
Reusable.
Integrates with LangChain.
```

---

Q: Difference between PromptTemplate and ChatPromptTemplate?

A:

```text
PromptTemplate -> single text prompt

ChatPromptTemplate -> list of chat messages
```

---

Q: Why MessagesPlaceholder?

A:

```text
Inject chat history dynamically.
Maintain conversation context.
```
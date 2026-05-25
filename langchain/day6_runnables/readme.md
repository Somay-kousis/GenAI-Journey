# Day 6 — Runnables

## Why Runnables?

Before Runnables, every LangChain component behaved differently.

```python
model.call()
prompt.format()
chain.run()
```

Different APIs.

Different methods.

Confusing.

---

Runnables solve this.

Everything follows one interface.

```text
Input
 ↓
Runnable
 ↓
Output
```

---

# What is a Runnable?

A Runnable is the fundamental building block in LangChain.

Anything that:

```text
Receives Input
Processes Input
Returns Output
```

can be treated as a Runnable.

---

Examples

```text
PromptTemplate
ChatPromptTemplate
LLM
Parser
Chain
```

are all Runnables.

---

# Runnable Flow

```text
Prompt
 ↓
LLM
 ↓
Parser
```

Each block is a Runnable.

---

# Common Methods

## invoke()

Single input.

```python
response = chain.invoke(
    {"topic": "RAG"}
)
```

---

Flow

```text
One Input
 ↓
One Output
```

---

## batch()

Multiple inputs.

```python
responses = chain.batch([
    {"topic": "RAG"},
    {"topic": "LangChain"},
    {"topic": "Agents"}
])
```

---

Flow

```text
Input 1
Input 2
Input 3
   ↓
 Process Together
   ↓
Outputs
```

---

## stream()

Streams output token-by-token.

```python
for chunk in chain.stream(
    {"topic": "RAG"}
):
    print(chunk)
```

---

Flow

```text
LLM
 ↓
Token
Token
Token
```

---

Useful for:

```text
ChatGPT-like UIs
Real-time streaming
```

---

# Why Runnables Matter?

Because now everything can be connected.

---

Without Runnables

```text
Different APIs
Different Logic
```

---

With Runnables

```text
Same Interface

invoke()
batch()
stream()
```

everywhere.

---

# Runnable Pipeline

```python
chain = prompt | llm | parser
```

---

Visual

```text
Runnable
 ↓
Runnable
 ↓
Runnable
```

---

This is the foundation of LCEL.

---

# Mental Model

Think of Runnables as LEGO blocks.

```text
Runnable
Runnable
Runnable
Runnable
```

You connect them together.

---

# Runnable Types

## RunnableSequence

Sequential execution.

---

Flow

```text
A
 ↓
B
 ↓
C
```

---

Output of A becomes input of B.

Output of B becomes input of C.

---

Equivalent To

```python
a(b(c()))
```

idea.

---

Use Cases

```text
Generate
 ↓
Improve
 ↓
Summarize
```

---

# RunnableParallel

Run multiple tasks simultaneously.

---

Flow

```text
Input
 ↓

Notes
Quiz
Summary

 ↓

Combined Result
```

---

Code Idea

```python
RunnableParallel(
    notes=notes_chain,
    quiz=quiz_chain
)
```

---

Benefits

```text
Faster
Independent Tasks
```

---

# RunnablePassthrough

Returns input unchanged.

---

Flow

```text
Input
 ↓
Same Input
```

---

Example

```python
RunnablePassthrough()
```

---

Useful when:

```text
Need original data later
```

---

Example

```text
Question
 ↓
Keep Original
 ↓
Pass To LLM
```

---

# RunnableLambda

Wrap custom Python logic.

---

Example

```python
def clean_text(text):
    return text.lower()

RunnableLambda(clean_text)
```

---

Flow

```text
Input
 ↓
Custom Function
 ↓
Output
```

---

Useful for:

```text
Preprocessing
Postprocessing
API Calls
Filtering
Transformations
```

---

# RunnableBranch

Adds decision making.

---

Acts like:

```python
if
elif
else
```

---

Flow

```text
Input
 ↓
Condition
 ↓

Path A
or
Path B
```

---

Example

```text
Feedback
 ↓

Positive?
 │
 ├─ Yes
 │    ↓
 │ Thank User
 │
 └─ No
      ↓
   Apologize
```

---

Use Cases

```text
Routing
Classification
Agents
Support Bots
```

---

# Relationship With Chains

Most chains are built from Runnables.

---

Simple Chain

```text
Prompt
 ↓
LLM
 ↓
Parser
```

---

Actually:

```text
Runnable
 ↓
Runnable
 ↓
Runnable
```

---

# Real Project Mapping

## Resume Analyzer

```text
Prompt
 ↓
LLM
 ↓
Pydantic Parser
```

All are Runnables.

---

## Study Assistant

```text
Document
 ↓

Notes
Quiz
Flashcards

 ↓

Merge
```

RunnableParallel.

---

## Customer Support

```text
Message
 ↓
Sentiment Check
 ↓
Branch
```

RunnableBranch.

---

# Must Remember

```text
Runnable
=
Input → Output
```

---

```text
invoke()
=
Single Input
```

---

```text
batch()
=
Multiple Inputs
```

---

```text
stream()
=
Token Streaming
```

---

```text
RunnableSequence
=
Sequential Flow
```

---

```text
RunnableParallel
=
Parallel Flow
```

---

```text
RunnablePassthrough
=
Keep Original Input
```

---

```text
RunnableLambda
=
Custom Python Logic
```

---

```text
RunnableBranch
=
If Else Logic
```

---

# Interview Revision

## What is a Runnable?

A standardized LangChain component that processes input and produces output.

---

## Why were Runnables introduced?

To provide a common interface across LangChain components.

---

## Most Important Runnable Methods?

```python
invoke()
batch()
stream()
```

---

## Difference Between RunnableSequence and RunnableParallel?

```text
Sequence:
One after another

Parallel:
Run simultaneously
```

---

## Purpose of RunnablePassthrough?

Keep original input unchanged.

---

## Purpose of RunnableLambda?

Run custom Python functions inside workflows.

---

## Purpose of RunnableBranch?

Conditional routing.

---

# One Line Summary

```text
Runnables are the universal building blocks of LangChain; everything eventually becomes a Runnable.
```

---

# The One Diagram To Remember

```text
Input
 ↓
Runnable
 ↓
Runnable
 ↓
Runnable
 ↓
Output
```

Everything in LangChain eventually reduces to this.V
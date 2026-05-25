# Day 5 — Chains

## What is a Chain?

A Chain is a pipeline where the output of one step becomes the input of the next step.

---

Without Chain

```text
Prompt
 ↓
LLM
 ↓
Output

(Manually pass output)

 ↓

Prompt
 ↓
LLM
 ↓
Output
```

Lots of manual work.

---

With Chain

```text
Prompt
 ↓
LLM
 ↓
Parser
 ↓
Output
```

Everything connected automatically.

---

# Why Chains?

Chains help combine multiple AI operations into a single workflow.

Benefits:

```text
Cleaner Code
Reusable Logic
Complex Workflows
Less Boilerplate
```

---

# LCEL

LangChain Expression Language

Allows chaining using:

```python
|
```

(pipe operator)

---

# Basic Chain

```python
chain = prompt | llm | parser
```

Flow:

```text
Prompt
 ↓
LLM
 ↓
Parser
```

---

Invoke

```python
response = chain.invoke({
    "topic": "LangChain"
})
```

---

# Visualizing LCEL

Instead of:

```python
prompt_value = prompt.invoke(...)
response = llm.invoke(prompt_value)
final = parser.invoke(response)
```

Use:

```python
chain = prompt | llm | parser
```

Cleaner.

---

# 1. Simple Chain

Single straight pipeline.

---

Flow

```text
Input
 ↓
Prompt
 ↓
LLM
 ↓
Parser
 ↓
Output
```

---

Example

```text
Topic
 ↓
Generate Explanation
 ↓
Return Text
```

---

Code

```python
chain = prompt | llm | StrOutputParser()
```

---

# 2. Sequential Chain

Multiple LLM steps.

---

Flow

```text
Input
 ↓
Generate Report
 ↓
Summarize Report
 ↓
Final Output
```

---

Visual

```text
LLM 1
 ↓
LLM 2
 ↓
LLM 3
```

---

Example

```text
Blog Topic
 ↓
Generate Blog
 ↓
Summarize Blog
```

---

Use Cases

```text
Research Assistant
Content Generation
Report Generation
```

---

# 3. Parallel Chain

Run multiple chains simultaneously.

---

Component

```python
RunnableParallel
```

---

Flow

```text
Document
      ↓
 ┌────┼────┐
 ↓    ↓    ↓
Notes Quiz Summary
      ↓
 Merge
```

---

Example

Input:

```text
Chapter
```

Outputs:

```text
Notes
Quiz
Flashcards
```

at the same time.

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

# 4. Conditional Chain

Adds decision making.

---

Component

```python
RunnableBranch
```

---

Flow

```text
Input
 ↓
Condition
 ↓
Route
```

---

Visual

```text
Feedback
 ↓

Positive?
  │
 ├── Yes
 │      ↓
 │  Thank User
 │
 └── No
        ↓
     Apologize
```

---

Example

```text
Customer Support
```

Different response depending on sentiment.

---

Use Cases

```text
Routing
Classification
Customer Support
Agents
```

---

# Chain Types Summary

## Simple

```text
A → B → C
```

---

## Sequential

```text
LLM → LLM → LLM
```

---

## Parallel

```text
      Input
         ↓
   A    B    C
         ↓
      Merge
```

---

## Conditional

```text
Input
 ↓
Decision
 ↓
Route
```

---

# Real Project Mapping

## Resume Analyzer

```text
Simple Chain
```

```text
Resume
 ↓
Prompt
 ↓
LLM
 ↓
Parser
```

---

## Blog Generator

```text
Sequential Chain
```

```text
Topic
 ↓
Write Blog
 ↓
Summarize Blog
```

---

## Study Assistant

```text
Parallel Chain
```

```text
Chapter
 ↓
Notes
Quiz
Flashcards
```

---

## Customer Support Bot

```text
Conditional Chain
```

```text
Feedback
 ↓
Positive/Negative
 ↓
Different Response
```

---

# Must Remember

```text
Chain
=
Pipeline
```

---

```text
Prompt
 ↓
LLM
 ↓
Parser
```

is a

```text
Simple Chain
```

---

```text
LLM
 ↓
LLM
 ↓
LLM
```

is a

```text
Sequential Chain
```

---

```text
Input
 ↓
Multiple Tasks
 ↓
Merge
```

is a

```text
Parallel Chain
```

---

```text
Input
 ↓
Decision
 ↓
Route
```

is a

```text
Conditional Chain
```

---

# Interview Revision

## What is a Chain?

A workflow where the output of one component becomes the input of another.

---

## What is LCEL?

LangChain Expression Language.

Uses:

```python
|
```

to connect components.

---

## Sequential vs Parallel?

```text
Sequential:
One after another

Parallel:
Run simultaneously
```

---

## Which component enables parallel execution?

```python
RunnableParallel
```

---

## Which component enables decision making?

```python
RunnableBranch
```

---

# One Line Summary

```text
Chains connect multiple AI operations into a single reusable workflow.
```

---

# The One Diagram To Remember

```text
Input
 ↓
Prompt
 ↓
LLM
 ↓
Parser
 ↓
Output
```

Everything else (Sequential, Parallel, Conditional) is just a more advanced version of this.
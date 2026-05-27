# Tool Calling

## What is Tool Calling?

Tools alone are not enough.

The AI must also decide:

```text
Which tool should I use?
```

This decision-making process is called:

```text
Tool Calling
```

---

# Before Tool Calling

Without Tool Calling:

```text
User
 ↓
Developer manually selects tool
 ↓
Tool runs
```

---

# After Tool Calling

```text
User
 ↓
LLM decides tool
 ↓
Tool runs
 ↓
LLM answers
```

---

# Core Idea

The LLM becomes capable of:

```text
Understanding Intent
Choosing Tools
Passing Correct Inputs
Using Outputs
```

---

# Example

Question:

```text
What is 45 * 19?
```

---

LLM thinks:

```text
Math Problem
 ↓
Use Calculator Tool
```

---

Flow

```text
User
 ↓
LLM
 ↓
Calculator Tool
 ↓
Result
 ↓
LLM
 ↓
Answer
```

---

# Another Example

Question:

```text
What's the weather in Delhi?
```

---

LLM thinks:

```text
Need real-time data
 ↓
Use Weather Tool
```

---

# Mental Model

```text
Tool
=
Capability
```

---

```text
Tool Calling
=
Choosing Capability
```

---

# Why Tool Calling Matters

Without tool calling:

```text
Static Systems
```

---

With tool calling:

```text
Dynamic Systems
```

The AI can adapt based on user intent.

---

# Main Components

## LLM

Understands question.

---

## Tool

Performs action.

---

## Tool Calling Logic

Determines:

```text
Which tool?
What input?
```

---

# Flow

```text
Question
 ↓
LLM decides tool
 ↓
Tool executes
 ↓
Output returned
 ↓
LLM creates final response
```

---

# Tool Binding

Tools are attached to the model.

---

Example

```python
llm_with_tools = llm.bind_tools(
    [calculator, weather]
)
```

---

Meaning:

```text
LLM now knows available tools.
```

---

# Important Realization

The model does NOT automatically know tools.

You must provide them.

---

# Tool Descriptions Matter

Example

```python
@tool
def weather(city:str):
    """
    Get current weather for a city.
    """
```

---

The LLM reads descriptions to decide:

```text
Should I use this tool?
```

---

Bad description:

```text
do weather stuff
```

😭

---

Good description:

```text
Get current weather information
for a given city.
```

---

# Tool Call Output

When the LLM chooses a tool:

```text
It does not answer immediately.
```

It first returns:

```text
Tool Name
Arguments
```

---

Example

```json
{
  "tool": "calculator",
  "args": {
    "a": 45,
    "b": 19
  }
}
```

---

Then:

```text
Tool executes
 ↓
Result returned
```

---

# Tool Result

Example

```text
855
```

---

Now LLM responds:

```text
45 * 19 = 855
```

---

# Multi Tool Scenarios

Question:

```text
What's the weather in Delhi
and convert 30°C to Fahrenheit?
```

---

Possible flow:

```text
Weather Tool
 ↓
Calculator Tool
 ↓
Final Response
```

---

This is why tool calling becomes powerful.

---

# Difference Between Tools and Tool Calling

## Tools

```text
What AI CAN use
```

---

## Tool Calling

```text
How AI CHOOSES what to use
```

---

# Tool Calling vs Agents

## Tool Calling

Usually:

```text
One Decision
```

---

Example

```text
Question
 ↓
Choose Tool
 ↓
Answer
```

---

## Agent

```text
Multiple Decisions
Reasoning Loop
```

---

Example

```text
Think
 ↓
Tool
 ↓
Observe
 ↓
Think Again
 ↓
Another Tool
```

---

# Real Examples

## Portfolio Assistant

Question:

```text
What projects has Somay built?
```

---

LLM decides:

```text
Use Retrieval Tool
```

---

## Terminal Assistant

Question:

```text
Undo git add
```

---

LLM decides:

```text
Use Git Tool
```

---

## Startup Research Agent

Question:

```text
Find startups similar to Mutiny
```

---

LLM decides:

```text
Use Search Tool
```

---

# Common Problems

## Wrong Tool Selection

Bad descriptions confuse model.

---

## Wrong Arguments

Model may send:

```text
Missing parameters
Wrong formats
```

---

## Hallucinated Tools

Sometimes model tries using:

```text
Nonexistent Tool
```

---

# Why Tool Calling Feels Powerful

Because this is the first time AI starts feeling like:

```text
Software interacting with software
```

instead of:

```text
Text generator
```

---

# Must Remember

```text
Tool
=
Capability
```

---

```text
Tool Calling
=
Choosing Capability
```

---

```text
LLM decides:
- Which tool
- What input
```

---

```text
Descriptions are critical.
```

---

```text
Tool Calling
≠
Agent
```

---

# Interview Revision

## What is Tool Calling?

The process where an LLM selects and invokes tools based on user queries.

---

## Why are tool descriptions important?

The model uses them to determine when a tool should be used.

---

## What is bind_tools()?

Attaches tools to an LLM.

---

## Difference Between Tools and Tool Calling?

```text
Tools
=
Capabilities

Tool Calling
=
Decision Making
```

---

## Difference Between Tool Calling and Agents?

```text
Tool Calling
=
Single tool decisions

Agents
=
Multi-step reasoning and tool usage
```

---

# One Line Summary

```text
Tool Calling allows LLMs to intelligently select and use external tools based on user intent.
```

---

# The One Diagram To Remember

```text
Question
 ↓
LLM
 ↓
Choose Tool
 ↓
Tool Executes
 ↓
Result
 ↓
LLM
 ↓
Final Answer
```

---

# The Journey So Far

```text
RAG
=
Knowledge

Tools
=
Capabilities

Tool Calling
=
Choosing Capabilities
```

Next comes:

```text
Agents
```

where the AI repeatedly thinks, acts and reasons in loops.
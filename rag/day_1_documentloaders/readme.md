# Day 7 — Document Loaders

## Why Do We Need Document Loaders?

LLMs can only work with data they receive.

They cannot directly read:

```text
PDF
Word File
Website
YouTube Transcript
TXT File
CSV
```

---

Document Loaders solve this problem.

```text
File / Source
      ↓
Document Loader
      ↓
LangChain Documents
```

---

# What is a Document?

LangChain converts everything into a standard format.

A document contains:

```python
Document(
    page_content="actual text",
    metadata={}
)
```

---

Example

```python
Document(
    page_content="LangChain is a framework...",
    metadata={
        "source": "notes.pdf"
    }
)
```

---

# Structure of a Document

## page_content

Actual text.

```text
The information we want.
```

---

## metadata

Information about the document.

Example:

```python
{
    "source": "notes.pdf",
    "page": 5
}
```

---

# Document Loader Flow

```text
PDF
 ↓
Loader
 ↓
Document Objects
 ↓
Text Splitter
```

---

# Why Metadata Matters

Imagine:

```text
500 pages
```

Later during retrieval:

```text
Answer found
 ↓
Which page?
```

Metadata helps answer that.

---

# Common Loaders

## Text Loader

Loads:

```text
.txt
```

---

Import

```python
from langchain_community.document_loaders import TextLoader
```

---

Example

```python
loader = TextLoader("notes.txt")

docs = loader.load()
```

---

# PDF Loader

Loads:

```text
PDF Files
```

---

Import

```python
from langchain_community.document_loaders import PyPDFLoader
```

---

Example

```python
loader = PyPDFLoader("notes.pdf")

docs = loader.load()
```

---

Output

```text
One Document per page
```

usually.

---

# CSV Loader

Loads:

```text
CSV Files
```

---

Example

```python
from langchain_community.document_loaders import CSVLoader

loader = CSVLoader("data.csv")

docs = loader.load()
```

---

# WebBaseLoader

Loads websites.

---

Example

```python
from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader(
    "https://example.com"
)

docs = loader.load()
```

---

Flow

```text
Website
 ↓
HTML
 ↓
Text
 ↓
Documents
```

---

# Directory Loader

Load many files at once.

---

Example

```python
from langchain_community.document_loaders import DirectoryLoader

loader = DirectoryLoader(
    "./documents"
)

docs = loader.load()
```

---

Flow

```text
Folder
 ↓
Many Files
 ↓
Documents
```

---

# Lazy Loading

Normal Load

```python
docs = loader.load()
```

Loads everything immediately.

---

Lazy Load

```python
for doc in loader.lazy_load():
    print(doc)
```

Loads one document at a time.

---

Useful for:

```text
Large PDFs
Large Datasets
Memory Efficiency
```

---

# RAG Pipeline Position

Document Loaders are the first step.

```text
PDF
 ↓
Document Loader
 ↓
Documents
 ↓
Text Splitter
 ↓
Embeddings
 ↓
Vector Store
 ↓
Retriever
 ↓
LLM
```

---

# Real Examples

## Resume Analyzer

```text
Resume.pdf
 ↓
PyPDFLoader
 ↓
Document
```

---

## Chat With Notes

```text
Notes.pdf
 ↓
PyPDFLoader
 ↓
Documents
```

---

## Chat With Website

```text
Website URL
 ↓
WebBaseLoader
 ↓
Documents
```

---

# Must Remember

```text
Loader
=
Bring data into LangChain
```

---

```text
Document
=
page_content + metadata
```

---

```text
page_content
=
Actual text
```

---

```text
metadata
=
Information about source
```

---

```text
PDF
TXT
CSV
Website
Folder
```

all become:

```text
Document Objects
```

---

# Interview Revision

## Why Document Loaders?

To convert external data into LangChain Documents.

---

## What is inside a Document?

```python
page_content
metadata
```

---

## Purpose of Metadata?

Store source information.

Example:

```text
File Name
Page Number
URL
Author
```

---

## What does PyPDFLoader do?

Loads PDFs into LangChain Documents.

---

## What does WebBaseLoader do?

Loads website content into Documents.

---

## Why Lazy Loading?

Improves memory efficiency for large datasets.

---

# One Line Summary

```text
Document Loaders are the entry point of RAG; they convert external sources into LangChain Document objects.
```

---

# The One Diagram To Remember

```text
PDF / Website / TXT
          ↓
   Document Loader
          ↓
       Documents
          ↓
     page_content
       metadata
```
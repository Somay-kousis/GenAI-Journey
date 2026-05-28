# LangChain — One Shot Syntax & Imports Cheatsheet

> Theory you know. This is just the code muscle memory.

---

## DAY 1 — MODELS

### Chat Model (Groq)
```python
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.7)
response = model.invoke("Hello")
print(response.content)
```

### Chat Model (OpenAI)
```python
from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4o", temperature=0.5)
```

### Chat Model (Anthropic)
```python
from langchain_anthropic import ChatAnthropic

model = ChatAnthropic(model_name="claude-3-5-sonnet-20241022")
```

### Chat Model (HuggingFace — Remote)
```python
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

llm = HuggingFaceEndpoint(repo_id="google/gemma-2-2b-it", task="text-generation")
model = ChatHuggingFace(llm=llm)
```

### Chat Model (HuggingFace — Local)
```python
from langchain_huggingface import HuggingFacePipeline, ChatHuggingFace

llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs={"max_new_tokens": 100, "temperature": 0.5}
)
model = ChatHuggingFace(llm=llm)
```

### Chat Model (Ollama — Local)
```python
from langchain_ollama import ChatOllama

model = ChatOllama(model="llama3")
```

### Raw LLM (not chat)
```python
from langchain_openai import OpenAI

llm = OpenAI(model="gpt-3.5-turbo-instruct")
result = llm.invoke("Hey")         # returns string, not AIMessage
```

### Embedding Models
```python
# OpenAI
from langchain_openai import OpenAIEmbeddings
embedding = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=300)

# HuggingFace
from langchain_huggingface import HuggingFaceEmbeddings
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Usage
vector = embedding.embed_query("some text")          # single → list of floats
vectors = embedding.embed_documents(["text1", "text2"])  # batch → list of lists
```

### Cosine Similarity
```python
from sklearn.metrics.pairwise import cosine_similarity
scores = cosine_similarity([query_vector], doc_vectors)[0]
best_index = scores.argmax()
```

---

## DAY 2 — PROMPTS

### Messages (manual)
```python
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

chat_history = [
    SystemMessage(content="You are a helpful assistant"),
    HumanMessage(content="What is RAG?"),
    AIMessage(content="RAG stands for..."),
]
response = model.invoke(chat_history)
```

### PromptTemplate (single string)
```python
from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    template="Explain {topic} in simple words",
    input_variables=["topic"]
)
prompt = template.invoke({"topic": "LangChain"})   # → StringPromptValue
```

### Save & Load PromptTemplate
```python
template.save("template.json")

from langchain_core.prompts import load_prompt
template = load_prompt("template.json")
```

### ChatPromptTemplate
```python
from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate([
    ("system", "You are a helpful {domain} expert"),
    ("human", "Explain {topic}")
])
prompt = chat_template.invoke({"domain": "cricket", "topic": "Dusra"})
```

### MessagesPlaceholder (chat history injection)
```python
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

template = ChatPromptTemplate([
    ("system", "You are a customer support agent"),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{query}")
])
prompt = template.invoke({"chat_history": chat_history, "query": "Where is my refund?"})
```

---

## DAY 3 — STRUCTURED OUTPUT

### TypedDict
```python
from typing import TypedDict, Annotated, Optional, Literal

class Review(TypedDict):
    summary: Annotated[str, "Brief summary"]
    sentiment: Annotated[Literal["pos", "neg"], "Sentiment"]
    pros: Annotated[Optional[list[str]], "List of pros"]

structured_model = model.with_structured_output(Review)
result = structured_model.invoke("some text...")
print(result["summary"])
```

### Pydantic
```python
from pydantic import BaseModel, Field
from typing import Optional, Literal

class Review(BaseModel):
    summary: str = Field(description="Brief summary")
    sentiment: Literal["pos", "neg"] = Field(description="Sentiment")
    pros: Optional[list[str]] = Field(default=None, description="List of pros")

structured_model = model.with_structured_output(Review)
result = structured_model.invoke("some text...")
print(result.summary)          # dot access, not dict
```

### JSON Schema
```python
json_schema = {
    "title": "Review",
    "type": "object",
    "properties": {
        "summary": {"type": "string", "description": "Brief summary"},
        "sentiment": {"type": "string", "enum": ["pos", "neg"]},
        "pros": {"type": ["array", "null"], "items": {"type": "string"}}
    },
    "required": ["summary", "sentiment"]
}

structured_model = model.with_structured_output(json_schema)
result = structured_model.invoke("some text...")
print(result["summary"])       # dict access
```

### Pydantic Validators
```python
from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str = "default_name"
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0, lt=10, default=5.0, description="CGPA between 0 and 10")

student = Student(age="32", email="abc@gmail.com")   # age auto-converts str → int
student_dict = dict(student)
student_json = student.model_dump_json()
```

---

## DAY 4 — OUTPUT PARSERS

### StrOutputParser
```python
from langchain_core.output_parsers import StrOutputParser

parser = StrOutputParser()
chain = prompt | model | parser     # returns plain string
```

### JsonOutputParser
```python
from langchain_core.output_parsers import JsonOutputParser

parser = JsonOutputParser()

template = PromptTemplate(
    template="Give 5 facts about {topic}\n{format_instruction}",
    input_variables=["topic"],
    partial_variables={"format_instruction": parser.get_format_instructions()}
)
chain = template | model | parser
result = chain.invoke({"topic": "black holes"})  # → dict/list
```

### StructuredOutputParser
```python
from langchain_core.output_parsers import StructuredOutputParser, ResponseSchema

schema = [
    ResponseSchema(name="fact_1", description="First fact"),
    ResponseSchema(name="fact_2", description="Second fact"),
]
parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template="Give facts about {topic}\n{format_instruction}",
    input_variables=["topic"],
    partial_variables={"format_instruction": parser.get_format_instructions()}
)
chain = template | model | parser
result = chain.invoke({"topic": "black holes"})  # → {"fact_1": ..., "fact_2": ...}
```

### PydanticOutputParser
```python
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

class Person(BaseModel):
    name: str = Field(description="Name of the person")
    age: int = Field(gt=18, description="Age of the person")
    city: str = Field(description="City")

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template="Generate a fictional {place} person\n{format_instruction}",
    input_variables=["place"],
    partial_variables={"format_instruction": parser.get_format_instructions()}
)
chain = template | model | parser
result = chain.invoke({"place": "Japanese"})  # → Person object
print(result.name, result.age)
```

---

## DAY 5 — CHAINS

### Simple Chain
```python
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

chain = prompt | model | StrOutputParser()
result = chain.invoke({"topic": "cricket"})
```

### Sequential Chain
```python
prompt1 = PromptTemplate(template="Write a report on {topic}", input_variables=["topic"])
prompt2 = PromptTemplate(template="Summarize this in 5 points:\n{text}", input_variables=["text"])

chain = prompt1 | model | StrOutputParser() | prompt2 | model | StrOutputParser()
result = chain.invoke({"topic": "AI"})
```

### Parallel Chain
```python
from langchain_core.runnables import RunnableParallel

parallel_chain = RunnableParallel({
    "notes": prompt1 | model | StrOutputParser(),
    "quiz":  prompt2 | model | StrOutputParser()
})
result = parallel_chain.invoke({"text": "some document"})
print(result["notes"])
print(result["quiz"])
```

### Conditional Chain (RunnableBranch)
```python
from langchain_core.runnables import RunnableBranch, RunnableLambda

branch_chain = RunnableBranch(
    (lambda x: x.sentiment == "positive", positive_prompt | model | StrOutputParser()),
    (lambda x: x.sentiment == "negative", negative_prompt | model | StrOutputParser()),
    RunnableLambda(lambda x: "Could not determine sentiment")   # default
)

chain = classifier_chain | branch_chain
result = chain.invoke({"feedback": "Great product!"})
```

### Visualise chain
```python
chain.get_graph().print_ascii()
```

---

## DAY 6 — RUNNABLES

### RunnableSequence (explicit)
```python
from langchain_core.runnables import RunnableSequence

chain = RunnableSequence(prompt, model, parser)
# same as: chain = prompt | model | parser
```

### RunnableParallel
```python
from langchain_core.runnables import RunnableParallel, RunnableSequence

parallel = RunnableParallel({
    "tweet":    RunnableSequence(tweet_prompt, model, parser),
    "linkedin": RunnableSequence(li_prompt, model, parser)
})
result = parallel.invoke({"topic": "AI"})
```

### RunnablePassthrough
```python
from langchain_core.runnables import RunnablePassthrough, RunnableParallel

# Passes input unchanged to next step
parallel = RunnableParallel({
    "joke":        RunnablePassthrough(),       # keeps original joke text
    "explanation": prompt2 | model | parser     # processes it
})
chain = RunnableSequence(joke_gen_chain, parallel)
```

### RunnableLambda
```python
from langchain_core.runnables import RunnableLambda

def word_count(text):
    return len(text.split())

parallel = RunnableParallel({
    "joke":       RunnablePassthrough(),
    "word_count": RunnableLambda(word_count)
})
```

### RunnableBranch
```python
from langchain_core.runnables import RunnableBranch, RunnablePassthrough

branch = RunnableBranch(
    (lambda x: len(x.split()) > 300, summarise_prompt | model | parser),
    RunnablePassthrough()     # default: return as-is
)
```

### Invoke / Batch / Stream
```python
# Single input
result = chain.invoke({"topic": "AI"})

# Multiple inputs in parallel
results = chain.batch([
    {"topic": "AI"},
    {"topic": "ML"},
    {"topic": "DL"}
])

# Stream token by token
for chunk in chain.stream({"topic": "AI"}):
    print(chunk, end="", flush=True)
```

---

## DAY 7 — TOOLS

### @tool decorator (simplest)
```python
from langchain_core.tools import tool

@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""      # description is CRITICAL — LLM reads this
    return a * b

result = multiply.invoke({"a": 3, "b": 5})
print(multiply.name)
print(multiply.description)
print(multiply.args)
```

### StructuredTool
```python
from langchain.tools import StructuredTool
from pydantic import BaseModel, Field

class MultiplyInput(BaseModel):
    a: int = Field(description="First number")
    b: int = Field(description="Second number")

def multiply_func(a: int, b: int) -> int:
    return a * b

tool = StructuredTool.from_function(
    func=multiply_func,
    name="multiply",
    description="Multiply two numbers",
    args_schema=MultiplyInput
)
```

### BaseTool (class based)
```python
from langchain.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Type

class MultiplyInput(BaseModel):
    a: int = Field(description="First number")
    b: int = Field(description="Second number")

class MultiplyTool(BaseTool):
    name: str = "multiply"
    description: str = "Multiply two numbers"
    args_schema: Type[BaseModel] = MultiplyInput

    def _run(self, a: int, b: int) -> int:
        return a * b

tool = MultiplyTool()
result = tool.invoke({"a": 3, "b": 5})
```

### Toolkit (grouping tools)
```python
class MathToolkit:
    def get_tools(self):
        return [add, multiply, divide]

toolkit = MathToolkit()
tools = toolkit.get_tools()
```

### Bind tools to model (Tool Calling)
```python
llm_with_tools = model.bind_tools([multiply, add, search])
response = llm_with_tools.invoke("What is 45 * 19?")
# response may contain tool_calls, not a final answer yet
```

### Built-in Tools
```python
# DuckDuckGo search
from langchain_community.tools import DuckDuckGoSearchRun
search = DuckDuckGoSearchRun()
result = search.invoke("latest AI news")

# Shell / Terminal
from langchain_community.tools import ShellTool
shell = ShellTool()
result = shell.invoke("ls -la")
```

---

## RAG DAY 1 — DOCUMENT LOADERS

```python
# Text
from langchain_community.document_loaders import TextLoader
loader = TextLoader("file.txt", encoding="utf-8")

# PDF
from langchain_community.document_loaders import PyPDFLoader
loader = PyPDFLoader("file.pdf")

# CSV
from langchain_community.document_loaders import CSVLoader
loader = CSVLoader(file_path="data.csv")

# Website
from langchain_community.document_loaders import WebBaseLoader
loader = WebBaseLoader("https://example.com")

# Directory (all PDFs in a folder)
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
loader = DirectoryLoader(path="books/", glob="*.pdf", loader_cls=PyPDFLoader)

# Load styles
docs = loader.load()                    # loads everything into memory
for doc in loader.lazy_load(): ...      # memory-efficient, one at a time

# Every doc has:
print(docs[0].page_content)
print(docs[0].metadata)                 # {"source": "file.pdf", "page": 0}
```

---

## RAG DAY 2 — TEXT SPLITTERS

```python
# Recursive (most common — respects paragraph > sentence > word)
from langchain_text_splitters import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = splitter.split_documents(docs)    # takes Document list
chunks = splitter.split_text("raw string") # takes raw string

# Character (simpler, can break meaning)
from langchain_text_splitters import CharacterTextSplitter

splitter = CharacterTextSplitter(separator="\n", chunk_size=200, chunk_overlap=0)
chunks = splitter.split_documents(docs)

# Code-aware
from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,    # or Language.MARKDOWN, Language.JS etc.
    chunk_size=300,
    chunk_overlap=0
)
chunks = splitter.split_text(code_string)

# Semantic (splits on meaning change — needs embeddings)
from langchain_text_splitters import SemanticChunker
from langchain_openai.embeddings import OpenAIEmbeddings

splitter = SemanticChunker(
    OpenAIEmbeddings(),
    breakpoint_threshold_type="standard_deviation",
    breakpoint_threshold_amount=3
)
docs = splitter.create_documents([text])
```

---

## RAG DAY 3 — VECTOR STORES

```python
# Chroma (local, beginner-friendly)
from langchain_chroma import Chroma

vectorstore = Chroma.from_documents(documents=chunks, embedding=embedding_model)

# Persist to disk
vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embedding_model,
    persist_directory="./chroma_db"
)
# Load back
vectorstore = Chroma(persist_directory="./chroma_db", embedding_function=embedding_model)

# FAISS (fast, local, Meta)
from langchain_community.vectorstores import FAISS

vectorstore = FAISS.from_documents(chunks, embedding_model)
vectorstore.save_local("faiss_index")
# Load back
vectorstore = FAISS.load_local("faiss_index", embedding_model, allow_dangerous_deserialization=True)

# Similarity search (direct)
results = vectorstore.similarity_search("What is LangChain?", k=3)
results = vectorstore.similarity_search_with_score("query", k=3)  # includes score
```

---

## RAG DAY 4 — RETRIEVERS

```python
# Basic retriever from vector store
retriever = vectorstore.as_retriever()
docs = retriever.invoke("What is LangChain?")

# Similarity — top k
retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 3}
)

# Similarity with score threshold
retriever = vectorstore.as_retriever(
    search_type="similarity_score_threshold",
    search_kwargs={"score_threshold": 0.8, "k": 3}
)

# MMR — relevant AND diverse results
retriever = vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={"k": 5, "fetch_k": 20}
)

# Output is always list of Document objects
for doc in docs:
    print(doc.page_content)
    print(doc.metadata)
```

---

## RAG DAY 5 — FULL RAG PIPELINE

```python
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from dotenv import load_dotenv

load_dotenv()

# 1. Load
loader = PyPDFLoader("your_doc.pdf")
docs = loader.load()

# 2. Split
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = splitter.split_documents(docs)

# 3. Embed + Store
embedding = OpenAIEmbeddings()
vectorstore = Chroma.from_documents(chunks, embedding)

# 4. Retrieve
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

# 5. Prompt
prompt = ChatPromptTemplate([
    ("system", "Answer using the context below. If unsure, say so.\n\nContext:\n{context}"),
    ("human", "{question}")
])

# 6. Model + Parser
model = ChatOpenAI()
parser = StrOutputParser()

# 7. Chain it all
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | model
    | parser
)

answer = rag_chain.invoke("What is this document about?")
print(answer)
```

---

## COMMON GOTCHAS

```
TypedDict result   → dict access   result["key"]
Pydantic result    → dot access    result.key
JSON Schema result → dict access   result["key"]

PromptTemplate     → takes string template
ChatPromptTemplate → takes list of (role, template) tuples

embed_query()      → single text  → 1D list of floats
embed_documents()  → list of text → 2D list of floats

loader.load()       → everything at once  (memory heavy for big files)
loader.lazy_load()  → iterator            (memory efficient)

split_text()        → takes raw string
split_documents()   → takes Document list

chain.invoke()  → single input  → single output
chain.batch()   → list of inputs → list of outputs
chain.stream()  → single input  → iterator of chunks

@tool needs:  type hints + docstring   (both required, LLM reads docstring)
```

---

## QUICK IMPORT REFERENCE

```python
# Models
from langchain_openai import ChatOpenAI, OpenAI, OpenAIEmbeddings
from langchain_groq import ChatGroq
from langchain_anthropic import ChatAnthropic
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint, HuggingFacePipeline, HuggingFaceEmbeddings
from langchain_ollama import ChatOllama

# Prompts
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate, MessagesPlaceholder, load_prompt
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

# Parsers
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser, StructuredOutputParser, ResponseSchema, PydanticOutputParser

# Runnables
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableBranch, RunnableLambda

# Tools
from langchain_core.tools import tool
from langchain.tools import StructuredTool, BaseTool
from langchain_community.tools import DuckDuckGoSearchRun, ShellTool

# Loaders
from langchain_community.document_loaders import TextLoader, PyPDFLoader, CSVLoader, WebBaseLoader, DirectoryLoader

# Splitters
from langchain_text_splitters import RecursiveCharacterTextSplitter, CharacterTextSplitter, SemanticChunker, Language

# Vector Stores
from langchain_chroma import Chroma
from langchain_community.vectorstores import FAISS

# Pydantic
from pydantic import BaseModel, Field, EmailStr
from typing import Optional, Literal, Annotated, TypedDict
```

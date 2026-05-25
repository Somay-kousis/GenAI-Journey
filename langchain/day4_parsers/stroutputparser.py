from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatGroq(
    model="llama-3.3-70b-versatile"
)

template1 = PromptTemplate(
    template = "Write a detailed report on {topic}",
    input_variables=['topic']
)

template2 = PromptTemplate(
    template = "Write a 5 line summary on {text}",
    input_variables=['text']
)

prompt1 = template1.invoke({'topic': 'blackhole'})
result1 = model.invoke(prompt1)

prompt2 = template2.invoke({'text': result1.content})
result2 = model.invoke(prompt2)

print(result2.content)
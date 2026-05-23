from langchain_groq import ChatGroq

from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

model = ChatGroq(
    model="llama-3.3-70b-versatile"
)

response = model.invoke("Hello", temperature=1.2, max_completion_tokens=10 )
print(response)
print(response.content)
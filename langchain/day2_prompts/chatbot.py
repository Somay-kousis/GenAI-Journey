from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(
    model="llama-3.3-70b-versatile"
)

chat_history = []

while True:
    user_input = input('You:  ')
    chat_history.append(user_input)
    if (user_input == 'exit'):
        break
    result = model.invoke(chat_history)
    chat_history.append(result.content)
    print("AI: ",result.content)

from langchain_core.messages import SystemMessage,AIMessage,HumanMessage
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# LLM
load_dotenv()
model = ChatGroq(
    model="openai/gpt-oss-120b"
)
chat_history=[SystemMessage(content="You are A Helpful AI Assistant")]
while True:
    user_input=input("You: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input=="exit":
        break;
    result=model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI: ", result.content)
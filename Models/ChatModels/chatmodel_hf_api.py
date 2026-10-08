from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()
model = ChatGroq(
    model="openai/gpt-oss-120b"
)

result=model.invoke("Who is Deputy CM of Maharashtra")
print(result.content)
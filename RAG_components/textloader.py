

from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
loader = TextLoader("RAG_components/cricket.txt",encoding="utf-8")
# LLM
load_dotenv()
model = ChatGroq(
    model="openai/gpt-oss-120b"
)
docs=loader.load()
print(docs)

from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader


# LLM
load_dotenv()
model = ChatGroq(
    model="openai/gpt-oss-120b"
)
loader = PyPDFLoader("RAG_components/dl-curriculum.pdf")
docs=loader.load()
splitter=RecursiveCharacterTextSplitter(
    chunk_size=50,
    chunk_overlap=0
)
result=splitter.split_documents(docs)
print(f"Total pages: {len(result)}")


print(result[0].page_content)
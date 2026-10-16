from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document


documents =[
Document(page_content="LangChain helps developers build LLM applications easily."),
Document(page_content="Chroma is a vector database optimized for LLM-based search."),
Document(page_content="Embeddings convert text into high-dimensional vectors."),
Document(page_content="OpenAI provides powerful embedding models."),
]

embedding_model=HuggingFaceEmbeddings()
vectorestore=Chroma.from_documents(
    documents=documents,
    embedding=embedding_model,
    collection_name="my_collection"
)

retriver = vectorestore.as_retriever(search_kwargs={"k":2})
query="what is chroma used for"
result=retriver.invoke(query)

for i,doc in enumerate(result):
    print(f"\n---Result--{i+1}---")
    print(doc.page_content)
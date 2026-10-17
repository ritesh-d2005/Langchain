
from langchain_community.retrievers import WikipediaRetriever

print("Creating retriever...")

retriever = WikipediaRetriever(
    top_k_results=2,
    lang="en"
)

query = "geopolitical history of India and Pakistan from the perspective of China"


result = retriever.invoke(query)


for i, doc in enumerate(result):
    print(f"\n--- Result {i+1} ---")
    print("Content:", doc.page_content[:500])
    print("Metadata:", doc.metadata)
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# LLM
load_dotenv()
model = ChatGroq(
    model="openai/gpt-oss-120b"
)
prompt=PromptTemplate(
    template="Give 5 interesting facts about {topic}",
    input_variables=["topic"]
)
parser=StrOutputParser()
chain=prompt|model|parser
result=chain.invoke({"topic":"cricket"})
print(result)
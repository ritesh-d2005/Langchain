from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# LLM
load_dotenv()
model = ChatGroq(
    model="openai/gpt-oss-120b"
)
prompt1=PromptTemplate(
    template="Generate a Detailed report on {topic}",
    input_variables=["topic"]
)
parser=StrOutputParser()
prompt2=PromptTemplate(
    template="Extract 5 important point's from {text}",
    input_variables=["text"]
)  
chain=prompt1|model|parser|prompt2|model|parser
result=chain.invoke({"topic":"IT Sector in 2026"})
print(result)
chain.get_graph().print_ascii()
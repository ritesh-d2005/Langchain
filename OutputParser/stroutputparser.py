from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


# LLM
load_dotenv()
model = ChatGroq(
    model="openai/gpt-oss-120b"
)
parser=StrOutputParser()
template1=PromptTemplate(
    template="Write a detailde report on {topic}",
    input_variables=['topic']
)
template2=PromptTemplate(
    template="""Summarize the following text in EXACTLY 5 lines.
Each line must contain only one concise sentence.
Do not add an introduction or conclusion. {text}""",
    input_variables=['text']
)
chain=template1|model|parser|template2|model|parser
result=chain.invoke({'topic': "Black hole"})
print(result)


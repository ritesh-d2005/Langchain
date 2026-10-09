from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field


# LLM
load_dotenv()
model = ChatGroq(
    model="openai/gpt-oss-120b"
)


class Person(BaseModel):
    name:str=Field(description="Name of th Person")
    age:int=Field(description="Age of the person")
    city:str=Field(description="Name of the city")

parser=PydanticOutputParser(pydantic_object=Person)
template=PromptTemplate(
    template="Genenrate the name, age, city of a fictional {place} person {format_instruction}",
    input_variables=['place'],
    partial_variables={'format_instruction':parser.get_format_instructions()}

)
chain=template|model|parser
result=chain.invoke({"place":"Russia"})
print(result)
     
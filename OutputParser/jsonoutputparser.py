from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser


# LLM
load_dotenv()
model = ChatGroq(
    model="openai/gpt-oss-120b"
)
parser=JsonOutputParser()
template=PromptTemplate(
    template="Give me the name , age, city of fictional person {format_instruction}",
    input_variables=[],
    partial_variables={'format_instruction':parser.get_format_instructions()}

)
prompt=template.format()
result=model.invoke(prompt)
final_result=parser.parse(result.content)
print(final_result)
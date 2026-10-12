from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel,RunnableSequence,RunnablePassthrough
# LLM
load_dotenv()
model = ChatGroq(
    model="openai/gpt-oss-120b"
)
prompt1=PromptTemplate(
    template="Generate A joke about {topic}",
    input_variables=["topic"]
)
prompt2=PromptTemplate(
    template="explain the following joke-{text} ",
    input_variables=["text"]
)
parser=StrOutputParser()
joke_gen_chain=RunnableSequence(prompt1,model,parser)
parrlel_chain=RunnableParallel({
    "joke":RunnablePassthrough(),
    "explanation":RunnableSequence(prompt2,model,parser)
})
final_chain=RunnableSequence(joke_gen_chain,parrlel_chain)
result=final_chain.invoke({"topic":"cricket"})
print(result)
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel,RunnableSequence,RunnablePassthrough,RunnableLambda
# LLM
load_dotenv()
model = ChatGroq(
    model="openai/gpt-oss-120b"
)
prompt1=PromptTemplate(
    template="Generate A joke about {topic}",
    input_variables=["topic"]
)
def word_count(text):
    return len(text.split())
parser=StrOutputParser()
joke_gen_chain=RunnableSequence(prompt1,model,parser)
parrllel_chain=RunnableParallel(
    {
        "joke":RunnablePassthrough(),
        "word_count":RunnableLambda(word_count)
    }
)
final_chain=RunnableSequence(joke_gen_chain,parrllel_chain)
result=final_chain.invoke({"topic":"AI"})
print(result)

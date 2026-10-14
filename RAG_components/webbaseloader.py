from langchain_community.document_loaders import WebBaseLoader
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# LLM
load_dotenv()
model = ChatGroq(
    model="openai/gpt-oss-120b"
)
parser=StrOutputParser()
url="https://www.flipkart.com/apple-macbook-air-m5-2026-m5-16-gb-512-gb-ssd-tahoe-mdhe4hn-a/p/itm8505e2f874525?pid=COMHZQX47WQ7YJZP&lid=LSTCOMHZQX47WQ7YJZPBZOHQJ&marketplace=FLIPKART&store=6bo%2Fb5g&spotlightTagId=default_BestsellerId_6bo%2Fb5g&srno=b_1_1&otracker=browse&fm=organic&iid=b65fb106-daa4-4e18-af18-17e167ff4c18.COMHZQX47WQ7YJZP.SEARCH&ppt=sp&ppn=productListView&ssid=4l7w2n38ow0000001791874764985&ov_redirect=true"
loader=WebBaseLoader(url)
docs=loader.load()
prompt=PromptTemplate(
    template="Answer the following \n {questions} from the following text- \n {text}",
    input_variables=["questions","text"]
)
chain=prompt|model|parser
print(chain.invoke({"questions":"what is it prize of product","text":docs[0]}))




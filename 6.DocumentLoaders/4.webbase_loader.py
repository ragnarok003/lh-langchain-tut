from langchain_community.document_loaders import WebBaseLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from rich.console import Console
from rich.markdown import Markdown

csl = Console()

model = ChatOllama(model="gemma4:e2b", temperature=0.0,)

prompt = PromptTemplate(
    template="answer the following question {question} from the following text {text}",
    input_variables=["question", "text"],
)

URL ="https://ai.google.dev/gemma/docs/core"

loader = WebBaseLoader(URL)

docs =loader.load()

parser =StrOutputParser()

chain =prompt | model | parser

result =chain.invoke({'question':"Summarize the page","text":docs[0].page_content})

csl.print(Markdown(result))
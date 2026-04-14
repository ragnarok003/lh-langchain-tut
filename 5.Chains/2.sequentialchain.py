from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from rich.console import Console
from rich.markdown import Markdown

csl = Console()

model = ChatOllama(model="gemma4", temperature=0.0)

prompt1 =PromptTemplate(
    template="generate detailed report on {topic}",
    input_variables=['topic'] 
)

prompt2 =PromptTemplate(
    template="generate a three point summary of the following text {text}",
    input_variables=['text'] 
)

parser =StrOutputParser()

chain =prompt1 | model | parser | prompt2 | model | parser

result =chain.invoke({"topic":"Aliens"})

csl.print(Markdown(result))
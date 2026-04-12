from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from rich.console import Console
from rich.markdown import Markdown

csl = Console()
model = ChatOllama(model="gemma4", temperature=0.0)
#  PromptTemplate1
template1 =PromptTemplate(template="Write a detailed report on {topic}", input_variables=['topic'])

#  PromptTemplate2
template2 =PromptTemplate(template="Write a summary on the following {topic}", input_variables=['topic'])

parser=StrOutputParser()

chain= template1 | model | parser |template2 | model | parser

response = chain.invoke({
    'topic':"Black Hole"
})



csl.print(Markdown(response))
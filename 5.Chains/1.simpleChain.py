from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from rich.console import Console
from rich.markdown import Markdown

csl = Console()


model = ChatOllama(model="gemma4", temperature=0.0)

prompt = PromptTemplate(
    template="generate 3 facts about a topic {topic}", input_variables=["topic"]
)

parser = StrOutputParser()
chain = prompt | model | parser
result = chain.invoke({"topic": "aliens"})

csl.print(Markdown(result))

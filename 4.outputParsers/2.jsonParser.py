from langchain_ollama import ChatOllama
from rich.console import Console
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

csl = Console()
model = ChatOllama(model="gemma4", temperature=0.0)
parser = JsonOutputParser()

template = PromptTemplate(
    template="Give me the name, age and city of a fictional person. and the name and city has to be indian. {format_instruction}",
    partial_variables={"format_instruction": parser.get_format_instructions()},
    input_variables=[],
)

chain =template | model | parser

result= chain.invoke({})

csl.print_json(data=result)
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel , Field
from rich.console import Console
csl = Console()



class Person (BaseModel):
    name:str =Field(description="The person's full name")
    age: int=Field(gt=18,lt=60,description="The person's age, must not be less than 18 and greater than 60")
    city:str=Field(description="The city where the person lives in")

parser =PydanticOutputParser(pydantic_object=Person)

template =PromptTemplate(
    template="""Give the name, age , city of the fictional {place} person
    Make sure the age is greater than 18.
    Return the response in the following format :{format_instruction}""",
    input_variables=["place"],
    partial_variables={"format_instruction": parser.get_format_instructions()}
)

model = ChatOllama(model="gemma4", temperature=0.0)
chain = template | model |parser 

result =chain.invoke({"place":"Dholakpur"})

csl.print_json(data=result.model_dump())
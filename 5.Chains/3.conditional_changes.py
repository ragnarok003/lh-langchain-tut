from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser,PydanticOutputParser
from langchain_core.runnables import RunnableParallel,RunnableBranch,RunnableLambda
from pydantic import BaseModel ,Field
from typing import Literal

from rich.console import Console
from rich.markdown import Markdown

csl = Console()

model1=ChatOllama(model='gemma4',temperature=0.0)

parser =StrOutputParser()

class Feedback (BaseModel):
    sentiment:Literal['positive','negative']=Field(description="The sentiment of the feedback, must be either positive or negative")

parser2= PydanticOutputParser(pydantic_object=Feedback)

prompt1= PromptTemplate(
    template="Classify the sentiment of the following text into postive or negative {feedback}, {format_instruction}",
    input_variables=['feedback'],
    partial_variables={'format_instruction':parser2.get_format_instructions()}
)

classifier_chain =prompt1 | model1 | parser2

prompt2=PromptTemplate(
    template="write an appropriate response to positive feedback {feedback}",
    input_variables=["feedback"]
)
prompt3=PromptTemplate(
    template="write an appropriate response to negative feedback {feedback}",
    input_variables=["feedback"]
)

branch_chain =RunnableBranch(
    (lambda x:x.sentiment=='positive', prompt2 | model1 | parser),
    (lambda x:x.sentiment=='negative', prompt3 | model1 | parser),
    RunnableLambda(lambda x: "No valid sentiment found")
)

chain =classifier_chain |branch_chain 

result =chain.invoke({"feedback":"This is a beautiful place"})
csl.print(Markdown(result))
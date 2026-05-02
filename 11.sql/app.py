from langchain_ollama import ChatOllama
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent
from rich.console import Console
from rich.markdown import Markdown

csl =Console()

db =SQLDatabase.from_uri("sqlite:///11.sql/chinook.db")

llm =ChatOllama(
    model="gemma4:e2b",
    temperature=0.0,
    # format="json"
)

agent_executor = create_sql_agent(llm=llm,db=db,agent_type="tool-calling",verbose=True)

# result =agent_executor.invoke({"input":"List all customers with their full names and email addresses."})
# result =agent_executor.invoke({"input":"List the top 5 customers who spent the most money."})
result =agent_executor.invoke({"input":"List employees and the number of customers they support."})


csl.print(Markdown(result['input']))
csl.print(Markdown(result['output']))
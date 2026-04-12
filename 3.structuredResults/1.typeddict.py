from langchain_ollama import ChatOllama
from typing import TypedDict

from rich.console import Console
from rich.markdown import Markdown

csl = Console()
model = ChatOllama(model="gemma4",temperature=0.0)

class Review(TypedDict):
    summary:str
    sentiment:str

prompt ="""
The hardware is great, but the software feels bloated.
There are too many pre-installed apps that i never use and can't uninstall.
The battery life is decent, but it could be better.
Also the UI tools outdated compared to other brands.
Hoping for a software update to fix this,
Overall, It's an average phone with some good feature but also some drawbacks.
"""
structured_model=model.with_structured_output(Review)
response=structured_model.invoke(prompt)

csl.print_json(data=response)
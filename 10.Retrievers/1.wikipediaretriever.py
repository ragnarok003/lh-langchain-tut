from langchain_community.retrievers import WikipediaRetriever
from rich.console import Console

csl =Console()
retriever = WikipediaRetriever(lang='en',top_k_results=2)

query ="Chennai Metro Rail"
docs = retriever.invoke(query)
csl.print(len(docs))

for i , doc in enumerate (docs):
    csl.print("Content:\n" , doc.page_content)
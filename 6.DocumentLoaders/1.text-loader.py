from langchain_community.document_loaders import TextLoader
from rich.markdown import Markdown
from rich.console import Console

csl =Console()

loader=TextLoader(file_path="cricket.txt",encoding='utf-8')

docs =loader.load()

print(docs)
print(type(docs))
print(docs[0].metadata)
print(docs[0].page_content)
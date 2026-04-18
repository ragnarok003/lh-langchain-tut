from langchain_community.document_loaders import PyPDFLoader
from rich.markdown import Markdown
from rich.console import Console

csl =Console()

loader =PyPDFLoader("docs/R2023-CSE-CS-Curriculum_and_Syllabus.pdf")

docs= loader.load()

csl.print(Markdown(f'{docs[0].metadata}'))
# print(docs[0])
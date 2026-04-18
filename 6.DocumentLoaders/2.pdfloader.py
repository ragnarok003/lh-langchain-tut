from langchain_community.document_loaders import PyPDFLoader
from rich.markdown import Markdown
from rich.console import Console

csl =Console()

loader =PyPDFLoader("docs/R2023-CSE-CS-Curriculum_and_Syllabus.pdf")

docs= loader.load()
for i in range(len(docs)):
    csl.print(Markdown(f'{docs[i]}'))
# print(docs[0])
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from rich.console import Console
from rich.markdown import Markdown

csl = Console()

loader =PyPDFLoader(file_path="docs/R2019R-CSE-Curriculum_and_Syllabus.pdf")

docs =loader.load()

splitter = CharacterTextSplitter(chunk_size = 500, chunk_overlap=50,separator="")

result =splitter.split_documents(docs)

csl.print(result[0].page_content)
csl.print(result[0].metadata)
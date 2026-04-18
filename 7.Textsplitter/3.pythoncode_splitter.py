from langchain_text_splitters import (
    PythonCodeTextSplitter,
    RecursiveCharacterTextSplitter,
    Language,
)
from rich.console import Console
from rich.markdown import Markdown

csl = Console()

text = """
class Student:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade

        def get_default(self):
            return self.name

        def is_passing(self):
            return self.grade >= 6.0

# Example Usage

student1 =Student("Vikram",23,8.2)
print("passed" if student_1.ispassing() else "fail")
"""

splitter = PythonCodeTextSplitter(chunk_size=300, chunk_overlap=100)

chunks =splitter.split_text(text)
csl.print(chunks)
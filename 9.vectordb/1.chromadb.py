from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from rich.console import Console

csl =Console()

texts =[
    "Large language models are trained on massive datasets",
    "large language models(llms) are particularly trained using transformers",
    "chroma is a lightweight vector storeused in langchain"
    "embeddings convert text into respresentation"
]

embeddings1 =OllamaEmbeddings(model="mxbai-embed-large")

vector_store = Chroma.from_texts(
    texts=texts,
    embedding=embeddings1,
    collection_name="Langchain_chroma_demo"
)

query ="tell me more about llms"
result =vector_store.similarity_search(query=query,k=2)

csl.print(result)
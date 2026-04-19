from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from rich.console import Console
from sympy import Q

csl =Console()

embeddings1 =OllamaEmbeddings(model="mxbai-embed-large")

vector_store = Chroma(
    create_collection_if_not_exists="vehicles",
    embedding_function=embeddings1,
    persist_directory="9.vectordb/chroma/youtube/db"
)

vector_store.add_texts([
    "Car runs on land",
    "Plane flies in the sky",
    "Boat travels on water",
    "Bus is public transport on road",
    "cycle runs without fuel"
], metadatas=[
    {"type":"Private transport"},
    {"type":"Public transport"},
    {"type":"Public transport"},
    {"type":"Public transport"},
    {"type":"Private transport"}
])

csl.print(vector_store.get(include=["embeddings", "documents", "metadatas"]))

query = [
    "vehicle that does not need fuel"
]

result = vector_store.similarity_search(query=query[0],k=1)

csl.print(result)
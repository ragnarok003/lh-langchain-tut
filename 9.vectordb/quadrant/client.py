from langchain_qdrant import QdrantVectorStore
from langchain_ollama import OllamaEmbeddings
from rich.console import Console

csl =Console()

embeddings = OllamaEmbeddings(model="mxbai-embed-large:latest")

vector_store = QdrantVectorStore.from_texts(
    texts=[
        "Car runs on land",
        "Plane flies in the sky",
        "Boat travels on water",
        "Bus is public transport on road",
        "cycle runs without fuel",
    ],
    embedding=embeddings,
    url="http://localhost:6333",
    collection_name="vehicles",
)


# retriever = vector_store.as_retriever(search_kwargs={"k":2})

# docs = retriever.invoke("vehicle that does not need fuel")
# csl.print(docs)

results=vector_store.similarity_search(query="vehicle that does not need fuel", k=2)
csl.print(results)


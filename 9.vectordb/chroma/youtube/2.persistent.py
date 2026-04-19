import chromadb
from rich.console import Console

csl = Console()

client = chromadb.PersistentClient(path="9.vectordb/chroma/youtube/db")
collection = client.get_or_create_collection(name="vehicles")

csl.print("Collection Created : ", collection.name)

collection.add(
    documents=[
        "Car runs on land",
    ],
    ids=["car1"],
)

csl.print("Colllection added and saved successfully")

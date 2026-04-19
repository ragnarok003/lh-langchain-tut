import chromadb
from rich.console import Console

csl = Console()

client = chromadb.PersistentClient(path="9.vectordb/chroma/youtube/db")
collection = client.get_or_create_collection(name="vehicles")

csl.print("Collection Created : ", collection.name)

csl.print(collection.get())
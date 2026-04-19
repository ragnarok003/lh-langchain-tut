import chromadb
from rich.console import Console

csl = Console()

client = chromadb.Client()

collection = client.create_collection(name="vehicles")

csl.print("Collection Created : ", collection.name)

collection.add(
    documents=[
        "Car runs on land",
        "Plane flies in the sky",
        "Boat travels on water",
        "Bus is public transport on road",
    ],
    ids=["car1", "plane1", "boat1", "bus1"],
)

query = [
    "vehicle thata runs on road",
    "If i have to catch fish what should i use",
    "which transort can carry more than 20 people",
]

result = collection.query(query_texts=query[2], n_results=2)

csl.print(result)

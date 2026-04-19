from langchain_qdrant import QdrantVectorStore, RetrievalMode
from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance

from uuid import uuid4
from langchain_core.documents import Document
from langchain_ollama import OllamaEmbeddings
from rich.console import Console

# -------------------------------
# Setup
# -------------------------------
csl = Console()

embeddings = OllamaEmbeddings(model="mxbai-embed-large:latest")

# Connect to Docker Qdrant
client = QdrantClient(
    url="http://localhost:6333",
)

COLLECTION_NAME = "my_documents"

# -------------------------------
# Create collection (if not exists)
# -------------------------------
collections = client.get_collections().collections
collection_names = [c.name for c in collections]

if COLLECTION_NAME not in collection_names:
    client.create_collection(
        collection_name=COLLECTION_NAME,
        vectors_config={
            "size": 1024,  # for mxbai-embed-large
            "distance": Distance.COSINE,
        },
    )
    csl.print("[green]Collection created[/green]")

# -------------------------------
# Vector Store
# -------------------------------
vector_store = QdrantVectorStore(
    client=client,
    collection_name=COLLECTION_NAME,
    embedding=embeddings,
    retrieval_mode=RetrievalMode.DENSE,
)

# -------------------------------
# Documents
# -------------------------------
documents = [
    Document(
        page_content="I had chocolate chip pancakes and scrambled eggs for breakfast this morning.",
        metadata={"source": "tweet"},
    ),
    Document(
        page_content="The weather forecast for tomorrow is cloudy and overcast.",
        metadata={"source": "news"},
    ),
    Document(
        page_content="Building an exciting new project with LangChain - come check it out!",
        metadata={"source": "tweet"},
    ),
    Document(
        page_content="Robbers broke into the city bank and stole $1 million in cash.",
        metadata={"source": "news"},
    ),
    Document(
        page_content="Wow! That was an amazing movie.", metadata={"source": "tweet"}
    ),
    Document(
        page_content="Is the new iPhone worth the price?",
        metadata={"source": "website"},
    ),
    Document(
        page_content="Top 10 soccer players in the world.",
        metadata={"source": "website"},
    ),
    Document(
        page_content="LangGraph is the best framework for agentic apps!",
        metadata={"source": "tweet"},
    ),
    Document(
        page_content="Stock market down 500 points due to recession fears.",
        metadata={"source": "news"},
    ),
    Document(
        page_content="I have a bad feeling I am going to get deleted :(",
        metadata={"source": "tweet"},
    ),
]

# -------------------------------
# Insert only if empty
# -------------------------------
count = client.count(collection_name=COLLECTION_NAME).count

if count == 0:
    ids = [str(uuid4()) for _ in documents]
    vector_store.add_documents(documents=documents, ids=ids)
    csl.print("[green]Documents inserted[/green]")
else:
    csl.print(f"[yellow]Already contains {count} documents[/yellow]")

# -------------------------------
# Query
# -------------------------------
query = "LangChain makes working with LLMs easier"

results = vector_store.similarity_search(query, k=3)

# -------------------------------
# Output
# -------------------------------
csl.print("\n[bold cyan]Query:[/bold cyan]", query)
csl.print("\n[bold green]Results:[/bold green]\n")

for i, doc in enumerate(results, 1):
    csl.print(f"[bold]{i}.[/bold] {doc.page_content}")
    csl.print(f"   [dim]Metadata:[/dim] {doc.metadata}\n")

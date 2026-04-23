from langchain_qdrant import QdrantVectorStore
from langchain_ollama import OllamaEmbeddings
from rich.console import Console
from langchain_core.documents import Document

csl = Console()

embeddings = OllamaEmbeddings(model="mxbai-embed-large:latest")

documents = [
    Document(page_content="Langchain helps developers build LLM applications easily"),
    Document(page_content="Chroma is a vector database optimized for LLM based search"),
    Document(page_content="Embeddings convert text into high-dimensional vectors"),
    Document(page_content="OpenAI provides powerful embedding models"),
]

vector_store = QdrantVectorStore.from_documents(
    documents=documents,
    embedding=embeddings,
    collection_name="my_collection",
    url="http://localhost:6333",
)

retriever = vector_store.as_retriever(search_kwargs={"k":2})
query="What is embedding used for ?"

results =retriever.invoke(query)

csl.print(results)
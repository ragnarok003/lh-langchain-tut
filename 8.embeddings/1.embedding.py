from langchain_ollama import OllamaEmbeddings
from rich.console import Console
import logging


logging.basicConfig(
    filename='8.embeddings/embedding.log',
    level=logging.INFO,
    encoding='utf-8',
)

csl =Console()

embeddings1 =OllamaEmbeddings(model="mxbai-embed-large")
embeddings2 =OllamaEmbeddings(model="embeddinggemma:latest")
texts = [
    "New York is a busy city",
    "NYC has a large population",
    "Bananas are yellow"
]
result1 = embeddings1.embed_query(text)
result2 = embeddings2.embed_query(text)

logging.info("mxbai-embed-large")
logging.info(result1)
logging.info("embeddinggemma:latest")
logging.info(result2)

print(len(result1), len(result2))
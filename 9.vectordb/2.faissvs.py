from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from rich.console import Console

csl = Console()

cricket_texts = [
    "Cricket is one of the most popular sports in the world, especially in countries like India, England, Australia, and Nepal.",
    "Sachin Tendulkar is known as the God of Cricket because of his consistency, technique, and long international career.",
    "Cricket is played in three major formats: Test cricket, One Day Internationals, and Twenty20.",
    "Each cricket team consists of eleven players including batsmen, bowlers, all-rounders, and a wicket-keeper.",
    "The International Cricket Council (ICC) governs cricket worldwide and organizes tournaments like the Cricket World Cup.",
    "Cricket requires physical fitness, strategy, teamwork, and strong mental discipline.",
]

embeddings1 =OllamaEmbeddings(model="mxbai-embed-large")

vectorstore =FAISS.from_texts(
    texts=cricket_texts,
    embedding=embeddings1
)

query ="Who is God of Cricket?"

results = vectorstore.similarity_search(query=query,k=1)
csl.print(results)
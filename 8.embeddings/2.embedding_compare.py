import numpy as np
from langchain_ollama import OllamaEmbeddings

# Models
embeddings1 = OllamaEmbeddings(model="mxbai-embed-large")
embeddings2 = OllamaEmbeddings(model="embeddinggemma:latest")

# Text samples
texts = [
    "New York is a busy city",
    "NYC has a large population",
    "Bananas are yellow"
]

# Cosine similarity function
def cosine_similarity(a, b):
    a = np.array(a)
    b = np.array(b)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

# Function to compute similarity matrix
def compute_similarities(embeddings, model_name):
    print(f"\n=== {model_name} ===")

    # Generate embeddings
    vectors = [embeddings.embed_query(text) for text in texts]

    # Compute pairwise similarities
    for i in range(len(texts)):
        for j in range(i + 1, len(texts)):
            sim = cosine_similarity(vectors[i], vectors[j])
            print(f"\nText 1: {texts[i]}")
            print(f"Text 2: {texts[j]}")
            print(f"Similarity: {sim:.4f}")

# Run for both models
compute_similarities(embeddings1, "mxbai-embed-large")
compute_similarities(embeddings2, "embeddinggemma")
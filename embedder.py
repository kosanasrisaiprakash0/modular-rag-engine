from sentence_transformers import SentenceTransformer

def load_embedder(model_name = "all-MiniLM-L6-v2"):
    embedder = SentenceTransformer(model_name)
    return embedder

def get_embeddings(embedder, texts):
    embeddings = embedder.encode(texts, convert_to_numpy=True)
    return embeddings

if __name__ == "__main__":
    embedder = load_embedder()
    sample = ["hello world", "RAG is retrieval augmented generation"]
    embeddings = get_embeddings(embedder, sample)
    print(f"number of embeddings: {len(embeddings)}")
    print(f"embedding size: {embeddings.shape}")
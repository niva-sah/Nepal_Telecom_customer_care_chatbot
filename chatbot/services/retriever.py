import faiss
import pickle
import numpy as np

# Load FAISS index
index = faiss.read_index(
    "chatbot/vectorstore/faiss_index.bin"
)

# Load stored text chunks
with open(
    "chatbot/vectorstore/chunks.pkl",
    "rb"
) as f:
    documents = pickle.load(f)


def search_documents(query_embedding, top_k=1):

    distances, indices = index.search(
        np.array(query_embedding).astype("float32"),
        top_k
    )

    results = []

    for idx in indices[0]:
        results.append(documents[idx])

    return results
import os
import faiss
import pickle
import pandas as pd
import numpy as np

from sentence_transformers import SentenceTransformer

# Create vectorstore folder
os.makedirs(
    "chatbot/vectorstore",
    exist_ok=True
)

# Load embedding model
model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

documents = []

# -----------------------------
# LOAD TXT FILES
# -----------------------------

data_folder = "chatbot/data"

for file_name in os.listdir(data_folder):

    file_path = os.path.join(
        data_folder,
        file_name
    )

    # TXT FILES
    if file_name.endswith(".txt"):

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as f:

            text = f.read()

            documents.append(text)

    # CSV FILES
    elif file_name.endswith(".csv"):

        df = pd.read_csv(file_path)

        # Convert each row to text
        for _, row in df.iterrows():

            row_text = " ".join(
                [str(value) for value in row.values]
            )

            documents.append(row_text)

# -----------------------------
# CREATE EMBEDDINGS
# -----------------------------

embeddings = model.encode(documents)

embeddings = np.array(
    embeddings
).astype("float32")

# -----------------------------
# BUILD FAISS INDEX
# -----------------------------

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(embeddings)

# -----------------------------
# SAVE INDEX
# -----------------------------

faiss.write_index(
    index,
    "chatbot/vectorstore/faiss_index.bin"
)

# Save text chunks
with open(
    "chatbot/vectorstore/chunks.pkl",
    "wb"
) as f:

    pickle.dump(documents, f)

print("Index built successfully")
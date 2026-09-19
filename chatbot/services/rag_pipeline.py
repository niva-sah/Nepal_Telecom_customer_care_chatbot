from .embedder import get_embedding
from .retriever import search_documents
from .prompt_builder import build_prompt
from .llm_client import generate_response


def get_rag_response(user_query):

    # Step 1: Convert query to embedding
    query_embedding = get_embedding(user_query)

    # Step 2: Retrieve relevant documents
    retrieved_docs = search_documents(query_embedding)

    # Step 3: Combine retrieved text
    context = "\n".join(
    [doc.strip() for doc in retrieved_docs]
)

    # Step 4: Build final prompt
    prompt = build_prompt(context, user_query)

    # Step 5: Generate answer from Ollama
    response = generate_response(prompt)

    return response
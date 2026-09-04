from src.document_loader import load_documents
from src.chunker import create_chunks
from src.embeddings import EmbeddingModel
from src.vector_store import VectorStore


DOCUMENT_FOLDER = "data/policies"


def main():

    print("Loading documents...")

    documents = load_documents(
        DOCUMENT_FOLDER
    )

    print(f"Documents loaded: {len(documents)}")

    print("Creating chunks...")

    chunks = create_chunks(documents)

    print(f"Chunks created: {len(chunks)}")

    texts = [
        chunk["text"]
        for chunk in chunks
    ]

    print("Generating embeddings...")

    embedding_model = EmbeddingModel()

    embeddings = embedding_model.generate_embeddings(
        texts
    )

    print("Creating FAISS index...")

    vector_store = VectorStore(
        "index/policy.index",
        "index/metadata.pkl"
    )

    vector_store.create_index(
        embeddings,
        chunks
    )

    vector_store.save()

    print("Index created successfully!")


if __name__ == "__main__":
    main()
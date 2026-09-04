from src.embeddings import EmbeddingModel
from src.vector_store import VectorStore
from src.metadata_filter import filter_results


class PolicySearch:

    def __init__(self):

        self.embedding_model = EmbeddingModel()

        self.vector_store = VectorStore(
            "index/policy.index",
            "index/metadata.pkl"
        )

        self.vector_store.load()

    def search(
        self,
        query,
        department=None,
        document_type=None,
        date=None,
        access_level=None,
        k=5
    ):

        query_embedding = (
            self.embedding_model
            .generate_embeddings([query])[0]
        )

        # Get more results first
        results = self.vector_store.search(
            query_embedding,
            k=20
        )

        # Apply metadata filters
        results = filter_results(
            results,
            department,
            document_type,
            date,
            access_level
        )

        return results[:k]
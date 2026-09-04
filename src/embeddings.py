from sentence_transformers import SentenceTransformer
from src.config import EMBEDDING_MODEL


class EmbeddingModel:

    def __init__(self):

        self.model = SentenceTransformer(EMBEDDING_MODEL)

    def generate_embeddings(self, texts):

        embeddings = self.model.encode(
            texts,
            normalize_embeddings=True
        )

        return embeddings
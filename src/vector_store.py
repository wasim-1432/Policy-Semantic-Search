import faiss
import pickle
import numpy as np


class VectorStore:

    def __init__(self, index_path, metadata_path):

        self.index_path = index_path
        self.metadata_path = metadata_path

        self.index = None
        self.chunks = []

    def create_index(self, embeddings, chunks):

        embeddings = np.asarray(
            embeddings,
            dtype="float32"
        )

        dimension = embeddings.shape[1]

        # Inner Product
        self.index = faiss.IndexFlatIP(dimension)

        self.index.add(embeddings)

        self.chunks = chunks

    def save(self):

        faiss.write_index(
            self.index,
            self.index_path
        )

        with open(self.metadata_path, "wb") as file:

            pickle.dump(
                self.chunks,
                file
            )

    def load(self):

        self.index = faiss.read_index(
            self.index_path
        )

        with open(self.metadata_path, "rb") as file:

            self.chunks = pickle.load(file)

    def search(self, query_embedding, k=5):

        query_embedding = np.asarray(
            [query_embedding],
            dtype="float32"
        )

        scores, indices = self.index.search(
            query_embedding,
            k
        )

        results = []

        for score, index in zip(
            scores[0],
            indices[0]
        ):

            if index == -1:
                continue

            results.append({
                "score": float(score),
                "text": self.chunks[index]["text"],
                "metadata": self.chunks[index]["metadata"]
            })

        return results
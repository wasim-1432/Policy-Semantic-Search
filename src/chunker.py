from src.config import CHUNK_SIZE, CHUNK_OVERLAP


def create_chunks(documents):

    chunks = []

    for document in documents:

        text = document["text"]
        metadata = document["metadata"]

        start = 0

        while start < len(text):

            end = start + CHUNK_SIZE

            chunk_text = text[start:end]

            chunks.append({
                "text": chunk_text,
                "metadata": metadata
            })

            start += CHUNK_SIZE - CHUNK_OVERLAP

    return chunks
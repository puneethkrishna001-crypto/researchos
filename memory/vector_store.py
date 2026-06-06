import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.PersistentClient(path="./memory/chroma_db")

collection = client.get_or_create_collection(
    name="research_memory"
)


def store_research(query, report):
    embedding = model.encode(report).tolist()

    collection.add(
        ids=[query],
        embeddings=[embedding],
        documents=[report]
    )


def retrieve_similar(query, n_results=3):
    embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[embedding],
        n_results=n_results
    )

    return results
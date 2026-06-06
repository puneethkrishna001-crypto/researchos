from memory.vector_store import (
    store_research,
    retrieve_similar
)


def save_report(query, report):
    store_research(query, report)


def search_memory(query):
    return retrieve_similar(query)
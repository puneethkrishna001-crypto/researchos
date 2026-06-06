from typing import TypedDict, List


class ResearchState(TypedDict):
    query: str
    memory_results: dict
    articles: List[dict]
    summaries: List[str]
    review: str
    report: str
    citations: List[str]
from langgraph.graph import StateGraph, END

from graph.state import ResearchState

from agents.researcher import research_topic
from agents.summarizer import summarize_article
from agents.critic import review_summaries
from agents.writer import write_report

from tools.memory_tools import (
    search_memory,
    save_report
)


def memory_node(state):
    memory_results = search_memory(
        state["query"]
    )

    return {
        "memory_results": memory_results
    }


def researcher_node(state):
    articles = research_topic(
        state["query"]
    )

    citations = []

    for article in articles:
        citations.append(article["url"])

    return {
        "articles": articles,
        "citations": citations
    }


def summarizer_node(state):
    summaries = []

    for article in state["articles"]:
        summary = summarize_article(
            article["content"]
        )

        summaries.append(summary)

    return {
        "summaries": summaries
    }


def critic_node(state):
    review = review_summaries(
        state["summaries"]
    )

    return {
        "review": review
    }


def writer_node(state):
    report = write_report(
        state["query"],
        state["summaries"]
    )

    citation_text = "\n\nSources:\n"

    for i, url in enumerate(state["citations"], start=1):
        citation_text += f"\n{i}. {url}"

    report += citation_text

    save_report(
        state["query"],
        report
    )

    return {
        "report": report
    }

def route_after_critic(state):
    review = state["review"].lower()

    if "quality score: 1" in review:
        return "retry"

    if "quality score: 2" in review:
        return "retry"

    if "quality score: 3" in review:
        return "retry"

    if "quality score: 4" in review:
        return "retry"

    return "write"


graph = StateGraph(
    ResearchState
)

graph.add_node(
    "memory",
    memory_node
)

graph.add_node(
    "researcher",
    researcher_node
)

graph.add_node(
    "summarizer",
    summarizer_node
)

graph.add_node(
    "critic",
    critic_node
)

graph.add_node(
    "writer",
    writer_node
)

graph.set_entry_point(
    "memory"
)

graph.add_edge(
    "memory",
    "researcher"
)

graph.add_edge(
    "researcher",
    "summarizer"
)

graph.add_edge(
    "summarizer",
    "critic"
)

graph.add_conditional_edges(
    "critic",
    route_after_critic,
    {
        "retry": "researcher",
        "write": "writer"
    }
)

graph.add_edge(
    "writer",
    END
)

research_graph = graph.compile()
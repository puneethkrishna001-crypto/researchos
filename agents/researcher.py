from tools.search import search_web
from tools.scraper import scrape_url


def research_topic(query):
    search_results = search_web(query)

    articles = []

    for result in search_results:
        text = scrape_url(result["url"])

        articles.append(
            {
                "title": result["title"],
                "url": result["url"],
                "content": text
            }
        )

    return articles
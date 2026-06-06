import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents.researcher import research_topic
from agents.summarizer import summarize_article

query = "Impact of AI on Healthcare in 2025"

articles = research_topic(query)

for i, article in enumerate(articles, start=1):
    print("\n" + "=" * 80)
    print(f"ARTICLE {i}")
    print("=" * 80)

    summary = summarize_article(article["content"])

    print(summary)
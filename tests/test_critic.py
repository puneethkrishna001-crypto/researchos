import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents.researcher import research_topic
from agents.summarizer import summarize_article
from agents.critic import review_summaries

query = "Impact of AI on Healthcare in 2025"

articles = research_topic(query)

summaries = []

for article in articles:
    summaries.append(
        summarize_article(article["content"])
    )

review = review_summaries(summaries)

print(review)
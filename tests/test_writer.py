import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents.researcher import research_topic
from agents.summarizer import summarize_article
from agents.writer import write_report

query = "Impact of AI on Healthcare in 2025"

articles = research_topic(query)

summaries = []

for article in articles:
    summary = summarize_article(article["content"])
    summaries.append(summary)

report = write_report(query, summaries)

print(report)
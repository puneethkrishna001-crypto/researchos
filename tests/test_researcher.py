import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents.researcher import research_topic

articles = research_topic("Impact of AI on Healthcare in 2025")

print(f"\nFound {len(articles)} articles\n")

for i, article in enumerate(articles, start=1):
    print("-" * 50)
    print("Title:", article["title"])
    print("URL:", article["url"])
    print("Content Length:", len(article["content"]))
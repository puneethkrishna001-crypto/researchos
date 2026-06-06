import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools.scraper import scrape_url
from agents.summarizer import summarize_article

url = "https://en.wikipedia.org/wiki/Artificial_intelligence_in_healthcare"

article = scrape_url(url)

summary = summarize_article(article)

print(summary)
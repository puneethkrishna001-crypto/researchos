import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools.scraper import scrape_url

url = "https://en.wikipedia.org/wiki/Artificial_intelligence_in_healthcare"

article = scrape_url(url)

print("\nArticle Length:", len(article))
print("\n")
print(article[:2000])
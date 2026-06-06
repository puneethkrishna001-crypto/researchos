import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools.search import search_web


query = "Impact of AI on Healthcare in 2025"

results = search_web(query)

print(f"\nFound {len(results)} results\n")

for i, result in enumerate(results, start=1):
    print("-" * 50)
    print(f"Result {i}")
    print("Title:", result["title"])
    print("URL:", result["url"])
    print("Snippet:", result["snippet"])
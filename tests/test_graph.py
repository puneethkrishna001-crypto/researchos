import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from graph.research_graph import research_graph

result = research_graph.invoke(
    {
        "query": "Impact of AI on Healthcare in 2025"
    }
)

print("\nFINAL REPORT\n")
print(result["report"])
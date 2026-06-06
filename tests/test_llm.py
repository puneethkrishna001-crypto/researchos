import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.llm import generate_response

response = generate_response(
    "Explain artificial intelligence in healthcare in 5 bullet points."
)

print(response)
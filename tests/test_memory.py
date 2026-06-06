import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

from tools.memory_tools import (
    save_report,
    search_memory
)

report = """
Artificial Intelligence is transforming healthcare
through diagnostics, telemedicine and drug discovery.
"""

save_report(
    "AI in Healthcare",
    report
)

results = search_memory(
    "Future of AI Hospitals"
)

print(results)
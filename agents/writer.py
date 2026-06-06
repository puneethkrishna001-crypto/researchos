from models.llm import generate_response


def write_report(query, summaries):
    combined_text = "\n\n".join(
        [
            f"Source {i+1}:\n{summary}"
            for i, summary in enumerate(summaries)
        ]
    )

    prompt = f"""
You are an expert research analyst.

Research Topic:
{query}

Below are summaries from multiple independent sources.

Use ALL sources.

Do not focus on only one source.

Identify common themes across sources.

Generate a detailed report.

Format:

Executive Summary

Key Findings

Detailed Analysis

Conclusion

Future Outlook

Sources:

{combined_text}
"""

    return generate_response(prompt)
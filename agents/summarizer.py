from models.llm import generate_response


def summarize_article(article_text):
    prompt = f"""
    You are a research assistant.

    Summarize the following article.

    Provide:

    1. Main Topic
    2. Key Findings
    3. Important Statistics
    4. Final Summary

    Article:

    {article_text[:4000]}
    """

    summary = generate_response(prompt)

    return summary
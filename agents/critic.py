from models.llm import generate_response


def review_summaries(summaries):
    combined = "\n\n".join(summaries)

    prompt = f"""
    You are a research quality reviewer.

    Review these research summaries.

    Check:

    1. Are there contradictory facts?
    2. Are there suspicious statistics?
    3. Are sources likely unreliable?
    4. Are important details missing?

    Give:

    Quality Score (1-10)

    Strengths

    Weaknesses

    Recommendation
    """

    return generate_response(prompt + combined)
from langchain_ollama import OllamaLLM

llm = OllamaLLM(
    model="qwen2.5:3b"
)


def generate_response(prompt):
    return llm.invoke(prompt)
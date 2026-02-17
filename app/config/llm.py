from langchain_openai import ChatOpenAI

def get_llm(model: str = "gpt-4o-mini", temperature: float = 0):
    return ChatOpenAI(
        model=model,
        temperature=temperature
    )

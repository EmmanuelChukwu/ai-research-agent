from langchain.tools import tool
from app.config.llm import get_llm

@tool
def summarize_text(text: str, max_length: int = 150) -> str:
    """
    Summarize a given text into a concise version.
    Takes long text content and produces a shorter, condensed summary.
    Args:
        text: The text to summarize (longer passages work best)
        max_length: Maximum length of the summary in words (default: 150)
    """
    try:
        if not text or len(text.strip()) == 0:
            return "Error: No text provided to summarize"
        
        if len(text.split()) < 20:
            return "Text is already too short to summarize meaningfully."
        
        # Use the LLM to summarize
        llm = get_llm()
        
        prompt = f"""Summarize the following text in approximately {max_length} words or less. 
Be concise and capture the main ideas:

{text}

Summary:"""
        
        response = llm.invoke(prompt)
        
        # Extract text content from response
        if hasattr(response, 'content'):
            return response.content
        else:
            return str(response)
            
    except Exception as e:
        return f"Error summarizing text: {str(e)}"

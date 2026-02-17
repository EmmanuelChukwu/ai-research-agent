from langchain.tools import tool

@tool
def get_current_year() -> str:
    """Returns the current year."""
    return "2026"

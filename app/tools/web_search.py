from langchain.tools import tool
from langchain_community.utilities import SerpAPIWrapper
from app.config.settings import SERPAPI_API_KEY

search = SerpAPIWrapper(serpapi_api_key=SERPAPI_API_KEY)

@tool
def web_search(query: str) -> str:
    """
    Search the web for recent information.
    Use this for current events, research topics, news, or general knowledge.
    """
    return search.run(query)

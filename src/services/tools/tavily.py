from langchain.tools import tool
from typing import Dict, Any
from tavily import TavilyClient

tavily_client = TavilyClient()

@tool
def web_search(query: str) -> Dict[str,Any]:
    """search the web for information"""
    return tavily_client.search(query=query)
from typing import Dict, Any

import requests
from dotenv import load_dotenv
from langchain_core.tools import tool
from mcp.server import FastMCP
from requests import get
from tavily.tavily import TavilyClient

load_dotenv()

mcp = FastMCP("mcp-server")

tavily_client = TavilyClient()


## TOOL
@tool
def search_web(query: str) -> Dict[str, Any]:
    """
    search the web for information
    """
    return tavily_client.search(query)


## RESOURCES
@mcp.resource("github://langchain-ai/langchain-mcp-adapters/blob/main/README.md")
def github_file():
    """
    Resource for accessing langchain-ai/langchain-mcp-adapters/README.md file
    """
    url = f"https://raw.githubusercontent.com/langchain-ai/langchain-mcp-adapters/blob/main/README.md"

    try:
        response = get(url)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"


## PROMPT TEMPLATE
@mcp.prompt()
def prompt():
    """Analyze data from a langchain-ai repo file with comprehensive insights"""
    return """
        You are a helpful assistant that answers user questions about LangChain, LangGraph and LangSmith.

        You can use the following tools/resources to answer user questions:
        - search_web: Search the web for information
        - github_file: Access the langchain-ai repo files

        If the user asks a question that is not related to LangChain, LangGraph or LangSmith, you should say "I'm sorry, I can only answer questions about LangChain, LangGraph and LangSmith."

        You may try multiple tool and resource calls to answer the user's question.

        You may also ask clarifying questions to the user to better understand their question.
        """


if __name__ == "__main__":
    mcp.run(transport="stdio")

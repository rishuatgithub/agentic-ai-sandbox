from typing import Any, Dict

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
from tavily import TavilyClient

load_dotenv()

tavily_client = TavilyClient()


@tool
def web_search(query: str) -> Dict[str, Any]:
    """
    search the web for information
    :param query: search query
    :return: information
    """
    return tavily_client.search(query)


agent = create_agent("gpt-5-nano", tools=[web_search])

question = HumanMessage(content="What is the flight status of EK002 as of 15th March 2026?")

response = agent.invoke({
    "messages": [question]
})

print(response)

"""
Assignment 01
Create a personal chef agent that will provide the recipie from the leftover items in your fridge or pantry.
"""
from pprint import pprint
from typing import Dict, Any

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
from langgraph.checkpoint.memory import InMemorySaver
from tavily.tavily import TavilyClient

load_dotenv()

tavily_client = TavilyClient()

system_prompt = """
    You are a personal home chef. The user will give you a list of ingredients they have left over in their house.
    
    Using the web search tool, search the web for recipes that can be made with the ingredients they have.
    
    Return recipe suggestions and eventually the recipe instructions to the user, if requested.
"""


@tool
def web_search(query: str) -> Dict[str, Any]:
    """
    search the web for information.
    :param query: query to search for
    :return: information about the web search
    """
    return tavily_client.search(query)


agent = create_agent("gpt-5-nano",
                     tools=[web_search],
                     system_prompt=system_prompt,
                     checkpointer=InMemorySaver()
                     )

#in memory config to remember the thread
config = {"configurable": {"thread_id": "1"}}

question = HumanMessage(content="I have some leftover chicken and rice. What can i prepare?")

#response = agent.invoke({"messages": [question]}, config=config)

#pprint(response['messages'][-1].content)

## using streaming output

for token, metadata in agent.stream({"messages": [question]}, config=config, stream_mode="messages"):
    if token.content:
        print(token.content, end="", flush=True)

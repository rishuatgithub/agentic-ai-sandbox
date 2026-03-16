from dataclasses import dataclass
from pprint import pprint

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain.tools import ToolRuntime, tool

load_dotenv()


@dataclass
class ColorContext:
    favorite_color: str = "blue"
    least_favorite_color: str = "yellow"


#agent = create_agent("gpt-5-nano", context_schema=ColorContext)

#response = agent.invoke({"messages": [HumanMessage(content="What is my favourite color?")]}, context=ColorContext())

#pprint(response) ## model doesn't have the runtime context.

## create tools to pass the runtime context default values.

@tool
def get_favourite_colour(runtime: ToolRuntime) -> str:
    """Get the favourite colour of the user"""
    return runtime.context.favorite_color

@tool
def get_least_favourite_colour(runtime: ToolRuntime) -> str:
    """Get the least favourite colour of the user"""
    return runtime.context.least_favorite_color


agent = create_agent("gpt-5-nano",
                     tools=[get_favourite_colour, get_least_favourite_colour],
                     context_schema=ColorContext)

response = agent.invoke({"messages": [HumanMessage(content="What is my favourite colour?")]}, context=ColorContext())

#pprint(response)

# changing the context in runtime
response = agent.invoke(
    {"messages": [HumanMessage(content="What is my least favourite colour?")]},
    context=ColorContext(least_favorite_color="green")
)

pprint(response)
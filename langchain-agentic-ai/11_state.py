from pprint import pprint

from dotenv import load_dotenv
from langchain.agents import AgentState, create_agent
from langchain.tools import tool, ToolRuntime
from langchain_core.messages import ToolMessage, HumanMessage
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.types import Command

load_dotenv()


class CustomState(AgentState):
    favorite_color: str


## write to a state

@tool
def update_favorite_color(favorite_color: str, runtime: ToolRuntime) -> Command:
    """Update the favorite color of the user in the state once they've revealed it."""
    return Command(update={
        "favorite_color": favorite_color,
        "messages": [ToolMessage("Successfully updated favourite colour", tool_call_id=runtime.tool_call_id)]}
    )


agent = create_agent(
    "gpt-5-nano",
    tools=[update_favorite_color],
    checkpointer=InMemorySaver(),
    state_schema=CustomState
)

response = agent.invoke(
    { "messages": [HumanMessage(content="My favourite colour is green")]},
    {"configurable": {"thread_id": "1"}}
)

pprint(response)


response = agent.invoke(
    {
        "messages": [HumanMessage(content="Hello, how are you?")],
        "favourite_colour": "green"
    },
    {"configurable": {"thread_id": "10"}}
)

pprint(response)
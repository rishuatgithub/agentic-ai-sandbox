from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import AnyMessage
from langchain_core.runnables import RunnableConfig
from langgraph.prebuilt import create_react_agent
from langgraph.prebuilt.chat_agent_executor import AgentState
from pydantic import BaseModel

load_dotenv()


class WeatherResponse(BaseModel):
    city: str
    conditions: str


def get_weather(city: str):
    """Get weather for a given city."""
    return f"The weather in {city} is sunny with a high of 75°F."


llm = init_chat_model(model='anthropic:claude-3-7-sonnet-latest', temperature=0.2)


def prompt() -> list[AnyMessage]:
    """
    Using dynamic prompt with ReAct agent.
    """
    system_msg = f"You are a helpful assistant."
    return [{"role": "system", "content": system_msg}]


agent = create_react_agent(
    model=llm,
    tools=[get_weather],
    response_format=WeatherResponse
)

state = agent.invoke(
    {'messages': [{"role": "user", "content": "What's the weather like in New York?"}]}
)

print(state["structured_response"])

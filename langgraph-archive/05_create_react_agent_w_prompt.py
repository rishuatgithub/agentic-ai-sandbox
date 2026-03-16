from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import AnyMessage
from langchain_core.runnables import RunnableConfig
from langgraph.prebuilt import create_react_agent
from langgraph.prebuilt.chat_agent_executor import AgentState

load_dotenv()


def get_weather(city: str):
    """Get weather for a given city."""
    return f"The weather in {city} is sunny with a high of 75°F."


llm = init_chat_model(model='anthropic:claude-3-7-sonnet-latest', temperature=0.2)


def prompt(state: AgentState, config: RunnableConfig) -> list[AnyMessage]:
    """
    Using dynamic prompt with ReAct agent.
    """
    user_name = config['configurable'].get('user_name')
    system_msg = f"You are a helpful assistant. Address the user as {user_name}."
    return [{"role": "system", "content": system_msg}] + state["messages"]


agent = create_react_agent(
    model=llm,
    tools=[get_weather],
    prompt=prompt
)

state = agent.invoke(
    {'messages': [{"role": "user", "content": "What's the weather like in New York?"}]},
    config = {'configurable': {'user_name': 'Alice'}}
)

print(state['messages'][-1].content)

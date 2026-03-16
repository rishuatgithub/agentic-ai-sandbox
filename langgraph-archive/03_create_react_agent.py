from dotenv import load_dotenv
from langgraph.prebuilt import create_react_agent

load_dotenv()


def get_weather(city: str):
    """Get weather for a given city."""
    return f"The weather in {city} is sunny with a high of 75°F."


agent = create_react_agent(
    model="anthropic:claude-3-7-sonnet-latest",
    tools=[get_weather],
    prompt="You are a helpful assistant that can use tools to answer questions."
)

state = agent.invoke(
    {'messages': [{"role": "user", "content": "What's the weather like in New York?"}]}
)

print(state['messages'][-1])
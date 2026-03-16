from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool

load_dotenv()


@tool
def add_two_numbers(num1, num2):
    """Calculate the sum of the two numbers added."""
    return num1 + num2


@tool("square_root", description="Calculate the square root of the given number.")
def tool1(x: float) -> float:
    return x ** 0.5


agent = create_agent("gpt-5-nano",
                     tools=[add_two_numbers, tool1],
                     system_prompt="You are maths genius and a calculator")

question = HumanMessage(content = "What is the square root of 489.")

response = agent.invoke({"messages": [question]})

print(response['messages'][-1].content)

print(response['messages'][1].tool_calls)

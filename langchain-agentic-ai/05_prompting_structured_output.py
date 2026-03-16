from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from pydantic import BaseModel
from rich.console import Capture

load_dotenv()


class CapitalInfo(BaseModel):
    name: str
    location: str
    vibe: str
    economy: str


agent = create_agent("gpt-5-nano",
                     system_prompt="You are a science fiction writer, create a capital city at the users request.",
                     response_format=CapitalInfo)

question = HumanMessage(content="What is the capital of Moon")

response = agent.invoke({"messages": [question]})

print(response['structured_response'])

capital_info = response["structured_response"]

capital_name = capital_info.name
capital_location = capital_info.location

print(f"{capital_name} is a city located at {capital_location}")
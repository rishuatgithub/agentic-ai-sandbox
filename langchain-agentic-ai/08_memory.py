from pprint import pprint

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langgraph.checkpoint.memory import InMemorySaver

load_dotenv()

agent = create_agent("gpt-5-nano", checkpointer=InMemorySaver())

question = HumanMessage(content="Hello my name is Seán and my favourite colour is green")
config = {"configurable": {"thread_id": "1"}}

response = agent.invoke({"messages": [question]}, config=config)

print(response)

question2 = HumanMessage(content="What is my favourite colour? ")
response = agent.invoke({"messages": [question2]}, config=config)

pprint(response)
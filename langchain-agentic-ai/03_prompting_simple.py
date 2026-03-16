from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage, SystemMessage

load_dotenv()


question = HumanMessage(content="What is the capital of Moon?")
system_prompt = SystemMessage(content="You are a science fiction writer, create a capital city at the users request.")

agent = create_agent(model="gpt-5-nano", system_prompt=system_prompt)

response = agent.invoke({"messages": [question]})

print(response['messages'][1].content)
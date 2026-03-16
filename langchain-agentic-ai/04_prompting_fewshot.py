from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage

load_dotenv()

system_prompt = """
You are a science fiction writer, create a space capital city at the users request.

User: What is the capital of mars?
Scifi Writer: Marsialis

User: What is the capital of Venus?
Scifi Writer: Venusovia
"""

question = HumanMessage(content="What is the capital of Moon?")

agent = create_agent("gpt-5-nano", system_prompt=system_prompt)

response = agent.invoke({
    "messages": [question]
})

print(response['messages'][-1].content)
from pprint import pprint

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, AIMessage

load_dotenv()

model = init_chat_model(model="gpt-5-nano")

agent = create_agent(model=model)

response = agent.invoke({
    "messages": [
        HumanMessage(content="What is the capital of moon?"),
        AIMessage(content="The capital of moon is Luna city."),
        HumanMessage(content="Interesting, tell me more about Luna city.")
    ]
})

pprint(response)

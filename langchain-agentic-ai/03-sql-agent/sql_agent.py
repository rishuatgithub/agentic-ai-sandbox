from pprint import pprint

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_community.utilities import SQLDatabase
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool

load_dotenv()

db = SQLDatabase.from_uri("sqlite:///chinook.db")

@tool
def sql_query(query):
    """
    Execute a SQL query against the database and return the results.
    """
    try:
        return db.run(query)
    except Exception as e:
        return f"Error: {e}"


agent = create_agent(model="gpt-5-nano", tools=[sql_query])

question = HumanMessage(content="Who is the most popular artist beginning with 'S' in this database?")

response = agent.invoke(
    {"messages": [question]}
)


pprint(response['messages'])

print(response["messages"][-3].tool_calls[0]['args']['query'])
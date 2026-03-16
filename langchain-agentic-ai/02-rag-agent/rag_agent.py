from pprint import pprint

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_community.document_loaders import PyPDFLoader
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

### building a simple RAG based agent for reading PDF

load_dotenv()

## load the PDF data
loader = PyPDFLoader("acmecorp-employee-handbook.pdf")

data = loader.load()

#print(data)

## split the data into chunks

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200, add_start_index=True)
all_splits = text_splitter.split_documents(data)

#print(len(all_splits))
#print(all_splits[1])

## embedd the data
embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

vector_store = InMemoryVectorStore(embeddings)

ids = vector_store.add_documents(documents=all_splits)

#result = vector_store.similarity_search("How many days of vacation does an employee get in their first year?")
#print(result[0])

## RAG Agent

@tool
def search_handbook(query: str) -> str:
    """Search the employee handbook for information"""
    results = vector_store.similarity_search(query)
    return results[0].page_content


agent = create_agent(model="gpt-5-nano",
                     tools=[search_handbook],
                     system_prompt="You are a helpful agent that can search the employee handbook for information.")

response = agent.invoke(
    {"messages": [HumanMessage(content="How many days of vacation does an employee get in their first year?")]}
)

pprint(response)
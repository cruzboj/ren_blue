import os
from dotenv import load_dotenv
load_dotenv()

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct", 
    task="conversational",
    huggingfacehub_api_token=os.getenv("HUGGINGFACE_API_KEY"),
    temperature=0.1
)
model = ChatHuggingFace(llm=llm)

from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver # to save agent state in memory
from src.services.tools.tavily import web_search

def get_agent():
    # creates and returns an agent with the specified model and tools
    agent = create_agent(
        model=model,
        tools=[web_search],
        # checkpointer=InMemorySaver(),
    )

    return agent

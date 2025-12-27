from src.services.llm_service.llm_service import get_agent
from langchain.messages import HumanMessage

agent = get_agent()

def llm_response(message: str) -> str:
    # takes a user message as input and returns the agent's response

    question = HumanMessage(content=message)
    response = agent.invoke({"messages": [question]})
    return response["messages"][-1].content

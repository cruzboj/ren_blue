from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from langchain_core.messages import HumanMessage
from src.services.llm_service.llm_service import get_agent

class MessageRequest(BaseModel):
    message: str

agent = get_agent()

async def llm_response(request: MessageRequest):
    user_input = request.message
    
    async def event_generator():
        try:
            async for chunk, metadata in agent.astream(
                {"messages": [HumanMessage(content=user_input)]},
                stream_mode="messages"
            ):
                if chunk.content:
                    yield str(chunk.content)
        except Exception as e:
            print(f"Server Error: {e}")
            yield f"\n[Error: {str(e)}]"

    return StreamingResponse(event_generator(), media_type="text/plain")
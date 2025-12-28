from fastapi import APIRouter
from src.controllers.login import login
from src.controllers.llm import llm_response

router = APIRouter()

# --- DB Controller ---
router.post("/login")(login)

# --- LLM Controller ---
router.post("/message/")(llm_response)
from fastapi import APIRouter
from controllers.login import login
router = APIRouter()

# --- DB Controller ---
router.post("/login")(login)
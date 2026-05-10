from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.llm import generate_llm_answer

router = APIRouter()

class ChatRequest(BaseModel):
    query: str

@router.post("/chat")
def chat(request: ChatRequest):
    query = request.query
    if not query:
        raise HTTPException(status_code=400, detail="Query is required")
    res = generate_llm_answer(query)
    return {"response": res}


    
    
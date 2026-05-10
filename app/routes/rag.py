from fastapi import APIRouter, HTTPException, UploadFile, File
from pydantic import BaseModel
from services.llm import generate_llm_answer
from services.ingest import ingestion
import os

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

@router.post("/upload-pdf")
async def upload_pdf(file: UploadFile=File(...)):
    if not file:
        raise HTTPException(status_code=400, detail="File is required")

    os.makedirs("data", exist_ok=True)
    file_path = f"data/{file.filename}"

    content = await file.read()
    with open(file_path, "wb") as f:
        f.write(content)

    ingestion(file_path)
    
    return {"response": "File uploaded successfully"}
    
    
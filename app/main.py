
from fastapi import FastAPI
from routes.rag import router

app = FastAPI()

@app.get("/")
def main():
    return {"message": "Hello from pdf-rag!"}

app.include_router(router)



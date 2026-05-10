
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def main():
    return {"message": "Hello from pdf-rag!"}

if __name__ == "__main__":
    main()


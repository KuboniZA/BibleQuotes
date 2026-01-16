from fastapi import FastAPI, APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID, uuid4

app = FastAPI(title="Quotes API", version="1.0.0")
router = APIRouter(prefix="/quotes", tags=["quotes"])

class Quote(BaseModel):
    id: UUID
    text: str
    author: Optional[str] = None

scripture = [
    {"id": uuid4(), "text": "For God so loved the world...", "author": "John 3:16"},
    {"id": uuid4(), "text": "I can do all things through Christ...", "author": "Philippians 4:13"},
]

@router.get("/quotes/", response_model=List[Quote])
async def get_quotes():
    return scripture

app.include_router(router, prefix="/api")

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Quotes API!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
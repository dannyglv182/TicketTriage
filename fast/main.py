from dotenv import load_dotenv
import os
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Move(BaseModel):
    row: int
    column: int

class TicketRequest(BaseModel):
    # title: str
    description: str
    # user_email: str
    # severity: str

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/analyze-ticket")
async def analyzeTicket(ticket: TicketRequest):
    return {
        "category": "authentication",
        "priority": "High",
        "team": "Backend",
        "summary": "Mock Response for testing."
    }

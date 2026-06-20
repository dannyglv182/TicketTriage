from dotenv import load_dotenv
import os
from openai import OpenAI
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
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

class TicketRequest(BaseModel):
    # title: str
    description: str
    # user_email: str
    # severity: str

class TicketResponse(BaseModel):
    category: str
    priority: str
    team: str
    summary: str

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/analyze-ticket")
async def analyzeTicket(ticket: TicketRequest):
    triage = client.responses.parse(
        model="gpt-5",
        input=f""" Please analyze this support ticket
        description: {ticket.description}
        Determine:
        - Category 
        - Priority 
        - Team 
        - Summary
        """,
        text_format=TicketResponse
    )
    return triage.output_parsed

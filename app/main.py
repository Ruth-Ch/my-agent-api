from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain_core.messages import HumanMessage
from app.agent import agent

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str

@app.get("/")
def root():
    return {"message": "Agent API is running"}

@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    try:
        result = agent.invoke({
            "messages": [HumanMessage(content=request.message)]
        })

        final_response = result["messages"][-1].content

        return ChatResponse(response=final_response)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
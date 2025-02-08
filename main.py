from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import asyncio
from gemini_inference import general_reasoning

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return JSONResponse(
        content={"API Status": "Online"}, media_type="application/json", status_code=200
    )

@app.websocket("/chat")
async def chat(websocket: WebSocket):
    await websocket.accept()
    client = websocket.client
    await websocket.send_text(f"IP: {client}")
    messages = []
    try:
        while True:
            data = await websocket.receive_text()
            await general_reasoning(data, websocket)
            messages.append("USER: " + data)
    except WebSocketDisconnect:
        print(f"Client {client} disconnected")
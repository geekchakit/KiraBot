from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from mongo import Client
from gemini_inference import general_reasoning
from datetime import datetime
from settings import Settings

secrets = Settings()
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

mongo_client = Client(secrets.mongo_url, "kira_bot_dev")


@app.get("/")
async def read_root():
    return JSONResponse(
        content={"API Status": "Online"}, media_type="application/json", status_code=200
    )


@app.websocket("/chat")
async def chat(websocket: WebSocket):
    await websocket.accept()
    client = websocket.client
    await websocket.send_text(f"IP: {client.host if client else None}")
    messages = []
    try:
        while True:
            data = await websocket.receive_text()
            messages.append(
                {
                    "role": "user",
                    "message": data,
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                }
            )
            response = await general_reasoning(data, websocket)
            messages.append(
                {
                    "role": "assistant",
                    "message": response,
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                }
            )

    except WebSocketDisconnect:
        print(f"Client {client.host if client else None} disconnected")
        mongo_client.push_data(
            client.host, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), messages
        )

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from mongo import Client
from gemini_inference import general_reasoning
from datetime import datetime
from settings import Settings
import logging
import asyncio
from utils import get_event_data, get_team_data

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

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
    logger.info("Health check endpoint accessed")
    return JSONResponse(
        content={"API Status": "Online"}, media_type="application/json", status_code=200
    )


@app.websocket("/chat")
async def chat(websocket: WebSocket):
    await websocket.accept()
    client = websocket.client
    if client is None:
        logger.error("Client is None")
        return
    client_ip = client.host
    logger.info(f"New WebSocket connection established from IP: {client_ip}")

    logger.info("Fetching Team Data and Event Data")
    tasks: list = []
    tasks.append(asyncio.create_task(get_event_data()))
    tasks.append(asyncio.create_task(get_team_data()))
    await asyncio.gather(*tasks)

    event_data = str(tasks[0])
    team_data = str(tasks[1])
    logger.info("Getting Team Data and Event Data Done")

    await websocket.send_text(f"IP: {client_ip}")
    messages = []
    try:
        while True:
            data = await websocket.receive_text()
            logger.info(
                f"Received message from {client_ip}: {data[:100]}..."
            )  # Log first 100 chars

            messages.append(
                {
                    "role": "user",
                    "message": data,
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                }
            )

            logger.info(f"Processing message from {client_ip}")
            response = await general_reasoning(data, websocket, event_data, team_data)
            logger.info(
                f"Sent response to {client_ip}: {response[:100]}..."
            )  # Log first 100 chars

            messages.append(
                {
                    "role": "assistant",
                    "message": response,
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                }
            )

    except WebSocketDisconnect:
        logger.info(f"Client {client_ip} disconnected")
        logger.info(f"Saving chat history for {client_ip} to MongoDB")
        if len(messages)!=0:
            mongo_client.push_data(
                client_ip, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), messages
            )

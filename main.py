"""Archivo main"""
import asyncio
import random
import numpy as np
from datetime import datetime as d
from contextlib import asynccontextmanager
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from router import labels
from data.gan_model import load_gan
from model import gan_model, request_model
from controllers.gan_model import generate_image
from common.common import CANT

GENERATOR = None
active_connections = set()
date = d.now()


def send_message_to_clients(message: str):
    """
    Envío de señal de carga
    """
    for connection in active_connections:
        asyncio.create_task(connection.send_text(message))


@asynccontextmanager
async def startup_event(app: FastAPI):
    """
    Lectura de los archivos, antes de la ejecución + llamados
    """
    global GENERATOR
    GENERATOR = load_gan()
    send_message_to_clients("Loaded Model")
    yield
    GENERATOR = None

app = FastAPI(lifespan=startup_event)
app.include_router(
    labels.router
)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """
    Conexión con el cliente
    """
    await websocket.accept()
    active_connections.add(websocket)

    try:
        while True:
            data = await websocket.receive_text()
            print(f"Received message: {data}")
    except WebSocketDisconnect:
        active_connections.remove(websocket)


@app.get("/")
def home():
    """
    Endpoint principal
    """
    return {
        "message": "Welcome to the Labels API"
    }


@app.post("/api/generate")
async def generate_images(label: request_model.Label):
    """
    Generacion de la imagen
    """
    images = []
    for _ in range(CANT):
        img_id = random.randint(1, 999)
        img_date = str(date.strftime("%Y-%m-%d %H:%M:%S"))
        image = generate_image(GENERATOR, label.label)
        img_object = gan_model.Image(
            id=img_id,
            name="Image_" + str(img_id),
            label=label.label,
            resolution="128px x 128px",
            date=img_date,
            image=image
        )
        images.append(img_object)
    return {
        "data": images
    }

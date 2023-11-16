"""Archivo main"""
import random
from datetime import datetime as d
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from router import labels
from data.gan_model import load_gan
from model import gan_model, request_model
from controllers.gan_model import generate_image
from common.common import CANT

GENERATOR = None
date = d.now()


@asynccontextmanager
async def startup_event(app: FastAPI):
    """
    Lectura de los archivos, antes de la ejecución + llamados
    """
    global GENERATOR
    GENERATOR = load_gan()
    yield
    GENERATOR = None

# CORS DE LA API
app = FastAPI(lifespan=startup_event)
app.include_router(
    labels.router
)
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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
    for index in range(CANT):
        img_date = str(date.strftime("%Y-%m-%d %H:%M:%S"))
        image = generate_image(GENERATOR, label.label)
        img_object = gan_model.Image(
            id=index,
            name=label.label + "Image" + str(index),
            label=label.label,
            resolution="128px x 128px",
            date=img_date,
            image=image
        )
        images.append(img_object)
    return {
        "data": images
    }

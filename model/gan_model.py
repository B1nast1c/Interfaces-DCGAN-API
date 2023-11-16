"""Modelo de la imagen a generar"""
from pydantic import BaseModel, ConfigDict


class Image(BaseModel):
    """
    Clase base de una imagen
    """
    model_config = ConfigDict(arbitrary_types_allowed=True)

    id: int
    name: str
    label: str
    resolution: str
    date: str
    image: str

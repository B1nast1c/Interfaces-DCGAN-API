"""Modelo de la peticion"""
from pydantic import BaseModel

class Label(BaseModel):
    """
    Clase base de la petición
    """
    label: str
    
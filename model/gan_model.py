"""Modelo de la imagen a generar"""
from typing_extensions import Annotated
from pydantic import BaseModel, ConfigDict, SkipValidation, BeforeValidator, PlainSerializer
import numpy as np

def nd_array_custom_before_validator(x):
    # custome before validation logic
    return x


def nd_array_custom_serializer(x):
    # custome serialization logic
    return str(x)

NdArray = Annotated[
    np.ndarray,
    BeforeValidator(nd_array_custom_before_validator),
    PlainSerializer(nd_array_custom_serializer, return_type=str),
]

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
    image: NdArray
    
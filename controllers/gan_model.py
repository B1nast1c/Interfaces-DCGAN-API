"""Controlador del modelo"""
from common.helper import generate

def generate_image(generator, label):
    """
    Generar imagenes + ENDPOINT
    """
    image = generate(generator, label)
    return image

"""Carga del modelo generativo"""
from keras.models import load_model
from common import common

def load_gan():
    """
    Carga la GAN antes de levantar la API
    """
    generator = load_model(common.GEN_LOCATION, compile=False)
    return generator

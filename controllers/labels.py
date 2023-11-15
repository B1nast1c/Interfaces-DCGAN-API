"""Carga de las labels para la interfaz"""
from data.labels import get_labels


def get_labels_api():
    """
    Obtener las labels para la selección del tipo de elemento a generar en la interfaz
    """
    return get_labels()

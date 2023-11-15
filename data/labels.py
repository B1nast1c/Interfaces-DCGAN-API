"""Carga de las labels para la interfaz"""
import csv
from common import common
def get_labels():
    """
    Leer las labels del archivo + retornalas para mandarlas al endpoint
    """
    with open(common.LABELS_LOCATION, encoding='utf-8') as filename:
        file = csv.DictReader(filename)
        labels = set()
        for col in file:
            labels.add(col['topic'])
    return labels

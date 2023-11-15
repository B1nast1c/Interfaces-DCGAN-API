"""Testing del modelo generativo"""
import numpy as np
import tensorflow as tf
from  data.labels import get_labels

class_map = {}


def generate(conditional_gen, text_label):
    """
    Generar imagenes por label
    """
    for idx, value in enumerate(get_labels):
        class_map[value] = idx
    # Momento generación XD
    name2idx = class_map
    label = list(name2idx.keys())[list(name2idx.values()).index(text_label)]
    label = tf.ones(1) * label
    noise = tf.random.normal([1, 100])
    img = np.array(conditional_gen.predict([noise, label]))
    pred = (img[0, :, :, :] + 1) * 127.5
    pred = np.array(pred)
    return pred.astype(np.uint8)

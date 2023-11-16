"""Testing del modelo generativo"""
import base64
import numpy as np
import tensorflow as tf
from data.labels import get_labels

class_map = {}


def generate(conditional_gen, text_label):
    """
    Generar imagenes por label
    """
    try:
        for idx, value in enumerate(get_labels()):
            class_map[value] = idx
        # Momento generación XD
        name2idx = class_map
        label = name2idx[text_label]
        label = tf.ones(1) * label
        noise = tf.random.normal([1, 100])
        img = np.array(conditional_gen.predict([noise, label]))
        pred = (img[0, :, :, :] + 1) * 127.5
        pred = np.array(pred)
        bytes_data = pred.tobytes()
        encoded_str = base64.b64encode(bytes_data).decode('utf-8')
        return encoded_str
    except KeyError as e:
        print("Error: ", e)
        return np.zeros((1))  # Label incorrecta
    except AttributeError as e:
        print("Error: ", e)
        return np.zeros((1))  # Label incorrecta

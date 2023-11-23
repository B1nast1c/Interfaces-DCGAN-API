"""Testing del modelo generativo"""
import base64
import numpy as np
import cv2
from data.labels import get_labels

class_map = {}


def generate_latent_points(latent_dim, n_samples, target_class):
    """
    Variaciones + Puntos latentes
    """
    x_input = np.random.randn(latent_dim * n_samples)
    z_input = x_input.reshape(n_samples, latent_dim)
    labels = np.full((n_samples,), target_class)
    return [z_input, labels]


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
        noise, numeric_label = generate_latent_points(100, 100, label)
        img = np.array(conditional_gen.predict([noise, numeric_label]))
        pred = (img[0, :, :, :] + 1) * 127.5

        # Redimensionamiento
        width = int(pred.shape[1] * 500 / 100)
        height = int(pred.shape[0] * 500 / 100)
        dim = (width, height)
        resized = cv2.resize(pred, dim, interpolation=cv2.INTER_AREA)

        _, buffer = cv2.imencode('.jpg', resized)
        encoded_str = base64.b64encode(buffer)
        return encoded_str
    except KeyError as e:
        print("Error: ", e)
        return "-1"  # Label incorrecta
    except AttributeError as e:
        print("Error: ", e)
        return "-1"  # Label incorrecta

"""API Testing"""
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_get_labels():
    """
    Testing de la ruta de obtención de labels
    """
    expected_list = [
        "profile",
        "chat",
        "modal",
        "news",
        "gallery",
        "tutorial",
        "form",
        "terms",
        "search",
        "mediaplayer",
        "calculator",
        "list",
        "editor",
        "menu",
        "login",
        "other",
        "settings",
        "bare",
        "maps",
        "camera"
    ]
    response = client.get("/api/labels")
    assert response.status_code == 200
    assert set(response.json()["name"]) == set(expected_list)


def test_generate_img():
    """
    Testing de la ruta de generación de imágenes
    NOTA: No lee las imágenes como tal, pero se encarga de validar formatos
    """
    response = client.post(
        "/api/generate",
        json={"label": "customLabel"}
    )
    json_data = response.json()["data"]
    assert response.status_code == 200
    assert len(json_data) == 5
    assert "label" in json_data[0]

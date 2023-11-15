"""Carga de las labels + fastapi"""
import fastapi
from controllers.labels import get_labels_api

router = fastapi.APIRouter(
    prefix='/api'
)

@router.get("/labels")
def load_labels():
    """
    Retornar las labels del archivo para mandarlas al endpoint
    """
    return {
        "name": get_labels_api()
    }

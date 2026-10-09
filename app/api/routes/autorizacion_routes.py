from fastapi import APIRouter, HTTPException
from app.models.autorizacion import Autorizacion
from app.repositories.autorizacion_repository import AutorizacionRepository

router = APIRouter(prefix="/autorizaciones", tags=["Autorizaciones"])
repo = AutorizacionRepository()

@router.get("/")
def obtener_todos():
    return repo.obtener_todos()

@router.get("/{autorizacion_id}")
def obtener_por_id(autorizacion_id: int):
    autorizacion = repo.obtener_por_id(autorizacion_id)
    if not autorizacion:
        raise HTTPException(status_code=404, detail="Autorización no encontrada")
    return autorizacion

@router.post("/")
def crear_autorizacion(autorizacion: Autorizacion):
    nuevo_id = repo.crear(autorizacion)
    return {"id": nuevo_id, "message": "Autorización creada exitosamente"}

@router.put("/{autorizacion_id}")
def actualizar_autorizacion(autorizacion_id: int, autorizacion: Autorizacion):
    if repo.actualizar(autorizacion_id, autorizacion):
        return {"message": "Autorización actualizada exitosamente"}
    raise HTTPException(status_code=404, detail="Autorización no encontrada")

@router.delete("/{autorizacion_id}")
def eliminar_autorizacion(autorizacion_id: int):
    if repo.eliminar(autorizacion_id):
        return {"message": "Autorización eliminada exitosamente"}
    raise HTTPException(status_code=404, detail="Autorización no encontrada")
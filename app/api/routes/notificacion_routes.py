from fastapi import APIRouter, HTTPException
from app.models.notificacion import Notificacion
from app.repositories.notificacion_repository import NotificacionRepository

router = APIRouter(prefix="/notificaciones", tags=["Notificaciones"])
repo = NotificacionRepository()

@router.get("/")
def obtener_todos():
    return repo.obtener_todos()

@router.get("/{notificacion_id}")
def obtener_por_id(notificacion_id: int):
    notificacion = repo.obtener_por_id(notificacion_id)
    if not notificacion:
        raise HTTPException(status_code=404, detail="Notificación no encontrada")
    return notificacion

@router.post("/")
def crear_notificacion(notificacion: Notificacion):
    nuevo_id = repo.crear(notificacion)
    return {"id": nuevo_id, "message": "Notificación creada exitosamente"}

@router.put("/{notificacion_id}")
def actualizar_notificacion(notificacion_id: int, notificacion: Notificacion):
    if repo.actualizar(notificacion_id, notificacion):
        return {"message": "Notificación actualizada exitosamente"}
    raise HTTPException(status_code=404, detail="Notificación no encontrada")

@router.delete("/{notificacion_id}")
def eliminar_notificacion(notificacion_id: int):
    if repo.eliminar(notificacion_id):
        return {"message": "Notificación eliminada exitosamente"}
    raise HTTPException(status_code=404, detail="Notificación no encontrada")
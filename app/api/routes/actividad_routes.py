from fastapi import APIRouter, HTTPException
from app.models.actividad import Actividad
from app.repositories.actividad_repository import ActividadRepository

router = APIRouter(prefix="/actividades", tags=["Actividades"])
repo = ActividadRepository()

@router.get("/")
def obtener_todos():
    return repo.obtener_todos()

@router.get("/{actividad_id}")
def obtener_por_id(actividad_id: int):
    actividad = repo.obtener_por_id(actividad_id)
    if not actividad:
        raise HTTPException(status_code=404, detail="Actividad no encontrada")
    return actividad

@router.post("/")
def crear_actividad(actividad: Actividad):
    nuevo_id = repo.crear(actividad)
    return {"id": nuevo_id, "message": "Actividad creada exitosamente"}

@router.put("/{actividad_id}")
def actualizar_actividad(actividad_id: int, actividad: Actividad):
    if repo.actualizar(actividad_id, actividad):
        return {"message": "Actividad actualizada exitosamente"}
    raise HTTPException(status_code=404, detail="Actividad no encontrada")

@router.delete("/{actividad_id}")
def eliminar_actividad(actividad_id: int):
    if repo.eliminar(actividad_id):
        return {"message": "Actividad eliminada exitosamente"}
    raise HTTPException(status_code=404, detail="Actividad no encontrada")
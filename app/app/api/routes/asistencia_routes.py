from fastapi import APIRouter, HTTPException
from app.models.asistencia import Asistencia
from app.repositories.asistencia_repository import AsistenciaRepository

router = APIRouter(prefix="/asistencias", tags=["Asistencias"])
repo = AsistenciaRepository()

@router.get("/")
def obtener_todos():
    return repo.obtener_todos()

@router.get("/{asistencia_id}")
def obtener_por_id(asistencia_id: int):
    asistencia = repo.obtener_por_id(asistencia_id)
    if not asistencia:
        raise HTTPException(status_code=404, detail="Asistencia no encontrada")
    return asistencia

@router.post("/")
def crear_asistencia(asistencia: Asistencia):
    nuevo_id = repo.crear(asistencia)
    return {"id": nuevo_id, "message": "Asistencia creada exitosamente"}

@router.put("/{asistencia_id}")
def actualizar_asistencia(asistencia_id: int, asistencia: Asistencia):
    if repo.actualizar(asistencia_id, asistencia):
        return {"message": "Asistencia actualizada exitosamente"}
    raise HTTPException(status_code=404, detail="Asistencia no encontrada")

@router.delete("/{asistencia_id}")
def eliminar_asistencia(asistencia_id: int):
    if repo.eliminar(asistencia_id):
        return {"message": "Asistencia eliminada exitosamente"}
    raise HTTPException(status_code=404, detail="Asistencia no encontrada")
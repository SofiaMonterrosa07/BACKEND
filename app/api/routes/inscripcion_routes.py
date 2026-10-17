from fastapi import APIRouter, HTTPException
from app.api.routes.audit_response import respuesta_con_auditoria
from app.models.inscripcion import Inscripcion
from app.repositories.inscripcion_repository import InscripcionRepository

router = APIRouter(prefix="/inscripciones", tags=["Inscripciones"])
repo = InscripcionRepository()

@router.get("/")
def obtener_todos():
    return repo.obtener_todos()

@router.get("/{inscripcion_id}")
def obtener_por_id(inscripcion_id: int):
    inscripcion = repo.obtener_por_id(inscripcion_id)
    if not inscripcion:
        raise HTTPException(status_code=404, detail="Inscripción no encontrada")
    return inscripcion

@router.post("/")
def crear_inscripcion(inscripcion: Inscripcion):
    nuevo_id = repo.crear(inscripcion)
    return respuesta_con_auditoria(repo, nuevo_id, "Inscripción creada exitosamente", incluir_id=True)

@router.put("/{inscripcion_id}")
def actualizar_inscripcion(inscripcion_id: int, inscripcion: Inscripcion):
    if repo.actualizar(inscripcion_id, inscripcion):
        return respuesta_con_auditoria(repo, inscripcion_id, "Inscripción actualizada exitosamente")
    raise HTTPException(status_code=404, detail="Inscripción no encontrada")

@router.delete("/{inscripcion_id}")
def eliminar_inscripcion(inscripcion_id: int):
    if repo.eliminar(inscripcion_id):
        return {"message": "Inscripción eliminada exitosamente"}
    raise HTTPException(status_code=404, detail="Inscripción no encontrada")
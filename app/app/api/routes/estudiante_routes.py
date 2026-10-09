from fastapi import APIRouter, HTTPException
from app.models.estudiante import Estudiante  
from app.repositories.estudiante_repository import EstudianteRepository  

router = APIRouter(prefix="/estudiantes", tags=["Estudiantes"])
repo = EstudianteRepository()

@router.get("/")
def obtener_todos():
    return repo.obtener_todos()

@router.get("/{estudiante_id}")
def obtener_por_id(estudiante_id: int):
    estudiante = repo.obtener_por_id(estudiante_id)
    if not estudiante:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    return estudiante

@router.post("/")
def crear_estudiante(estudiante: Estudiante):
    nuevo_id = repo.crear(estudiante)
    return {"id": nuevo_id, "message": "Estudiante creado exitosamente"}

@router.put("/{estudiante_id}")
def actualizar_estudiante(estudiante_id: int, estudiante: Estudiante):
    if repo.actualizar(estudiante_id, estudiante):
        return {"message": "Estudiante actualizado exitosamente"}
    raise HTTPException(status_code=404, detail="Estudiante no encontrado")

@router.delete("/{estudiante_id}")
def eliminar_estudiante(estudiante_id: int):
    if repo.eliminar(estudiante_id):
        return {"message": "Estudiante eliminado exitosamente"}
    raise HTTPException(status_code=404, detail="Estudiante no encontrado")
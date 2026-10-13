from fastapi import APIRouter, HTTPException
from app.models.acudiente import Acudiente
from app.repositories.acudiente_repository import AcudienteRepository

router = APIRouter(prefix="/acudientes", tags=["Acudientes"])
repo = AcudienteRepository()

@router.get("/")
def obtener_todos():
    return repo.obtener_todos()

@router.get("/{acudiente_id}")
def obtener_por_id(acudiente_id: int):
    acudiente = repo.obtener_por_id(acudiente_id)
    if not acudiente:
        raise HTTPException(status_code=404, detail="Acudiente no encontrado")
    return acudiente

@router.post("/")
def crear_acudiente(acudiente: Acudiente):
    nuevo_id = repo.crear(acudiente)
    return {"id": nuevo_id, "message": "Acudiente creado exitosamente"}

@router.put("/{acudiente_id}")
def actualizar_acudiente(acudiente_id: int, acudiente: Acudiente):
    if repo.actualizar(acudiente_id, acudiente):
        return {"message": "Acudiente actualizado exitosamente"}
    raise HTTPException(status_code=404, detail="Acudiente no encontrado")

@router.delete("/{acudiente_id}")
def eliminar_acudiente(acudiente_id: int):
    if repo.eliminar(acudiente_id):
        return {"message": "Acudiente eliminado exitosamente"}
    raise HTTPException(status_code=404, detail="Acudiente no encontrado")
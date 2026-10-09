from fastapi import APIRouter, HTTPException
from app.models.modulo import Modulo
from app.repositories.modulo_repository import ModuloRepository

router = APIRouter(prefix="/modulos", tags=["Módulos"])
repo = ModuloRepository()

@router.get("/")
def obtener_todos():
    return repo.obtener_todos()

@router.get("/{modulo_id}")
def obtener_por_id(modulo_id: int):
    modulo = repo.obtener_por_id(modulo_id)
    if not modulo:
        raise HTTPException(status_code=404, detail="Módulo no encontrado")
    return modulo

@router.post("/")
def crear_modulo(modulo: Modulo):
    nuevo_id = repo.crear(modulo)
    return {"id": nuevo_id, "message": "Módulo creado exitosamente"}

@router.put("/{modulo_id}")
def actualizar_modulo(modulo_id: int, modulo: Modulo):
    if repo.actualizar(modulo_id, modulo):
        return {"message": "Módulo actualizado exitosamente"}
    raise HTTPException(status_code=404, detail="Módulo no encontrado")

@router.delete("/{modulo_id}")
def eliminar_modulo(modulo_id: int):
    if repo.eliminar(modulo_id):
        return {"message": "Módulo eliminado exitosamente"}
    raise HTTPException(status_code=404, detail="Módulo no encontrado")
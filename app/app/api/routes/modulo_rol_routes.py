from fastapi import APIRouter, HTTPException
from app.models.modulo_rol import ModuloRol
from app.repositories.modulo_rol_repository import ModuloRolRepository

router = APIRouter(prefix="/modulos-roles", tags=["Módulos Roles"])
repo = ModuloRolRepository()

@router.get("/")
def obtener_todos():
    return repo.obtener_todos()

@router.get("/{id}")
def obtener_por_id(id: int):
    registro = repo.obtener_por_id(id)
    if not registro:
        raise HTTPException(status_code=404, detail="Relación módulo-rol no encontrada")
    return registro

@router.post("/")
def crear_relacion(data: ModuloRol):
    nuevo_id = repo.crear(data)
    return {"id": nuevo_id, "message": "Relación módulo-rol creada exitosamente"}

@router.put("/{id}")
def actualizar_relacion(id: int, data: ModuloRol):
    if repo.actualizar(id, data):
        return {"message": "Relación módulo-rol actualizada exitosamente"}
    raise HTTPException(status_code=404, detail="Relación módulo-rol no encontrada")

@router.delete("/{id}")
def eliminar_relacion(id: int):
    if repo.eliminar(id):
        return {"message": "Relación módulo-rol eliminada exitosamente"}
    raise HTTPException(status_code=404, detail="Relación módulo-rol no encontrada")
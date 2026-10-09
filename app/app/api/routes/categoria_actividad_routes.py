from fastapi import APIRouter, HTTPException
from app.models.categoria_actividad import CategoriaActividad
from app.repositories.categoria_actividad_repository import CategoriaActividadRepository

router = APIRouter(prefix="/categorias-actividades", tags=["Categorías de Actividades"])
repo = CategoriaActividadRepository()

@router.get("/")
def obtener_todos():
    return repo.obtener_todos()

@router.get("/{categoria_id}")
def obtener_por_id(categoria_id: int):
    categoria = repo.obtener_por_id(categoria_id)
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    return categoria

@router.post("/")
def crear_categoria(categoria: CategoriaActividad):
    nuevo_id = repo.crear(categoria)
    return {"id": nuevo_id, "message": "Categoría creada exitosamente"}

@router.put("/{categoria_id}")
def actualizar_categoria(categoria_id: int, categoria: CategoriaActividad):
    if repo.actualizar(categoria_id, categoria):
        return {"message": "Categoría actualizada exitosamente"}
    raise HTTPException(status_code=404, detail="Categoría no encontrada")

@router.delete("/{categoria_id}")
def eliminar_categoria(categoria_id: int):
    if repo.eliminar(categoria_id):
        return {"message": "Categoría eliminada exitosamente"}
    raise HTTPException(status_code=404, detail="Categoría no encontrada")
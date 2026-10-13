from fastapi import APIRouter, HTTPException
from app.models.configuracion import Configuracion
from app.repositories.configuracion_repository import ConfiguracionRepository

router = APIRouter(prefix="/configuracion", tags=["Configuración"])
repo = ConfiguracionRepository()

@router.get("/")
def obtener_todos():
    return repo.obtener_todos()

@router.get("/{configuracion_id}")
def obtener_por_id(configuracion_id: int):
    config = repo.obtener_por_id(configuracion_id)
    if not config:
        raise HTTPException(status_code=404, detail="Configuración no encontrada")
    return config

@router.get("/clave/{clave}")
def obtener_por_clave(clave: str):
    config = repo.obtener_por_clave(clave)
    if not config:
        raise HTTPException(status_code=404, detail="Configuración no encontrada")
    return config

@router.post("/")
def crear_configuracion(configuracion: Configuracion):
    nuevo_id = repo.crear(configuracion)
    return {"id": nuevo_id, "message": "Configuración creada exitosamente"}

@router.put("/{configuracion_id}")
def actualizar_configuracion(configuracion_id: int, configuracion: Configuracion):
    if repo.actualizar(configuracion_id, configuracion):
        return {"message": "Configuración actualizada exitosamente"}
    raise HTTPException(status_code=404, detail="Configuración no encontrada")

@router.delete("/{configuracion_id}")
def eliminar_configuracion(configuracion_id: int):
    if repo.eliminar(configuracion_id):
        return {"message": "Configuración eliminada exitosamente"}
    raise HTTPException(status_code=404, detail="Configuración no encontrada")
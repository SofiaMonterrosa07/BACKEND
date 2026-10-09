from fastapi import APIRouter, HTTPException
from app.models.usuario import Usuario
from app.repositories.usuario_repository import UsuarioRepository

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])
repo = UsuarioRepository()

@router.get("/")
def obtener_todos():
    return repo.obtener_todos()

@router.get("/{usuario_id}")
def obtener_por_id(usuario_id: int):
    usuario = repo.obtener_por_id(usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

@router.post("/")
def crear_usuario(usuario: Usuario):
    nuevo_id = repo.crear(usuario)
    return {"id": nuevo_id, "message": "Usuario creado exitosamente"}

@router.put("/{usuario_id}")
def actualizar_usuario(usuario_id: int, usuario: Usuario):
    if repo.actualizar(usuario_id, usuario):
        return {"message": "Usuario actualizado exitosamente"}
    raise HTTPException(status_code=404, detail="Usuario no encontrado")

@router.delete("/{usuario_id}")
def eliminar_usuario(usuario_id: int):
    if repo.eliminar(usuario_id):
        return {"message": "Usuario eliminado exitosamente"}
    raise HTTPException(status_code=404, detail="Usuario no encontrado")
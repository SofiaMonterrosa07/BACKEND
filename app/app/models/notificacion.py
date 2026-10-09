from pydantic import BaseModel
from typing import Optional

class Notificacion(BaseModel):
    id: Optional[int] = None
    usuario_id: Optional[int] = None
    actividad_id: Optional[int] = None
    titulo: str
    mensaje: str
    fecha_envio: Optional[str] = None  
    leida: bool = False
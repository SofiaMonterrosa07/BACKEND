from app.models.base import BaseRequestModel
from pydantic import Field, StrictBool
from datetime import datetime
from typing import Optional

class Notificacion(BaseRequestModel):
    id: Optional[int] = None
    usuario_id: Optional[int] = None
    actividad_id: Optional[int] = None
    titulo: str
    mensaje: str
    fecha_envio: Optional[str] = None  
    leida: bool = False
    creado: Optional[datetime] = Field(default=None, json_schema_extra={"readOnly": True})
    actualizado: Optional[datetime] = Field(default=None, json_schema_extra={"readOnly": True})
    estado: StrictBool

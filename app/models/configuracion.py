from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Configuracion(BaseModel):
    id: Optional[int] = None
    clave: str
    valor: Optional[str] = None
    descripcion: Optional[str] = None
    estado: Optional[bool] = True
    creado: Optional[datetime] = None
    actualizado: Optional[datetime] = None
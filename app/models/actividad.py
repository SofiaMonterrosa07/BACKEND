from pydantic import BaseModel
from typing import Optional
from datetime import date, time

class Actividad(BaseModel):
    id: Optional[int] = None
    nombre: str
    descripcion: Optional[str] = None
    fecha: date
    hora: time
    lugar: str
    cupo: int
    categoria_id: int
    estado: str = "Próxima"  
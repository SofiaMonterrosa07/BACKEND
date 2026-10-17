from app.models.base import BaseRequestModel
from pydantic import Field, StrictBool
from typing import Optional
from datetime import date, datetime, time

class Actividad(BaseRequestModel):
    id: Optional[int] = None
    nombre: str
    descripcion: Optional[str] = None
    fecha: date
    hora: time
    lugar: str
    cupo: int
    categoria_id: int
    creado: Optional[datetime] = Field(default=None, json_schema_extra={"readOnly": True})
    actualizado: Optional[datetime] = Field(default=None, json_schema_extra={"readOnly": True})
    estado: StrictBool
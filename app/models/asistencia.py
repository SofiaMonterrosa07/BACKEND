from app.models.base import BaseRequestModel
from pydantic import Field, StrictBool
from datetime import datetime
from typing import Optional

class Asistencia(BaseRequestModel):
    id: Optional[int] = None
    inscripcion_id: int
    asistio: bool = False
    observacion: Optional[str] = None
    creado: Optional[datetime] = Field(default=None, json_schema_extra={"readOnly": True})
    actualizado: Optional[datetime] = Field(default=None, json_schema_extra={"readOnly": True})
    estado: StrictBool

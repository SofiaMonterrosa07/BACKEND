from pydantic import BaseModel
from typing import Optional

class Inscripcion(BaseModel):
    id: Optional[int] = None
    estudiante_id: int
    actividad_id: int
    fecha_inscripcion: Optional[str] = None
    estado: str
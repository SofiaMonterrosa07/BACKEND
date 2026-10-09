from pydantic import BaseModel
from typing import Optional

class Estudiante(BaseModel):
    id: Optional[int] = None
    usuario_id: int
    codigo_estudiante: str
    grado: str
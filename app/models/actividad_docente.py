from pydantic import BaseModel
from typing import Optional

class ActividadDocente(BaseModel):
    id: Optional[int] = None
    actividad_id: int
    docente_id: int
    rol_en_actividad: Optional[str] = "Acompañante"
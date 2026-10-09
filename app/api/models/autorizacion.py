from pydantic import BaseModel
from typing import Optional

class Autorizacion(BaseModel):
    id: Optional[int] = None
    inscripcion_id: int
    acudiente_id: int
    estado: str
    fecha_autorizacion: Optional[str] = None  # Formato: "YYYY-MM-DD"
from pydantic import BaseModel
from typing import Optional

class CategoriaActividad(BaseModel):
    id: Optional[int] = None
    nombre: str
    descripcion: Optional[str] = None
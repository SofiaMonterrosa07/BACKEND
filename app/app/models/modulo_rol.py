from pydantic import BaseModel
from typing import Optional

class ModuloRol(BaseModel):
    id: Optional[int] = None
    rol_id: int
    modulo_id: int
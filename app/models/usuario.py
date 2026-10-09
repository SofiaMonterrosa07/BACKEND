from pydantic import BaseModel
from typing import Optional

class Usuario(BaseModel):
    id: Optional[int] = None
    nombre: str
    correo: str
    password: str
    rol_id: int
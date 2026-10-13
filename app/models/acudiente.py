from pydantic import BaseModel
from typing import Optional

class Acudiente(BaseModel):
    id: Optional[int] = None
    usuario_id: int
    documento: str
    telefono: str
    parentesco: Optional[str] = None

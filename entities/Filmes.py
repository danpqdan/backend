from pydantic import BaseModel
from typing import Optional

class Filme(BaseModel):
    id: Optional[int] = None
    titulo: str
    descricao: str
    ano: int

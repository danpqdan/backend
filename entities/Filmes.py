from pydantic import BaseModel, Field, model_validator
from typing import Optional

class Filme(BaseModel):
    id: Optional[int] = None
    titulo: str
    descricao: str
    ano: int

    @model_validator(mode='before')
    def check_required_fields(cls, values):
        if not values.get('titulo') or not values.get('descricao') or not values.get('ano'):
            raise ValueError("Os campos 'titulo', 'descricao' e 'ano' precisam ser preenchidos corretamente.")
        return values

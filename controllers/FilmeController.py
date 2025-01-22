from fastapi import APIRouter, HTTPException
from pydantic import ValidationError
from entities.Filmes import Filme
from services.FilmeService import FilmeService
from fastapi.responses import JSONResponse

filmeService = FilmeService()

filme_router = APIRouter(prefix="/filmes", tags=["Filmes"])

@filme_router.post("", response_model=Filme)
def criar_filme(filme: Filme):
    try:
        return JSONResponse(
            content={"message": "Filme adicionado com sucesso","filme": filme.model_dump(exclude={"id"})},
            status_code=201
        )
    except ValidationError as e:
        raise HTTPException(
            status_code=400,
            detail="Erro de validação: Os campos 'titulo', 'descricao' e 'ano' precisam ser preenchidos corretamente."
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail="Ocorreu um erro inesperado. Por favor, tente novamente mais tarde."
        )

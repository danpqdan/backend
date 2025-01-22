from fastapi import APIRouter, HTTPException
from entities.Filmes import Filme
from typing import List
from services.FilmeService import FilmeService
from fastapi.responses import JSONResponse

filmeService = FilmeService()

filme_router = APIRouter(prefix="/filmes", tags=["Filmes"])

@filme_router.post("/", response_model=Filme)
def criar_filme(filme: Filme):
    resultado = filmeService.adicionar_filme_db((filme.titulo, filme.descricao, filme.ano))
    if "sucesso" in resultado:
        return JSONResponse(
            content={"message": "Filme adicionado com sucesso", "filme": filme.model_dump()},
            status_code=201  # Código HTTP para criação bem-sucedida
        )
    else:
        return JSONResponse(
            content={"message": resultado},
            status_code=400  # Código HTTP para erro
        )
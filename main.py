from fastapi import FastAPI
from interfaces.FilmeDB import Conexao
from controllers.FilmeController import filme_router

def lifespan(app: FastAPI):
    conexao = Conexao()
    conexao.connect()
    conexao.create_tables()
    print("Startup tasks completed")
    yield
    print("Shutdown tasks completed")
    conexao.fechar()


app = FastAPI(title="CRUD de Filmes", version="1.0", lifespan=lifespan)

app.include_router(filme_router)
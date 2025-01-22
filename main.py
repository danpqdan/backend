from fastapi import FastAPI

app = FastAPI(title="CRUD de Filmes", version="1.0")

@app.get("/")
def root():
    return {"message": "Bem-vindo ao CRUD de Filmes"}

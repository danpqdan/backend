from pydantic import ValidationError
from entities.Filmes import Filme
from interfaces.FilmeDB import Conexao
from typing import List, Optional, Tuple
class FilmeService:

    @staticmethod
    def listar_filmes() -> List[Filme]:
        try:
            conexão = Conexao()
            sql = "SELECT * FROM Filme"
            filmes = conexão.consultar_lista(sql)
            if not filmes:
                return []
            return filmes
        except Exception as e:
            return f'Erro ao consultar lista de filme: {str(e)}'

    @staticmethod
    def buscar_filme_por_id(id: int) -> Optional[Filme]:
        try:
            conexão = Conexao()
            sql = "SELECT * FROM Filme WHERE id = ?"
            filme = conexão.consultar_um(sql, (id,))
            if filme:
                return Filme(id=filme[0], titulo=filme[1], descricao=filme[2], ano=filme[3])
            return None
        except Exception as e:
            print(f"Erro ao buscar filme por ID: {str(e)}")
            return None

    @staticmethod
    def adicionar_filme(values: Tuple[str, str, int]):
        titulo, descricao, ano = values
        try:    
            conexao = Conexao()
            sql = ("INSERT INTO Filme (titulo, descricao, ano) VALUES (?, ?, ?) ")
            params = (titulo, descricao, ano)
            if conexao.gravar(sql, params):
                return "sucesso"
            else:
                return "Erro ao gravar no banco."
        except Exception as e:
            return f'Erro ao salvar o filme: {str(e)}'                
    
                
                
            
                
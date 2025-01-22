from pydantic import ValidationError
from entities.Filmes import Filme
from interfaces.FilmeDB import Conexao
from typing import List, Tuple
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
    
                
                
            
                
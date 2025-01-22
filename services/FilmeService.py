from interfaces.FilmeDB import Conexao
from typing import Tuple
class FilmeService:

    @staticmethod
    def adicionar_filme_db(values: Tuple[str, str, int]):
        titulo, descricao, ano = values
        if not titulo or not descricao or not ano:
            return "Os campos 'titulo', 'descricao' e 'ano' precisam ser preenchidos corretamente."
        else:
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
                
            
                
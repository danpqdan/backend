#### Descrição

O desafio consiste em implementar um CRUD de filmes, utilizando [python](https://www.python.org/ "python") integrando com uma API REST e uma possível persistência de dados.

### Como utilizar

#### Iniciando

1. Faça o clone do projeto:
```bash
git clone git@github.com:danpqdan/backend.git
```

#### Executando

2. 1. Certifique-se do docker e o docker-compose estar funcionando:
```bash
docker --version
docker-compose --version
```

2. 2. Localize a pasta do projeto e abra o terminal na pasta raiz como administrador

2. 3. Executando o projeto:
```bash
# -d sair do console de build
# --build construi o projeto e as novas alterações
docker-compose up -d --build
```
ou

```bash
# Caso queira iniciar o projeto sem as futuras atualizações e com console de logs
docker compose up
```

# Consumindo

3. 1. Servidor estará rodando na porta: **8000**

3. 2. Acesse a documentação via navegador:
```bash
http://0.0.0.0:8002/docs
```

3. 3. Realizando seu primeiro post via terminal:
```bash
curl -X POST "http://127.0.0.1:8000/filmes"
    -H "Content-Type: application/json"
    -d '{
           "titulo": "A procura da felicidade",
           "descricao": "Chris enfrenta sérios problemas financeiros e sua esposa, Linda, decide partir. Agora solteiro, ele precisa cuidar de Christopher, seu filho de cinco anos. Chris tenta usar sua habilidade como vendedor para conseguir um emprego melhor, mas só consegue um estágio não-remunerado.",
           "ano": 2007
         }'
```



<details>
  <summary>Descrição do Desafio</summary>
    ![WATTIO](http://wattio.com.br/web/image/1204-212f47c3/Logo%20Wattio.png)

    #### Descrição

    O desafio consiste em implementar um CRUD de filmes, utilizando [python](https://www.python.org/ "python") integrando com uma API REST e uma possível persistência de dados.


    Rotas da API:

    - `/filmes` - [GET] deve retornar todos os filmes cadastrados.
    - `/filmes` - [POST] deve cadastrar um novo filme.
    - `/filmes/{id}` -  [GET] deve retornar o filme com ID especificado.

    O Objetivo é te desafiar e reconhecer seu esforço para aprender e se adaptar. Qualquer código enviado, ficaremos muito felizes e avaliaremos com toda atenção!

    #### Sugestão de Ferramentas 
    Não é obrigatório utilizar todas as as tecnologias sugeridas, mas será um diferencial =]

    - Orientação a objetos (utilizar objetos, classes para manipular os filmes)
    - [FastAPI](https://fastapi.tiangolo.com/) (API com documentação auto gerada)
    - [Docker](https://www.docker.com/) / [Docker-compose](https://docs.docker.com/compose/install/) (Aplicação deverá ficar em um container docker, e o start deverá seer com o comando ``` docker-compose up ```
    - Integração com banco de dados (persistir as informações em json (iniciante) /[SqLite](https://www.sqlite.org/index.html) / [SQLAlchemy](https://fastapi.tiangolo.com/tutorial/sql-databases/#sql-relational-databases) / outros DB)


    #### Como começar?

    - Fork do repositório
    - Criar branch com seu nome ``` git checkout -b feature/ana ```
    - Faça os commits de suas alterações ``` git commit -m "[ADD] Funcionalidade" ```
    - Envie a branch para seu repositório ``` git push origin feature/ana ```
    - Navegue até o [Github](https://github.com/), crie seu Pull Request apontando para a branch **```main```**
    - Atualize o README.md descrevendo como subir sua aplicação

    #### Dúvidas?

    Qualquer dúvida / sugestão / melhoria / orientação adicional só enviar email para hendrix@wattio.com.br

Salve!
</details>

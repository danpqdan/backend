# Usar uma imagem Python como base
FROM python:3.12-slim

# Update da imagem e evitar que a imagem contenha arquivos temporários ou desnecessários
RUN apt-get update && apt-get install -y sqlite3 && rm -rf /var/lib/apt/lists/*

# Configurar o diretório de trabalho no contêiner
WORKDIR /app

# Copiar os arquivos principais para o contêiner
COPY . /app

# Instalar dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Comando padrão para rodar a aplicação
CMD ["python", "main.py"]

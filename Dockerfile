# Imagem base enxuta com Python 3.10 (versão usada no projeto)
FROM python:3.10-slim

# Evita arquivos .pyc e garante logs sem buffer (úteis no Docker)
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Instala as dependências primeiro para aproveitar o cache de camadas
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código
COPY . .

# Porta padrão do Streamlit
EXPOSE 8501

# Sobe o app acessível fora do container
CMD ["streamlit", "run", "app_do_bilhao_python/main.py", \
     "--server.address=0.0.0.0", "--server.port=8501"]

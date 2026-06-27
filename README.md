# App do Bilhão

Aplicativo em Python/[Streamlit](https://streamlit.io/) para visualização do histórico de preços de ações. Os dados são obtidos via [yfinance](https://pypi.org/project/yfinance/) e os gráficos são gerados com [Plotly](https://plotly.com/python/).

## Funcionalidades

- Busca de uma ação pelo *ticker* por uma barra lateral (ações da B3 usam o sufixo `.SA`, ex.: `PETR4.SA`, `TAEE11.SA`).
- Seleção do **período** (1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max).
- Exibição do histórico de cotações em formato de tabela.
- Gráfico interativo do preço de fechamento.

## Requisitos

- Python 3.10+
- Dependências: `streamlit`, `yfinance`, `plotly`, `pandas`

## Instalação

```bash
# Crie e ative um ambiente virtual
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt
```

## Como rodar

A partir da raiz do repositório:

```bash
streamlit run app_do_bilhao_python/main.py
```

O Streamlit abrirá o app no navegador (por padrão em `http://localhost:8501`).

## Usando o uv

[uv](https://docs.astral.sh/uv/) é um gerenciador de pacotes/ambientes Python rápido. Com ele você testa o sistema sem precisar ativar manualmente um virtualenv:

```bash
# Cria o ambiente e instala as dependências
uv venv
uv pip install -r requirements.txt

# Roda o app (uv usa o .venv automaticamente)
uv run streamlit run app_do_bilhao_python/main.py
```

## Usando Docker

Para rodar o sistema em container, sem instalar Python ou dependências localmente:

```bash
# Sobe o app (build na primeira execução)
docker compose up --build

# Em segundo plano
docker compose up -d --build

# Para parar
docker compose down
```

Depois acesse `http://localhost:8501`. O `compose.yaml` monta a pasta `app_do_bilhao_python/`
no container, então alterações no código são refletidas ao recarregar a página.

## Estrutura do projeto

```
AppDoBilhao/
├── app_do_bilhao_python/
│   └── main.py          # App principal (Streamlit)
├── requirements.txt     # Dependências do projeto
├── Dockerfile           # Imagem do app
└── compose.yaml         # Orquestração via Docker Compose
```

## Status

Projeto pessoal em estágio inicial, em desenvolvimento.

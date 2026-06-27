# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

App do Bilhão — aplicativo Python/Streamlit para visualização de preços de ações (usa `yfinance` e `plotly`). Projeto pessoal em estágio inicial.

## Comandos

- Rodar o app: `streamlit run app_do_bilhao_python/main.py` (a partir da raiz do repositório)

## Convenções

- **Idioma:** código, comentários, docstrings e mensagens de commit em **português (pt-BR)**.
- **Dependências:** ao adicionar um novo `import` de biblioteca externa, mantenha o `requirements.txt` sincronizado (atualmente: streamlit, yfinance, plotly, pandas). Use `/sync-requirements` para gerar/atualizar.
- **Virtualenv:** não versione ambientes virtuais (ex.: `app_do_bilhao_python/app_bilhao/`). Mantenha-os no `.gitignore`.
- **Formatação:** formate o código Python com `black`.

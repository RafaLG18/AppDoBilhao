---
name: sync-requirements
description: Scan the project's Python imports and update requirements.txt so external dependencies stay declared. Use when new imports are added or requirements.txt is missing/stale.
---

# sync-requirements

Mantém o `requirements.txt` na raiz do repositório sincronizado com os imports reais do código.

## Passos

1. Encontre todos os `import`/`from ... import` em arquivos `.py` do projeto (ignore o diretório do virtualenv, ex.: `app_do_bilhao_python/app_bilhao/`, e qualquer `.venv`).
2. Filtre apenas pacotes de terceiros (exclua módulos da biblioteca padrão e módulos locais do próprio projeto). Mapeie nomes de import para nomes de pacote PyPI quando diferirem (ex.: `import yfinance` → `yfinance`).
3. Leia o `requirements.txt` atual, se existir.
4. Adicione pacotes ausentes. Preserve linhas e versões já fixadas; não remova entradas sem confirmar com o usuário.
5. Se `pip freeze` estiver disponível e os pacotes estiverem instalados, prefira fixar as versões instaladas (`pacote==versão`); caso contrário, adicione sem versão.
6. Escreva o `requirements.txt` ordenado e mostre ao usuário um resumo do que foi adicionado.

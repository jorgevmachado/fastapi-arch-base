# Template Map

Este projeto separa o boilerplate em duas partes: base obrigatoria e arquivos opcionais.

## Base

Diretorio: `assets/template/base`

Conteudo principal:

- `app/`: codigo principal da aplicacao FastAPI.
- `tests/`: suite de testes inicial.
- `migrations/`: estrutura base do Alembic.
- `pyproject.toml`: metadados e dependencias do projeto.
- `README.md`: documentacao inicial do projeto gerado.
- `AGENTS.md`: identificacao do projeto para fluxos com agentes.
- `Makefile`: comandos utilitarios.
- `alembic.ini`: configuracao do Alembic.
- `.env.example`: exemplo de variaveis de ambiente.
- `LICENSE`: licenca base incluida no template.

## Opcionais

Diretorio: `assets/template/optional`

Conteudo principal:

- `Dockerfile`: build da aplicacao.
- `docker-compose.yml`: stack local com aplicacao, Postgres e Redis.
- `entrypoint.sh`: script de inicializacao para o ambiente containerizado.

## Regra de montagem

- O conteudo de `base` sempre e copiado.
- O conteudo de `optional` so e copiado quando `--use-docker` for informado, ou quando o modo interativo receber confirmacao positiva.

## Ordem logica do scaffold

1. Coletar parametros.
2. Gerar `project_slug`.
3. Copiar `assets/template/base`.
4. Copiar `assets/template/optional` se Docker estiver habilitado.
5. Substituir placeholders.
6. Validar se restou algum placeholder.

## Observacoes importantes

- O diretorio de destino nao pode estar preenchido.
- O template opcional hoje contem arquivos relacionados a Docker, Postgres e Redis.
- O template base ja inclui um `README.md` proprio para o projeto que sera gerado.

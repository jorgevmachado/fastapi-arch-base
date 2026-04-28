# fastapi-arch-base

`fastapi-arch-base` e um CLI para gerar a base de um novo projeto FastAPI a partir de um template reutilizavel.

Neste repositorio, ele tambem pode ser usado como uma `skill`, porque a automacao esta descrita em [SKILL.md](/home/jorge.machado/MY_PROJECTS/CLIS/fastapi-arch-base/SKILL.md) e o fluxo principal e executado por [scripts/scaffold.py](/home/jorge.machado/MY_PROJECTS/CLIS/fastapi-arch-base/scripts/scaffold.py).

## O que ele faz

- Cria a estrutura inicial de um projeto FastAPI com arquitetura padrao.
- Copia o template base de `assets/template/base`.
- Inclui arquivos opcionais de Docker a partir de `assets/template/optional` quando solicitado.
- Substitui placeholders de nome do projeto, autor e configuracao de banco.

## Como usar como CLI

Modo interativo:

```bash
python scripts/scaffold.py
```

Modo parametrizado:

```bash
python scripts/scaffold.py \
  --project-name "Minha API" \
  --target-dir /tmp/minha-api \
  --project-author-name "Jorge Machado" \
  --project-author-email "jorge.vmachado@gmail.com" \
  --db-host 127.0.0.1 \
  --db-port 5432 \
  --db-name postgres \
  --db-user postgres \
  --db-password postgres \
  --use-docker
```

## Como usar como skill

Esse projeto tambem funciona bem como skill em outro projeto ou ambiente Codex porque:

- o comportamento esperado esta documentado em `SKILL.md`;
- o template fica versionado dentro do proprio repositorio;
- a geracao do projeto acontece por um script deterministico.

Em um fluxo baseado em skills, a integracao recomendada e apontar para este repositorio e instruir o agente a executar:

```bash
python scripts/scaffold.py --project-name "Minha API" --target-dir /caminho/do/projeto
```

## Estrutura

- [SKILL.md](/home/jorge.machado/MY_PROJECTS/CLIS/fastapi-arch-base/SKILL.md): define a skill e o fluxo esperado.
- [scripts/scaffold.py](/home/jorge.machado/MY_PROJECTS/CLIS/fastapi-arch-base/scripts/scaffold.py): CLI principal.
- [assets/template/base](/home/jorge.machado/MY_PROJECTS/CLIS/fastapi-arch-base/assets/template/base): template base do projeto.
- [assets/template/optional](/home/jorge.machado/MY_PROJECTS/CLIS/fastapi-arch-base/assets/template/optional): arquivos opcionais, como Docker.

## Observacoes

- O diretorio de destino nao pode existir com arquivos dentro.
- O script valida placeholders remanescentes e falha se algum valor obrigatorio nao for substituido.
- O banco padrao previsto no template atual e PostgreSQL.

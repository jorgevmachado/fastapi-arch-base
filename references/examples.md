# Examples

Exemplos praticos de uso do CLI e da skill.

## Execucao interativa

```bash
python scripts/scaffold.py
```

Esse modo pergunta:

- nome do projeto
- diretorio de destino
- autor e email
- host, porta, nome, usuario e senha do banco
- se deve incluir Docker

## Execucao minima

```bash
python scripts/scaffold.py \
  --project-name "Minha API" \
  --target-dir /tmp/minha-api
```

Campos nao informados por argumento sao solicitados no terminal.

## Execucao completa com Docker

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

## Uso em um fluxo de skill

Exemplo de instrucao para um agente:

```text
Use a skill fastapi-arch-base para criar um novo projeto FastAPI em /tmp/minha-api com Docker habilitado.
```

Comportamento esperado:

- ler `SKILL.md`
- executar `scripts/scaffold.py`
- gerar o projeto a partir do template versionado no repositorio

## Casos de falha comuns

Diretorio nao vazio:

```text
O diretorio de destino '/tmp/minha-api' ja existe e nao esta vazio.
```

Slug invalido:

```text
Nao foi possivel gerar um project_slug valido a partir do nome do projeto.
```

Placeholder remanescente:

```text
Ainda existem placeholders nao substituidos no projeto gerado.
```

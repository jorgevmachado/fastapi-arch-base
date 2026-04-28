# Placeholders

Este arquivo documenta os placeholders atualmente usados pelo template e como o CLI os preenche.

## Placeholders em uso no template

| Placeholder | Origem no CLI | Onde aparece hoje | Obrigatorio |
| --- | --- | --- | --- |
| `__PROJECT_NAME__` | `--project-name` | `assets/template/base/AGENTS.md` | Sim |
| `__PROJECT_SLUG__` | derivado de `--project-name` | `pyproject.toml`, `README.md`, `docker-compose.yml` | Sim |
| `__PROJECT_AUTHOR_NAME__` | `--project-author-name` | `pyproject.toml` | Sim |
| `__PROJECT_AUTHOR_EMAIL__` | `--project-author-email` | `pyproject.toml` | Sim |
| `__DB_PORT__` | `--db-port` | `docker-compose.yml` | Sim |
| `__DB_NAME__` | `--db-name` | `README.md`, `docker-compose.yml` | Sim |
| `__DB_USER__` | `--db-user` | `docker-compose.yml` | Sim |
| `__DB_PASSWORD__` | `--db-password` | `docker-compose.yml` | Sim |

## Placeholder suportado pelo CLI, mas nao usado no template atual

| Placeholder | Origem no CLI | Observacao |
| --- | --- | --- |
| `__DB_HOST__` | `--db-host` | O script aceita o valor, mas nenhum arquivo atual do template referencia esse placeholder. |

## Como a substituicao funciona

- O script copia o template para o diretorio de destino.
- Depois percorre todos os arquivos de texto e faz substituicao literal dos placeholders.
- Ao final, ele procura qualquer token no formato `__NOME__`.
- Se ainda restar algum placeholder, a geracao falha.

## Observacoes

- `__PROJECT_SLUG__` e gerado automaticamente a partir de `project-name`.
- Se o nome do projeto nao gerar um slug valido, o CLI interrompe a execucao.
- Arquivos binarios sao ignorados no passo de substituicao.

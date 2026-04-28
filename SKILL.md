---
name: fastapi-arch-base
description: Use esta skill quando o usuário quiser criar a base de um novo projeto Python com FastAPI seguindo uma arquitetura padrão reutilizável, com estrutura de pastas, componentes compartilhados, configurações iniciais, convenções de código e arquivos base definidos pelo
  usuário.
---
# FastAPI Arch Base
Use esta skill quando o usuário pedir para iniciar um novo projeto FastAPI usando a arquitetura padrão dele.

## Objetivo
Criar a base de um projeto FastAPI reaproveitando os arquivos e padrões existentes em `assets/template/`.

## Variáveis suportadas
A skill deve reconhecer e substituir, quando aplicável, as seguintes variáveis:
- `__PROJECT_NAME__` — nome do projeto.
- `__PROJECT_SLUG__` — identificador técnico do projeto gerado automaticamente a partir do nome, usado em containers, package metadata e links técnicos.
- `__PROJECT_AUTHOR_NAME__` — nome do autor do projeto ( o Padrão será `Jorge Machado`) caso o usuário não queira informar um nome específico.
- `__PROJECT_AUTHOR_EMAIL__` — email do autor do projeto (o Padrão será `jorge.vmachado@gmail.com`) caso o usuário não queira informar um email específico.
- `__DB_HOST__` — host do banco de dados (o Padrão será `127.0.0.1`), caso o usuário não queira informar um host específico.
- `__DB_NAME__` — nome do banco de dados (o Padrão será `postgres`), caso o usuário não queira informar um nome específico.
- `__DB_PORT__` — porta do banco de dados (o padrão será `5432`), caso o usuário não queira informar uma porta específica.
- `__DB_USER__` — usuário do banco de dados. (o padrão será `postgres`), caso o usuário não queira informar um usuário específico.
- `__DB_PASSWORD__` — senha do banco de dados. (o padrão será `postgres`), caso o usuário não queira informar uma senha específica.

## Placeholders obrigatórios
Ao copiar o template, substituir todos os placeholders presentes nos arquivos do projeto. se algum placeholder obrigatório não receber valor, avisar o usuário antes de finalizar.

## Opcionais
- Se o usuário pedir Docker, incluir `docker-compose.yml` e `Dockerfile`.
- Se o usuário não pedir Docker, não incluir esses arquivos.

## Fluxo
1. Perguntar ou identificar:
  - nome do projeto
  - diretório de destino
  - se deve criar Docker
  - Avisar que o banco de dados padrão do projeto é o PostgreSQL.
  - Nome do banco de dados
  - Host do banco de dados
  - usuário do banco
  - senha do banco
  - porta do banco
  - Autor do projeto
  - email do autor do projeto  
2. Copiar o conteúdo de `assets/template/` para o novo projeto.
3. Substituir placeholders pelos valores informados.
4. Se o usuário não quiser docker, não criar `docker-compose.yml` e `Dockerfile` e remover as referências a ele nos arquivos de configuração.
5. Se o template tiver arquivos opcionais por stack, incluir apenas os ncessários.
6. Explicar ao usuário o que foi criado e quais são os próximos passos.

## Regras
- Nunca fixar nome do projeto no template final.
- Tratar credenciais e nome do banco como valores variáveis.
- Só criar `docker-compose.yml` e `Dockerfile` se o usuário pedir.
- Se o banco não for informado, criar o projeto sem compose ou pedir confirmação.
- Manter o projeto compátivel com FastAPI.
- Respeitar a organização e convenções definidas pelo usuário.
- Se o template ainda estiver incompleto, avisar o usuário e criar apenas o que já estiver disponivel.
- Preferir executar `scripts/scaffold.py` para gerar o projeto.
- Não recriar manualmente a estrutura se o script puder ser usado.
- Validar o resultado final após a execução do script.

## Recursos
- Template base: `assets/template/`
- Referência adicionais: `references/`

## Execução
Para gerar um novo projeto, a skill deve executar o script:
`scripts/scaffold.py`

O script deve ser o caminho preferencial para criação do projeto, em vez de copiar arquivos manualmente.

Exemplo de uso:
```bash
  python ~/.codex/skills/fastapi-arch-base/scripts/scaffold.py \
    --project-name "Meu Projeto API" \
    --target-dir /tmp/meu-projeto \
    --db-host 127.0.0.1 \
    --db-port 5432 \
    --db-name meu_banco \
    --db-user admin \
    --db-password senha123 \
    --use-docker
```
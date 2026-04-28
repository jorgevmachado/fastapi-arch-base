from __future__ import annotations

import argparse
import re
import shutil
import unicodedata
from pathlib import Path
import sys

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Gera um novo projeto FastAPI a partir da skill."
    )
    parser.add_argument("--project-name",  help="Nome do projeto a ser criado.")
    parser.add_argument("--target-dir",  help="Diretório onde o projeto será criado.")
    parser.add_argument("--project-author-name", help="Nome do autor do projeto.")
    parser.add_argument("--project-author-email",  help="Email do autor do projeto.")

    parser.add_argument("--db-host",  help="Host do banco de dados.")
    parser.add_argument("--db-port", help="Porta do banco de dados.")
    parser.add_argument("--db-name",  help="Nome do banco de dados.")
    parser.add_argument("--db-user",  help="Usuário do banco de dados.")
    parser.add_argument("--db-password",  help="Senha do banco de dados.")

    parser.add_argument("--use-docker", action="store_true", help="Incluir arquivos de configuração para Docker.")  
    
    return parser

def get_skill_root() -> Path:
    return Path(__file__).resolve().parent.parent

def get_template_base_dir() -> Path:
    return get_skill_root() / "assets" / "template" / "base"

def get_template_optional_dir( ) -> Path:
    return get_skill_root() / "assets" / "template" / "optional"

def resolve_target_dir(target_dir: str) -> Path:
    normalized_target_dir = target_dir.strip()

    if normalized_target_dir == "/~":
        normalized_target_dir = "~"
    elif normalized_target_dir.startswith("/~/"):
        normalized_target_dir = "~/" + normalized_target_dir[3:]

    return Path(normalized_target_dir).expanduser().resolve()

def copy_base_template(target_dir: Path) -> None:
    source_dir = get_template_base_dir()

    if not source_dir.exists():
        raise FileNotFoundError(f"Diretório de template base não encontrado: {source_dir}")
    
    if target_dir.exists() and any(target_dir.iterdir()):
        raise FileExistsError(f"O diretório de destino '{target_dir}' já existe e não está vazio.")

    target_dir.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source_dir, target_dir, dirs_exist_ok=True)

def copy_optional_template(target_dir: Path) -> None:
    source_dir = get_template_optional_dir()

    if not source_dir.exists():
        raise FileNotFoundError(f"Diretório de template opcional não encontrado: {source_dir}")
    
    shutil.copytree(source_dir, target_dir, dirs_exist_ok=True)

def build_project_slug(project_name: str) -> str:
    normalized = unicodedata.normalize("NFKD", project_name)
    ascii_name = normalized.encode("ascii", "ignore").decode("ascii")
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", ascii_name.strip().lower()).strip("-")

    if not slug:
        raise ValueError(
            "Nao foi possivel gerar um project_slug valido a partir do nome do projeto."
        )

    return slug

def build_replacements(args: argparse.Namespace) -> dict[str, str]:
    project_slug = build_project_slug(args.project_name)
    return {
        "__PROJECT_NAME__": args.project_name,
        "__PROJECT_SLUG__": project_slug,
        "__PROJECT_AUTHOR_NAME__": args.project_author_name,
        "__PROJECT_AUTHOR_EMAIL__": args.project_author_email,
        "__DB_HOST__": args.db_host,
        "__DB_PORT__": args.db_port,
        "__DB_NAME__": args.db_name,
        "__DB_USER__": args.db_user,
        "__DB_PASSWORD__": args.db_password,
    }

def replace_placeholders_in_file(file_path: Path, replacements: dict[str, str]) -> None:
    try:
        content = file_path.read_text(encoding='utf-8')
    except UnicodeDecodeError:
        return

    updated_content = content

    for placeholder, value in replacements.items():
        updated_content = updated_content.replace(placeholder, value)

    if updated_content != content:
        file_path.write_text(updated_content, encoding='utf-8')    

def replace_placeholders_in_project(target_dir: Path, replacements: dict[str, str]) -> None:
    for file_path in target_dir.rglob("*"):
        if file_path.is_file():
            replace_placeholders_in_file(file_path, replacements)

def find_remaining_placeholders(target_dir: Path) -> dict[str, list[str]]:
    remaining: dict[str, list[str]] = {}
    placeholder_pattern = re.compile(r"__[A-Z0-9_]+__")

    for file_path in target_dir.rglob("*"):
        if not file_path.is_file():
            continue
        try:
            content = file_path.read_text(encoding='utf-8')
        except UnicodeDecodeError:
            continue
        matches = sorted(set(placeholder_pattern.findall(content)))
        if matches:
            remaining[str(file_path)] = matches

    return remaining

def prompt_text(question: str, default: str | None = None) -> str:
    if default:
        answer =input(f"{question} [{default}]: ").strip()
        return answer or default
    while True:
        answer = input(f"{question}: ").strip()
        if answer:
            return answer
        print("Esse campo é obrigatório.")

def prompt_bool(question: str, default: bool = False) -> bool:
    suffix = "Y/n" if default else "y/N"
    while True:
        answer = input(f"{question} [{suffix}]: ").strip().lower()
        
        if not answer:
            return default
        if answer in {"y", "yes", "s", "sim"}:
              return True
        if answer in {"n", "no", "nao", "não"}:
              return False

        print("Responda com sim ou não.")

def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    interactive_mode = len(sys.argv) == 1

    if not args.project_name:
          args.project_name = prompt_text("Qual o nome do projeto")

    if not args.target_dir:
          args.target_dir = prompt_text("Qual o diretório de destino")

    if not args.project_author_name:
          args.project_author_name = prompt_text(
              "Qual o nome do autor do projeto",
              "Jorge Machado",
          )

    if not args.project_author_email:
          args.project_author_email = prompt_text(
              "Qual o email do autor do projeto",
              "jorge.vmachado@gmail.com",
          )

    if not args.db_host:
          args.db_host = prompt_text("Qual o host do banco", "127.0.0.1")

    if not args.db_port:
          args.db_port = prompt_text("Qual a porta do banco", "5432")

    if not args.db_name:
          args.db_name = prompt_text("Qual o nome do banco", "postgres")

    if not args.db_user:
          args.db_user = prompt_text("Qual o usuário do banco", "postgres")

    if not args.db_password:
          args.db_password = prompt_text("Qual a senha do banco", "postgres")

    if interactive_mode:
          args.use_docker = prompt_bool("Deseja incluir Docker?", False)


    target_dir = resolve_target_dir(args.target_dir)
    project_slug = build_project_slug(args.project_name)

    print("Projeto:", args.project_name)
    print("Project slug:", project_slug)
    print("Diretório de destino:", target_dir)
    print("Autor do projeto:", args.project_author_name)
    print("Email do autor do projeto:", args.project_author_email)
    print("Host do banco de dados:", args.db_host)
    print("Porta do banco de dados:", args.db_port)
    print("Nome do banco de dados:", args.db_name)
    print("Usuário do banco de dados:", args.db_user)
    print("Senha do banco de dados:", args.db_password)
    print("Incluir Docker:", args.use_docker)

    copy_base_template(target_dir)
    if args.use_docker:
        copy_optional_template(target_dir)

    replacements = build_replacements(args)
    replace_placeholders_in_project(target_dir, replacements)

    remaining = find_remaining_placeholders(target_dir)
    if remaining:
        print("Placeholders não substituidos encontrados:")
        for file_path, placeholders in remaining.items():
            print(f"  {file_path}: {', '.join(placeholders)}")
        raise ValueError("Ainda existem placeholders não substituidos no projeto gerado.")

    print(f"Template base copiado para: {target_dir}")
    print("Placeholders Substituidos com sucesso.")

if __name__ == "__main__":
    main()    

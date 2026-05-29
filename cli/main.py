from typing import Optional

import typer

from cli.commands.add import add_non_interactive, create_adding_stmt
from utils.add_to_docs import get_categories_names

app = typer.Typer()


@app.command()
def add(
    interactive: bool = typer.Option(
        False, "--interactive", "-i", help="Интерактивный режим"
    ),
    category: Optional[str] = typer.Option(None, "--category", "-c", help="Категория"),
    section: Optional[str] = typer.Option(
        None, "--section", "-s", help="Секция (файл .md)"
    ),
    title: Optional[str] = typer.Option(None, "--title", "-t", help="Заголовок"),
    text: Optional[str] = typer.Option(None, "--text", "-T", help="Текст заметки"),
    code: Optional[str] = typer.Option(None, "--code", "-C", help="Блок кода"),
):
    if interactive:
        categories = get_categories_names()
        try:
            cat, sec, tit, txt, cd = create_adding_stmt(categories)
        except KeyboardInterrupt:
            typer.echo("Отменено")
            raise typer.Exit()
        from utils.add_to_docs import add_to_docs

        add_to_docs(cat, sec, tit, txt or "", cd or "")
        typer.echo("\nДобавлено!")
    else:
        if not all([category, section, title, text]):
            typer.echo(
                "Ошибка: в неинтерактивном режиме укажите --category, --section, --title, --text"
            )
            raise typer.Exit(code=1)
        # TODO: Подправить типизацию вот тут
        add_non_interactive(category, section, title, text, code)
        typer.echo("\nДобавлено!")


def main():
    app()


if __name__ == "__main__":
    main()

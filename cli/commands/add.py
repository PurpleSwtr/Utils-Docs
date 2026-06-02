import questionary

from utils.add_to_docs import add_to_docs, get_categories_names, get_sections_names


def create_adding_stmt(categories: list[str]) -> tuple[str, str, str, str, str | None]:
    category = questionary.select(
        "Выберите категорию:",
        choices=categories,
        use_arrow_keys=True,
        use_jk_keys=True,
    ).ask()
    if category is None:
        raise KeyboardInterrupt("Ввод отменён пользователем")

    sections = get_sections_names(category=category)
    if not sections:
        raise ValueError(f"Для категории '{category}' не найдено секций")

    section = questionary.select(
        f"Секция → '{category}':",
        choices=sections,
        use_arrow_keys=True,
        use_jk_keys=True,
    ).ask()
    if section is None:
        raise KeyboardInterrupt("Ввод отменён пользователем")

    title = questionary.text(
        "Заголовок:",
    ).ask()
    if title is None:
        raise KeyboardInterrupt("Ввод отменён пользователем")

    text_body = questionary.text(
        "Текст:",
        multiline=True,
    ).ask()
    if text_body is None:
        raise KeyboardInterrupt("Ввод отменён пользователем")

    code_flag = questionary.confirm(
        "Добавить блок кода?",
        default=False,
    ).ask()
    if code_flag is None:
        raise KeyboardInterrupt("Ввод отменён пользователем")

    code = None
    if code_flag:
        code = questionary.text(
            "Код:",
            multiline=True,
        ).ask()
        if code is None:
            raise KeyboardInterrupt("Ввод отменён пользователем")

    return category, section, title, text_body, code


def add_non_interactive(
    category: str, section: str, title: str, text: str, code: str = ""
) -> None:
    add_to_docs(category, section, title, text, code)


if __name__ == "__main__":
    categories = get_categories_names()
    result = create_adding_stmt(categories)
    add_to_docs(*result)

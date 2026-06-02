from fastapi import HTTPException

from utils.add_to_docs import add_to_docs, get_categories_names, get_sections_names


class DocsService:
    def __init__(
        self,
    ): ...

    @staticmethod
    def get_categories_names() -> list:
        return get_categories_names()

    @staticmethod
    def get_sections_names(category: str) -> list:
        return get_sections_names(category=category)

    @staticmethod
    def add(
        category: str, section: str, title: str, text: str, code: str = ""
    ) -> None | HTTPException:
        try:
            add_to_docs(category, section, title, text, code)
        except FileNotFoundError as e:
            raise HTTPException(status_code=404, detail=f"Файл {e} не найден")

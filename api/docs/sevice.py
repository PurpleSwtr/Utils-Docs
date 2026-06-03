from fastapi import HTTPException

from api.docs.models import DocsNote
from utils.add_to_docs import (
    add_to_docs,
    get_categories_names,
    get_md_text,
    get_sections_names,
)


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
    def get_md_text(category: str, section: str):
        return get_md_text(category=category, section=section)

    @staticmethod
    def add(docs_note: DocsNote) -> None | HTTPException:
        try:
            add_to_docs(**docs_note.model_dump())
        except FileNotFoundError as e:
            raise HTTPException(status_code=404, detail=f"Файл {e} не найден")

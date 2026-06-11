import logging

from fastapi import HTTPException

from api.core.config import config
from api.docs.models import DocsNote
from utils.add_to_docs import (
    add_to_docs,
    get_categories_names,
    get_md_text,
    get_sections_names,
)
from utils.utils import get_mkdocs_nav_files_raw


class DocsService:
    def __init__(
        self,
    ):
        self.logger = logging.getLogger(__name__)

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

    def get_paths_mkdocs_yml_nav_files(self):

        nav_files = get_mkdocs_nav_files_raw(str(config.MKDOCS_YML))

        self.logger.debug(nav_files)
        return nav_files

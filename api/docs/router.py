from fastapi import APIRouter

from api.core.config import config
from api.docs.sevice import DocsService

router = APIRouter(prefix="/docs", tags=["Docs"])


@router.get("/docs_path")
def get_docs_path():
    return config.DOCS


@router.get("/categories")
def get_categories():
    return DocsService.get_categories_names()


@router.get("/sections")
def get_sections(category: str):
    return DocsService.get_sections_names(category=category)


@router.post("/add")
def add_to_docs(
    category: str, section: str, title: str, text: str, code: str = ""
) -> None:
    DocsService.add(category, section, title, text, code)

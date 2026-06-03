from fastapi import APIRouter

from api.core.config import config
from api.docs.models import DocsNote
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


@router.get("/md_text")
def get_md_text(category: str, section: str):
    return DocsService.get_md_text(category=category, section=section)


@router.post("/add")
def add_to_docs(docs_note: DocsNote) -> None:
    DocsService.add(docs_note)

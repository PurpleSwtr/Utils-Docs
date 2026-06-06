from pydantic import BaseModel


class DocsNote(BaseModel):
    category: str
    section: str
    title: str
    text: str
    is_note: bool
    code: str = ""

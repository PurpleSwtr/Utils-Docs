from pydantic import BaseModel


class DocsNote(BaseModel):
    category: str
    section: str
    title: str
    text: str
    code: str = ""

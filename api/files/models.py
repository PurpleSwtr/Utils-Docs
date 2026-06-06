from fastapi import UploadFile
from pydantic import BaseModel


# Использую когда буду связывать с фронтом
class MediaFile(BaseModel):
    file: UploadFile
    custom_filename: str | None = None

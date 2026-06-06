from fastapi import APIRouter, UploadFile

from api.files.service import FilesService

router = APIRouter(prefix="/files", tags=["Files"])


@router.post("/uploadfile/")
async def create_upload_file(
    uploaded_file: UploadFile, custom_filename: str | None = None
):
    service = FilesService()
    return await service.create_upload_file(uploaded_file, custom_filename)

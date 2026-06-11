import io

from fastapi import APIRouter, UploadFile
from fastapi.responses import StreamingResponse

from api.files.service import FilesService

router = APIRouter(prefix="/files", tags=["Files"])


@router.post("/uploadfile")
async def create_upload_file(
    uploaded_file: UploadFile, custom_filename: str | None = None
):
    service = FilesService()
    return await service.create_upload_file(uploaded_file, custom_filename)


@router.get("/download_backup")
async def download_backup():
    service = FilesService()
    zip_bytes = await service.get_zip_docs()
    return StreamingResponse(
        io.BytesIO(zip_bytes),
        media_type="application/zip",
        headers={"Content-Disposition": "attachment; filename=backup.zip"},
    )

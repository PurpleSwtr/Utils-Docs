from pathlib import Path

from fastapi import HTTPException, UploadFile

from api.core.config import config


class FilesService:
    @staticmethod
    async def create_upload_file(
        uploaded_file: UploadFile, custom_filename: str | None
    ):
        filename = uploaded_file.filename
        if filename:
            file_ext = Path(filename).suffix.lower()
            if file_ext not in config.allowed_extensions:
                raise HTTPException(
                    status_code=400,
                    detail=f"Недопустимый формат файла. Разрешены только: {', '.join(config.allowed_extensions)}",
                )
            save_dir = config.GIFS_PATH if file_ext == ".gif" else config.IMAGES_PATH

            result_filename = (
                custom_filename + file_ext if custom_filename else filename
            )

            save_path = save_dir / result_filename
            if save_path.is_file():
                raise HTTPException(
                    status_code=409,
                    detail=f"Файл {result_filename} уже существует.",
                )
            else:
                content = await uploaded_file.read()

                with open(save_path, "wb") as f:
                    f.write(content)

                return {"filename": result_filename, "status": "success"}

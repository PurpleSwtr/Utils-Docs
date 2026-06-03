from fastapi import APIRouter

from api.settings.sevice import SettingsService

router = APIRouter(prefix="/settings", tags=["Settings"])


@router.get("/mkdocs_yml")
async def get_mkdocs_yml() -> str:
    service = SettingsService()
    return service.get_mkdocs_yml()

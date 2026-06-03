from fastapi import APIRouter, Query

from api.sync.sevice import SyncService

router = APIRouter(prefix="/sync", tags=["Sync"])


@router.post("/sync")
async def github_sync(
    msg: str = Query(..., description="Сообщение для коммита"),
) -> None:
    service = SyncService()
    await service.sync_run(msg)

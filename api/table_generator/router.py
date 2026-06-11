from fastapi import APIRouter

from api.table_generator.service import TableGeneratorService

router = APIRouter(prefix="/table_generator ", tags=["TableGenerator"])


@router.patch("/generate_todo")
def generate_todo() -> None:
    service = TableGeneratorService()
    service.create_md_table()

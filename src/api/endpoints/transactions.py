from fastapi import APIRouter, FastAPI

router = APIRouter()


@router.get("/search")
async def read_users(
    q: str = None,
):
    return [{"username": "Rick"}, {"username": "Morty"}]

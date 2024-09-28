from fastapi import APIRouter

from src.api.endpoints import transactions

api_router = APIRouter()
api_router.include_router(
    transactions.router, prefix="/transactions", tags=["login"])

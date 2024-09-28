from typing import Union

from fastapi import FastAPI, APIRouter
from src.api.api import api_router

app = FastAPI()


app.include_router(api_router, prefix="/api/v1")

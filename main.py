from fastapi import FastAPI
from app.api.test import test as test_router

app = FastAPI()

app.include_router(test_router)


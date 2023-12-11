from fastapi import FastAPI
from app.api.test import test as test_router
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.include_router(test_router)


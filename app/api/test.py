from fastapi import APIRouter

test = APIRouter()

@test.get("/")
async def hello_world():
  return {"message": "Hello World"}
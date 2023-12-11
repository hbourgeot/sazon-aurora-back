from fastapi import APIRouter
from app.supabase.supabase import supabase

test = APIRouter()

@test.get("/")
async def hello_world():
  return {"message": "Hello World"}
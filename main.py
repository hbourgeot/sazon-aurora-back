from fastapi import FastAPI
from app.api.foods import foods as foods_router

app = FastAPI()

# Routers
app.include_router(foods_router, prefix="/food", tags=["foods"])
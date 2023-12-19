from fastapi import FastAPI
from app.api.foods import foods as foods_router
from app.api.invoices import inv as invoices_router

app = FastAPI()

# Routers
app.include_router(foods_router, prefix="/food", tags=["foods"])
app.include_router(invoices_router, prefix="/invoice", tags=["invoices"])
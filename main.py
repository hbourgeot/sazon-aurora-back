from fastapi import FastAPI
from app.api.foods import foods as foods_router
from app.api.invoices import inv as invoices_router
from app.api.products import products as products_router
from app.api.providers import provs as providers_router

app = FastAPI()

# Routers
app.include_router(foods_router, prefix="/food", tags=["foods"])
app.include_router(invoices_router, prefix="/invoice", tags=["invoices"])
app.include_router(products_router, prefix="/product", tags=["products"])
app.include_router(providers_router, prefix="/provider", tags=["providers"])
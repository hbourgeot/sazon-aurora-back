from fastapi import FastAPI
from app.api.foods import foods as foods_router
from app.api.invoices import inv as invoices_router
from app.api.products import products as products_router
from app.api.providers import provs as providers_router
from app.api.roles import roles as roles_router
from app.api.users import users as users_router
from app.api.graphics import graph as graph_router
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

# Routers
app.include_router(foods_router, prefix="/food", tags=["foods"])
app.include_router(invoices_router, prefix="/invoice", tags=["invoices"])
app.include_router(products_router, prefix="/product", tags=["products"])
app.include_router(providers_router, prefix="/provider", tags=["providers"])
app.include_router(roles_router, prefix="/role", tags=["role"])
app.include_router(users_router, prefix="/user", tags=["user"])
app.include_router(graph_router, prefix="/graphs", tags=["common", "foods", "products"])
from fastapi import APIRouter
from app.supabase.functions.invoice import get_sales
inv = APIRouter()


# Routes
@inv.get("/all")
def get_invoices():
    total_sales = 0
    sales = get_sales()
    for sale in sales:
        total_sales += sale["ventas"]
    
    return total_sales


@inv.get("/{id}")
def get_invoice(id: int):
    return {"take":id}


@inv.post("/new")
def create_invoice():
    return {"message": "Hey"}

@inv.put("/{id}")
def update_invoice(id: int):
    return {"message": "up"}
from fastapi import APIRouter

inv = APIRouter()


# Routes
@inv.get("/all")
def get_invoices():
    return {"take": []}


@inv.get("/{id}")
def get_invoice(id: int):
    return {"take":id}


@inv.post("/new")
def create_invoice():
    return {"message": "Hey"}

@inv.put("/{id}")
def update_invoice(id: int):
    return {"message": "up"}
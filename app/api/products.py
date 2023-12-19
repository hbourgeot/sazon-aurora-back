from fastapi import APIRouter

products = APIRouter()


# Routes
@products.get("/all")
def get_products():
    return {"take": []}


@products.get("/{id}")
def get_product(id: int):
    return {"take":id}


@products.post("/new")
def create_product():
    return {"message": "Hey"}

@products.put("/{id}")
def update_product(id: int):
    return {"message": "up"}
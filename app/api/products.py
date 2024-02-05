from fastapi import APIRouter, HTTPException
import app.supabase.functions.products as products_table
from app.schemas import Product

products = APIRouter()


# Routes
@products.get("/all")
def get_products():
    return products_table.get_products()


@products.get("/{product_id}")
def get_product(product_id: int):
    return products_table.get_product_by_id(product_id)


@products.post("/new")
def create_product(prod: Product):
    product_dict = prod.model_dump()
    product = products_table.upsert_product(product_dict)
    if product is not None:
        return product

    raise HTTPException(status_code=400, detail="Product Bad Request")


@products.put("/{prod_id}")
def update_product(prod_id: int, prod: Product):
    product_dict = prod.model_dump()

    existing_prod = products_table.get_product_by_id(prod_id)
    if existing_prod is None:
        raise HTTPException(status_code=404, detail="Product not found")

    product_dict["id"] = prod_id
    prov_response = products_table.upsert_product(product_dict)

    if prov_response is not None:
        return prov_response

    raise HTTPException(status_code=400, detail="Product bad request")
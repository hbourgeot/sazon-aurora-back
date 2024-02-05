from fastapi import APIRouter, HTTPException
from app.schemas import Food
from app.supabase.functions import foods as food_table, food_product as food_product_table

foods = APIRouter()


# Routes
@foods.get("/all")
def get_foods():
    res = food_table.get_foods()
    return res


@foods.get("/{id}")
def get_food(food_id: int):
    res = food_table.get_food_by_id(food_id)
    return res


@foods.post("/new")
def create_food(food: Food):
    try:
        food_dict = {
            "name": food.name,
            "price": food.price,
            "created_at": food.created_at.isoformat(),
            "description": food.description
        }
        result = food_table.upsert_food(food_dict)
        
        return result
    except Exception as ex:
        return {"error": str(ex)}, 500


@foods.patch("/{food_id}")
def update_food(food: Food, food_id: int):
    existing_food = food_table.get_food_by_id(food_id)
    if not existing_food:
        raise HTTPException(status_code=404, detail="Food not found")

    # Convertimos el objeto Food a un diccionario
    food_dict = {
        "name": food.name,
        "price": food.price,
        "created_at": food.created_at.isoformat(),
        "description": food.description
    }

    # Aquí comparamos los campos del objeto existente con los del objeto enviado
    updated_data = {}
    for key, value in food_dict.items():
        if value != getattr(existing_food, key, None):
            updated_data[key] = value

    # Si no hay cambios, no hacemos nada
    if not updated_data:
        return {"message": "No updates were made"}

    # Llamamos a la función de upsert con los datos actualizados
    try:
        res = food_table.upsert_food({"id": food_id, **updated_data})
        return res
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))
    
    
@foods.post("/{food_id}/product/{product_id}")
def add_product_to_food(food_id: int, product_id: int, quantity: int = 1):
    try:
        food_product_dict = {
            "food_id": food_id,
            "product_id": product_id,
            "amount": quantity
        }
        res = food_product_table.upsert_food_product(food_product_dict)
        return res
    except Exception as ex:
        return {"error": str(ex)}
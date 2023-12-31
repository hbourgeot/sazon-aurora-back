from fastapi import APIRouter, HTTPException
from app.schemas import Food
from app.supabase.functions import foods as food_table

foods = APIRouter()


# Routes
@foods.get("/all")
def get_foods():
    res = food_table.get_foods()
    foods = res.model_dump()
    return {"foods": foods}


@foods.get("/{id}")
def get_food(food_id: int):
    res = food_table.get_food_by_id(food_id)
    food = res.model_dump()
    return {"food":food}


@foods.post("/new")
def create_food(food: Food):
    try:
        food_dict = {
            "name": food.name,
            "price": food.price,
            "id": food.id,
            "created_at": food.created_at.isoformat(),
            "description": food.description
        }
        result = food_table.upsert_food(food_dict)
        res = {"data": result.data}
        return res
    except Exception as ex:
        return {"error": str(ex)}


@foods.patch("/{id}")
def update_food(food: Food, food_id: int):
    existing_food = food_table.get_food_by_id(food_id)
    if not existing_food:
        raise HTTPException(status_code=404, detail="Food not found")

    # Convertimos el objeto Food a un diccionario
    food_data = food.model_dump()

    # Aquí comparamos los campos del objeto existente con los del objeto enviado
    updated_data = {}
    for key, value in food_data.items():
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
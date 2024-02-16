from fastapi import APIRouter, HTTPException
from app.schemas import User
from app.supabase.functions import users as user_table
from app.core.recommendations import CoreRecommendation
import traceback
users = APIRouter()


# Routes
@users.get("/all")
def get_users():
    res = user_table.get_user()
    users = res.data
    return users


@users.get("/{id}")
def get_user(user_id: int):
    res = user_table.get_user_by_id(user_id)
    user = res.model_dump()
    return {"user":user}


@users.post("/new")
def create_user(user: User):
    try:
        user_dict = user.model_dump()
        result = user_table.upsert_user(user_dict)
        return result.data
    except Exception as ex:
        return {"error": str(ex)}


@users.patch("/{id}")
def update_user(user: User, user_id: int):
    existing_user = user_table.get_user_by_id(user_id)
    if not existing_user:
        raise HTTPException(status_code=404, detail="User not found")

    # Convertimos el objeto User a un diccionario
    user_data = user.model_dump()

    # Aquí comparamos los campos del objeto existente con los del objeto enviado
    updated_data = {}
    for key, value in user_data.items():
        if value != getattr(existing_user, key, None):
            updated_data[key] = value

    # Si no hay cambios, no hacemos nada
    if not updated_data:
        return {"message": "No updates were made"}

    # Llamamos a la función de upsert con los datos actualizados
    try:
        res = user_table.upsert_user({"id": user_id, **updated_data})
        return res
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))


@users.get("/{user_id}/recommendations")
def get_recommendations(user_id: int):
    try:
        recommendations_foods = user_table.get_cart_and_invoice(user_id)
        search = CoreRecommendation()
        recommendations = search.recommended_products(recommendations_foods, top_k=3)
        print(recommendations)
        
        return recommendations
    except Exception as ex:
        traceback.print_exc()
        return {"error": str(ex)}

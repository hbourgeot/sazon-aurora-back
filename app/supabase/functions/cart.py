from app.supabase import supabase

def get_foods_recommendations(user_id: int):
    res = supabase.table("cart").select("*").eq("user_id", user_id).execute()
    
    if not res.data:
        return []
    
    cart_details = supabase.table("cart_details").select("*").in_("cart_id", res.data["id"]).execute()
    
    foods = []
    
    food_ids = [x["food_id"] for x in cart_details.data]
    for food_id in food_ids:
        food = supabase.table("foods").select("*").eq("id", food_id).execute()
        
        appended_food = {"name": food.data["name"], "price": food.data["price"], "description": food.data["description"]}
        foods.append(appended_food)
    


def get_food_by_id(food_id: int):
    res = supabase.table("foods").select("*").eq("id", food_id)


def upsert_food(data):
    res = supabase.table("foods").upsert(data)


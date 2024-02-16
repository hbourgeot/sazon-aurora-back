from app.supabase import supabase


def get_foods_recommendations(user_id: int):
    res = supabase.table("invoices").select("*").eq("user_id", user_id).execute()

    if not res.data:
        return []
    
    foods = []
    for data in res.data:
        invoice_details = supabase.table("invoice_details").select(
            "*").eq("invoice_id", data["id"]).execute()


        food_ids = [x["food_id"] for x in invoice_details.data]
        for food_id in food_ids:
            food = supabase.table("foods").select("*").eq("id", food_id).limit(1).single().execute()

            appended_food = {
                "name": food.data["name"], "price": food.data["price"], "description": food.data["description"]}
            foods.append(appended_food)
    
    return foods


def get_food_by_id(food_id: int):
    res = supabase.table("foods").select("*").eq("id", food_id)
    print(res)


def upsert_food(data):
    res = supabase.table("foods").upsert(data)
    print(res)


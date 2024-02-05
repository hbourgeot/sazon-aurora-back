from app.supabase import supabase

def get_foods():
    res = supabase.table("products").select("*").execute()
    return res.data


def get_food_by_id(food_id: int):
    res = supabase.table("products").select("*").eq("id", food_id).execute()
    return res.data


def upsert_product(data):
    res = supabase.table("products").upsert(data).execute()
    return res.data

